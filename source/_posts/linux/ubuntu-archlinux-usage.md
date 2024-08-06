---
title: Ubuntu、Arch Linux 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Ubuntu、Arch Linux 使用
description: Ubuntu、Arch Linux 使用
tags:
  - Ubuntu
  - ArchLinux
categories:
  - Linux
date: 2023-09-18 16:50:00
abbrlink: 142249
password:
---

# Ubuntu、Arch Linux 安装与使用

## Ubuntu 使用

### 安装

- 磁盘分区，使部分磁盘空间处于未分配状态
- 通过镜像加速下载 Ubuntu ISO 文件
- 使用 U 盘 +Rufus 软件制作启动盘
- 关机，进入 BIOS（联想拯救者是按 F2 键），更改启动顺序，设置 U 盘为首选启动设备
- 安装 Ubuntu，过程中手动分配磁盘空间，将 free space 主要分成 4 部分
    - `/boot` - 引导分区，用于存储启动加载器和一些启动时需要的文件；一般 500MB 到 1GB 足够
    - `Swap` - 该分区用作内存不足时的虚拟内存；通常为物理内存（RAM）的大小的 1 至 2 倍
    - `/` - 根分区，包含大部分系统文件；建议 50GB 及以上
    - `/home` - 该分区用于存储用户文件和设置；建议 `/` 和 `/home` 比例为 1:2 或 1:3
    - `EFI` - UEFI 固件用来存储 EFI 应用程序和驱动程序；建议 100MB 到 500MB（一般该分区已设置）
- 安装完成后，系统会提示拔掉 U 盘


---

### 基础设置

#### 换源

- 修改软件源以加速 package 下载
- 镜像源文件:
	- Debian/Ubuntu - `/etc/apt/sources.list`；Ubuntu 软件源镜像：[ubuntu - 清华大学镜像](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)
	- Fedora/RHEL/CentOS - `/etc/yum.repos.d/` 或 `/etc/dnf/dnf.conf`
	- Arch Linux - `/etc/pacman.d/mirrorlist`


```bash
# 备份
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

# 换源（Ubuntu 版本不同，源也不同）

# 更新并升级
sudo apt update && sudo apt upgrade
```


---

#### 安装显卡驱动

Softwares & Update - Additional Drivers - Additional Drivers - 选择其中一个 NVIDIA driver


---

#### 中英文输入法

- 添加中文语言支持：Settings - Region&Language - Manage Install Languages - Install/Remove Languages - Chinese(simplified) 
- 已集成 iBus：Settings - Keyboard - Input Sourses - 添加 Chinese(Intelligent Pinyin)


---

#### GRUB 设置

>[GRUB - Arch Linux 中文维基](https://wiki.archlinuxcn.org/zh-hans/GRUB)

>[GitHub - vinceliuice/grub2-themes: Modern Design theme for Grub2](https://github.com/vinceliuice/grub2-themes)

GRUB：开机引导

```bash
# grub theme 路径
/usr/share/grub/themes/

# 获取 Windows 引导菜单名称（含单引号）
cat /boot/grub/grub.cfg | grep 'windows'

# 修改 GRUB_DEFAULT 和 GRUB_TIMEOUT 选项
sudo vi /etc/default/grub

# 更新
sudo update-grub

# 美化 grub
git clone git@github.com:vinceliuice/grub2-themes.git
sudo ./install.sh -t tela -s 2k
```


---

#### 快捷键

- `Crtl + Alt + T` - 打开终端
- `Crtl + Shift + T` - 打开终端新标签页
- `Crtl + Shift + C` - 复制
- `Crtl + Shift + V` - 粘贴
- `Ctrl + Alt + Del` - 打开睡眠、关机、重启、登出对话框
- `Alt + F2` - 打开运行对话框
- `Win` - 也称 Super 键，可进行程序搜索


---

#### 网络代理

```bash
mkdir ~/clash; cd ~/clash

# 下载适合的 Clash 二进制文件并重命名为 clash
# 一般 clashpremium-linux-amd64

# 下载 Clash 配置文件

chmod +x clash

# 启动 Clash
# 同时启动 HTTP 代理和 Socks5 代理 
./clash -d .

# 访问 Clash Dashboard 可以进行切换节点、测延迟等操作
# https://clash.razord.top/
# 编辑外部控制设置：Host: 127.0.0.1，端口: 9090

# 启用系统代理
# Settings - Network，点击网络代理右边的 ⚙ 按钮，选择手动，
# 填写 HTTP 和 HTTPS 代理为 127.0.0.1:7890，填写 Socks 主机为 127.0.0.1:7891
```


---

##### 开机自启动

>[systemd -  Arch Linux 中文维基](https://wiki.archlinuxcn.org/wiki/Systemd)

>[Arch Linux Clash 安装配置记录](https://blog.linioi.com/posts/clash-on-arch/)

创建 systemd 配置文件：`/etc/systemd/system/clash.service`

```bash
[Unit]
Description=Clash daemon, A rule-based proxy in Go.
After=network.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/local/bin/clash -d /etc/clash # /usr/local/bin/clash 为绝对路径，请根据你实际情况修改

[Install]
WantedBy=multi-user.target
```

---

systemd 相关命令

```bash
# 启用 Clash 服务
sudo systemctl enable clash

# 启动 Clash
sudo systemctl start clash

# 获取 Clash 日志
systemctl status clash

# 列出所有正在运行的 systemd 服务
systemctl list-units --type=service

# 列出所有已安装的 systemd 服务
systemctl list-unit-files --type=service

# 查看代理
env | grep -i proxy
```


---

#### GNOME 桌面

>[Gnome-look.org](https://www.gnome-look.org/)

>[GitHub - vinceliuice/Colloid-gtk-theme: Colloid gtk theme for linux](https://github.com/vinceliuice/Colloid-gtk-theme)


tweak：设置 GNOME 主题

```bash
sudo apt -y install gnome-tweaks
```

---

安装 CNOME 桌面扩展：[如何安装GNOME插件 - 知乎](https://zhuanlan.zhihu.com/p/36265103)

```bash
sudo apt install chrome-gnome-shell
```

GNOME 桌面扩展推荐：

- Dash to Dock
- Clipboard Indicator
- system-monitor
- User Themes


---

#### KDE Plasma 桌面

>[Ubuntu 给 Dash 添加程序图标](https://github.com/judasn/Linux-Tutorial/blob/master/markdown-file/ubuntu-settings/Ubuntu-Create-Desktop.md)

>[首页 - KDE 社区](https://kde.org/zh-cn/)

>[KDE美化及常用设置 - pipci - 博客园](https://www.cnblogs.com/pipci/p/14862648.html)

>[KDE常用桌面插件总结 - pipci - 博客园](https://www.cnblogs.com/pipci/p/14861412.html)

- GNOME 与 KDE 的区别：
	- GNOME 使用 GDM3 显示管理器；KDE 使用 SDDM (Simple Desktop Display Manager) 显示管理器
	- GNOME 主要使用 GTK 构建 GUI 工具，KDE 使用 Qt
	- KDE 默认终端 Konsole，默认文本编辑器 Kate

```bash
sudo apt install kde-plasma-desktop

# 完整 KDE
sudo apt install kubuntu-desktop
```

- style 更换


---

#### SDDM 设置

>[SDDM -  Arch Linux 中文维基](https://wiki.archlinuxcn.org/wiki/SDDM)

sddm theme：[corners](https://github.com/aczw/sddm-theme-corners)

sddm 相关命令

```bash
# sddm theme 路径
/usr/share/sddm/themes/

# 生成 sddm 示例配置文件
sudo sddm --example-config > /etc/sddm.conf

# 测试（预览）theme
sddm-greeter --test-mode --theme <path>
```

---

编辑或创建 `/etc/sddm.conf` 文件

```bash
# sddm theme
[Theme]
Current=corners

# 虚拟键盘
[General]
InputMethod=
```


---

#### package 安装

- apt 方式

```bash
sudo apt install <package>

# 卸载 libreoffice
sudo apt remove libreoffice-common
# 卸载 firefox Linux 中原生的 firefox 不完整
sudo apt remove firefox
```

---

- snap 方式：[Install Linux apps using the Snap Store | Snapcraft](https://snapcraft.io/store)

```bash
sudo snap install <package>
sudo snap install --dangerous <package>.snap

# 示例
sudo snap install mailspring
sudo snap install alacritty --classic

# 删除 package
sudo snap remove <package>
```

---

- deb 方式：`.deb` 是 Ubuntu 和 Debian 的程序包格式； `.rpm` 是 Red Hat 等的程序包格式

```bash
sudo apt install ./<package>.deb
sudo dpkg -i <package>

# 删除 package
sudo apt remove <package>
```

---

- AppImage 方式

```bash
chmod +x <package>.AppImage

./<package>.AppImage

# 删除 package
rm <package>.AppImage
```

可能会出现以下报错内容：
```bash
dlopen(): error loading libfuse.so.2 
AppImages require FUSE to run. 
You might still be able to extract the contents of this AppImage
```

解决方法：
```bash
sudo apt update
sudo apt install libfuse2
```


---

##### package 彻底卸载

>[Ubuntu apt-get彻底卸载软件包\_apt卸载包\_享学IT的博客-CSDN博客](https://blog.csdn.net/get_set/article/details/51276609)


```bash
apt-cache  # 搜索、查看和管理 package 缓存

# 卸载 package 及删除其配置文件
sudo apt --purge remove <package>
sudo apt purge <package>

# 自动卸载被安装来满足其他软件包依赖关系但现在不再需要的 packages
sudo apt autoremove

# 列出已安装 packages 及信息
apt list --installed | less

# 查看已安装 package 的文件列表（可查看头文件和库文件路径）
dpkg -L <package>

# packages 列表
# ii: 已正确安装使用的 packages
# rc: 已卸载但配置文件未删除的 packages
dpkg -l | less
dpkg-query -l | less

# 删除已卸载但配置文件仍留在系统中的 packages
dpkg -l | grep '^rc' | awk '{print $2}' | sudo xargs dpkg -P

# 统计已安装 packages 数量
dpkg-query -f '${binary:Package}\n' -W | wc -l
```


---

##### 常用软件

- 快速启动工具：Rofi（不是很好用）
- VPN 网络代理：ClashX
- 代码编辑器：vscode-insiders
- Office 替代：WPS
- 终端工具：Tabby、Alacritty
- 远程服务器连接工具：Termius
- 数据同步（交大服务）：交大云盘
- 浏览器： Chrome
- 媒体播放器：VLC
- 笔记管理：Obsidian
- Markdown 编辑器：Typora（安装 0.11.18 版本）
- 图床：PicGo
- 文献管理：Zotero
- 构型可视化：VESTA、OVITO
- 邮件服务：Mailspring
- 截图：Snipaste
- pt 下载工具：qBittorrent 或 Transmissioin


---

##### 具体软件安装与设置

###### Alacritty 设置

>[GitHub - tmcdonell/config-alacritty: Alacrity configuration](https://github.com/tmcdonell/config-alacritty)

创建配置文件
```bash
mkdir ~/.config/alacritty
touch ~/.config/alacritty/alacritty.yml
```

配置内容
```yaml
# 透明度
window:
 opacity: 0.7
```

---

###### VLC

VLC 打开时报错：[vlc doesn't work after \`sudo snap install vlc\` - Ask Ubuntu](https://askubuntu.com/questions/1278422/vlc-doesnt-work-after-sudo-snap-install-vlc)

```bash
sudo rm /var/cache/fontconfig/* 
rm ~/.cache/fontconfig/* 
fc-cache -r
```

---

###### Transmission

```bash
# cmake 配置时，若出现 curl 或 openssl 相关报错
sudo apt install libcurl4-openssl-dev
sudo apt install libssl-dev

git clone --recurse-submodules https://github.com/transmission/transmission Transmission
cd Transmission
# Use -DCMAKE_BUILD_TYPE=RelWithDebInfo to build optimized binary with debug information. (preferred)
# Use -DCMAKE_BUILD_TYPE=Release to build full optimized binary.
cmake -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
cd build
cmake --build .
sudo cmake --install .
```

- [ ] 源码编译没有 gui 程序？


---

###### PicGo 安装

```bash
wget https://picgo-release.molunerfinn.com/2.4.0-beta.6/picgo_2.4.0-beta.6_amd64.snap

sudo snap install --dangerous picgo_2.4.0-beta.6_amd64.snap

# 或 snap 安装
```


---

###### deepin 版微信安装

打开微信：[安装成功了，怎么打开？也没有说明 · Issue #334 · zq1997/deepin-wine · GitHub](https://github.com/zq1997/deepin-wine/issues/334)

```bash
wget -O- https://deepin-wine.i-m.dev/setup.sh | sh

sudo apt-get install com.qq.weixin.deepin
```


---

###### Linux 本地访问交大云盘

>[开始 | JboxWebdav 说明文档](https://1357310795.github.io/JboxWebdav/start/)

```bash
# 安装 .NET 6.0 Runtime
sudo apt-get install -y dotnet-runtime-6.0

# 创建服务器配置
rclone config create jbox webdav url=http://127.0.0.1:65472/ vendor=other --non-interactive

# 启动 Rclone 挂载 需要映射到一个空文件夹
rclone mount jbox: /home/yangsl/jbox --vfs-cache-mode=minimal
```


---

###### 其他

- Tabby 相关设置：设置 - 终端 - 鼠标，鼠标右键点击设置为 “粘贴”；剪贴板，勾选 “选中时复制”
- WPS 界面中文设置：[Linux 英文系统下，切换wps界面语言为中文 · GitHub](https://gist.github.com/YcSmile/039024e79b9d7dca38e80fdca7890620)


---

##### Linux 端没有的一些软件

- 官方微信
- 交大云盘
- PotPlayer
- Notepad++
- MobaXterm
- WinSCP


---

#### 字体安装

- 中文字体：[得意黑](https://github.com/atelier-anchor/smiley-sans)
- 英文字体： [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts)（主要下载 Meslo 或 Hack）

```bash
# 字体路径
/usr/share/fonts      # 系统
~/.fonts              # 个人用户
~/.local/share/fonts  # 较新 Ubuntu 版本

# 拷贝字体
sudo cp <font>.ttf /usr/share/fonts/truetype  # ttf 字体
sudo cp <font>.otf /usr/share/fonts/opentype  # otf 字体
sudo cp *.ttf /usr/share/fonts

# 更新字体缓存 或 重新登录 生效
sudo fc-cache -f -v

fc-list  # 查看字体
fc-list :lang=zh  # 查看中文字体
```


- 字体设置
	- 系统设置： Settings - Appearance - Fonts
	- Chrome 浏览器设置：Settings - Appearance - Customize font
	- Obsidian 设置：设置 - 外观 - 字体 - 界面、正文、代码字体


---

#### 其他

- Windows、Linux 双系统时，Windows 盘符 及 U 盘的路径为 `/media/username/`
- KDE 任务栏应用程序图标大小设置：相应位置右键 - Enter Edit Mode - 调整 Panel height
- KDE 任务栏系统托盘（System Tray）图标大小设置：相应位置右键 - Configure System Tray - General - Panal icon size
- Linux 相关程序介绍：[目录 -  Arch Linux 中文维基](https://wiki.archlinuxcn.org/wiki/%E7%9B%AE%E5%BD%95)、[StrongSwan](https://wiki.archlinuxcn.org/wiki/StrongSwan)、[OpenSSH](https://wiki.archlinuxcn.org/wiki/OpenSSH)、[窗口管理器](https://wiki.archlinuxcn.org/zh/%E7%AA%97%E5%8F%A3%E7%AE%A1%E7%90%86%E5%99%A8)

---

相关命令

```bash
# 在终端用默认程序打开文件或 URL
open file
open URL

# 查看 GPU 信息
lspci | grep -i nvidia

# 查看显示器信息
xrandr

# 查看 shell
cat /etc/shells

# 查看当前 shell
echo $0
echo $SHELL

# 设置默认 shell 
chsh -s /bin/zsh
sudo chsh -s /usr/bin/zsh root

# 设置 root 密码
sudo passwd root

# 安装 ifconfig
sudo apt install net-tools

# 查看 ip 地址 Linux/macOS
ifconfig
```


---

### 相关问题

- 用户无 sudo 权限：
	- 问题：`xxx is not in the sudoers file`
	- 解决方法：切换到 root 用户，修改 `/etc/sudoers` 内容

```bash
# User privilege specification
root    ALL=(ALL:ALL) ALL
# add
xxx    ALL=(ALL:ALL) ALL
```

- Ubuntu KDE 关闭开机时的虚拟键盘：[KDE Plasma, virtual keyboard on login - Ask Ubuntu](https://askubuntu.com/questions/1445190/kde-plasma-virtual-keyboard-on-login)

- 双系统 Win 比 Ubuntu 慢 8 小时：[怎样解决Windows10时间快和Ubuntu时间差问题？ - 知乎](https://www.zhihu.com/question/46525639)

```bash
timedatectl set-local-rtc 1
```

- 连接校园网：[Linux设备连接校园SJTU无线网络说明-上海交通大学网络信息中心](https://net.sjtu.edu.cn/info/1215/2712.htm)

- [ ] 触控板，如何右键？



---

## Arch Linux 使用

- 参考资料：
	- [Arch Linux 安装使用教程 - ArchTutorial - Arch Linux Studio](https://archlinuxstudio.github.io/ArchLinuxTutorial/#/)
	- [archlinux 简明指南 | archlinux 简明指南](https://arch.icekylin.online/)


---

### 安装

archinstall：安装过程会有引导；已集成到安装镜像中，无需额外安装


---

### 基础设置

#### 换源

Arch Linux 软件源镜像：[archlinux - 清华大学镜像](https://mirrors.tuna.tsinghua.edu.cn/help/archlinux/)

```bash
# 备份
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak

# 在文件头部添加镜像源
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch 

# 更新
pacman -Syy
```


---

#### Vim 相关设置

Arch Linux 中的 Vim，鼠标右键进入插入的块模式，而不是复制文本

解决方法：创建 `~/.vimrc` 文件即可恢复（insert 和 normal 模式均可右键实现复制文本）


---

#### 安装中文字体

```bash
# 文泉驿正黑字体
sudo pacman -S wqy-zenhei

# 在~/.vimrc中添加
set encoding=utf-8
```


---

#### 安装 yay

AUR 介绍： archlinux user repository。任何用户都可以上传自己制作的 AUR 包，这也是 Arch Linux 可用软件众多的原因。由于任何人都可上传，也存在对应的风险，一般选用大众认可的包即可。使用 `yay` 或 `paru` 可以安装 AUR 中的包。

```bash
wget https://raw.githubusercontent.com/ArchLinuxStudio/ArchLinuxTutorial/master/docs/res/yay-bin-11.1.2-1-x86_64.pkg.tar.zst

sudo pacman -U yay-bin-11.1.2-1-x86_64.pkg.tar.zst
```

>`yay` 安装的包通常位于 `~/.cache/yay` 目录中。每个包都会被下载和存储在以包名称命名的子目录中


---

#### pacman 常用命令

>`yay` 命令与其类似

- `pacman -Syu` - 系统更新，同步软件仓库并升级系统
- `pacman -Syyu` - 强制刷新软件仓库数据库并系统完全升级
- `pacman -S <package>` - 安装 package
- `pacman -Rs <package>` - 删除 package，保留配置文件
- `pacman -Rns <package>` - 删除 package 和配置文件
- `pacman -Q <package>` - 查看 package 详情信息
- `pacman -Qs <string>` - 搜索含有 string 的 package
- `pacman -Qdt` - 列出系统中所有没用的依赖包
- `pacman -Sc` - 清理 package 缓存
- `pacman -Ss <string>` - 搜索含有 string 的已安装和可安装的 package
- `pacman -Qi <package>` - 查看已安装 package 的详情
- `pacman -Sw <package>` - 下载 package 而不安装
- `pacman -U /path/to/package.tar.xz` - 安装本地 package


查看可执行命令是通过安装哪个 package 得到的

```bash
pacman -Qo $(which gfortran)
```


---

### 相关问题

#### plasma 组件相关

完全卸载 plasma 组件：[[SOLVED] Help removing plasma and kde-applications / Newbie Corner / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=269353)

```bash
# 查看安装的 plasma 组件（desktop 等）
pacman -Q | grep plasma

# 卸载 plasma 组件
sudo pacman -Rcns plasma
```


---

## 常用编程程序安装

### tree

```bash
sudo apt install tree
```

源码编译

```bash
# 可能会连接不上
wget https://mama.indstate.edu/users/ice/tree/src/tree-2.1.1.tgz --no-check-certificate

make PREFIX=. install && make clean
```


---

### g++、gcc

```bash
sudo apt install build-essential

sudo pacman -S gcc
```


---

### gfortran

```bash
sudo apt install gfortran

sudo pacman -S gcc-fortran
```


---

### clang

```bash
sudo apt install clang

sudo pacman -S clang

bash -c "$(wget -O - https://apt.llvm.org/llvm.sh)"
```


---

### cmake

```bash
sudo apt install cmake
```


---

### C++ Tools

>[GitHub - include-what-you-use/include-what-you-use: A tool for use with clang to analyze #includes in C and C++ source files](https://github.com/include-what-you-use/include-what-you-use#how-to-install)

>[README\_dependencies.md](https://github.com/cpp-best-practices/infiz/blob/main/README_dependencies.md)

cppcheck：开源的 C/C++ 代码静态分析工具，用于检测源代码中的潜在错误和代码质量问题

conan：开源的 C/C++ 包管理器，用于管理和构建 C/C++ 依赖项、库和二进制包

```bash
sudo apt-get install doxygen
sudo apt-get install graphviz

sudo apt-get install ccache

sudo apt-get install cppcheck

sudo pacman -S cppcheck

sudo pacman -S conan

pip install conan
```


ARM 交叉编译工具
>[linaro公司：交叉编译器 arm-linux-gnueabi 和 arm-linux-gnueabihf 的区别\_学无止境2022的博客-CSDN博客](https://blog.csdn.net/dianqicyuyan/article/details/122979359)

---

### gsl

>[14.04 - GSL libray and header paths - Ask Ubuntu](https://askubuntu.com/questions/710907/gsl-libray-and-header-paths)

```bash
sudo apt install libgsl-dev
# 头文件及库文件路径 /usr/include/gsl /usr/lib/x86_64-linux-gnu

sudo pacman -S gsl
# 头文件及库文件路径 /usr/include/gsl /usr/lib
```

源码编译

```bash
wget https://mirror.ibcp.fr/pub/gnu/gsl/gsl-latest.tar.gz

./configure --prefix=${HOME}/src/gsl

make && make install
```


---

### voro++

无 root 权限时，需修改 `config.mk` 文件中的 `PREFIX` 内容 `PREFIX=${HOME}/src/voro++`，再编译安装

```bash
# Ubuntu 需源码编译
wget https://math.lbl.gov/voro++/download/dir/voro++-0.4.6.tar.gz

tar -xzvf voro++-0.4.6.tar.gz
cd voro++-0.4.6

make && sudo make install
# 头文件及库文件路径 /usr/local/include/voro++ /usr/local/lib

yay -S voro++  # Arch Linux
# 头文件及库文件路径 /usr/include/voro++ /usr/lib
```



---

### Open MPI

```bash
sudo apt install openmpi-bin libopenmpi-dev

sudo pacman -S openmpi
```

---

查看 OpenMPI 的头文件路径

```bash
mpicc -showme:compile
```


---

### boost

```bash
sudo apt install libboost-all-dev
```


---

### ninja

构建工具

```bash
sudo apt install ninja-build

sudo pacman -S ninja
```


---

### protobuf

一种轻量级的数据序列化格式

```bash
sudo apt install protobuf-compiler libprotobuf-dev

sudo pacman -S protobuf
```


---

### 其他

- 安装 tcsh（csh 通常作为 tcsh 的链接或别名；tcsh 是 C Shell 的增强版）

```bash
sudo apt install tcsh
```

- 查看图片：imagemagick 和 eog

```bash
sudo apt install imagemagick
sudo apt install eog

display figure
identify figure  # 显示图片信息

eog figure
```



---

## Virtualbox 虚拟机使用

### 基础设置

全局设定：

- 修改默认虚拟电脑位置：`D:\Oracle\VirtualBox VMs`
- 取消自动独占键盘

---

安装的虚拟机设置：

- 常规 - 高级：共享粘贴板和拖放设置成“双向”
- 网络 - 网卡 1：网络地址转换 (NAT)

---

虚拟机安装增强功能：设备 - 安装增强功能；打开 iso 镜像文件，右键运行 `autorun.sh` 文件


---

### 相关问题

Ubuntu2204 的 Terminal 无法打开：[VirtualBox\_Ubuntu22.10\_Terminal无法打开\_虚拟机打不开终端\_gt29的博客-CSDN博客](https://blog.csdn.net/weixin_43959807/article/details/128872860)

虚拟机使用主机代理：[Virtualbox+Uubntu16.04 NAT模式下使用宿主机代理上网 - 水中墨色 - 博客园](https://www.cnblogs.com/veraland/p/13490217.html)


---

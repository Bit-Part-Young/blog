---
title: Linux 命令行工具
top: false
pin: false
cover: false
toc: true
mathjax: true
math: true
summary: Linux 命令行工具
tags:
  - CLI
categories:
  - Linux
date: 2023-09-18 09:00:00
abbrlink: 16854
password:
---

# Linux 命令行工具

## 介绍

命令行工具安装方式：

- Linux 端：Ubuntu（apt、snap 等）、Arch Linux（pacman、yay 等）；
- Windows 端：scoop、winget 等；
- Mac 端：brew；
- 程序端：Python（pip conda）、Rust（cargo）、Nodejs（npm）；
- [webinstall.dev](https://webinstall.dev/) 网站（后三者可以在无 root 权限情况下安装）；
- 源码安装与编译


参考资料：[GitHub - ibraheemdev/modern-unix: A collection of modern/faster/saner alternatives to common unix commands.](https://github.com/ibraheemdev/modern-unix)



---

## 常用终端工具

### zsh

- 提升终端使用体验。功能：命令自动补全、高亮、建议；简化 git 命令，git 状态可视化；`x` 解压任意格式压缩文件；`z` 路径快速跳转等）
- master、manager 上没有 zsh；Pi 和思源一号有 zsh，版本较老；
- zsh 系列插件：[awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins)
- 管理 zsh 配置：[ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)
- 管理 bash 配置：[oh-my-bash](https://github.com/ohmybash/oh-my-bash)（没 ohmyzsh 好用）


---

#### Linux 端安装配置 zsh

```bash
############ 安装 zsh ############
# Ubuntu
sudo apt install zsh
# Arch Linux
sudo pacman -S zsh


############ 安装 ohmyzsh ############
# gitee 源
# via curl
sh -c "$(curl -fsSL https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh)"
# via wget
sh -c "$(wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O -)"

# github 源
# via curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# via wget
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


############ 插件下载 ############
# 自动补全、高亮、建议：zsh-completions、zsh-syntax-highlighting、zsh-autosuggestions；
# 主题下载：powerlevel10k
# github 源
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM}/plugins/zsh-completions && \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions && \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting && \
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM}/themes/powerlevel10k

# gitee 源
git clone https://gitee.com/yuhldr/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting && \
git clone https://gitee.com/yuhldr/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions && \
git clone https://gitee.com/yuhldr/zsh-completions ${ZSH_CUSTOM}/plugins/zsh-completions && \
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM}/themes/powerlevel10k


############ 备份 ~/.zshrc（如果有）############
cp ~/.zshrc ~/.zshrc.bak

############ 更新 ohmyzsh ############
omz update

############ 配置 powerlevel10k ############
p10k configure
```

>下载安装好 ohmyzsh 和 powerlevel10k 后，重新登录，会进入配置 powerlevel10k 的交互，按照指示自定义设置即可。


---

ohmyzsh 有用的内置与外置插件：[Plugins · ohmyzsh/ohmyzsh Wiki · GitHub](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)

```bash
################ 内置插件 ################
# 目录自动跳转，模糊匹配最近进入过的目录
z
# 丰富的 git alias
git

################ 外置插件 ################
zsh-syntax-highlighting
zsh-autosuggestions
zsh-completions
```


---

#### Windows 端安装配置 zsh

两种方式：WSL+zsh，git bash+zsh：[Windows高效开发环境配置（一） - 北鱼扶摇](https://ifuyao.com/blog/install-zsh-and-oh-my-zsh-in-windows-git-bash/)、[在 Windows 中使用 Bash shell - 北辞](https://northword.cn/code/bash-for-windows/)

windows terminal 以及 vscode 本地设置默认终端为 git bash：[Windows Terminal添加Git Bash支持 - TruthHell - 博客园](https://www.cnblogs.com/cong-wang/p/15026535.html)

---

- 下载 zsh 包

```bash
wget https://mirror.msys2.org/msys/x86_64/zsh-5.9-2-x86_64.pkg.tar.zst

tar --zstd -xvf zsh-5.9-2-x86_64.pkg.tar.zst
```

- 复制 `etc/`、`usr/` 到 Git 安装目录中
- 打开 Git Bash，执行命令 `zsh`
- 设置 zsh 为默认 shell，在 `.bashrc` 添加

```bash
 # Enable zsh
 if [ -t 1 ]; then
    exec zsh
 fi
```

- 安装、配置 ohmyzsh
- 修改 Windows Terminal 的 `settings.json` 内容

```json
{
    // ...
    // 添加项 
    // 默认启动为 Git Bash
    "defaultProfile": "{5D1F95DF-36E8-56AD-C203-EA75CE06422C}",
    // "defaultProfile": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
    // ...
        "list": 
        [			
            // 添加项
	        {
                "guid" : "{5D1F95DF-36E8-56AD-C203-EA75CE06422C}",
                "name" : "Git Bash",
                "commandline" : "D:\\Scoop\\apps\\git\\current\\bin\\bash.exe --login -i",
                "icon" : "D:\\Scoop\\apps\\git\\current\\usr\\share\\git\\git-for-windows.ico",
                "startingDirectory": "C:\\Users\\SLY\\Desktop"
            },
		    // ...
        ],
    },
}
```


---

#### 源码编译

服务器及超算平台需源码编译 zsh：[Building Zsh from Source and Configuring It on CentOS - jdhao's digital space](https://jdhao.github.io/2018/10/13/centos_zsh_install_use/)

---

- 编译 ncurses

```bash
wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.4.tar.gz --no-check-certificate

./configure --prefix=${HOME}/local CXXFLAGS="-fPIC" CFLAGS="-fPIC"

make -j && make install
```

---

- 编译 zsh

```bash
wget https://sourceforge.net/projects/zsh/files/zsh/5.9/zsh-5.9.tar.xz/download -O zsh-5.9.tar.xz --no-check-certificate

./configure --prefix="${HOME}/local" \ CPPFLAGS="-I${HOME}/local/include" \ LDFLAGS="-L${HOME}/local/lib"

make -j && make install
```

---

- 设置 zsh 为默认 shell：有 root 权限：`chsh -s /bin/zsh`；无 root 权限：在 `~/.bashrc_profile` 添加以下内容（不建议）

```bash
export PATH=$HOME/bin:$PATH
export SHELL=`which zsh`
[ -f "$SHELL" ] && exec "$SHELL" -l
```


---

#### 相关问题

- zsh 中的 `[nyae]` 的含义：[What does nyae mean in Zsh? - Stack Overflow](https://stackoverflow.com/questions/800182/what-does-nyae-mean-in-zsh)
- zsh 安装后，可能会出现 `Home / End` 失灵问题，使用对应的快捷键：`Home = Ctrl + A`，`End = Ctrl + E`。


---

### 其他终端工具

- 替代 `ls`：[lsd](https://github.com/lsd-rs/lsd)（可下载二进制文件，x86_64-unknown-linux-gnu 版本）、[exa](https://github.com/ogham/exa)
- 替代 `grep`：[ripgrep](https://github.com/BurntSushi/ripgrep)（可执行命令为 `rg`）
- 替代 `cat`：[bat](https://github.com/sharkdp/bat)
- 替代 `find`：[fd](https://github.com/sharkdp/fd)
- 替代 `ps`：[procs](https://github.com/dalance/procs)
- 终端 markdown 渲染：[frogmouth](https://github.com/Textualize/frogmouth)、[glow](https://github.com/charmbracelet/glow)
- git 相关：[lazygit](https://github.com/jesseduffield/lazygit)
- 显示系统信息：[neofetch](https://github.com/dylanaraps/neofetch)
- 磁盘分析：[ncdu](https://dev.yorhel.nl/ncdu)
- 文件对比：[difftastic](https://github.com/Wilfred/difftastic)
- 文件搜索：[fzf](https://github.com/junegunn/fzf)
- 文件管理：[yazi](https://github.com/sxyazi/yazi)、[ranger](https://github.com/ranger/ranger)
- 快速查看常用命令的使用实例：[tldr](https://github.com/tldr-pages/tldr)（有时会失效）
- 富文本：[rich](https://github.com/textualize/rich)
- 命令纠正：[thefuck](https://github.com/nvbn/thefuck)
- 将源代码生成美观图片：[silicon](https://github.com/Aloxaf/silicon)、[carbon](https://github.com/carbon-app/carbon)
- neovim 配置：[lazyvim](https://github.com/LazyVim/LazyVim)（siyuan 无法使用）
- 其他小工具： cowsay、figlet、sl、fortune（幸运饼干；格言）、lolcat、boxes、cmatrix、asciiquarium

---

ripgrep 过滤搜索：`-g` 参数

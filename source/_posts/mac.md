---
title: Mac 使用
top: false
pin: false
cover: false
toc: true
mathjax: true
math: true
summary: Mac 使用
tags:
  - Mac
categories:
  - Linux
date: 2023-12-15 14:45:00
abbrlink: 8586
password:
---

# Mac 使用

## 介绍

Macbook Air 很轻便；续航很强；音响很好；触控板功能丰富…


---

### 参考资料

>[awesome-mac](https://github.com/jaywcjlove/awesome-mac)

>[GitHub - nikitavoloboev/my-mac: Apps/tools I use on macOS](https://github.com/nikitavoloboev/my-mac)

>[GitHub - serhii-londar/open-source-mac-os-apps: 🚀 Awesome list of open source applications for macOS. https://t.me/s/opensourcemacosapps](https://github.com/serhii-londar/open-source-mac-os-apps)

>[GitHub - itcharge/macOS-Tips: macOS 系统的使用技巧介绍、常用软件推荐、效率工具推荐。](https://github.com/itcharge/macOS-Tips)

>[大洋的朝九晚十的个人空间-大洋的朝九晚十个人主页-哔哩哔哩视频](https://space.bilibili.com/33734786)


---

## 使用

### 基本设置

- 不同的 macOS 版本对应的操作设置会有不同，建议在官网上查询
- Mac 中的大部分程序的**设置快捷键**都是 `command + ,`
- 正常的鼠标接入 Mac，滚轮控制的上下滚动与 Windows 是相反的
- macOS 对大小写不敏感，Linux 和 Windows 对大小写敏感
- [修改用户名](https://support.apple.com/zh-cn/102547)
- [删除用户](https://support.apple.com/zh-cn/guide/mac-help/mchlp1557/mac)
- [Apple ID 申请](https://support.apple.com/zh-cn/108647)
- 英文大小写转换：点按「中/英」键即可切换中英文；切换成大写，长按两秒「中英」键，直至亮灯；按住 shift 键的同时输入字母
- 程序坞（dock）相关：双手指点击触控板的软件 logo，可将软件 logo 在程序坞中保留或移除，进而从 dock 中移除一些不常用的软件 logo
- 小组件设置：点击菜单栏右上角的时钟，会有其他的小组件，可移除，保留“每日使用情况”小组件
- 默认终端 Theme 设置：设置 - Profile - Pro Theme，点击下方的默认按钮
- Mac 合盖不休眠：连接电源、键鼠即可
- 程序坞呼出时长设置

```bash
# 程序坞立即呼出
defaults write com.apple.dock "autohide-delay" -float "0" && killall Dock

# 恢复默认程序坞呼出时长
defaults delete com.apple.dock "autohide-delay" && killall Dock​
```

- [ ] 修改 Mac 邮箱

---

#### 系统设置相关

- 修改系统语言：系统设置 - 语言和地区 - 简体中文，将其向上拖到第一个
- macOS 版本升级到最新：系统设置 - 通用 - 软件更新
- 修改电脑名称：系统设置 - 通用 - 关于本机
- 文本字体：系统设置 - 文本字体（使用 `MesloLGM Nerd Font`）
- 菜单栏设置：系统设置 - 控制中心 - 选择模块应用“不在菜单栏显示”
- 台前调度：系统设置 - 桌面与程序坞 - 桌面与台前调度 - 打开 “台前调度”
- 去掉留在程序坞中最近打开过的软件：系统设置 - 桌面与程序坞 - 取消勾选“在程序坞中显示建议 App 和最近使用的 App”
- 关闭开机时的声音：系统设置 - 声音 - 取消勾选“启动时播放声音”
- 调整键盘背光、键重复速率和重复前延迟：系统设置 - 键盘
- 显示电池百分比：系统设置 - 控制中心 - 电池 - 显示百分比
- 时钟 24 小时格式：系统设置 - 日期与时间 - 24 小时制
- 外部显示器设置：系统设置 - 显示器 - 内建显示器用作主显示器，适配此 Mac 名称；外部显示器用作内建显示器的镜像，适配此 Mac 名称


---

#### 访达相关

- 访达：显示路径栏和状态栏，鼠标靠近路径栏，右键可以拷贝路径名称
- 隐藏 “最近使用” ：访达 - 设置 - 边栏 - 取消勾选“最近使用”
- 文件夹用图标展示时，右键 - 查看显示选项 - 勾选“显示项目简介”和“用作默认”
- 访达可以打开多个标签页，打开多个窗口时，可以合并所有窗口
- 右键文件，选择快速操作，有“创建 PDF”、“转换图像”、“移除背景”等操作
- 按住 `command` 键，可以将文件夹拖到工具栏中，实现快速访问
- 更改同类型文件的默认打开方式：右键 - 显示简介 - 打开方式，选择指定的默认应用程序，全部更改；[基础教程：如何更改 Mac 文件的默认打开方式 - 少数派](https://sspai.com/post/28394)


---

#### 触控板相关

>三指拖移会与三指上下左右轻扫会冲突，不能同时设置

- 三指拖移文件/文件夹/窗口：系统设置 - 辅助功能 - 指针控制 - 触控板选项 - 拖移样式 - 三指拖移
- 切换全屏显示的程序：四指左右轻扫
- 调度中心：四指上下轻扫（比 `command + tab` 要简便一些）
- 返回桌面：四指向外扩展


---

#### 快捷键

快捷键：[macOS常用快捷键.md](https://github.com/itcharge/macOS-Tips/blob/main/02%20-%20macOS%20%E5%B8%B8%E7%94%A8%E5%BF%AB%E6%8D%B7%E9%94%AE.md)、[Mac 键盘快捷键 - 官方 Apple 支持 (中国)](https://support.apple.com/zh-cn/HT201236)

- `command + Space` - 聚焦搜索（没有 Alfred 的 `option + Space` 好用）
- `Space` - 预览功能
- `Control ⌃ + Left ⬅︎ / Right ➡︎` - 左右切换「空间」（有全屏的窗口的话）
- `command + Q` - 退出程序（macOS 关闭窗口不是完全退出程序）
- `command + ⬆️/⬇️` - 返回上一层文件夹；进入文件夹
- `command + shift + G` 打开“前往文件夹” 窗口
- 打开 Alfred，输入 `Restart`、`Sleep`、`Shut down` 实现重启、睡眠、关机
- 返回桌面 - `command + F3`

注：无 Windows 的 `Win + X` 等效快捷键


---

### 软件/程序安装及设置

>网络上下载的程序包安装到 Mac 上，需将包（`*.app`）移动到 applications 里

- 软件包安装、管理工具：Homebrew
- 文件搜索、程序启动工具：Alfred 5
- VPN 网络代理：ClashX
- 代码编辑器：vscode-insiders（**vscode-insdiers 的命令行启动工具需在官网上下载 CLI 版本，解压将其拷贝到 bin 目录中**）
- 终端工具：使用 iTerm
- 远程服务器连接工具：Termius
- 数据同步：交大云盘
- 浏览器： Chrome
- 压缩文件解压工具：The Unarchiver
- 媒体播放器：IINA（开源）、Infuse（apple store 付费）
- 笔记管理：Obsidian、Typora
- 图床：PicGo
- 文献管理：Zotero
- 构型可视化：VESTA、OVITO
- 邮件服务：Mailspring 或 Mac 自带邮件
- 截图：Snipaste（可通过 brew 安装）
- 文本翻译：Bob（社区版免费，翻译引擎需自己设置；app store 版本需收费）
- 垃圾清理：Cleaner One Pro（可查看 CPU、内存、电池、垃圾文件等情况；完整版本需收费）、CleanMyMac X（完整版本需收费）
- 系统资源监控：RunCat
- 快捷键提示：flykey
- 切换窗口：alt-tab
- 鼠标：mos
- 输入法切换：自动切换输入法 Lite 版
- pdf 查看、编辑：updf
- 窗口管理：Rectangle
- 其他：微信等


---

#### Homebrew 使用

大部分命令行工具及开源程序都可以通过 Homebrew 安装（类似 Windows 上的 Scoop）。

加速安装 Homebrew：[安装和使用 Homebrew｜韬秧道](https://blog.tauyoung.top/article/Homebrew/)

相关命令：[Homebrew 备忘清单 &  homebrew cheatsheet &  Quick Reference](https://quickref.me/zh-CN/docs/homebrew.html)

```bash
# 查找包
brew search <package>

# 安装
brew install <package>

# 卸载
brew uninstall <package>

# 显示已安装的包
brew list

# 显示可以升级的包
brew outdated

# 升级
brew upgrade
brew upgrade <package>

# Homebrew-cask 管理桌面程序

# 忽视依赖关系卸载
brew uninstall --ignore-dependencies gcc

# 显示安装包、文件数量，和总占用空间
brew info

# 查看已安装的包的依赖，树形显示
brew deps --installed --tree

# 查看可清理的旧版本包
brew cleanup -n
# 清理所有包的旧版本
brew cleanup
# 删除缓存
brew cleanup --prune=all

# 锁定包
brew pin <package>
# 取消锁定
brew unpin <package>
```


---

wget 安装（可能较耗时）

---

 字体安装

>[PowerShell with Oh My Posh as Default Shell on macOS - Half-Blood Programmer](https://halfblood.pro/powershell-on-macos/)

```bash
# nerd font 字体
brew tap homebrew/cask-fonts
brew install --cask font-meslo-lg-nerd-font
brew install --cask font-hack-nerd-font

# 可用 nerd font
brew search '/font-.*-nerd-font/' | awk '{ print $1 }'

# 得意黑字体
brew install font-smiley-sans

# Mac 字体路径
# 系统
/Library/Fonts
# 用户
~/Library/Fonts
```


---

#### Termius

- 支持 Windows Mac Linux iPad Android，多端数据记录同步
- 可 ssh 远程连接和 sftp 远程文件传输
- 可进行学生认证
- 可保存并显示历史命令
- 可保存自定义 Theme

---

适合的 Theme：

- Monokai
- Pro
- Solarized Dark（个人主要采用该 Theme）
- Atom One Dark
- Tokyo Night

---

- 设置 font：设置 - Terminal - Text Size 上方，选择“Meslo”
- 连接本地终端：Hosts - TERMINAL

---


iTerm 字体设置：Prefrences - profiles - text

---

IINA 相关快捷键：

- 倍速播放
	- `command + ]` - 1/2/4 倍速加快
	- `command + option + ]` - 1.1 倍速加快
- 字幕切换 - `control + command + S`
- 音频切换 - `control + command + A`


---

#### MacTeX 安装与卸载

- 安装：[MacTeX - TeX Users Group](https://www.tug.org/mactex/mactex-download.html)；在官网上下载最新 pkg 包，双击，按照提示安装
- 卸载：[Uninstalling - MacTeX - TeX Users Group](https://tug.org/mactex/uninstalling.html)；卸载 GUI，直接将 TeX 移入废纸篓；卸载 TeX Distribution；卸载 Ghostscript

```bash
sudo rm -rf /Library/TeX
sudo rm -rf /usr/local/texlive
```



---

#### Mac 端没有的一些软件

- PotPlayer
- Notepad++
- MobaXterm
- WinSCP


---

### 编程相关

- macOS 版本不同，Homobrew 之前安装的程序有可能会出现不兼容的情况
- Miniconda3 安装：需要与芯片类型（如 M1）适配
- Mac 的 gcc 和 g++ 编译器 默认是 clang 的；建议安装 gcc 套件

```bash
ln -s /opt/homebrew/bin/g++-13 ~/bin/g++
ln -s /opt/homebrew/bin/gcc-13 ~/bin/gcc
```

- clang 没有 `fopenmp` 选项

```bash
clang: error: unsupported option '-fopenmp'
make: *** [atom.o] Error 1
```

- Homebrew 安装的 voro++ 在编译 latgen 时会出问题，建议源码编译
- brew 安装的 gsl 编译 dumpana 出现以下报错（源码编译也有）

```bash
spherical.cpp:4:10: fatal error: gsl/gsl_sf_coupling.h: No such file or directory
    4 | #include "gsl/gsl_sf_coupling.h"
      |          ^~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make: *** [spherical.o] Error 1
```




---

## 相关问题

### git 相关

macOS 11 升级至最新时，git 出现以下报错：

```bash
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

解决方法：`xcode-select --install`


---

### vscode-insiders 相关

- 如何将 vscode-insiders 从 Downloads 放入到 Applications（可直接拖到侧边栏的 Applications 中）：[Moving VS Code Insiders ARM to programs "folder" on M1 mac makes it unable to start (crashes/exits immediately). Can only start from "downloads" folder · Issue #113751 · microsoft/vscode · GitHub](https://github.com/microsoft/vscode/issues/113751)
- 切换不同的实例窗口：双指点击 vscode 软件 logo，会显示不同窗口，选中其中一个
- 终端切换（Windows 端的快捷键无法切换）
	- 上下关系 - `shift + command + [ / ]`
	- 左右关系 - `option + command + Left ⬅︎ / Right ➡︎`
	- 命令面板 - 聚焦下一终端组 / 在终端组聚焦下一终端
- Mac 的 vsocde 系列中的 Vim 插件快捷键无法连续移动：[GitHub - VSCodeVim/Vim: :star: Vim for Visual Studio Code](https://github.com/VSCodeVim/Vim#mac)

```bash
$ defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false              # For VS Code
$ defaults write com.microsoft.VSCodeInsiders ApplePressAndHoldEnabled -bool false      # For VS Code Insider
```


---

### Mac 软件安装问题

- 身份不明开发者：右键打开文件，非双击，弹出的窗口会有打开按钮；[Mac如何打开身份不明开发者的程序？ - 知乎](https://www.zhihu.com/question/52623818)
- [Apple 无法检查 App 是否包含恶意软件 - 官方 Apple 支持 (中国)](https://support.apple.com/zh-cn/guide/mac-help/mchleab3a043/mac)
- PicGo 安装显示文件已损坏：[PicGo arm64文件已损坏](https://github.com/Molunerfinn/PicGo/issues/1055)

```bash
sudo xattr -d com.apple.quarantine "/Applications/PicGo.app"
```


---

### 其他

- 文件创建 Mac 无法直接创建文件（可通过终端 `touch` 命令或安装 “超级右键”软件），只能创建文件夹
- Apple ID 相关问题：此 Apple ID 尚未在 app store 使用（弹出“检查”窗口时，会出现要求完善支付方式信息内容；macOS 11 在检查这步一直无法弹出后面的内容，将版本更新至最新无此问题）
- 蓝牙耳机连接：长按 Redmi Airdots3 Pro 耳机盒的开关机键；将 Bose qc45 电源键推至右侧一段时间
- [Word for Mac彻底删除Endnote插件的方法 - 知乎](https://zhuanlan.zhihu.com/p/29321865)

---
title: Mac 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Mac 使用
description: Mac 使用
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

- Macbook Air 轻便；续航强；音响音质好；触控板功能丰富...

- 明确 Macbook 购买机型：
	- [Mac - 机型比较](https://www.apple.com.cn/mac/compare/)
	- [2024年苹果 MacBook 选购指南(MacBook Air/Pro 的 M123/Pro/Max/Ultra有什么区别，13/14/15/16寸怎么选)](https://www.zhihu.com/tardis/zm/art/378347974?source_id=1003)

- 2024.08.19：M1 pro 电池健康 98%

- macOS 可以运行的游戏：[Mac能玩哪些游戏？实测5种游玩方式\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Vy421a7Rd)
	- 运行 Windows 3A 游戏：使用 Game Porting Toolkit


---

### 参考资料

- [Mac：终极配置教程 - BLOG](https://44maker.github.io/wiki/Mac/index.html)
- [GitHub - maoxiaoke/setup-a-mac-for-frontend-dev: How I setup a Mac, with lots of productivity tools, step-by-step guide](https://github.com/maoxiaoke/setup-a-mac-for-frontend-dev)
- [awesome-mac](https://github.com/jaywcjlove/awesome-mac)
- [GitHub - nikitavoloboev/my-mac: Apps/tools I use on macOS](https://github.com/nikitavoloboev/my-mac)
- [GitHub - serhii-londar/open-source-mac-os-apps: 🚀 Awesome list of open source applications for macOS. https://t.me/s/opensourcemacosapps](https://github.com/serhii-londar/open-source-mac-os-apps)
- [GitHub - itcharge/macOS-Tips: macOS 系统的使用技巧介绍、常用软件推荐、效率工具推荐。](https://github.com/itcharge/macOS-Tips)
- [Mac\_张的个人空间-Mac\_张个人主页-哔哩哔哩视频](https://space.bilibili.com/49574614)
- [大洋的朝九晚十的个人空间-大洋的朝九晚十个人主页-哔哩哔哩视频](https://space.bilibili.com/33734786)
- [GitHub - macdao/ocds-guide-to-setting-up-mac: OCD's Guide to Setting up Mac](https://github.com/macdao/ocds-guide-to-setting-up-mac)
- [摸鱼人的 macOS 工作流 - 水源社区](https://shuiyuan.sjtu.edu.cn/t/topic/282518)



---

## 使用

### 基本设置

- 不同的 macOS 版本对应的操作设置会有不同，建议在官网上查询
- MacBook 中的大部分程序的**设置快捷键**都是 `command + ,`
- MacBook 接入鼠标 ，滚轮控制的上下滚动与 Windows 相反（可借助 Mos 软件使其保持一致）
- macOS 对大小写不敏感，Linux 和 Windows 对大小写敏感
- [修改用户名](https://support.apple.com/zh-cn/102547)：需创建另一个用户，登录该用户，在其系统设置中修改原用户名
- [删除用户](https://support.apple.com/zh-cn/guide/mac-help/mchlp1557/mac)
- [Apple ID 申请](https://support.apple.com/zh-cn/108647)
- 英文大小写转换：点按「中/英」键即可切换中英文；切换成大写，长按两秒「中英」键，直至亮灯；按住 shift 键的同时输入字母
- 程序坞（Dock）相关：双手指点击触控板的软件 logo，可将软件 logo 在程序坞中保留或移除，进而从 Dock 中移除一些不常用的软件 logo
- 小组件设置：点击菜单栏右上角的时钟，会有其他的小组件，可移除，保留 “每日使用情况” 小组件
- 默认终端 Theme 设置：设置 - Profile - Pro Theme，点击下方的默认按钮
- MacBook 合盖不休眠：系统设置 - 电池 - 勾选 “使用电源适配器供电且显示器关闭时，防止自动进入睡”

- 接入 Windows 键盘，进行修饰键的键位重映射：
	- Alt（相当于 option 键）和 Win 键（相当于 command 键）互换，Fn 和 Ctrl 键无法互换（联想 USB 薄膜键盘）；
	- [Mac电脑 + Windows机械键盘？功能键映射了解一下说起 Mac 电脑最独特的地方的话，就是它的操作系统了。mac - 掘金](https://juejin.cn/post/6948294239960694797)；
	- [在 Mac 上更改修饰键的行为 - 官方 Apple 支持 (中国)](https://support.apple.com/zh-cn/guide/mac-help/mchlp1011/mac)

- 程序坞呼出时长设置：

```bash
# 程序坞立即呼出
defaults write com.apple.dock "autohide-delay" -float "0" && killall Dock

# 恢复默认程序坞呼出时长
defaults delete com.apple.dock "autohide-delay" && killall Dock​
```

- [ ] 修改 MacBook 邮箱

---

#### 系统设置相关

- 修改系统语言：系统设置 - 语言和地区 - 简体中文，将其向上拖到第一个
- macOS 版本升级到最新：系统设置 - 通用 - 软件更新
- 修改电脑名称：系统设置 - 通用 - 关于本机
- 文本字体：系统设置 - 文本字体（使用 `MesloLGM Nerd Font`）
- 菜单栏设置：系统设置 - 控制中心 - 选择模块应用 “不在菜单栏显示”
- 台前调度：系统设置 - 桌面与程序坞 - 桌面与台前调度 - 打开 “台前调度”
- 去掉留在程序坞中最近打开过的软件：系统设置 - 桌面与程序坞 - 取消勾选 “在程序坞中显示建议 App 和最近使用的 App”
- 关闭开机时的声音：系统设置 - 声音 - 取消勾选 “启动时播放声音”
- 调整键盘背光、键重复速率和重复前延迟：系统设置 - 键盘
- 显示电池百分比：系统设置 - 控制中心 - 电池 - 显示百分比
- 时钟 24 小时格式：系统设置 - 日期与时间 - 24 小时制
- 外部显示器设置：系统设置 - 显示器 - 内建显示器用作主显示器，适配此 MacBook 名称；外部显示器用作内建显示器的镜像，适配此 MacBook 名称
- 摇动鼠标指针以定位：系统设置 - 辅助功能 - 显示 - 指针，摇动鼠标指针以定位（快速移动鼠标指针以使其变大）


---

#### 访达相关

- 访达：显示路径栏和状态栏，鼠标靠近路径栏，右键可以拷贝路径名称
- 隐藏 “最近使用” ：访达 - 设置 - 边栏 - 取消勾选 “最近使用”
- 文件夹用图标展示时，右键 - 查看显示选项 - 勾选 “显示项目简介” 和 “用作默认”
- 访达可以打开多个标签页，打开多个窗口时，可以合并所有窗口
- 右键文件，选择快速操作，有 “创建 PDF”、“转换图像”、“移除背景”等操作
- 按住 `command` 键，可以将文件夹拖到工具栏中，实现快速访问
- 更改同类型文件的默认打开方式：选中文件，右键 - 显示简介 - 打开方式，选择指定的默认应用程序，全部更改；[基础教程：如何更改 Mac 文件的默认打开方式 - 少数派](https://sspai.com/post/28394)


---

#### 触控板相关

>三指拖移会与三指上下左右轻扫会冲突，不能同时设置

- 三指拖移文件/文件夹/窗口：系统设置 - 辅助功能 - 指针控制 - 触控板选项 - 拖移样式 - 三指拖移
- 切换全屏显示的程序：四指左右轻扫
- 调度中心：四指上下轻扫（比 `command + tab` 要简便一些）
- 返回桌面：四指向外扩展；可设置**触发角**，使光标移动到屏幕右下角时返回桌面


---

#### 快捷键

参考：[macOS常用快捷键.md](https://github.com/itcharge/macOS-Tips/blob/main/02%20-%20macOS%20%E5%B8%B8%E7%94%A8%E5%BF%AB%E6%8D%B7%E9%94%AE.md)、[Mac 键盘快捷键 - 官方 Apple 支持 (中国)](https://support.apple.com/zh-cn/HT201236)

快捷键：

- 剪切移动文件：`command + C` 复制，然后 `command + option + V` 将其移动到目标目录
- 删除文件：`command + delete`
- `command + Space` - 聚焦搜索（没有 Alfred 的 `option + Space` 好用）
- `Space` - 预览功能
- `control + ⬅︎ / ➡︎` - 左右切换「空间」（有全屏的窗口的话）
- `command + Q` - 退出程序（macOS 关闭窗口不是完全退出程序）
- `command + ⬆️ / ⬇️` - 返回上一层文件夹；进入文件夹
- `command + shift + G` 打开 “前往文件夹” 窗口
- 打开 Alfred，输入 `Restart`、`Sleep`、`Shut down` 实现重启、睡眠、关机
- 返回桌面 - `command + F3`
- 更加细致地调节音量、亮度：`option + shift + F1/2/11/12`
- `option + command + 5`：显示截图、录屏选项
- `option + command + esc`：强制退出应用程序
- `command + ~`：切换同一个程序下的窗口

注：无 Windows 的 `Win + X` 等效快捷键


---

### 软件/程序安装及设置

- 网络上下载的程序安装包安装到 Mac 上，需将包（`*.app`）移动到 Applications 里；卸载：直接将其移到废纸篓
- [macOS 破解软件、游戏](https://appstorrent.ru/)
- [🍏 我的 macOS 常用软件 - 老胡的周刊](https://weekly.howie6879.com/soft/mac.html)
- [GitHub - hzlzh/Best-App: 收集&推荐优秀的 Apps/硬件/技巧/周边等](https://github.com/hzlzh/Best-App)
- [GitHub - Louiszhai/tool: 开发效率提升：Mac生产力工具链推荐](https://github.com/Louiszhai/tool)


---

#### 软件/程序推荐

- 包安装、管理工具：Homebrew
- 文件搜索、程序启动工具：Alfred 5、[Raycast](https://www.raycast.com/)
- 网络代理：ClashX
- 系统资源监控：iStat Menus、RunCat、[stats](https://github.com/exelban/stats)、[mactop](https://github.com/context-labs/mactop)、[asitop](https://github.com/tlkh/asitop)、[glances](https://github.com/nicolargo/glances)
- 代码编辑器：VSCode、VSCode-Insiders（VSCode-Insdiers 的命令行启动工具需在官网上下载 CLI 版本，解压将其拷贝到 bin 目录中）
- 终端模拟器：默认终端、iTerm2（最实用）、Tabby、Termius、kitty、[Warp](https://www.warp.dev/)（需注册；有 AI 功能）
- 浏览器：Safari、Chrome、Arc、Zen
- 压缩、解压缩工具：The Unarchiver
- 媒体播放器：IINA（免费）、Infuse（付费，有破解版）
- Markdown 笔记管理：Obsidian、Typora、MarkText
- 预览渲染后的 Markdown 文档：[QLMarkdown](https://github.com/sbarex/QLMarkdown)
- 打开当前路径下的终端：[OpenInTerminal](https://github.com/Ji4n1ng/OpenInTerminal)
- 图床：PicList（基于 PicGo 开发）、PicGo
- 文献管理：Zotero
- 构型可视化：VESTA、OVITO
- 邮件服务：Mailspring 或 Mac 自带邮件程序
- 截图：Snipaste、Shottr（可以长截图）
- 文本翻译：Bob（社区版免费，翻译引擎需自己设置；Apple Store 版本需收费）
- 垃圾清理：CleanMyMac X（完整版本需收费；有破解版）、Cleaner One Pro（可查看 CPU、内存、电池、垃圾文件等情况；完整版本需收费）
- 快捷键提示：FlyKey、CheatSheet
- 切换窗口：AltTab（显示窗口内容；`command + Tab` 键的窗口切换不会显示窗口内容）
- 鼠标滚轮方向切换：Mos、LinearMouse、Mac Mouse Fix
- 输入法切换：自动切换输入法 Lite 版、[Input Source Pro](https://inputsource.pro/zh-CN)
- pdf 阅读器：UPDF、skim、[sioyek](https://github.com/ahrm/sioyek)（支持部分 vim 快捷键）
- 窗口管理：Rectangle、Loop
- 菜单栏管理：Ice、Bartender
- 录屏：QuickRecorder
- 运行 Docker 容器、k8s 和 Linux：[orbstack](https://github.com/orbstack/orbstack)
- 电池电量：AirBattery（显示所有苹果产品设备电量）、Battery Buddy（可爱电池电量图标）
- 刘海屏相关：
	- 将刘海屏当作 AirDrop：NotchDrop、Folder Hub
	- 隐藏刘海屏：Only Switch（将菜单栏调成黑色）、zNotch（将菜单栏下移）、
	- 增加趣味：Notchmeister
- 控制外置显示器亮度：MonitorControl、BetterDisplay（功能更强大，需付费）
- 快捷功能集合：Only Switch（屏幕检测与清洁、推出磁盘映像、清空废纸篓等）
- 限制电池最大充电量：[bclm](https://github.com/zackelia/bclm)、AlDente
- 文件互传：LocalSend（跨平台）
- 文件同步：[Syncthing](https://github.com/syncthing/syncthing)（跨平台）、交大云盘
- 虚拟机：Parallels Desktop、VMware Fusion
- 剪贴板相关：[PasteBar](https://www.pastebar.app/)（Windows、macOS 平台，可预览剪贴内容）;[GitHub - CrossPaste](https://github.com/CrossPaste/crosspaste-desktop)（可剪贴文件）、Maccy
- 窗口平铺：tiling window manager；[yabai](https://github.com/koekeishiya/yabai)、[Amethyst](https://github.com/ianyh/Amethyst)
- macOS 截图转 LaTeX 公式：[Snap2LaTeX](https://github.com/ProfFan/Snap2LaTeX)、[snip2tex](https://github.com/shanto268/snip2tex)
- 阻止 iTunes 或 Apple Music 自动启动和弹出：[noTune](https://github.com/tombonez/noTunes)
- 异地组网、内网穿透：Tailscale（跨平台）
- 挂载云盘：AList、CloudMounter
- 视频下载：Downie、Motrix、imFile
- 远程控制：向日葵、TeamViewer Host、ToDesk
- 抠图：鲜艺 AI 抠图
- Android 连接 Mac：Macdroid（需付费）、OpenMTP、Android 文件传输助手（有时无法识别）
- 用魔法增强 MacbookPro 的屏幕亮度：[LumosMaxima - Boost Your MacBook Pro's Screen Brightness](https://lumosmaxima.000ooo.ooo/cn)
- 软件更新：Latest（一般）
- 媒体库管理：Emby（海报墙）
- 可视化键盘输入：KeyCastr
- 编程语言 API 下载、查看：Dash
- 趣味 App：Ball、Bananabin、Desktop Goose（桌面宠物）、Eyeballs、FireBox、Logoer（修改左上角的苹果 logo）、Numi（计算器）、One Thing（在菜单栏显示文字）、Things（to-do 清单）
- 其他：微信（Windows 端没有深色模式，macOS 有深色模式）等


---

#### Mac 端没有的一些软件

- PotPlayer
- Notepad++（可以用 [Notepad--](https://github.com/cxasm/notepad--) 代替；[micro](https://github.com/zyedidia/micro)（基于终端的文本编辑器））
- MobaXterm
- WinSCP


---

#### 部分软件设置

- 在 macOS 中，由 Intel 芯片编译得到的程序在 Apple Silicon 芯片上通常可以运行，得益于 Apple 提供的 Rosetta 2 技术

- Notepad-- macOS 安装：[macOS Sonoma 14.1.1安装提示已损坏 · Issue #I8JTJN · 爬山虎/ndd - Gitee.com](https://gitee.com/cxasm/notepad--/issues/I8JTJN)

- kitty 使用：
	- 介绍：[kitty - Arch Linux 中文维基](https://wiki.archlinuxcn.org/wiki/Kitty)；[Kitty基于GPU的终端工具 - Escape](https://www.escapelife.site/posts/8e342b57.html)
	- Linux 安装路径：`~/.local/kitty.app`
	- 配置文件路径：`~/.config/kitty/kitty.conf`
	- kitty 参考配置文件：[dotfiles/kitty/.config/kitty at main · Fireond/dotfiles · GitHub](https://github.com/Fireond/dotfiles/tree/main/kitty/.config/kitty)
	- [ ] 如何将 kitty 的窗口信息放到上面，而非默认的下方

```bash
kitty +kitten diff file1 file2

kitty +kitten icat <figure>

kitty +kitten themes
```

---

 - Termius 设置：
	- [ ] Termius 无法复制粘贴
	- 跨平台，多端数据记录同步；有学生认证
	- 可 ssh 远程连接和 sftp 远程文件传输
	- 可进行学生认证
	- 可保存并显示历史命令
	- 字体设置：设置 - Terminal - Text Size 上方，选择“Meslo”
	- 连接本地终端：Hosts - TERMINAL
	- 可保存自定义 Theme；不错的预设 Theme：
		- Monokai
		- Pro
		- Solarized Dark（个人主要采用该 Theme）
		- Atom One Dark
		- Tokyo Night

---

- iTerm2 字体设置：Prefrences - profiles - text

- IINA 相关快捷键：
	- 倍速播放
		- `command + ]` - 1/2/4 倍速加快
		- `command + option + ]` - 1.1 倍速加快
	- 字幕切换 - `control + command + S`
	- 音频切换 - `control + command + A`

- yabai 使用：[yabai - Mac 的窗口平铺管理软件 - KawaiHe - 博客园](https://www.cnblogs.com/kawaihe/p/yabai--mac-de-chuang-kou-ping-pu-guan-li-ruan-jian.html)

- bclm 安装与配置

```bash
# 安装
brew tap zackelia/formulae
brew install bclm

# 设置
sudo bclm write 80
bclm read

# 出现以下报错
keyNotFound(code: "CHWA")
```

- [Cannot install MarkText 0.17.0rc2-arm64 on M1 MacBook Air · Issue #2983 · marktext/marktext · GitHub](https://github.com/marktext/marktext/issues/2983)

- LocalSend 连接 SJTU WiFi 无法互相发现设备，使用手机热点可以
	- SJTU 的公共 WiFi 不支持局域网下设备互相发现（AP 隔离，导致不能正常使用）
	- [连SJTU wifi，ios和windows怎么互传文件呢？ - 水源社区](https://shuiyuan.sjtu.edu.cn/t/topic/248270)
	- AP 隔离：种将同一无线网络中各个设备 “隔离开来” 的功能，确保它们只能与互联网或路由器通信，而不能直接相互通信。

- Tailscale 安装与配置：
	- [部署TailScale实现异地组网+全内网设备远程访问！一次上手Tailscale！轻松打通内外网！群晖、威联通NAS部署Tailscale内网穿透！\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1ns4y1p768?p=1)
	- [TailScale子网路由配置，实现使用原生内网IP远程访问，异地组网更加优雅！TailScale Subnet Router使用教程！\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1ns4y1p768/?p=2)
	- [ ] macOS `tailscale ssh` 无法使用（sandbox 原因）
	- IPv6 不需要做穿透，外网也能连：[IPv6 不需要做穿透，外网也能连 - 水源社区](https://shuiyuan.sjtu.edu.cn/t/topic/214653)
	- 交大接入有线网会分配一个公网 IPv6 地址

- AList docker-compose 部署，挂载网盘时出现 `tcp XXX: connect: connection refused`：[挂载阿里云盘报错 · alist-org/alist · Discussion #1063 · GitHub](https://github.com/alist-org/alist/discussions/1063)
	- [GitHub - DDS-Derek/xiaoya-alist: 小雅Alist的相关周边](https://github.com/DDS-Derek/xiaoya-alist)
	- [x] AList macOS 本地存储路径写法 `/Users/XXX/XXX`，报路径不存在的错：正确写法：把本地路径挂载到 Docker 里，AList 里应该填 Docker 内的路径（可以挂载多个本地路径）

```yaml
{
        # 注释 port 参数，将 bridge 模式改成 host
        network_mode: 'host'
}
```


---

#### 终端模拟器集成 SFTP

- tabby 集成 SFTP（无法查看远程文件内容），需要在 “设置 - 配置和连接” 中打开远程服务器，终端右上方才会显示 SFTP（直接在终端 SSH 连接不会显示）
	- 在当前目录下打开 SFTP 面板：[Shell working directory reporting · Eugeny/tabby Wiki · GitHub](https://github.com/Eugeny/tabby/wiki/Shell-working-directory-reporting)

```bash
# bash ~/.bash_profile
export PS1="$PS1\[\e]1337;CurrentDir="'$(pwd)\a\]'

# zsh ~/.zshrc
precmd () { echo -n "\x1b]1337;CurrentDir=$(pwd)\x07" }
```

- Termius 集成 SFTP（可以查看远程文件内容）

- iTerm2 安装 Shell Integration：登录远程服务器，iTerm2 - Install Shell Integration，安装成功后，当前登录的用户名最前面会出现向右的小三角，将本地文件（支持多个）或文件夹选中，按住 option 键的同时拖动到 iTerm2 窗口，松开即可上传；[使用iTerm2管理SSH服务器 – 爪哇堂 JavaTang](https://www.javatang.com/archives/2021/11/29/13063392.html)
	- 可以在终端查看图片和 gif 图（imgls）；[Features - iTerm2 - macOS Terminal Replacement](https://iterm2.com/features.html)


---

#### Homebrew 使用

- 大部分开源命令行工具、程序、库和 GUI 程序（cask，不太推荐用该方式，有时下载速度很慢，建议直接官网下载）都可以通过 Homebrew 安装（类似 Windows 上的 Scoop）

- 安装 Homebrew：
	- [安装和使用 Homebrew - 韬秧道](https://blog.tauyoung.top/article/Homebrew/)
	- [homebrew - 清华大学镜像](https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/)

```bash
# 安装
/bin/bash -c "$(curl -fsSL https://github.com/Homebrew/install/raw/master/install.sh)"

# 交大镜像
export HOMEBREW_BREW_GIT_REMOTE=https://mirrors.sjtug.sjtu.edu.cn/git/brew.git  
export HOMEBREW_CORE_GIT_REMOTE=https://mirrors.sjtug.sjtu.edu.cn/git/homebrew-core.git  
export HOMEBREW_BOTTLE_DOMAIN=https://mirror.sjtu.edu.cn/homebrew-bottles/bottles
```

- 相关命令：[Homebrew 备忘清单 &  homebrew cheatsheet &  Quick Reference](https://quickref.me/zh-CN/docs/homebrew.html)

```bash
brew install <package>         # 安装
brew install --cask <package>  # 安装 GUI 程序
brew uninstall <package>       # 卸载
brew search <package>          # 查找
# 显示安装包相关信息 是否安装，依赖，头文件、库路径等
brew info <package>
brew list          # 列出已安装的包
brew list --casks  # 仅列出已安装的软件
brew doctor        # 诊断
brew outdated      # 列出可以升级的包
brew upgrade [package]  # 升级

# 忽视依赖关系卸载
brew uninstall --ignore-dependencies <package>

# 查看已安装的包的依赖，树形显示
brew deps --installed --tree [package]

brew cleanup -n           # 查看可清理的旧版本包
brew cleanup              # 清理所有包的旧版本
brew cleanup --prune=all  # 删除缓存

brew pin <package>    # 锁定包
brew unpin <package>  # 取消锁定

# 取消 对 homebrew/core 仓库的关注
brew untap homebrew/core
```

---

#### 字体安装

方法一：手动下载字体，双击安装字体

方法二：brew 命令行安装

>中文字体：[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)、[得意黑](https://github.com/atelier-anchor/smiley-sans)

```bash
# nerd font
brew tap homebrew/cask-fonts
brew install --cask font-meslo-lg-nerd-font
brew install --cask font-hack-nerd-font

brew install --cask font-jetbrains-mono
brew install --cask font-juliamono

# 查看可用 nerd font
brew search '/font-.*-nerd-font/' | awk '{ print $1 }'

# 中文字体
brew install font-smiley-sans  # 得意黑
brew install font-lxgw-wenkai  # 霞鹜文楷

# Mac 字体路径
/Library/Fonts   # 系统
~/Library/Fonts  # 用户
```


---

#### MacTeX 安装与卸载

- 安装：[MacTeX - TeX Users Group](https://www.tug.org/mactex/mactex-download.html)；在官网上下载最新 pkg 包，双击，按照提示安装
- 卸载：[Uninstalling - MacTeX - TeX Users Group](https://tug.org/mactex/uninstalling.html)；卸载 GUI，直接将 TeX 移入废纸篓；卸载 TeX Distribution；卸载 Ghostscript（删除较复杂；通常在 `/usr/local/share` 或 `/usr/local/bin` 目录）

```bash
brew install --cask mactex-no-gui  # 不建议

sudo rm -rf /Library/TeX
sudo rm -rf /usr/local/texlive
```


---

#### Rime 输入法引擎 + 雾凇拼音

- 参考：
	- [RIME 鼠须管输入法简明使用教程 - BAI YUN](https://baiyun.me/rime-simple-tutorial)
	- [GitHub - Mintimate/oh-my-rime: The Simple Config Template Of Rime By Mintimate.](https://github.com/Mintimate/oh-my-rime)

```bash
# 安装 Rime 鼠须管 输入法引擎
brew install --cask squirrel

# 安装配置管理工具
git clone --depth=1 https://github.com/rime/plum
cd plum

# 安装 雾凇拼音
bash rime-install iDvel/rime-ice:others/recipes/full
```

可修改的配置文件路径：
```bash
/Users/XXX/Library/Rime/squirrel.yaml
/Users/XXX/Library/Rime/default.yaml
```

macOS 修改应用的默认 ascii_mode（个人更倾向修改成默认英文）：`squirrel.yaml`
```yaml
# 可参考 /Library/Input Methods/Squirrel.app/Contents/SharedSupport/squirrel.yaml
app_options:
  com.apple.Spotlight:
    ascii_mode: true  # 开启默认英文
  com.microsoft.VSCodeInsiders:
    ascii_mode: true
  md.obsidian:
    ascii_mode: false
    ascii_punct: false
  com.googlecode.iterm2:
    ascii_mode: true
    ascii_punct: false
  com.google.Chrome:
    ascii_mode: true
    ascii_punct: false
  com.runningwithcrayons.Alfred:
    ascii_mode: true

style:
  horizontal: true
```

修改候选词个数：`default.yaml`
```yaml
# 菜单
menu:
  page_size: 9  # 候选词个数
```


---

#### Safari 浏览器插件

- 去广告：AdGuard
- 合并标签页：OneTab
- 使用 Vim 快捷键操作网页内容：Vimlike
- 视频倍速：Accelerate
- 中英文翻译：沉浸式翻译、无官方的 DeepL（有非官方的，不是很好用）、沙拉查词翻译（无官方）
- 油猴（需收费，有破解版；很多油猴脚本未适配 Safari）
- 网络代理：[如何在safari上实现类SwitchyOmega代理切换功能](https://www.youtube.com/watch?v=pAY8pNou9Gk)

```bash
sudo apachectl start
```

- B 站相关插件：[\[Safari\]：安装指南 · Issue #679 · BewlyBewly/BewlyBewly · GitHub](https://github.com/BewlyBewly/BewlyBewly/issues/679)


---

### 编程相关

- macOS 版本不同，Homobrew 之前安装的程序有可能会出现不兼容的情况

- Miniconda3 安装：版本需要与芯片类型（如 M1）适配

- 安装性能提升的 NumPy：[Option to install numpy built with Apple's Accelerate BLAS implementation · Issue #253 · conda-forge/numpy-feedstock · GitHub](https://github.com/conda-forge/numpy-feedstock/issues/253)
	- NumPy、SciPy 和 Matlab 支持 AMX 单元加速：[一次讲透！工科生用Mac，体验如何？\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1YJ4m1M7bD)

```bash
conda install -c conda-forge numpy "libblas=*=*accelerate"
conda install numpy "libblas=*=*accelerate"
```

- Mac 的 gcc 和 g++ 编译器 默认是 clang 的；建议安装 gcc 套件，并设置软链接

```bash
ln -s /opt/homebrew/bin/g++-13 ~/bin/g++
ln -s /opt/homebrew/bin/gcc-13 ~/bin/gcc
```

- clang 没有 `fopenmp` 选项

```bash
clang: error: unsupported option '-fopenmp'
make: *** [atom.o] Error 1
```

- dumpana 编译出现以下报错（应该是不兼容 macOS arm64 架构的原因）

```bash
ld: symbol(s) not found for architecture arm64
collect2: error: ld returned 1 exit status
make: *** [dumpana] Error 1
```

- macOS 彻底删除 Node.js：[javascript - How do I completely uninstall Node.js, and reinstall from beginning (Mac OS X) - Stack Overflow](https://stackoverflow.com/questions/11177954/how-do-i-completely-uninstall-node-js-and-reinstall-from-beginning-mac-os-x)

- Mac M1 运行 node、npm 报 `rsh: Command not found.` 错误，是由于 ATAT 编译后也有可执行命令 node（默认使用 rsh 远程登录（较早的远程访问工具之一，但由于安全隐患较大，现在很少使用），-s，指定使用 ssh），系统将 Node.js 的 node 指向了 ATAT 的，导致该错误出现。

- Mac 中的 Vim Delete 键无法向左删除：[vim中delete（backspace）键不能向左删除 - 脚本小娃子 - 博客园](https://www.cnblogs.com/shengulong/p/10530188.html)

```bash
set backspace=2
```

- 查看 Macbook GPU 信息：
	- 系统设置 - 通用 - 系统报告 - 图形卡/显示器
	- 运行命令：`system_profiler SPDisplaysDataType`

- 查看网线 IP 地址：系统设置 - 网络 - USB XXX LAN，IP 地址
- 获取本机 WiFi IP 地址：`ipconfig getifaddr en0`

- 安装 Java：Java 存档下载：[Java Archive Downloads - Java SE 18](https://www.oracle.com/java/technologies/javase/jdk18-archive-downloads.html)

```bash
brew install openjdk  # 安装 Java
```

- 专为 macOS 设计的 Jupyter Notebook：[Satyrn](https://satyrn.app/)
	- 有 command（类似 vim） 和 edit 模式；需自己添加 miniconda 虚拟环境的 kernel

- macOS 中终端下安全删除文件工具（可恢复）：[GitHub - hotoo/rm-trash](https://github.com/hotoo/rm-trash)

```bash
npm i rm-trash -g  # 安装
```

- 在 macOS 中，LAPACK 库是作为 Accelerate.framework 框架的一部分被提供的

```bash
lapack is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides LAPACK in Accelerate.framework.

For compilers to find lapack you may need to set:
  export LDFLAGS="-L/opt/homebrew/opt/lapack/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/lapack/include"

For pkg-config to find lapack you may need to set:
  export PKG_CONFIG_PATH="/opt/homebrew/opt/lapack/lib/pkgconfig"
```

```bash
# lib 路径
/System/Library/Frameworks/Accelerate.framework/Versions/Current/Frameworks/vecLib.framework/libBLAS.dylib
/System/Library/Frameworks/Accelerate.framework/Versions/Current/Frameworks/vecLib.framework/libLAPACK.dylib
```



---

## 相关问题

### git 相关

git 出现以下报错：

```bash
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

解决方法：`xcode-select --install`


---

### VSCode-Insiders 相关

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

### coreutils 相关

- `coreutils` (GNU Core Utilities) 包含了很多基本的文件、shell 和文本操作工具
- macOS 中的一些命令的参数没有 Ubuntu 的全（如 `du`）
- 通过在命令前加 `g` 来调用 GNU 版本的命令（如 `gdu`）

```bash
brew install coreutils
```


---

### 软件安装问题

- 身份不明开发者：按住 `Control` 键，点击 App，弹出的窗口会有打开按钮；[Mac如何打开身份不明开发者的程序？ - 知乎](https://www.zhihu.com/question/52623818)
- [Apple 无法检查 App 是否包含恶意软件 - 官方 Apple 支持 (中国)](https://support.apple.com/zh-cn/guide/mac-help/mchleab3a043/mac)
- PicGo 安装显示文件已损坏：[PicGo arm64文件已损坏](https://github.com/Molunerfinn/PicGo/issues/1055)

```bash
sudo xattr -d com.apple.quarantine "/Applications/PicGo.app"
```


---

### Beta 系统升级问题

macOS beta 版本系统，brew 安装的程序升级时，会出现的无法识别 macOS 版本的问题

```bash
# 设置环境变量来强制 Homebrew 认为它在支持的 macOS 版本上运行
export HOMEBREW_DEVELOPER=1
export HOMEBREW_MACOS_VERSION=14.5
```


---

### 其他

- Mac 终端模拟器（Terminal、iTerm）ssh 连接远程服务器，打开 GUI 程序：[Enable X11 forward for ssh to load images from remote server on MacOS Mojave · GitHub](https://gist.github.com/fengyuentau/7c43c06fb563752b6947affaf4677f2a)
- 文件创建 Mac 无法直接创建文件（可通过终端 `touch` 命令或安装 “超级右键”软件），只能创建文件夹
- Apple ID 相关问题：此 Apple ID 尚未在 app store 使用（弹出“检查”窗口时，会出现要求完善支付方式信息内容；macOS 11 在检查这步一直无法弹出后面的内容，将版本更新至最新无此问题）
- 蓝牙耳机连接：长按 Redmi Airdots3 Pro 耳机盒的开关机键；将 Bose qc45 电源键推至右侧一段时间
- [Word for Mac彻底删除Endnote插件的方法 - 知乎](https://zhuanlan.zhihu.com/p/29321865)
- Final Cut Pro 软件无法打开 mkv 格式文件（和 PR 一样）

- [ ] 如何安装黑苹果

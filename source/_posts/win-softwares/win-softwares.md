---
title: Windows 常用软件
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Windows 常用软件
description: Windows 常用软件
tags:
  - 软件
categories:
  - Win 软件
date: 2023-07-10 15:00:00
abbrlink: 400627
password:
---

# Windows 常用软件

- 参考：[Windows实用软件推荐](https://blog.wfso.cn/archives/115/)



---

## 自带邮件关联教育邮箱

- 网页版交大邮箱界面不是很美观，可使用 Windows 邮件关联教育邮箱。

- 管理账户 - 添加账户 - 高级设置 - Internet 电子邮件 - 传入、传出电子邮件服务器填 `mail.sjtu.edu.cn`，账户类型选择 `IMAP4` - 登录

- qq 邮箱设置：[qq 邮箱 SMTP/IMAP 服务](https://wx.mail.qq.com/list/readtemplate?name=app_intro.html#/agreement/authorizationCode)



---

## Windows Terminal

- 新版本 Windows 会自带；比 PowerShell 和 CMD 美观，可通过 oh-my-posh 美化；可直接连接已安装的 WSL

---

### 美化

- 安装 oh-my-posh 和 Meslo-NF，在设置中选择 `MesloLGM Nerd Font` 字体

```powershell
scoop install oh-my-posh

scoop bucket add nerd-fonts
scoop install nerd-fonts/Meslo-NF

```

- 初始化 oh-my-posh

```powershell
notepad $Profile

# 上述命令默认打开的文件；若没有该文件，可手动创建
Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

# 写入以下内容
# 自动配置 oh-my-posh 在 PowerShell 中的初始化设置
oh-my-posh init pwsh | Invoke-Expression


Get-PoshThemes  # 获取主题
. $Profile      # 重新加载 profile
```


---

### 自动补全

- 参考：[PSReadLine - Powershell 的强化工具\_sigmarising的博客-CSDN博客](https://blog.csdn.net/sigmarising/article/details/107287275)

- 安装 PSReadLine

```powershell
# 管理员模式下
Install-Module PSReadLine -RequiredVersion 2.1.0
# 或者
Install-Module PSReadLine

# user
Install-Module PSReadLine -RequiredVersion 2.1.0 -Scope CurrentUser
```

- 设置快捷键

```powershell
notepad $Profile

# 写入以下内容
# Get-PSReadLineKeyHandler 查看所有设置的快捷键绑定
# PSReadLine
Import-Module PSReadLine
# Enable Prediction History
Set-PSReadLineOption -PredictionSource History
# Advanced Autocompletion for arrow keys
Set-PSReadlineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward
Set-PSReadLineKeyHandler -Key Tab -Function Complete
Set-PSReadLineKeyHandler -Key Ctrl+d -Function DeleteChar
Set-PSReadLineKeyHandler -Key Alt+Backspace -Function BackwardDeleteWord
Set-PSReadLineKeyHandler -Key Alt+b -Function BackwardWord
Set-PSReadLineKeyHandler -Key Alt+f -Function ForwardWord
Set-PSReadLineKeyHandler -Key Ctrl+a -Function BeginningOfLine
Set-PSReadLineKeyHandler -Key Ctrl+e -Function EndOfLine
Set-PSReadLineKeyHandler -Key Ctrl+z -Function Undo
```


---

## Scoop

- 参考：
    - [Windows - Scoop软件包管理神器 | 新壳记](https://www.cdnxin.top/post/scoop/)
    - [GitHub - duzyn/scoop-cn: 中国用户能用的 Scoop 应用库，每日同步 Scoop 的官方库，加速应用的下载速度](https://github.com/duzyn/scoop-cn#)

- Scoop 官网：[Scoop](https://scoop.sh/)

- Windows 的程序包安装管理工具（类似工具：Winget 和 Chocolatey；macOS 为 Homebrew）

- 可安装大部分的开源程序和命令行工具（如本文提到的所有软件）

- 程序安装后无需再手动添加环境变量（自动配置；Scoop 中的 Shim 工具）

```powershell
# 将 Scoop 安装到 D 盘
$env:SCOOP='D:\Scoop'
[environment]::setEnvironmentVariable('SCOOP',$env:SCOOP,'User')
iwr -useb get.scoop.sh | iex


# 添加国内 bucket
scoop bucket add scoop-cn https://github.com/duzyn/scoop-cn
scoop bucket rm scoop-cn       # 删除 bucket
scoop bucket list              # 列出 bucket
scoop update -a                # 更新所有程序
scoop status                   # 查看状态
scoop cache rm -a              # 删除缓存
scoop cleanup -a               # 删除所有旧版本
scoop uninstall scoop          # 卸载 Scoop

scoop config name value        # 配置 scoop
# 配置文件路径 ~/.config/scoop/config.json
```



---

## 其他常用软件

- Zotero：文献管理

- Typora：Markdown 笔记软件

- Listary：一款实用的文件搜索、程序启动工具
    - 与 Mac 的 Alfred 类似；快速切换到当前打开的目录 `CTRL + G`

- MobaXterm：远程服务器连接工具；集成 X11 和 SFTP；可自动识别已安装的 WSL
    - [Mobaxterm: how to prevent ssh session from exiting? - Stack Overflow](https://stackoverflow.com/questions/57385896/mobaxterm-how-to-prevent-ssh-session-from-exiting)
    - [ ] Mobaxterm 左侧文件目录无法随右侧终端命令实时改变（暂无法解决）

- WinSCP：远程服务器文件传输工具，比在 MobaXterm 上拖拽传输好用一些

- Obsidian：本地笔记管理软件，比 Notion、Typora 好用

- MongoDB Compass：MongoDB 数据库的管理工具

- Snipaste：截图软件，可以截图、**贴图**、标注；可以获取颜色的 rgb 值等

- PicGo：图床工具
    - 相关设置：设置 GitHub 图床；开启时间戳重命名；禁用 `Crtl + Shift + P` 快捷键（与 VSCode 和 Obsidian 中的快捷键有冲突）

- PicList：图床工具，基于 PicGo 开发

- Notepad++：文本编辑器；直接关闭软件不会删除未保存的内容，可用做临时记录（最新版本的 Windows 的记事本也可以）
    - 自动换行设置：“视图” -- 勾选 “自动换行”
    - 文件每行末尾显示 `CRLF`：“视图” -- “显示符号” -- 取消勾选 “显示行尾符”
    - 该软件开发者涉及辱华，建议使用其他替代工具（Notepad--）

- Internet Download Manager：简称 IDM，下载工具，可嗅探到网页中任何可下载的东西（如文件、视频、音频等）并自动分类归档。一些配置：
    - 选项 -- 常规设置 -- 接管以下浏览器，仅 Chrome 和 Firefox（取消勾选 Edge，因其会经常提示下载更新包）
    - 选项 -- 文件类型 -- 以下站点不自动下载

```text
pdf.sciencedirectassets.com
pubs.acs.org
journals.aps.org
onlinelibrary.wiley.com
```

- Geek Uninstaller：软件卸载工具，能清除软件的注册表，卸载较为彻底

- TreeSize Free：磁盘管理工具，有利于查看哪些文件占用较大体积进行删除

- Mathpix：LaTeX OCR 识别；使用教育邮箱，可增加 Mathpix 使用次数；支持临时邮箱

- Potplayer：媒体播放器
    - [基于PotPlayer和madVR的播放器教程 | VCB-Studio - the chosen one](http://lbj007.headns.com/archives/479/)

- QuickLook：快速预览文件的工具，按空格键即可实现预览且可以复制文件内容
    - 类似于 Mac 的空格键；有插件可实现预览 Office 套件文件，但效果不是很好
    - [GitHub - QL-Win/QuickLook.Plugin.OfficeViewer: Word, Excel, and PowerPoint plugin for QuickLook.](https://github.com/QL-Win/QuickLook.Plugin.OfficeViewer)

- Rime 输入法引擎 + 雾凇拼音（Windows 端个人感觉不是很好用）
    - [Windows RIME输入法安装](https://www.cnblogs.com/deali/p/18022187)
    - [小狼毫&雾凇拼音安装及部署-Windows（图文）](https://www.cnblogs.com/HookDing/p/17949199)

- 调节显示器亮度：Twinkle Tray（部分显示器设备无效；一般）

- [GitHub - Planshit/Tai: 👻 在Windows上统计软件使用时长和网站浏览时长](https://github.com/Planshit/Tai)

- 切换统一程序下的不同窗口：[GitHub - sigoden/window-switcher: Easily switch between windows of the same app with Alt+\` (Backtick), also switch between apps with Alt+Tab.](https://github.com/sigoden/window-switcher)

- 自动切换中英文输入法：[GitHub - flyinclouds/KBLAutoSwitch: AHK自动切换中英文输入法，输入法，自动切换](https://github.com/flyinclouds/KBLAutoSwitch)

- 应用窗口居中和大小重置：[GitHub - Devail1/window-center-resize: A utility application that allows you to easily center and resize windows on your desktop using customizable keyboard shortcuts.](https://github.com/Devail1/window-center-resize)

---

>以下软件并未实际下载使用测试

- 锁定键盘：[GitHub - Nigh/I-wanna-clean-keyboard](https://github.com/Nigh/I-wanna-clean-keyboard)

- 右键菜单：[GitHub - moudey/Shell: Powerful context menu manager for Windows File Explorer](https://github.com/moudey/Shell)

- 为 Windows 系统提供 Vim 风格的快捷键：[GitHub - pit-ray/win-vind: You can operate Windows with key bindings like Vim.](https://github.com/pit-ray/win-vind)

- 优化 Windows 11 系统的脚本：[GitHub - Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat)

- 查看磁盘占用：[WinDirStat - Windows Directory Statistics](https://windirstat.net/)

- Windows 常见的 CLI 包管理器 GUI：[GitHub - marticliment/UniGetUI](https://github.com/marticliment/UniGetUI)

- [GitHub - the1812/Malware-Patch: 阻止中国流氓软件的管理员授权. / Prevent UAC authorization of Chinese malware.](https://github.com/the1812/Malware-Patch)

- 删除 Outlook：[GitHub - matej137/OutlookRemover: a little batch file that permanently removes the Outlook (New) app from Windows 10/11](https://github.com/matej137/OutlookRemover)

- [pdf-bookmark](https://github.com/ifnoelse/pdf-bookmark)：给 pdf 生成目录， README 中有详细的操作介绍。
    - 生成目录内容时，中文可能会出现乱码的情况，可直接将 china-pub 中书籍详情页完整目录复制到 pdf-bookmark 目录编辑框中
    - pdf 的目录可在京东、当当、读秀、图书馆联盟、豆瓣图书中找到并复制过来，但需带页码

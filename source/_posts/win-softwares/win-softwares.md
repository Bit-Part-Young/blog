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

新版本 Windows 会自带；比 powershell 和 cmd 美观，可通过 oh-my-posh 美化；可直接连接已安装的 WSL。

---

### 美化

- 安装 oh-my-posh 和 Meslo-NF，在设置中选择 `MesloLGM Nerd Font` 字体；

```powershell
scoop install oh-my-posh

scoop bucket add nerd-fonts
scoop install nerd-fonts/Meslo-NF
```


```powershell
notepad $Profile  # 初始化 oh-my-posh

# 文件目录结构；若没有该文件，可手动创建
Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

# 写入以下内容
# 自动配置 oh-my-posh 在 PowerShell 中的初始化设置
oh-my-posh init pwsh | Invoke-Expression

Get-PoshThemes  # 获取主题
. $Profile      # 重新加载 profile
```


---

### 自动补全

>[PSReadLine - Powershell 的强化工具\_sigmarising的博客-CSDN博客](https://blog.csdn.net/sigmarising/article/details/107287275)

- 安装 PSReadLine

```powershell
# 管理员模式下
Install-Module PSReadLine -RequiredVersion 2.1.0
# 或者
Install-Module PSReadLine

# user
Install-Module PSReadLine -RequiredVersion 2.1.0 -Scope CurrentUser
```

- `notepad $Profile`，设置快捷键，写入以下内容：

```powershell
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

>[Scoop](https://scoop.sh/)

>[Windows - Scoop软件包管理神器 | 新壳记](https://www.cdnxin.top/post/scoop/)

>[GitHub - duzyn/scoop-cn: 中国用户能用的 Scoop 应用库，每日同步 Scoop 的官方库，加速应用的下载速度](https://github.com/duzyn/scoop-cn#)


- Windows 平台的程序包安装管理工具（类似工具：Winget 和 Chocolatey；Mac 平台为 Homebrew）
- 可以安装几乎所有的开源程序和命令行工具（如本文提到的所有软件）
- 程序安装后无需再手动添加环境变量（自动配置；Scoop 中的 Shim 工具）。


```powershell
# 将 Scoop 安装到 D 盘
$env:SCOOP='D:\Scoop'
[environment]::setEnvironmentVariable('SCOOP',$env:SCOOP,'User')
iwr -useb get.scoop.sh | iex

# 添加国内 bucket
scoop bucket add scoop-cn https://github.com/duzyn/scoop-cn
# 删除 bucket
scoop bucket rm scoop-cn
# 列出 bucket
scoop bucket list

# 更新所有程序
scoop update -a

# 查看状态
scoop status

# 配置 scoop
# 配置文件路径 ~/.config/scoop/config.json
scoop config name value

# 删除缓存
scoop cache rm -a

# 删除所有旧版本
scoop cleanup -a

# 卸载 Scoop
scoop uninstall scoop
```



---

## Zotero

- 文献管理软件，可通过插件保存网页中的文献，也可直接导入文献文件；
- 可实现文献、文献中的批注云同步（需找到合适的同步盘软件，如坚果云，InfiniCLOUD 等，推荐使用后者）；
- 插件生态很好，比 EndNote 好用很多。

- Zotero 文献存储路径修改（默认 C 盘）：[Zotero更改储存路径&迁移文件 - 知乎](https://zhuanlan.zhihu.com/p/478035708)

- 文献云同步：通过 WebDAV，主要有 infini-cloud 和坚果云：[如何在Zotero中设置webdav连接到坚果云？ - 坚果云帮助中心](https://help.jianguoyun.com/?p=3168)、[Zotero × Logseq - 有意栽花花满枝](https://blog.hjroyal.top/posts/tools/2023-04-zotero_logseq/)

```text
toi.teracloud.jp/dav
dav.jianguoyun.com/dav
```

- Zotero 插件：[plugins [Zotero Documentation]](https://www.zotero.org/support/plugins)、[文献管理软件Zotero常用插件安装及配置使用\_zotero插件\_qq\_43309940的博客-CSDN博客](https://blog.csdn.net/qq_43309940/article/details/117126357)

- Zotero style 插件安装后会导致软件很卡

- 将 Zotero 中导入的文献按添加时间进行排序：文献库界面右上方，附件（“链接” 图标），添加 “添加时间”；或者添加导入文献具体日期的文献库分类



---

## Notion

- 跨平台同步的笔记软件；也有网页版，但网页版的体验不如客户端，很卡
- 可以查看每一个页面的内容更新情况（页面右上角的时钟图标）
- Notion 可以用教育邮箱使用教育版
- 不可以改变图片大小
- task list 没有快捷键

---

- [Notion工具资源集合](https://notion2go.com/)
- Notion 开源替代品：[GitHub - docmost/docmost](https://github.com/docmost/docmost)
- 备份（不好用，且复杂）：[GitHub - LoneKingCode/notion-backup](https://github.com/LoneKingCode/notion-backup)
- 使用 Notion 的 Authorization：[Authorization](https://developers.notion.com/docs/authorization)


---

### 快捷键

```text
# + Space         # 一级标题；其他类推
" + Space         # 引用
> + Space         # toggle list
Ctrl + E          # 将文本转为内联代码
/color            # 更改文本颜色（可在开头或结尾输入；默认 /default）
Crtl + F          # 查找（当前页面）
Crtl + P          # 查找（所有页面）
Ctrl + Shift + E  # 公式
Ctrl + Shift + 8  # 代码块
/pdf              # 嵌入 pdf
```


---

### notion2md

- Notion 自带的导出 md 效果不是很好

- notion 转 md：[GitHub - echo724/notion2md](https://github.com/echo724/notion2md)

- 设置 Notion Integration，获取 API KEY，在 Notion 每个 page 下 add connection 设置的 Notion Integration

```bash
export NOTION_TOKEN='<token>'

notion2md --download --unzipped -n name -p folder -u [[]]
```


---

### md2notion

- md 转成 notion（在 Notion 的页面中生成子页面）：[GitHub - Cobertos/md2notion: A better Notion.so Markdown importer](https://github.com/Cobertos/md2notion)

- 安装出现 `Invalid input` 报错解决方法：[HTTPError - Invalid Input · Issue #40 · Cobertos/md2notion · GitHub](https://github.com/Cobertos/md2notion/issues/40)

```bash
pip install notion-cobertos-fork
```

- CLI 形式

```bash
python -m md2notion token_v2 [[test]] [[]]
```

- Python 脚本形式

```python
from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload

# Follow the instructions at https://github.com/jamalex/notion-py#quickstart to setup Notion.py
client = NotionClient(token_v2="")
page = [[test]]

with [[]]", "r", encoding="utf-8") as mdFile:
    newPage = page.children.add_new(PageBlock, title="TestMarkdown Upload")
    upload(mdFile, newPage) #Appends the converted contents of [[]] to newPage
```



---

## Typora

- Markdown 语法笔记软件；新版本收费，建议安装旧版本或者破解版。

- 破解版：[GitHub - markyin0707/typora-activation: Typora最新的激活方案，三步即激活.（😊实时更新中/👩‍🎓学生党必备，有条件支持正版的请不要点开🔞🈲️）。Activate Typora](https://github.com/markyin0707/typora-activation)

- [手摸手教你安装激活最新的Typora1.8.10\_typora1.8.10 linux 激活-CSDN博客](https://blog.csdn.net/qq_37636739/article/details/136338284)

- Theme 主题：
    - [GitHub - liangjingkanji/DrakeTyporaTheme: 十二种主题风格 - Material Google JetBrains Vue Juejin Purple Ayu Dark](https://github.com/liangjingkanji/DrakeTyporaTheme)
    - [GitHub - Soanguy/typora-theme-autumnus: Typora theme for 中文](https://github.com/Soanguy/typora-theme-autumnus)
    - [GitHub - Keldos-Li/typora-latex-theme: 将Typora伪装成LaTeX的中文样式主题，本科生轻量级课程论文撰写的好帮手。This is a theme disguising Typora into Chinese LaTeX style.](https://github.com/Keldos-Li/typora-latex-theme)

- 侧边栏大纲视图允许折叠和展开：[Typora强烈推荐的两个设置\_typora如何变成双窗口-CSDN博客](https://blog.csdn.net/haojie_duan/article/details/113747929)

- 标题自动分级编号：[Markdown文件的标题分级自动编号——Typora\_markdown编号-CSDN博客](https://blog.csdn.net/qq_39103283/article/details/115302824)

- 快捷键重映射（如将默认的行内代码快捷键 Ctrl + Shift +\` 重映射成 `Ctrl + Q`）：[Typora 快捷键设置\_typora快捷键设置为正文-CSDN博客](https://blog.csdn.net/oneby1314/article/details/111030417)

- 插件：[GitHub - obgnail/typora\_plugin: Typora plugin. feature enhancement tool - Typora 插件，功能增强工具](https://github.com/obgnail/typora_plugin)



---

## 其他常用软件

- Listary：一款实用的文件搜索、程序启动工具
    - 与 Mac 的 Alfred 类似；快速切换目录 `CTRL+G`

- MobaXterm：远程服务器连接工具；可自动识别已安装的 WSL
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
    - 选项 - 常规设置 - 接管以下浏览器，仅 chrome 和 firefox（取消勾选 edge，因其会经常提示下载更新包）
    - 选项 - 文件类型 - 以下站点不自动下载

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

- Rime 输入法引擎 + 雾凇拼音
    - [Windows RIME输入法安装](https://www.cnblogs.com/deali/p/18022187)
    - [小狼毫&雾凇拼音安装及部署-Windows（图文）](https://www.cnblogs.com/HookDing/p/17949199)

- 调节显示器亮度：Twinkle Tray（部分显示器设备无效）

- [GitHub - Planshit/Tai: 👻 在Windows上统计软件使用时长和网站浏览时长](https://github.com/Planshit/Tai)


---

>以下软件并未实际下载使用测试

- 锁定键盘：[GitHub - Nigh/I-wanna-clean-keyboard](https://github.com/Nigh/I-wanna-clean-keyboard)

- 为 Windows 系统提供 Vim 风格的快捷键：[GitHub - pit-ray/win-vind: You can operate Windows with key bindings like Vim.](https://github.com/pit-ray/win-vind)

- PPT 插件，插入 LaTeX 公式：[GitHub - Jonathan-LeRoux/IguanaTex: A PowerPoint add-in allowing you to insert LaTeX equations into PowerPoint presentations on Windows and Mac](https://github.com/Jonathan-LeRoux/IguanaTex)

- 优化 Windows 11 系统的脚本：[GitHub - Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat)

- 查看磁盘占用：[WinDirStat - Windows Directory Statistics](https://windirstat.net/)

- Windows 常见的 CLI 包管理器 GUI：[GitHub - marticliment/UniGetUI](https://github.com/marticliment/UniGetUI)

- [GitHub - the1812/Malware-Patch: 阻止中国流氓软件的管理员授权. / Prevent UAC authorization of Chinese malware.](https://github.com/the1812/Malware-Patch)

- [pdf-bookmark](https://github.com/ifnoelse/pdf-bookmark)：给 pdf 生成目录， README 中有详细的操作介绍。
    - 生成目录内容时，中文可能会出现乱码的情况，可直接将 china-pub 中书籍详情页完整目录复制到 pdf-bookmark 目录编辑框中
    - pdf 的目录可在京东、当当、读秀、图书馆联盟、豆瓣图书中找到并复制过来，但需带页码

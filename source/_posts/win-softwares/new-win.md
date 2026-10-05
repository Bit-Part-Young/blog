---
title: Windows 新机使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Windows 新机使用
description: Windows 新机使用
tags:
  - Windows
  - 计算机
categories:
  - Win 软件
date: 2023-09-28 09:00:00
abbrlink: 407358
password:
---

# Windows 新机使用

## 开箱验机

- 参考：
    - [【建议收藏】新笔记本到手验机指南，小白买笔记本不再担心翻车！ 2023版\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1DX4y1n72y/?spm_id_from=333.788.top_right_bar_window_history.content.click&vd_source=aebed606e85dc126ebe030ffeb93a8e8)
    - [【拯救者R9000P2023 7945HX】验机抽奖：特等奖\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV18P411D7JD/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=aebed606e85dc126ebe030ffeb93a8e8)

- 笔记本开箱验机步骤：
    - 检查外包装是否有已拆除的痕迹
    - 不插电源看是否能开机（大部分品牌笔记本有运输模式，正常不能开机）
    - 跳过联网：`Shift + F10` 或 `Fn + Shift + F10`，命令行输入 `oobe\bypassnro`，可以不设置密码
    - U 盘拷贝图吧工具箱，查看笔记本相关信息
        - 硬件信息（处理器、显卡、屏幕、磁盘、网卡、内存等品牌信息）
        - 电脑开机时间
        - 磁盘通电、使用时间


---

## 软件安装

### 手动安装

软件/程序及安装前后需注意事项介绍见：[Windows 常用软件 - Seek Another Land](https://bit-part-young.github.io/hexo-demo/posts/400627.html)。

- 文件搜索、程序启动工具：Listary

- 软件包安装、管理工具：Scoop

- 笔记管理：Obsidian

- 终端模拟器：
    - Windows Terminal（Windows 11 自带）
    - MobaXterm

- 代码编辑器：
    - Cursor
    - VSCode-Insiders

- 浏览器：Chrome

- 文献管理：Zotero

- 远程文件传输：WinSCP

- MongoDB：MongoDB Compass

- 文本编辑器：
    - Notepad++
    - Notepad--

- 交大云盘：jBox

- 构型可视化：
    - VESTA
    - OVITO

- 媒体播放器：PotPlayer

- PT 资源下载：qBittorrent

- 网络代理：Clash

- 压缩、解压缩：WinRAR

- 图床：
    - PicGo
    - PicList

- 联想工具箱：[GitHub - BartoszCichecki/LenovoLegionToolkit: Lightweight Lenovo Vantage and Hotkeys replacement for Lenovo Legion laptops.](https://github.com/BartoszCichecki/LenovoLegionToolkit/)


---

### Scoop 安装

软件/程序及安装前后需注意事项介绍见：[Linux 命令行工具 - Seek Another Land](https://bit-part-young.github.io/hexo-demo/posts/168542.html)

- 图片查看：jpegview

- 磁盘管理：treesize-free

- 截图：Snipaste

- 系统资源监控：RunCat

- 网速监控：TrafficMonitor

- 程序卸载：Geek Uninstaller

- 美化 Windows Terminal：oh-my-posh

- Linux 相关：Git、Vim、Neovim、lsd、fzf、ripgrep 等

- 字体：
    - Code 字体：Meslo-NF、JetBrains-Mono
    - 中文字体：得意黑、霞鹜文楷

```powershell
# Code 字体
scoop bucket add nerd-fonts
scoop install Meslo-NF
scoop install JetBrains-Mono

# 中文字体
scoop install LXGWWenKai        # 霞鹜文楷
scoop install smiley-sans       # 得意黑
```



---

## 设置

- 网络代理软件开启 TUN 模式（虚拟网卡模式），而非系统代理，可解决 OneDrive、Microsoft Store 无法打开/登录的问题

- [Windows 11 系统终极优化指南](https://zhuanlan.zhihu.com/p/693407803)

- [接纳不等于忍受，为舒服使用 Windows 11 的若干优化调整记录 - 少数派](https://sspai.com/post/92064)

- 将默认桌面、视频、照片、音乐目录路径迁移至非 C 盘

- Chrome、Edge 浏览器下载路径迁移至非 C 盘

- 关闭小组件、任务视图：设置 -- 个性化 -- 任务栏项

- 任务栏中的搜索图标过长：设置 -- 个性化 -- 任务栏项，搜索，选择仅 “搜索” 图标

- 关闭资源管理器最近使用的文件：设置 -- 个性化 -- 开始

- 关闭资源管理器常用文件夹：资源管理器 -- 主文件夹 -- 点击三个点图标，选项 -- 常规，隐私，取消勾选 “显示常用文件夹” 和 “最近使用的文件”

- 关闭搜索中的文字热门搜索

- 删除桌面回收站图标

- 关闭部分应用开机自启动（如 Xbox、OneDrive、OneNote 等）：任务管理器 -- 启动应用

- 外接键盘 Windows 键失效：有些键盘（如联想薄膜键盘）右上角有 Windows 锁定键，可以切换 Windows 键的开启和关闭

- Win11 右键默认显示更多选项：[有没有什么办法可以让win11右键默认显示更多选项？ - 知乎](https://www.zhihu.com/question/480356710)

```powershell
# powershell 管理员运行
# win10 右键
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve 

# 恢复 win11 右键
reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /va /f

# cmd 管理员运行
# 重启资源管理器
taskkill /f /im explorer.exe & start explorer.exe
```

- 取消 Win11 息屏断网：控制面板 -- 网络和 Internet -- 网络和共享中心 -- 更改适配器设置 -- 选中网络，属性，配置，电源管理，取消勾选 “允许计算机关闭设备以节约电源”；[更新win11以后，休眠模式下断网，怎么改？ - 知乎](https://www.zhihu.com/question/498326700)

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CTF\TIP\{0055AAB0-EACB-46DB-9BB4-1B97FC046D02}\LanguageProfile\0x00000804\{89E1D5C2-A068-44B6-B820-F8406C8A4706}
```

- 老电脑绕过 TPM 和 CPU 兼容性升级到 Win11：去官网下载对应版本的 Win11 的 ISO 镜像文件，之后克隆 [GitHub - AveYo/MediaCreationTool.bat](https://github.com/AveYo/MediaCreationTool.bat) repo 或下载压缩包，（管理员）运行其中的 `Skip_TPM_Check_on_Dynamic_Update.cmd` 文件，耐心等待更新升级

- [如何关闭Win10搜索栏内的系统广告](https://www.zhihu.com/question/569384371/answer/2790041626)（建议使用方法二）

- [解决Windows删除文件或文件夹时的【该项目不在XXX中。请确认该项目的位置，然后重试。】问题\_该项目不在d: 请确认该项目位置,然后重试-CSDN博客](https://blog.csdn.net/zgnckzn/article/details/109764025)

- 磁盘分区：此电脑 -- 管理 -- 存储，磁盘管理

- 删除双系统中的 Linux 时，不要将 Windows 的 EFI 分区误删!!！
    - 拯救者会出现的开机启动报错：`EFI PXE 0 for IPv4(XX-XX-XX-XX-XX-XX) boot failed`
    - 误删后，可制作 PE 的 U 盘，重建 Windows 的 EFI 引导分区 [Windows EFI引导分区重建。UEFI启动设置\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1k24y1y7qa/?spm_id_from=333.999.0.0)

- 修复电脑：制作 Windows 安装的 U 盘，在 BIOS 中将 USB 驱动器设置为启动优先项（拯救者进入 BIOS 菜单快捷键：启动时连续按 F2 键），选择 “修复计算机”

- [解决windows显示开启HDR后chrome内截图泛白问题\_截图浏览器变色\_Athus\_c的博客-CSDN博客](https://blog.csdn.net/Athus_c/article/details/106494715)

- 去除 C 盘及程序快捷方式的两个朝内的蓝色箭头（**无法从根本上去除**）：右键 -- 属性 -- 高级 -- 取消勾选 “压缩内容以便节省磁盘空间”

- Microsoft 365 无法删除里面的应用

- 删除 2345 王牌输入法：`win + R`，输入 `regedit`，搜索以下内容并删除；[如何彻底删除2345输入法？ - 知乎](https://www.zhihu.com/question/37679187)

- [删除右键菜单中的Git Gui Here、Git Bash Here的方法 - blogging - 博客园](https://www.cnblogs.com/family-626-77/p/5747953.html)

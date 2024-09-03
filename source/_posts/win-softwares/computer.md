---
title: Windows 计算机相关
top: false
cover: 
toc: true
mathjax: true
summary: Windows 计算机相关
description: Windows 计算机相关
tags:
  - 计算机
  - Windows
categories:
  - Win 软件
date: 2024-01-11 13:00:00
abbrlink: 131401
password:
---

# Windows 计算机相关

参考资料：

- [GitHub - criwits/missing-web: Your Missing Semester of Using Computer | 你缺失的那门计算机课（网页版）](https://github.com/criwits/missing-web/)



---

## 快捷键

```bash
win + E             # 打开资源管理器
win + D             # 返回桌面
win + X             # 打开高级用户菜单
win + n             # 启动任务栏中相应的应用程序（n为数字，0-9）
Alt + F4            # 关闭窗口
Alt + Tab           # 窗口快速切换：按 Tab 进行切换
Backspace           # 返回上级目录
Win+ ↑/↓            # 最大化当前窗口
Ctrl + Tab          # 标签页切换（向右切换；浏览器、终端、文本编辑器等）
Ctrl + Shift + Tab  # 向左切换
```



---

## PowerShell

- CMD 与 PowerShell 的区别：PowerShell 是 CMD 的升级版；支持管道操作；支持 Tab（命令）补全（CMD 支持路径、文件名参数补全）

- PowerShell 设置别名：
	- [给 PowerShell 带来 zsh 的体验](https://zhuanlan.zhihu.com/p/137251716)
	- [GitHub - PowerShell/PSReadLine: A bash inspired readline implementation for PowerShell](https://github.com/PowerShell/PSReadLine)

```powershell
notepad $Profile  # 打开 PowerShell 的配置文件

function new_alias { old_alias }  # 设置别名

# 输出 HOME 路径
echo %USERPROFILE%     # cmd
echo $env:USERPROFILE  # powershell

ipconfig  # 查看 IP
arp -a    # ARP（地址解析协议）；查看本地网络中的设备
```



---

## CMD

- [CMD常用命令大全（值得收藏)\_cmd命令大全\_张时贰的博客-CSDN博客](https://blog.csdn.net/qq_49488584/article/details/122609779)
- CMD 设置 alias 别名：[window中的cmd中设置别名(alias)及设置快捷键打开cmd\_cmd alias-CSDN博客](https://blog.csdn.net/YiRanZhiLiPoSui/article/details/83116819)

```bash
cd            # 进入目录
cd ..         # 返回上一级
cd \          # 跳转到根目录

start            # 打开文件夹或文件
md               # 新建文件夹
cd .> 1.txt      # 新建文件
type nul> 1.txt  # 新建文件

cls           # 清屏
copy          # 复制文件
move          # 移动文件
dir           # 遍历当前路径下所有文件
dir /d        # 显示文件以及文件大小、个数
tree          # 生成目录树
rd            # 删除文件夹
del           # 删除文件

calc          # 计算器
notepad       # 记事本
winver        # 检查Windows版本
net user      # 查看用户
whoami        # 查看当前用户

shutdown -s   # 关机
shutdown -r   # 关机并重启
shutdown -s -t 60  # 定时关机

# 环境变量
set           # 查看所有环境变量
set ...=...   # 添加环境变量
echo %path%   # 查看 PATH

# 路径切换
cd /d d:      # 切换至 D 盘
cd /d c:
```



---

## 其他

- 在指定路径下打开 CMD、PowerShell
	- 点击当前路径栏并输入 `cmd`
	- 在当前路径中，在空白处按住 shift 键并点击鼠标右键，在菜单栏中选择 “在此处打开 Powershell 窗口”

- Windows 版本还原程序：MediaCreationTool

- Office 套件快捷键：`Alt + N`，上方菜单栏会出现每种操作选项的快捷键

- Adobe Acrobat 快捷键：[Adobe Acrobat 中的键盘快捷键](https://helpx.adobe.com/cn/acrobat/using/keyboard-shortcuts.html)
	- 启用单键快捷方式：编辑，首选项 -- 一般，选择 “使用单键加速键访问工具” 选项

- `win + R`，输入 `dxdiag`，查看系统信息

- 个人惠普笔记本型号：[惠普 Pavilion 畅游人 Power - 15-cb074tx 产品规格 - HP®客户支持](https://support.hp.com/cn-zh/document/c05549489)

- 在文件资源管理器输入 `%LocalAppData%`，进入 C 盘的 AppData 路径

- Windows 端查看防火墙是否允许 ICMP 请求（ping 请求）：控制面板 - 系统安全 - 允许应用通过 Windows 防火墙 - “文件和打印机共享” 相关选项，更改设置，勾选

```powershell
# 查看当前防火墙规则
netsh advfirewall firewall show rule name=all

# 查看 ICMP 请求
netsh advfirewall firewall show rule name="文件和打印机共享(后台打印程 序服务 - RPC-EPMAP)"

# 设置 ICMP 请求
netsh advfirewall firewall set rule name="文件和打印机共享(后台打印程 序服务 - RPC-EPMAP)" new enable=yes
```

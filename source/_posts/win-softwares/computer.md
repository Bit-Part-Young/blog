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

[GitHub - criwits/missing-web: Your Missing Semester of Using Computer | 你缺失的那门计算机课（网页版）](https://github.com/criwits/missing-web/)


---

## 快捷键

```bash
Alt + F4            # 关闭窗口（文件夹和程序）
Alt + Tab           # 窗口快速切换：按 Tab 进行切换
Backspace           # 返回上级目录
Win+ ↑/↓            # 最大化当前窗口
Ctrl + Tab          # 标签页切换（向右切换；适用于浏览器、终端、文本编辑器等）
Ctrl + Shift + Tab  # 向左切换
```


```powershell
# Windows
ipconfig

# ARP（地址解析协议） 查看本地网络中的设备（Windows）
arp -a
```

Windows 端查看防火墙是否允许 ICMP 请求（ping 请求）：控制面板 - 系统安全 - 允许应用通过 Windows 防火墙 - “ 文件和打印机共享 ” 相关选项，更改设置，勾选

```bash
# 查看当前防火墙规则
netsh advfirewall firewall show rule name=all

# 查看 ICMP 请求
netsh advfirewall firewall show rule name="文件和打印机共享(后台打印程 序服务 - RPC-EPMAP)"

# 设置 ICMP 请求
netsh advfirewall firewall set rule name="文件和打印机共享(后台打印程 序服务 - RPC-EPMAP)" new enable=yes
```


在 Excel 中使用以下 IF 函数来判断分数所对应的等级
```bash
=IF(A1>=95, "A+", IF(A1>=90, "A", IF(A1>=85, "A-", IF(A1>=80, "B+", IF(A1>=75, "B", IF(A1>=70, "B-", IF(A1>=65, "C+", IF(A1>=60, "C", "C-"))))))))
```

Excel 值粘贴


---

## CMD

- 输出 HOME 路径：

```powershell
# cmd
echo %USERPROFILE%

# powershell
echo $env:USERPROFILE
```


环境变量设置

```bash
# 查看所有的环境变量
set

# 添加环境变量
set ...=...
```


powershell 设置别名

- [给 PowerShell 带来 zsh 的体验](https://zhuanlan.zhihu.com/p/137251716)
- [GitHub - PowerShell/PSReadLine: A bash inspired readline implementation for PowerShell](https://github.com/PowerShell/PSReadLine)


```powershell
# 打开powershell的配置文件
notepad $Profile

# 设置别名
function 别名 { 需要替代的命令，可以包含空格 }

```

在 windows 中的 cmd 设置 alias 别名
>[window中的cmd中设置别名(alias)及设置快捷键打开cmd\_cmd alias-CSDN博客](https://blog.csdn.net/YiRanZhiLiPoSui/article/details/83116819)



---

## 常用快捷键

```shell
ctrl + F  # word、pdf、网页、其他文本编辑器软件都可以用该命令查找目标文本内容；退出一般按ESC
win + E   # 打开文件管理器
win + I   # 打开设置
win + A   # 打开通知中心
win + D  # 返回桌面；再按一次，返回原来的界面
win + Q  # 打开“搜索”超级按钮来搜索应用
win + X  # 打开“快速链接”菜单，可以看到有很多选项的快捷方式
win + 数字 # 启动任务栏中相应的应用程序（从1-0）
win + W # 关掉浏览器标签、windows本地窗口
Alt + F4  # 关掉程序窗口、把浏览器整个窗口关掉、能关掉图片
Alt + 空格 + C  # 能关掉的比Alt+F4还多（比Alt+F4好按许多）
shift + win + 数字 # 启动已经运行的应用程序的新实例
ctrl + A  # 选中所有文本,或所有文件
ctrl + alt + delete / ctrl+shift+Esc  # 打开任务管理器
crtl + alt + tab  # 选中窗口但不打开，使用回车打开；按tab或← →切换
alt + tab   # 选中窗口并打开
win + tab # 任务视图 
ctrl + tab  # 切换窗口(仅同一软件内多个窗口有效，如浏览器开了许多个网页)
```

---

## CMD

command-line interface (CLI)：命令行界面

---

### 常用命令

```shell
cd # 进入文件夹
cd .. # 返回上一级
cd \  # 跳转到根目录

start  # 打开文件夹或文件
md # 新建文件夹
cd .> 1.txt    # 新建空文件
type nul> 1.txt   # 新建空文件
echo content > 1.txt  # 新建非空文件
echo content >> 1.txt # 追加内容

cls  # 清屏
copy  # 复制文件
move  # 移动文件
dir  # 遍历当前路径下所有文件
dir /d  # 显示文件以及文件大小、个数
tree  # 生成目录树
rd  # 删除文件夹
del # 删除文件

ipconfig   # 查看ip地址
shutdown -s  # 关机
shutdown -r  # 关机并重启
shutdown -s -t 60  # 定时关机，定时60s,时间自定

esc    # 清除当前命令行
Ctrl + H # 删除光标左边的一个字符
calc		# 计算器
notepad		# 记事本
winver	# 检查Windows版本
net user  	# 查看用户
whoami		# 查看当前用户

echo %path%  # 查看环境变量

```

>[CMD常用命令大全（值得收藏)\_cmd命令大全\_张时贰的博客-CSDN博客](https://blog.csdn.net/qq_49488584/article/details/122609779)

---

### 切换到目标路径

- 切换至 D 盘、C 盘

```shell
# 切换至D盘、C盘
cd /d d:
cd /d c:
```

- 切换到目标路径
  - 打开指定的文件夹，在路径栏里点击并输入 `cmd`，回车，就进入控制台了。默认路径就是指定文件夹的路径（**快捷简单**）
  - 打开 `cmd`，输入 `cd /d destination`
  - 打开指定的文件夹，按住 shift 键，在空白处右击，在菜单栏中选择 “ 在此处打开 Powershell 窗口 ”

>[如何在cmd中打开指定文件夹路径 - 知乎](https://zhuanlan.zhihu.com/p/370034641)

---

### CMD 与 PowerShell 的区别

- PowerShell 是 CMD 的升级版；支持管道操作；支持 tab（命令）补全（CMD 支持路径、文件名参数补全）

```shell
# 更改目录
cd                  # CMD
cd / Set-Location   # PowerShell

# 列出目录中的文件
dir                  # CMD
Get-ChildItem / dir / ls        # PowerShell

# 重命名
rename              # CMD
Rename-Item         # PowerShell


# PowerShell可查看DOS命令的别名
Get-Alias ls
Get-Alias cd
```



windows 版本还原程序：MediaCreationTool

---

## OFFICE 套件快捷键

按 `Alt + N` 键，上方的选项栏会出现每种操作选项的快捷键


```shell
# 常用选项

P   # 插入图片
```

---

## Acrobat 快捷键

>[Adobe Acrobat 中的键盘快捷键](https://helpx.adobe.com/cn/acrobat/using/keyboard-shortcuts.html)

要启用单键快捷方式，请打开 “ 首选项 ” 对话框（” 编辑 “>” 首选项 “），然后在 ” 一般 “ 下，选择 ” 使用单键加速键访问工具 “ 选项，最后点击最下方的 ” 确定 “。


```shell
# 常用快捷键（做笔记用）
H           # 手形工具
V           # 选择工具
Z           # “选框缩放”工具
P           # 带箭头的“文本框”工具
X           # “文本框”工具
shift + U   # 循环选择高亮工具：“高亮工具”、“下划线文本”、“删划线文本
U           # 当前高亮工具
shift + D   # 循环选择图画标记工具：“云”、“箭头”、“线条”、“矩形”、“椭圆形”、“多边形线条”、“多边形”、“铅笔工具”、“橡皮擦工具”
U           # 当前图画标记工具
```




---

## 系统硬件

`win + R`，输入 `dxdiag`，查看系统信息


惠普笔记本型号：[惠普 Pavilion 畅游人 Power - 15-cb074tx 产品规格 - HP®客户支持](https://support.hp.com/cn-zh/document/c05549489)



---

在文件资源管理器输入下面语句回车

```bash
%LocalAppData%
```

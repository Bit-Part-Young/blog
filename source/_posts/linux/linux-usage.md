---
title: Linux 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Linux 使用
description: Linux 使用
tags:
  - Linux
categories:
  - Linux
date: 2023-07-25 15:00:00
abbrlink: 187835
password:
---

# Linux 使用

## 介绍

WIP...

Bash 脚本，用来生成 Markdown 表格：[Pure bash markdown table generator — josh.fail](https://josh.fail/2022/pure-bash-markdown-table-generator/)

命令历史文件：`~/.bash_history`，`~/.zsh_history`


在线试用各种 Linux 发行版，它会分配一个虚拟机，浏览器里连接桌面：[Test Linux distros online - DistroSea](https://distrosea.com/)


```bash
# 在 .bashrc .zshrc 中 创建与函数功能等同的 alias
cha='WorkDir|JobState|JobId|JobName|NumNodes|NumCPUs|StdErr|StdOut|Command|RunTime|BatchHost|Partition'

showjob() {
    scontrol show job "$1" | grep -E "$cha"
}

alias showjob='showjob'
```


---

### 参考资料

- bash 速查表：[bash cheatsheet](https://github.com/skywind3000/awesome-cheatsheets/blob/master/languages/bash.sh)
- 在线的 Unix 和 Linux 手册页（man 页）：[Linux Man Pages Online](http://man.he.net/)
- Shell 基础及 CLI 工具推荐：[lec1.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec1.md)
- 中科大 Linux 教程：[欢迎 - Linux 101](https://101.lug.ustc.edu.cn/)
- [GitHub - linuxhitchhiker/THGLG: The Hitchhiker's Guide to the Linux : Linux 漫游指南](https://github.com/linuxhitchhiker/THGLG)
- [GitHub - dunwu/linux-tutorial: :penguin: Linux教程，主要内容：Linux 命令、Linux 系统运维、软件运维、精选常用Shell脚本](https://github.com/dunwu/linux-tutorial)
- 用纯 bash 命令实现众多功能：[GitHub - dylanaraps/pure-bash-bible: 📖 A collection of pure bash alternatives to external processes.](https://github.com/dylanaraps/pure-bash-bible)
- 命令行艺术：[GitHub - jlevy/the-art-of-command-line: Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)
- bash 一行命令：[https://github.com/onceupon/Bash-Oneliner](https://github.com/onceupon/Bash-Oneliner)
- [真有人用Linux？（Linux下的工作、科研、学习与生活） - 水源社区](https://shuiyuan.sjtu.edu.cn/t/topic/281312)
- [工具是第一生产力——Linux入门教程](https://ysyx.oscc.cc/slides/2306/02.html)

- Linux 设置：[Setting up Linux • Linux tutorial](https://pranabdas.github.io/linux/setup)

---

- [GitHub - 1Panel-dev/1Panel：现代化、开源的 Linux 服务器运维管理面板。](https://github.com/1Panel-dev/1Panel)
- 备份 dotfiles 工具：[GitHub - deadc0de6/dotdrop: Save your dotfiles once, deploy them everywhere](https://github.com/deadc0de6/dotdrop)
- [GitHub - RubyMetric/chsrc: chsrc 全平台通用换源工具](https://github.com/RubyMetric/chsrc)
- [Bash 脚本如何创建临时文件：mktemp 命令和 trap 命令教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/12/mktemp.html)

[GitHub - skwp/dotfiles: YADR - The best vim,git,zsh plugins and the cleanest vimrc you've ever seen](https://github.com/skwp/dotfiles)

[GitHub - yutkat/dotfiles: The best and strongest dotfiles. Editor: Neovim; Shell: zsh(zinit, powerlevel10k); Terminal: wezterm; Desktop: sway, ulauncher, dunst; OS: ArchLinux (Ubuntu/Fedora/CentOS)](https://github.com/yutkat/dotfiles)（内含一键安装脚本，可参考写法）

[GitHub - dibingfa/flash-linux0.11-talk: 你管这破玩意叫操作系统源码 — 像小说一样品读 Linux 0.11 核心代码](https://github.com/dibingfa/flash-linux0.11-talk)



---

## 使用

```bash
# 设置 root 密码
sudo passwd root

# 安装 ifconfig
sudo apt install net-tools

# 查看 ip 地址 Linux/macOS
ifconfig
```

---

### 基本使用

用户切换：
- 切换到用户：`su username`
- 切换到 root：
	- `sudo -i` 或 `sudo su` 只需输入当前用户密码
	- `su` 需输入 root 用户的密码，Ubuntu 默认没有设置，需通过 `sudo passwd root` 给 root 创建密码

---

#### 系统信息查看

- 系统信息

```bash
lsb_release -a        # 显示 LSB 版本信息
uname -r              # 显示内核版本
uname -a              # 查看完整的内核版本信息
hostnamectl           # 显示系统信息，包括主机名、操作系统、内核等
cat /proc/version
cat /etc/os-release
cat /etc/lsb-release
cat /etc/issue
```


Linux 内核与发行版之间的关系与区别：[Linux的发行版 描述不同发行版之间的区别与联系 - 法月将臣 - 博客园](https://www.cnblogs.com/feifa/p/15430524.html)

- 资源查看

```bash
lscpu  # 查看 CPU 信息
lsmem  # 查看内存信息
lspci  # 查看 PCI 设备信息

intel_gpu_top  # intel 集显

free -gh  # 以 GB 单位显示内存使用情况
vmstat -S M  # 以 MB 单位显示虚拟内存使用情况
htop  # 显示系统资源；增强版 top
```

---

**SSH 配置**

- 用户配置：`~/.ssh/config`
- 系统配置：`/etc/ssh/ssh_config`


---

**Linux 系统文件颜色**

- 白色：一般性文件，如文本文件，配置文件，代码文件等
- 蓝色：目录
- 绿色： 可执行文件
- 红色：压缩文件
- 浅蓝色：链接文件


---

图片查看：`eog` 或 `display`


---

登录 shell 与非登录 shell

- 登录 shell：物理登录到系统上（如在登录界面输入用户名和密码）或远程登录（如 SSH）
- 非登录 shell：打开新终端窗口或启动新 shell（如输入 `bash` 命令）


---

查看环境变量（`PATH`）

```bash
echo $PATH
```

添加环境变量

```bash
# 方式 1
export PATH=$PATH:$HOME/bin

# 方式 2
export PATH=$HOME/bin:$PATH
```


---

### 配置文件

在 Linux 系统中，开机或用户登录时会执行的配置文件（系统级别 > 用户级别）。

---

- 系统级别

1. `/etc/profile`：系统级别全局配置文件，影响所有用户；在登录时执行。
2. `/etc/bash.bashrc`：针对 Bash shell 的全局配置。


---

- 用户级别（用户登录时执行）

当创建新用户时，默认的 `~/.bashrc`，`~/.profile` 等配置文件从 `/etc/skel` 目录复制而来。

1. `~/.bash_profile` 或 `~/.profile` 或 `~/.bash_login`：用户级别配置文件，仅影响当前用户；在用户登录时执行，用于设置个人的环境变量和启动程序；优先级：`~/.bash_profile` > `~/.profile` 或 `~/.bash_login`
2. `~/.bashrc`：用户级别 Bash shell 配置文件；在 Bash shell 中执行，用于设置 shell 选项、别名和环境变量。


---

### 常用命令

参考：

- [Linux命令搜索引擎](https://wangchujiang.com/linux-command/)
- [Shell - Isshiki修's Notebook](https://note.isshikih.top/tech_accu/tool/Shell/)

---

#### 基本命令

```bash
man         # 查看命令帮助
echo        # 打印字符串
pwd         # 显示当前路径
cd          # 切换目录
ls          # 列出目录内容；
cat         # 显示文件内容
tac         # 从最后一行显示文件内容
head tail   # 打印文件首尾内容，默认 10 行
less        # 逐页显示文件内容
touch       # 创建文件/修改文件时间属性
mkdir       # 创建目录
mv          # 移动/重命名
cp          # 复制
rm          # 删除
>  >>       # 标准输出流重定向
<           # 标准输入流重定向
2>  2>>     # 标准错误流重定向
|           # 管道符
rmdir       # 删除空目录
diff        # 查看文件差异
which       # 查看可执行命令所在路径
cut         # 剪切命令
```

```bash
man man                 # 查看如何使用 man 命令
man 3 printf            # 查看如何使用 printf 库函数
man -k xxx              # 检索关键字含有 xxx 的命令

ls -a                   # 会列出 . 和 ..
ls -A                   # almost all，不列出 . 和 ..
ls -1 | grep -v 'XXX*'  # ls 不列出特定的文件/目录

cd -                    # 返回上一次的目录

mkdir -p xxx/xxx        # 创建多级目录

tail -n +2 file         # 从第二行开始输出内容

# 建议设置 
alias mv="mv -v"
alias cp="cp -v"
alias rm="rm -v"


which -a command  # 查看所有同名命令

readlink -f path  # 查看相对路径文件的绝对路径

cut -d, -f3 file  # 从每一行文本中提取以逗号分隔的第三个字段
```


注：简单命令直接列出来

```bash
Basic:
      more
      chmod
      chown
      wget
      top
      history
      uname
      hostname
      
Advanced:
      seq
      scp
      zip
      time
      unzip
      nohup
```



```bash
!!                 # 执行上一条命令
clear # 这个命令并非真正清空，只是把内容全部向上滚，让它们消失在视野中
reset # 这个命令是真正的清空
```


dirname basename



```bash
history  # 返回所有的执行命令及其序号
!! 执行最后一次的命令
!n  # 执行第 n 个命令
```


---

#### tar

- 打包命令，不是压缩/解压缩命令（和其他压缩程序如 gzip、bzip2 等一起实现压缩/解压缩功能）
- 不同压缩格式的文件体积大小：`tar.gz` > `tar.bz2` > `tar.xz`

```bash
# 常用参数
-c             # 创建归档
-x             # 从归档中提取文件
-v             # 显示详细信息
-f             # 指定归档文件名称
-z             # tar.gz 格式
-j             # tar.bz2 格式
-J             # tar.xz 格式
--zstd         # tar.zst 格式
-t             # 显示归档文件中的内容，而非提取文件
-C             # 指定路径
--exclude      # 排除指定文件或目录
--remove-files # 删除原始文件，谨慎使用


# 示例
tar -czvf file.tar.gz file  # 压缩

# 指定解压缩路径
tar -xzvf archive.tar.gz -C /path/destination

# 排除指定文件
tar -czvf archive.tar.gz --exclude=exclude_file file1 file2

gzip -d all.gz  # 解压 .gz 文件
gunzip all.gz   # 同上

zip file.zip file
zip -r xxx.zip directory  # 压缩目录
unzip all.zip             # 解压 .zip 文件

zcat     # 查看 .gz 文件
bzcat    # 查看 .bz2 文件
```


---

#### ln

给文件/目录设置软/字符链接（**需绝对路径**）

```bash
ln -s path/src path/des

# -f force 创建新链接前删除与之同名的文件或链接
# 在当前目录创建与目标文件同名的符号链接
ln -s -f .tmux/.tmux.conf
```


---

#### curl

利用 URL 规则在命令行下工作的文件传输工具

```bash
# 常用参数
-o             # 指定保存文件名
-O             # 保存文件名与远程文件相同
--progress     # 显示进度条
-L             # 跟随重定向，如果服务器返回重定向响应，将自动请求新的 URL
-C             # 下载中断时，继续下载，通常与 -o 一起使用
-s             # 安静模式，减少输出信息，只显示错误信息
-I             # 仅获取远程文件的头部信息，而不下载实际内容
-f             # 请求发生错误时，返回非零的退出状态码，表示请求失败
-S             # 在发生错误时显示错误信息


# 示例
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh

# 有趣 curl 命令；输出 ascii live 字符
curl parrot.live
curl ascii.live/forrest
curl ascii.live/parrot
```


---

#### wget

从网络下载文件

```bash
# 参数
-P         # 指定保存目录
-O         # 指定保存文件名


# 示例
wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O install.sh

# wget -O - 将下载的内容输出到标准输出，而非将其保存为文件
```


---

#### find

查找文件；与另外两个命令对比：

- `whereis`：查找程序的二进制文件、源代码文件和 man 手册路径
- `locate`：通过数据库定位文件路径（可能需要自己安装，数据库更新慢）

```bash
# 常用参数
-name          # 按照文件名查找
-iname         # 按照文件名查找，忽略大小写
-type          # 文件类型；f 普通文件，d 目录，l 软链接
-maxdepth      # 目录最大深度
-mindepth      # 目录最小深度
-size          # 文件大小
-regex         # 正则表达式匹配
-iregex        # 正则表达式匹配，忽略大小写
-exec          # 执行指令
-ok            # 执行指令，但需确认


# 示例
# 查找 txt 或 pdf 文件
find . -type f -name "*.txt" -or -name "*.pdf"
# 查找 tar.gz 文件并删除
find . -type f -name "*.tar.gz" -exec rm {} +

# 找到含下划线的 Python 脚本，并将其换成连字符输出
fes=$(find . -maxdepth 2 -type f -name "*_*.py"); for f in ${fes}; do echo ${f//_/-}; done


# 安装 locate
sudo apt install mlocate

# 更新 locate 数据库
sudo updatedb

locate libstdc++.so.6

# 查看库文件中包含的字符串信息
strings libstdc++.so.6 | grep GLIBCXX
```


---

#### sed

文本处理工具

```bash
# 命令格式
sed [options] 'command' file(s)

# 常用 options
-i             # 直接修改文件内容，而不是输出到标准输出
-n             # 只处理特定行，常与 p 命令一起使用
-e             # 多个命令

# 常用命令
s              # 替换指定字符串
d              # 删除行
p              # 打印行
a              # 在行后添加文本
i              # 在行前插入文本
c              # 替换行
```

示例：

```bash
# 替换指定字符串
sed 's/old/new/' file  # 只替换每行第一个匹配的
sed 's/old/new/g' file  # 标志 g 全局替换
sed 's/old/new/Ng' file  # 从第 N 处匹配开始替换

# 定界符
# / 在 sed 中作为定界符使用，可使用其他任意的定界符
sed 's:old:new:g' file
sed 's|old|new|g' file

# 在行后添加文本
sed '1a\content' file  # 在第 1 行添加内容
sed -i '$a\content' file  # 在最后一行添加内容

# 在行前插入文本
sed '1i\content' file  # 在第 1 行前插入内容
sed '/pattern/i\content' file  # 在匹配内容所在行前插入内容

# 删除行
sed '/cat/d' file  # 删除含 cat 的行
sed '$d' file  # 删除最后一行
sed 'N,Md' file  # 删除第 N-M 行
sed '/^$/d' file  # 删除空白行

# 打印行
sed -n 4p file  # 打印第 4 行
sed -n 4,8p file  # 打印第 4-8 行

# 替换行
sed '1c\content' file  # 替换第 1 行内容

# 组合多个命令
sed -e '1d' -e '/pattern/d' file  # 删除多行
```


---

#### grep

文本搜索工具

```bash
# 常用参数
-i             # 忽略字符大小写
-n             # 显示行号
-c             # 统计匹配的行数
-A N           # N 数字；输出匹配行及之后 N 行
-B N           # N 数字；输出匹配行及之前 N 行
-C N           # N 数字；输出匹配行及之前后各 N 行
-E             # 使用扩展正则表达式
-o             # 只输出匹配到的部分
-v             # 反向匹配 即输出不匹配指定模式的行
-I             # 跳过二进制文件 等同于 --binary-files=without-match
--exclude-dir  # 排除目录
--exclude      # 排除文件
-r             # 递归
-h             # 在匹配内容前标示文件名
-H             # 在匹配内容前不标示文件名
-l             # 列出匹配内容前所属文件名
-L             # 列出无匹配内容的文件名
-m N           # 找到 N 行结果后停止查找，用来限制匹配行数
```


---

#### awk

文本处理工具

- 将输入数据视为记录，每个记录又被进一步划分为字段
- 默认分隔符为空格（可以为多个空格），指定分隔符（`-F:`）
- awk 程序由模式和动作组成（可以没有模式）
- `-v var=` 定义变量

---

awk 中的变量

- `$0`：所有字段
- `$n`：第 n 个字段
- `NR`：记录行号
- `NF`：记录字段数（列数）
- `FNR`：记录文件数

---

awk 中的模式

- `BEGIN`：在 awk 开始读取输入数据流之前执行一些初始化操作
- `END`：在 awk 读取完输入数据流之后执行一些最终操作

```awk
BEGIN {
   command
}

END {
   command
}
```

---

常用功能 awk 命令实现

```bash
awk '{ print NR, $0 }' file  # 输出文件内容并显示行号 

awk 'END { print NR }' file  # 统计行数

awk '{ nf = nf + NF } END { print nf }' file  # 返回总字段数

awk '$3 == 0' file  # 输出第三列为 0 的行

awk 'NR % 2 == 1' file  # 打印奇数行

awk '{ print $NF }' file  # 输出最后一列

# 输出最后一行
awk 'END { print $0 }' file
awk '{ last = $0 } END { print last }' file

# 将第 2 列输出成一行
awk '{printf "%s ", $2}' file
awk '{ names = names $2 " " } END { print names }' file

awk '{printf "%s", $0} END {print ""}' file  # 将所有行输出成 1 行

awk '{ temp = $1; $1 = $2; $2 = temp; print }' file  # 第 1、2 列交换

awk '{ for (i = NF; i > 0; i = i - 1) {printf("%s ", $i)} {printf("\n")}}'  # 逆向排列

awk 'FNR == NR {a[NR] = $0; next} {print a[FNR], $0}' file1 file2 > concat  # 列拼接文件

# 去除重复行（包括空行）
awk '!seen [$0]++' file
# 去除重复行（不包括空行）
awk '!seen[$0]++ || $0 == ""' file
```


---

#### 其他命令

- cat

```bash
cat -          # 读取标准输入
echo '#' | cat - test.log  # 将标准输入的内容和文件内容一并显示

# 参数
-n             # 附加行号
-b             # 给非空行附加行号
-s             # 压缩连续的空行到一行
```

- du：查看文件/目录大小

```bash
du -sh file/folder
du -sh file/folder | sort -h  # 按大小排序
```

- dirs：显示目录堆栈，按照最近访问的目录排序（ohmyzsh 有关 dirs 的 alias 是 `d`）

```bash
# 常用参数
-l             # 展开 ~
-p             # 每个目录按行显示
-v             # 每个目录按行显示并进行编号
-c             # 清空目录堆栈
```

- xargs：参数转化器，将输入数据转换为命令行参数并执行命令。常用于将管道或标准输入 (stdin) 的数据转换为命令的参数。

```bash
# 将 find 找到的文件删除
find . -name *.tmp | xargs rm -f

# 每行 3 个输出
echo "a b c d" | xargs -n 2 echo
```

- tee：从标准输入读取数据并重定向到标准输出和文件（即输出到屏幕上，也保存到文件中，可以多个文件）

```bash
command | tee file

-a             # 不覆盖文件，输出附加到文件的末尾
-i             # 忽略中断信号
```

- nohup：全称 no hang up。允许在用户注销或者断开终端连接之后，仍然运行后台的程序（或直接在命令后添加 `&`，使程序进入后台运行）

```bash
nohup command &
nohup command > output.log &
```

- paste: 可以用来进行多个（csv）文件之间的列合并

```bash
paste -d' ' file1 file2  # 以空格为间隔符来进行列合并文件
```

- kill：杀死进程

```bash
kill -9 PID  # 发送强制终止信号给进程
```

- column：将文本输入格式化成多列输出

```bash
column -s, -t data.csv  # 指定分隔符格式化（表格形式）输出
```

- nl：显示行号

```bash
nl file         # 显示行号
nl -n ln file   # 行号在荧幕的最左方显示；
nl -n rn file   # 行号在自己栏位的最右方显示，且不加 0 ；
nl -n rz file   # 行号在自己栏位的最右方显示，且加 0 ；
nl -b a file    # 表示不论是否为空行，也同样列出行号
```

- type：判断命令的来源（内置命令，外部程序）；命令的类型：别名（alias），关键词（keyword），函数（function），内置命令（builtin）和文件（file）

```bash
# 参数
-a    # 查看一个命令的所有定义
-t    # 返回一个命令的类型
```

- 格式化输出日期：[Bash Date Format Options - Examples](https://www.tutorialkart.com/bash-shell-scripting/bash-date-format-options-examples/)

```bash
date                       # Sun Mar 12 00:32:26 CST 2023
date +%Y%m%d               # 20240228
date +"%Y/%m/%d %H:%M:%S"  # 2023/03/12 00:32:33
```

- hostname：输出主机名

```bash
/etc/hostname  # 配置文件路径

# 临时修改主机名
hostname new_hostname

# 永久修改主机名
hostnamectl set-hostname new_hostname
```

- ldconfig: 用于创建、更新和维护动态链接器运行时绑定的缓存；常在系统启动时运行

```bash
ldconfig -p    # 查看库文件路径和实际缓存的库
sudo ldconfig  # 更新缓存
```

- 文件行数统计

```bash
grep -c '' file
awk 'END { print NR }' file
wc -l file
sed -n '$=' file
```


- 其他

```bash
ldd                    # 列出可执行文件在运行时所需要的共享库
ldd --version          # 查看 GLIBC 版本

echo -n 'XXX' | wc -c  # 统计字符串长度 c 可换成 m

getconf NAME_MAX /     # 获取系统中文件名的最大长度

# Win 行尾符通常是 \r\n（回车符+换行符），Unix/Linux 为 \n
tr -d '\r'             # 删除字符串中的回车符

zcat                   # 查看 gz 压缩文件内容

cal 2024               # 显示 2024 年的日历；或 cal 8 2024，精确到月

env                    # 显示环境变量

pstree                 # 将所有进程以树状图显示
nmon                   # 监控系统资源（应该不常用）
```


---

### Tmux

参考资料：

- [Tmux 配置：打造最适合自己的终端复用工具 - zuorn - 博客园](https://www.cnblogs.com/zuoruining/p/11074367.html)
- [Tmux 使用教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/10/tmux.html)
- [tmux + oh-my-tmux使用指北](https://ixjx.github.io/2020-04-14/tmux-+-oh-my-tmux%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8C%97/)
- tmux 配置：[GitHub - gpakosz/.tmux: 🇫🇷 Oh my tmux! My self-contained, pretty & versatile tmux configuration made with ❤️](https://github.com/gpakosz/.tmux)

tmux session 管理：

- [GitHub - tmux-python/tmuxp: 🖥️ Session manager for tmux, build on libtmux.](https://github.com/tmux-python/tmuxp)
- [GitHub - tmuxinator/tmuxinator: Manage complex tmux sessions easily](https://github.com/tmuxinator/tmuxinator)

替代工具：[GitHub - zellij-org/zellij: A terminal workspace with batteries included](https://github.com/zellij-org/zellij)


```bash
# 安装在 ~
cd ~
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```


将终端和会话分离

后台服务 (server)，会话 (session)，窗口 (window)，窗格 (pane)
一个 session 可以包含多个 window，一个 window 可以被分割成多个 pane


安装
```bash
brew install tmux  # macOS

sudo apt install tmux  # Ubuntu
```

session 相关命令

```bash
tmux -V  # 查看版本

tmux source-file ~/.tmux.conf  # 刷新配置

tmux new -s <session-name>  # 新建 session，默认从 0 开始

tmux detach  # 分离 session

tmux ls  # tmux list-sessions 查看所有 sessions

tmux a  # tmux attach 重新连接 session
tmux attach -t <session-name>

tmux kill-session -t <session-name>  # kill

tmux switchc -t <session-name>  # 切换

tmux rename-session -t 0 <new-name>  # 重命名
```


默认前缀键：`Ctrl + b`，oh-my-tmux 添加了 `Ctrl + a`（如何将其取消或换成别的）

快捷键

```bash
prefix + s       # 可视化 session


# 分屏相关
prefix + %       # 
prefix + "       # 
```



---

### 文件系统

>[Linux 系统目录结构 | 菜鸟教程](https://www.runoob.com/linux/linux-system-contents.html)


![ft.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202312311529652.png)

| 文件夹                     | 描述                                                         |
|:--------------------------: | :------------------------------------------------------------: |
| `/bin`                     | 包含用户的基本二进制程序（如 ls, cat 等）。对所有用户可用。  |
| `/sbin`                    | 存放系统管理和维护的必需二进制程序，如启动和修复工具。只有 root 或需要特定权限的用户可用。 |
| `/etc`                     | 包含系统配置文件。这些文件由系统管理员编辑，控制系统的行为。 |
| `/lib`、`/lib32`、`/lib64` | 存放系统库文件和内核模块。`/lib32` 和 `/lib64` 分别用于 32 位和 64 位库。 |
| `/usr`                     | 包含用户程序和数据。类似于 Windows 下的 Program Files，包括 `/usr/bin`、`/usr/sbin`、`/usr/local` 等子目录。 |
| `/home`                    | 用户的个人文件夹。每个用户都有一个对应的目录。               |
| `/root`                    | root 用户的家目录。                                          |
| `/var`                     | 存放经常变化的文件，如日志、数据库等。                       |
| `/tmp`                     | 用于存放临时文件。系统重启时，这些文件可能会被删除。         |
| `/boot`                    | 包含启动 Linux 系统所需的文件，如内核、引导加载程序等。      |
| `/dev`                     | 包含设备文件，这些文件代表系统中的硬件设备。                 |
| `/proc`                    | 虚拟文件系统，提供对内核和进程信息的访问。                   |
| `/sys`                     | 另一个虚拟文件系统，用于与内核交互。                         |
| `/media`                   | 用于挂载可移除媒体，如 CD-ROMs、USB 驱动器等。               |
| `/mnt`                     | 通常用于临时挂载文件系统。                                   |
| `/opt`                     | 用于存放可选的应用软件包和数据文件。                         |
| `/run`                     | 用于存储系统运行时的数据，如套接字和进程 ID，通常在启动时创建。 |
| `/srv`                     | 存放服务相关的数据，如 FTP 或 Web 服务器的数据。             |
| `/lost+found`               | 当系统意外崩溃或机器非正常关机时，文件系统检查 (fsck) 的恢复文件存放地。 |
| `/snap`                    | 用于存放 Snappy 软件包管理器的应用程序和数据。               |

---

### 其他

- 命令提示符：环境变量 `PS1`；[note/Linux系统管理/PS1：配置命令提示符.md at main · zze326/note · GitHub](https://github.com/zze326/note/blob/main/Linux%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86/PS1%EF%BC%9A%E9%85%8D%E7%BD%AE%E5%91%BD%E4%BB%A4%E6%8F%90%E7%A4%BA%E7%AC%A6.md)

- ETA（Estimated Time of Arrival，预计到达时间）是 Linux 系统中一个常见的术语，用于估计正在运行的进程或任务剩余执行时间。

- 终端 Tab 补全忽略大小写：[linux下，按tab补全时，忽略大小写的配置\_linux命令行终端设置tab补全文件名或路径不区分大小写-CSDN博客](https://blog.csdn.net/lianshaohua/article/details/108710098)


alias 使用参数：以定义函数的方式进行：[https://forsworns.github.io/zh/blogs/20190919/](https://forsworns.github.io/zh/blogs/20190919/)

```bash
alias ipynb2md="py2md(){jupyter nbconvert --to markdown $1}; py2md"
```


zsh 与 bash 之间的一些区别：

- zsh 数组索引从 1 开始， bash 从 0 开始



```bash
if [[ "$kind" == "app" ]]; then
    git status &>/dev/null && echo "error: your current working directory is inside a git repository" >&2 && exit 1
fi
```


>&2 表示将标准输出重定向到标准错误输出（>&重定向操作符）（1 表示标准输出，2 表示标准错误）

`&>`：重定向操作符，将标准输出和标准错误都重定向到同一个文件或设备中

`/dev/null`：空设备文件，将所有的输出都丢弃掉


一般来说，头文件通常位于 **`/usr/include`** 或 **`/usr/local/include`** 目录中，而库文件通常位于 **`/usr/lib`** 或 **`/usr/local/lib`** 目录中。请注意，库文件可能会有不同的后缀，例如 `.so` 动态库 `.a` 静态库。


crysinfo 程序（孔老师程序）
6a 选项 查看 Assign Wyckoff letter（等同位点）


configure、 make、 make install 相关区别：[configure、 make、 make install 背后的原理(翻译) - 知乎](https://zhuanlan.zhihu.com/p/77813702)

linux configure `--prefix` 的作用是：编译的时候用来指定程序存放路径


>[linux configure 的 --prefix 参数的作用-CSDN博客](https://blog.csdn.net/xiaojin21cen/article/details/90600284)

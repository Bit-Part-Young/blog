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


---

### 参考资料

- Bash 速查表：[bash cheatsheet](https://github.com/skywind3000/awesome-cheatsheets/blob/master/languages/bash.sh)
- [Comprehensive Linux Cheatsheet](https://gto76.github.io/linux-cheatsheet/)
- 在线的 Unix 和 Linux 手册页（man 页）：[Linux Man Pages Online](http://man.he.net/)
- Shell 基础及 CLI 工具推荐：[lec1.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec1.md)
- 中科大 Linux 教程：[欢迎 - Linux 101](https://101.lug.ustc.edu.cn/)
- [GitHub - ustclug/Linux201-docs: Linux 201 进阶教程阅读资料](https://github.com/ustclug/Linux201-docs)
- [GitHub - linuxhitchhiker/THGLG: Linux 漫游指南](https://github.com/linuxhitchhiker/THGLG)
- [GitHub - dunwu/linux-tutorial: :penguin: Linux教程，主要内容：Linux 命令、Linux 系统运维、软件运维、精选常用Shell脚本](https://github.com/dunwu/linux-tutorial)
- [真有人用Linux？（Linux下的工作、科研、学习与生活） - 水源社区](https://shuiyuan.sjtu.edu.cn/t/topic/281312)
- [工具是第一生产力——Linux入门教程](https://ysyx.oscc.cc/slides/2306/02.html)
- Linux 设置：[Setting up Linux • Linux tutorial](https://pranabdas.github.io/linux/setup)
- [GitHub - dibingfa/flash-linux0.11-talk: 你管这破玩意叫操作系统源码 — 像小说一样品读 Linux 0.11 核心代码](https://github.com/dibingfa/flash-linux0.11-talk)
- Linux 内核与发行版之间的关系与区别：[Linux的发行版 描述不同发行版之间的区别与联系 - 法月将臣 - 博客园](https://www.cnblogs.com/feifa/p/15430524.html)
- [Linux 教程 - Note/wiki/linux\_teach.md at master · Kicamon/Note · GitHub](https://github.com/Kicamon/Note/blob/master/wiki/linux_teach.md)

- Linux 软件：[Office & Productivity Apps - AlternativeTo](https://alternativeto.net/category/productivity/)

- [direnv](https://github.com/direnv/direnv)：Shell 扩展，可根据当前目录加载和卸载环境变量

- 环境变量管理工具：[misc/bmod at master · yhli1016/misc · GitHub](https://github.com/yhli1016/misc/tree/master/bmod)

- 单行 Shell 命令：[Shell One Liner - GitHub - trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge#shell-one-liners-toc)

- SSH 配置管理：[GitHub - soulteary/ssh-config: 1MB size, 100% Coverage, Use more expressive YAML / JSON to manage your Config files. --- 1MB大小，100% 测试覆盖，使用更具表现力的YAML / JSON来管理您的配置文件。](https://github.com/soulteary/ssh-config)



---

## 使用

### 工具

- 在线试用各种 Linux 发行版，它会分配一个虚拟机，浏览器里连接桌面：[Test Linux distros online - DistroSea](https://distrosea.com/)

- 用纯 Bash 命令实现众多功能：[GitHub - dylanaraps/pure-bash-bible: 📖 A collection of pure bash alternatives to external processes.](https://github.com/dylanaraps/pure-bash-bible)

- 命令行艺术：[GitHub - jlevy/the-art-of-command-line: Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)

- Bash 一行命令：[https://github.com/onceupon/Bash-Oneliner](https://github.com/onceupon/Bash-Oneliner)

- [GitHub - RubyMetric/chsrc: chsrc 全平台通用换源工具](https://github.com/RubyMetric/chsrc)

- [Bash 脚本如何创建临时文件：mktemp 命令和 trap 命令教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/12/mktemp.html)

- Linux 配置文件：
    - [GitHub - skwp/dotfiles](https://github.com/skwp/dotfiles)
    - [GitHub - yutkat/dotfiles](https://github.com/yutkat/dotfiles)（内含一键安装脚本，可参考写法）
    - Linux 配置文件（还行）：[GitHub - LintaoAmons/CoolStuffes: 我的分享放这里了，大家随便拿去用啊，记得给个星星就行啦～](https://github.com/LintaoAmons/CoolStuffes)
    - 备份 dotfiles：[GitHub - deadc0de6/dotdrop: Save your dotfiles once, deploy them everywhere](https://github.com/deadc0de6/dotdrop)

- 生成 Markdown 表格（Bash 脚本）：[Pure bash markdown table generator — josh.fail](https://josh.fail/2022/pure-bash-markdown-table-generator/)


---

### 基本使用

- 系统信息查看

```bash
hostnamectl           # 显示系统信息，包括主机名、操作系统、内核等
lsb_release -a        # 显示 LSB 版本信息
uname -r              # 显示内核版本
uname -a              # 查看完整的内核版本信息
cat /proc/version
cat /etc/os-release
cat /etc/lsb-release
cat /etc/issue
```

- 系统资源查看

```bash
lscpu                 # 查看 CPU 信息
lsmem                 # 查看内存信息
lspci                 # 查看 PCI 设备信息

intel_gpu_top         # Intel 集显

free -gh              # 以 GB 单位显示内存使用情况
vmstat -S M           # 以 MB 单位显示虚拟内存使用情况
htop                  # 增强版 top
```

- 图片查看：`eog` 或 `display`

- Linux 系统文件颜色
    - 白色：一般性文件，如文本文件，配置文件，代码文件等
    - 蓝色：目录
    - 绿色： 可执行文件
    - 红色：压缩文件
    - 浅蓝色：链接文件

- SSH 配置
    - 用户配置：`~/.ssh/config`
    - 系统配置：`/etc/ssh/ssh_config`

- 用户切换
    - 切换到用户：`su username`
    - 切换到 root：
        - `sudo -i` 或 `sudo su` 只需输入当前用户密码
        - `su` 需输入 root 用户的密码，Ubuntu 默认没有设置，通过 `sudo passwd root` 给 root 创建密码

- 创建新用户

```bash
# 方式 1
sudo useradd -m user        # -m 表示为新用户创建主目录，默认位置在 /home/user
sudo passwd user            # 为新用户设置密码

# 方式 2
sudo adduser user           # 系统会提示输入一些信息，如密码、全名等，按提示操作即可

sudo usermod -aG sudo user  # 可选；将新用户添加到 sudo 组，以便赋予管理员权限

su - user                   # 切换到新用户
```


---

### Session

profile、bash_profile、bashrc 之间的区别：[profile、bash\_profile、bashrc的用途与区别 - 简书](https://www.jianshu.com/p/a57e8f1a3426)

---

用户每次使用 Shell，都会开启一个与 Shell 的 Session（对话）。

Session 有两种类型：登录 Session 和非登录 Session。

---

登录 Session 是用户登录系统以后，系统为用户开启的原始 Session，通常需要用户输入用户名和密码进行登录。

登录 Session 一般进行整个系统环境的初始化，启动的初始化脚本依次如下：

- `/etc/profile`：所有用户的全局配置脚本
- `/etc/profile.d` 目录里面所有 `.sh` 文件
- `~/.bash_profile`、`~/.bash_login`、`~/.profile`：用户的个人配置脚本（执行顺序同书写顺序）

Linux 发行版更新的时候，会更新 `/etc` 里面的文件，比如 `/etc/profile`，因此不要直接修改这个文件。如果想修改所有用户的登陆环境，就在 `/etc/profile.d` 目录里面新建 `.sh` 脚本。

修改个人的登录环境，一般是写在 `~/.bash_profile` 里面。

```bash
bash --login          # 强制执行登录 Session 会执行的脚本
bash --noprofile      # 跳过上面这些 Profile 脚本
```

---

非登录 Session 是用户进入系统以后，手动新建的 Session，这时不会进行环境初始化。如执行 `bash` 命令，就会新建一个非登录 Session。

非登录 Session 的初始化脚本依次如下：

- `/etc/bash.bashrc`：对全体用户有效
- `~/.bashrc`：仅对当前用户有效

`~/.bashrc` 通常是最重要的脚本。非登录 Session 默认会执行它，而登录 Session 一般也会通过调用执行它。每次新建一个 Bash 窗口，就相当于新建一个非登录 Session，所以 `~/.bashrc` 每次都会执行。注意，执行脚本相当于新建一个非互动的 Bash 环境，但是这种情况不会调用 `~/.bashrc`。

```bash
bash --norc           # 禁止在非登录 Session 执行 ~/.bashrc 脚本

bash --rcfile testrc  # 指定另一个脚本代替 .bashrc
```


---

### 常用命令

- [Linux命令搜索引擎](https://wangchujiang.com/linux-command/)

---

#### 常用基本命令

- 常用基本命令

```bash
man                     # 查看命令帮助
echo                    # 打印字符串
pwd                     # 显示当前路径
cd                      # 切换目录
ls                      # 列出目录内容
cat                     # 显示文件内容
tac                     # 从最后一行显示文件内容
head tail               # 打印文件首尾内容，默认 10 行
less                    # 逐页显示文件内容
touch                   # 创建文件/修改文件时间属性
mkdir                   # 创建目录
mv                      # 移动/重命名
cp                      # 复制
rm                      # 删除
rmdir                   # 删除空目录
diff                    # 查看文件差异
which                   # 查看可执行命令所在路径
cut                     # 剪切命令
clear                   # 清屏
reset                   # 重置终端
dirname                 # 获取文件路径的目录部分
basename                # 获取文件路径的文件部分
chmod                   # 变更文件或目录的权限（rwx: 读、写、执行权限）
chown                   # 变更文件或目录的拥有者或所属群组
time                    # 统计指定命令运行耗时
|                       # 管道符
>  >>                   # 标准输出流重定向
<                       # 标准输入流重定向
2>  2>>                 # 标准错误流重定向
```

- 常用基本命令进阶用法

```bash
man man                 # 查看如何使用 man 命令
man 3 printf            # 查看如何使用 printf 库函数
man -k xxx              # 检索关键字含有 xxx 的命令

ls -a                   # 会列出 . 和 ..
ls -A                   # almost all，不列出 . 和 ..
ls -d */                # 只列出目录
ls -1 | grep -v 'XXX*'  # 不列出特定的文件/目录
ls -tr                  # -t 按修改时间排序（新文件排在前面）；-r 逆序排列
ls -v                   # 按数值大小排序（默认字母顺序；使 10 显示在 9 后面）

cd -                    # 返回上一次的目录

mkdir  xxx/xxx          # 会报错
mkdir -p xxx/xxx        # 创建多级目录；不会报错

tail -n +2 file         # 从第二行开始输出内容

# 建议设置的命令 alias
alias mv="mv -v"
alias cp="cp -v"
alias rm="rm -v"

# 对比目录差异
diff -urp folder1 folder2 2>/dev/null

which -a command  # 查看所有同名命令

readlink -f path  # 查看相对路径文件的绝对路径

cut -d, -f3 file  # 从每一行文本中提取以逗号分隔的第三个字段
```


---

#### tar

- 打包命令，非压缩/解压缩命令（和其他程序如 gzip、bzip2 等一起实现压缩/解压缩功能）

- 不同压缩格式的文件体积大小：`tar.gz` > `tar.bz2` > `tar.xz`

```bash
# 常用参数
-c                    # 创建归档
-x                    # 从归档中提取文件
-v                    # 显示详细信息
-f                    # 指定归档文件名称
-z                    # tar.gz 格式
-j                    # tar.bz2 格式
-J                    # tar.xz 格式
--zstd                # tar.zst 格式
-t                    # 显示归档文件中的内容，而非提取文件
-C                    # 指定路径
--exclude             # 排除指定文件或目录


# 示例
tar -czvf file.tar.gz file  # 压缩
# 指定解压缩路径
tar -xzvf archive.tar.gz -C DEST
# 排除指定文件
tar -czvf archive.tar.gz --exclude=exclude_file file

gzip -d all.gz             # 解压 .gz 文件
gunzip all.gz              # 同上

zip xxx.zip file           # 压缩
zip -r xxx.zip directory   # 递归压缩目录
unzip all.zip              # 解压 .zip 文件

zcat           # 查看 .gz 文件
bzcat          # 查看 .bz2 文件
```


---

#### ln

- 给文件/目录设置符号（软）链接（**建议绝对路径**）

```bash
ln -s SRC DEST

# 参数
-f                    # 强制；创建新链接前删除与之同名的文件或链接
```


---

#### curl

- 利用 URL 规则在命令行下工作的文件传输工具

```bash
# 常用参数
-o                    # 写入到文件中（指定文件名）
-O                    # 同上（保存文件名与远程文件相同）
--progress            # 显示进度条
-L                    # 跟随服务器的重定向
-C                    # 下载中断时，继续下载，通常与 -o 一起使用
-I                    # 仅获取 HTTP 响应头而不下载响应体
-i                    # 获取 HTTP 响应头、下载响应体
-v                    # 显示完整的 HTTP 通信过程
-s                    # 安静模式
-f                    # 请求发生错误时，返回非零的退出状态码，表示请求失败
-S                    # 在发生错误时显示错误信息
-X                    # 指定请求使用的 HTTP 方法，如 GET, POST, PUT 等


# 示例
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh

# 有趣 curl 命令；输出 ascii live 字符
curl parrot.live
curl ascii.live/forrest
curl ascii.live/parrot
```


---

#### wget

- 从网络下载文件

```bash
# 参数
-P                    # 指定保存目录
-O                    # 指定保存文件名


# 示例
wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O install.sh

# wget -O - 将下载的内容输出到标准输出，而非将其保存为文件
```


---

#### find

- 查找文件

```bash
# find 与另外两个命令对比
whereis               # 查找程序的二进制文件、源代码文件和 man 手册路径
locate                # 通过数据库定位文件路径（可能需要自己安装，数据库更新慢）

# 常用参数
-name                 # 按照文件名查找
-iname                # 同上，忽略大小写
-type                 # 文件类型（f 普通文件；d 目录；l 符号链接）
-maxdepth             # 目录最大深度
-mindepth             # 目录最小深度
-size                 # 文件大小
-regex                # 正则表达式匹配
-iregex               # 同上；忽略大小写
-exec                 # 执行指令
-ok                   # 同上；但需确认
-perm                 # 按照文件权限查找；111 精确匹配，/111 任意一个匹配，-111 都必须匹配


# 示例
# 查找 txt 或 pdf 文件
find . -type f -name "*.txt" -or -name "*.pdf"

# 查找 tar.gz 文件并删除
find . -type f -name "*.tar.gz" -exec rm {} +

# 查找文件（使用 for 循环等长 Shell 命令）
# for f 为简略写法，可全写为 for f in $@
# 第 2 个 bash 是脚本名，可任意命名
find . -type f -name "*.txt" -exec bash -c "for f; do echo $f; done" bash {} +


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

- 文本处理工具

- 注意事项：
    - macOS 中需在使用 `i\` `a\`、`c\` 命令时，需在 `\` 后换行
    - macOS 在使用 `-i` 选项时，需在后面添加 `''`

```bash
# 命令格式
sed [options] 'command' file(s)

# 常用 options
-i                    # 直接修改文件内容，而不是输出到标准输出
-n                    # 只处理特定行，常与 p 命令一起使用
-e                    # 多个命令

# 常用命令
s                     # 替换指定字符串
d                     # 删除行
p                     # 打印行
a\                    # 在行后添加文本
i\                    # 在行前插入文本
c\                    # 替换行
```

- 示例

```bash
# 替换指定字符串
sed 's/old/new/' file      # 只替换每行第一个匹配的
sed 's/old/new/g' file     # 标志 g 全局替换
sed 's/old/new/Ng' file    # 从第 N 处匹配开始替换

# 定界符
# / 在 sed 中作为定界符使用，可使用其他任意的定界符
sed 's:old:new:g' file
sed 's|old|new|g' file

# 在行后添加文本
sed '1a\xxx' file          # 在第 1 行添加内容

# 在行前插入文本
sed '1i\content' file      # 在第 1 行前插入内容
sed '/xxx/i\content' file  # 在匹配内容所在行前插入内容

# 删除行
sed '/cat/d' file          # 删除含 cat 的行
sed '$d' file              # 删除最后一行
sed 'N,Md' file            # 删除第 N-M 行
sed '/^$/d' file           # 删除空白行

# 打印行；command 可不加引号
sed -n 4p file             # 打印第 4 行
sed -n 4,8p file           # 打印第 4-8 行

# 替换行
sed '1c\xxx' file          # 替换第 1 行内容

# 组合多个命令 -e
sed -e '1d' -e '$d' file   # 删除多行
```


---

#### grep

- 文本搜索工具

```bash
# 常用参数
-q                    # 安静模式
-i                    # 忽略字符大小写
-n                    # 显示行号
-c                    # 统计匹配的行数
-A N                  # N 数字；输出匹配行及之后 N 行
-B N                  # N 数字；输出匹配行及之前 N 行
-C N                  # N 数字；输出匹配行及之前后各 N 行
-E                    # 使用扩展正则表达式
-o                    # 只输出匹配到的部分
-P                    # 
-v                    # 反向匹配，即输出不匹配指定模式的行
-I                    # 跳过二进制文件 等同于 --binary-files=without-match
--exclude-dir         # 排除目录
--exclude             # 排除文件
-r                    # 递归
-h                    # 在匹配内容前标示文件名
-H                    # 在匹配内容前不标示文件名
-l                    # 列出匹配内容前所属文件名
-L                    # 列出无匹配内容的文件名
-m N                  # 找到 N 行结果后停止查找，用来限制匹配行数

egrep                 # 等同于 grep -E

grep -E 'p1|p2' file  # 匹配多个 pattern

grep '\-1.2' file     # 匹配负数时需 \ 转义 


grep -c "^[[:space:]]*$" file    # 统计空行
```


---

#### awk

- 文本处理工具

- 将输入数据视为记录，每个记录又被进一步划分为字段

- 默认分隔符为空格（可以为多个空格），指定分隔符（`-F:`）

- awk 程序由模式和动作组成（可以没有模式）

- `-v var=` 定义变量

```bash
# awk 中的变量
$0             # 所有字段
$n             # 第 n 个字段
NR             # 记录行号
NF             # 记录字段数（列数）
FNR            # 记录文件数

# awk 中的模式
BEGIN          # 在 awk 开始读取输入数据流之前执行一些初始化操作
END            # 在 awk 读取完输入数据流之后执行一些最终操作

-F':'          # 指定 : 为分隔符

# 语法
BEGIN {
   command
}

END {
   command
}
```

- 常用功能 awk 命令实现

```bash
awk '{ print NR, $0 }' file        # 输出文件内容并显示行号
awk 'END { print NR }' file        # 统计行数
awk '$3 == 0' file                 # 输出第三列为 0 的行
awk 'NR % 2 == 1' file             # 输出奇数行
awk 'NR <= 3' file                 # 输出前 3 行
awk '{ print $NF }' file           # 输出最后一列
awk '/kwd/{flag=1} flag' file      # 输出匹配的关键词所在行至最后一行的内容
awk '/kwd1/,/kwd2/' file           # 输出匹配的关键词之间的行内容
awk '{printf "%.5f\n", $1}' file   # 保留 5 位小数输出

# 返回总字段数
awk '{ nf = nf + NF } END { print nf }' file

# 输出最后一行
awk 'END { print $0 }' file
awk '{ last = $0 } END { print last }' file

# 将第 2 列输出成一行
awk '{printf "%s ", $2}' file
awk '{ names = names $2 " " } END { print names }' file

# 将所有行输出成 1 行
awk '{printf "%s", $0} END {print ""}' file

# 第 1、2 列交换
awk '{ temp = $1; $1 = $2; $2 = temp; print }' file

# 将第 2 列数值相加
awk '{sum += $2} END {print sum}' file

# 逆向排列
awk '{ for (i = NF; i > 0; i = i - 1) {printf("%s ", $i)} {printf("\n")}}' file

# 列拼接文件
awk 'FNR == NR {a[NR] = $0; next} {print a[FNR], $0}' file1 file2 > concat

# 去除重复行（包括空行）
awk '!seen[$0]++' file
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

- dirs：显示目录堆栈，按照最近访问的目录排序

```bash
# 常用参数
-l             # 展开 ~
-p             # 每个目录按行显示
-v             # 每个目录按行显示并进行编号
-c             # 清空目录堆栈
```

- xargs：参数转化器，将输入数据转换为命令行参数并执行命令。常用于将管道或标准输入 (stdin) 的数据转换为命令的参数

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

- nohup：全称 no hang up；允许在用户注销或者断开终端连接之后，仍然运行后台的程序（或直接在命令后添加 `&`，使程序进入后台运行）

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
nl -n ln file   # 行号在荧幕的最左方显示
nl -n rn file   # 行号在自己栏位的最右方显示，且不加 0
nl -n rz file   # 行号在自己栏位的最右方显示，且加 0
nl -b a file    # 表示不论是否为空行，也同样列出行号
```

- stat：查看文件的创建时间和最新修改时间

```bash
stat file

# 信息
Access              # 文件上次访问时间
Modify              # 文件内容的最后修改时间
Change              # 文件的元数据（权限、所有者等）最后修改的时间
Birth               # 文件的创建时间（超算文件系统不支持）

# 输出示例
  File: file
  Size: 34680         Blocks: 72         IO Block: 4096   regular file
Device: 800h/2048d    Inode: 332005565   Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1010/  XXX)   Gid: ( 1011/  XXX)
Access: 2025-03-06 10:31:27.649498750 +0800
Modify: 2025-03-06 03:15:05.169757697 +0800
Change: 2025-03-06 10:29:34.115994373 +0800
 Birth: 2025-03-06 10:29:34.115994373 +0800
```

- type：判断命令的类型/来源（内置命令，外部程序）

```bash
# 参数
-a           # 查看一个命令的所有定义
-t           # 返回一个命令的类型

# 命令类型
alias        # 别名
keyword      # 关键词
function     # 函数
builtin      # 内置命令
file         # 文件
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

- ps：显示进程信息

```bash
-e / -A        # 显示所有进程
-f             # 全格式显示
-l             # 长格式显示
-u USER        # 指定用户
-o             # 自定义输出
-p PID         # 指定 PID
-c             # 显示进程的实际命令名，而非完整的命令行

# 进程信息
UID            # 用户 ID
PID            # 进程 ID
PPID           # 父进程 ID
C              # CPU 使用率
STIME          # 启动时间
TTY            # 终端名称
TIME           # CPU 时间
CMD            # 命令名称

ps -p PID -o ...
# 后面添加 =，会不显示 title
user           # 用户
lstart         # 开始时间；详细
lstart         # 同上；简短
psr            # 进行运行对应的 CPU 编号
comm           # 命令行

# 统计每个用户的进程数
ps hax -o user | sort | uniq -c | sort -r
```

- top：显示系统资源使用情况的实时工具；运行时是交互式的

```bash
# 常用交互操作快捷键
h / ?          # 查看帮助
q              # 退出
M              # 以内存使用量排序
P              # 以 CPU 使用率排序
T              # 以进程运行时间排序
n              # 设定 top 显示的进程数量
z              # 切换彩色显示
x              # 高亮显示当前排序列
y              # 高亮运行状态为 running 的进程
o              # 小写字母 O；筛选 PID，输入筛选条件（如 COMMAND=bash）
```

- wc：统计文件的行数、字数和字节数（或字符数）

```bash
wc file        # 基本使用
# 参数
-l             # 只显示行数
-w             # 只显示单词数
-c             # 只显示字节数
-m             # 只显示字符数

# 输出内容示例
10   35  240 file
```

- strace：Linux 系统中诊断、调试和指令跟踪工具。它主要用于跟踪系统调用：程序与操作系统内核之间的交互

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

# 在终端上打印一行由井号(#)组成的横条，其长度与终端的列数相同
# 可作为视觉分隔线
printf "%`tput cols`s" | tr ' ' '#'

# 文件行数统计
grep -c '' file
awk 'END { print NR }' file
wc -l file
sed -n '$=' file

# 获取关键词的下一行内容
# 相同的关键词有多个时，grep 得到的内容会多出 --- 一行内容
grep -A 1 'Size' filename | awk 'NR % 3 == 2 {print $1}'
sed -n '/Size/{n;p}' filename
```


---

### 文件系统层次结构

- 参考：
    - [Unix filesystem - Wikipedia](https://en.wikipedia.org/wiki/Unix_filesystem#Conventional_directory_layout)
    - [Filesystem Hierarchy Standard - Wikipedia](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
    - [Linux 系统目录结构 - 菜鸟教程](https://www.runoob.com/linux/linux-system-contents.html)

- 示意图
![](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images/Standard-unix-filesystem-hierarchy.svg)

---

- 注意事项：
    - `/usr/bin`：系统预装的可执行程序，会随着系统升级而改变
    - `/usr/local/bin`：用户放置本地可执行程序的目录，不会被系统升级而覆盖同名文件

```bash
/bin              # 基本二进制文件；对所有用户可用
/sbin             # 系统二进制文件
/etc              # 配置文件
/lib              # 库文件
/usr              # 用户程序和数据
  /usr/bin          # 用户二进制文件
  /usr/sbin         # 
  /usr/lib          # 用户库文件
  /usr/local        # 用户本地安装的程序（含 bin lib etc 等目录）
/home             # 用户家目录
/root             # root 用户家目录
/var              # 可变文件（日志、缓存）
  /var/cache        # 应用程序缓存数据
  /var/log          # 日志文件
/tmp              # 临时文件（重启不会保留）
/boot             # 引导启动文件
/dev              # 设备文件
/proc             # 虚拟文件系统，以文件形式提供对内核和进程信息
/mnt              # 临时挂载文件系统
/opt              # 可选/附加软件
```

---

### 其他

- 命令提示符：环境变量 `PS1`
    - [note/Linux系统管理/PS1：配置命令提示符.md at main · zze326/note · GitHub](https://github.com/zze326/note/blob/main/Linux%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86/PS1%EF%BC%9A%E9%85%8D%E7%BD%AE%E5%91%BD%E4%BB%A4%E6%8F%90%E7%A4%BA%E7%AC%A6.md)；
    - [命令提示符 - Bash 脚本教程 - 网道](https://wangdoc.com/bash/prompt)

- ETA（Estimated Time of Arrival，预计到达时间）是 Linux 系统中一个常见的术语，用于估计正在运行的进程或任务剩余执行时间。

- 终端 Tab 补全忽略大小写：[linux下，按tab补全时，忽略大小写的配置\_linux命令行终端设置tab补全文件名或路径不区分大小写-CSDN博客](https://blog.csdn.net/lianshaohua/article/details/108710098)

- 在 `.bashrc` 中定义函数

```bash
# 详细列出给定目录及其子目录的文件信息
lsr() { find "${@:-.}" -print0 | sort -z | xargs -0 ls --color=auto -dlha; }
```

- zsh 与 bash 之间的一些区别：
    - zsh 数组索引从 1 开始， bash 从 0 开始

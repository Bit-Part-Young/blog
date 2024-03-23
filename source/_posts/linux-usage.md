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
abbrlink: "18783"
password:
---

# Linux 使用

## 介绍

WIP…

---

### 参考资料

Shell 基础及 CLI 工具推荐
>[lec1.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec1.md)

>[GitHub - linuxhitchhiker/THGLG: The Hitchhiker's Guide to the Linux : Linux 漫游指南](https://github.com/linuxhitchhiker/THGLG)

bash 速查表
>[https://github.com/skywind3000/awesome-cheatsheets/blob/master/languages/bash.sh](https://github.com/skywind3000/awesome-cheatsheets/blob/master/languages/bash.sh)

不借助 bash 中已有命令实现众多功能
>[GitHub - dylanaraps/pure-bash-bible: 📖 A collection of pure bash alternatives to external processes.](https://github.com/dylanaraps/pure-bash-bible)

>[GitHub - dunwu/linux-tutorial: :penguin: Linux教程，主要内容：Linux 命令、Linux 系统运维、软件运维、精选常用Shell脚本](https://github.com/dunwu/linux-tutorial)



---

## 使用

### 基本使用

**查看系统信息**

- `lsb_release -a` - 显示 LSB 版本信息。
- `uname -r` - 显示内核版本。
- `uname -a` - 查看完整的内核版本信息
- `hostnamectl` - 显示系统信息，包括主机名、操作系统、内核等。
- 其他 - 如 `cat /proc/version`、`cat /etc/os-release`、`cat /etc/lsb-release`、`cat /etc/issue` 等


Linux 内核与发行版之间的关系与区别
>[Linux的发行版 描述不同发行版之间的区别与联系 - 法月将臣 - 博客园](https://www.cnblogs.com/feifa/p/15430524.html)


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

**图片查看**：`eog` 或 `display`


---

**登录 shell 与非登录 shell**

- 登录 shell：物理登录到系统上（如在登录界面输入用户名和密码）或远程登录（如 SSH）
- 非登录 shell：打开新终端窗口或启动新 shell（如输入 `bash` 命令）


---

**查看环境变量**（`PATH`）

```bash
echo $PATH
```

**添加环境变量**

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

>[Linux命令搜索引擎](https://wangchujiang.com/linux-command/)

>[Shell - Isshiki修's Notebook](https://note.isshikih.top/tech_accu/tool/Shell/)

- `man` - 查看命令帮助
- `echo` - 打印字符串
- `pwd` - 显示当前路径
- `cd` - 切换目录
- `ls` - 列出目录内容
- `cat` - 打印文件内容
- `head` & `tail` - 打印文件首尾内容
- `less` - 逐页显示文件内容
- `touch` - 创建文件/修改文件时间属性
- `mkdir` - 创建目录；创建多级目录：`mkdir -p 1/2/3/4`
- `mv` - 移动/重命名
- `cp` - 复制
- `rm` - 删除
- `>`、`>>` - 标准输出流重定向
- `<` - 标准输入流重定向
- `2>`、`2>>` - 标准错误流重定向
- `|` - 管道符
- `rmdir` - 删除空目录
- `tac` - 从最后一行显示文件内容

- `cut` - 剪切命令


注：简单命令直接列出来

```bash
Basic:
      which
      more
      grep
      diff
      tar
      chmod
      chown
      wget
      top
      history
      uname
      hostname
      
Advanced:
      vi
      awk
      seq
      sed
      scp
      zip
      time
      kill
      unzip
      nohup

```



bash 快捷键
```bash
Crtl + A              # 光标移动到命令首
Crtl + E              # 光标移动到命令尾
Alt + B / Ctrl + ←    # 光标向左移动一个单词
Alt + F / Ctrl + →    # 光标向右移动一个单词
Crtl + W              # 删除光标左方的单词
Alt + D               # 删除光标右方的单词
Crtl + R           # 搜索之前输入过的命令
Crtl + _           # 回复之前的状态；撤销操作
Crtl + G           # 退出历史搜索模式
Crtl + ↓           # 跳到最底部
Crtl + L           # 清屏（不算清除内容） 
!!                 # 执行上一条命令
```




```bash
clear # 这个命令并非真正清空，只是把内容全部向上滚，让它们消失在视野中
reset # 这个命令是真正的清空
```




dirname basename

```bash
${file%.*}  # 删掉最后一个.及其右边的字符串
${file%%.*}  # 删掉第一个.及其右边的字符串
${file#.*}  # 删掉第一个.及其右边的字符串
${file##.*}  # 删掉最后一个.及其右边的字符串
```



nl 显示行号
```bash
nl file # 显示行号
nl -n ln file # 行号在荧幕的最左方显示；
nl -n rn file # 行号在自己栏位的最右方显示，且不加 0 ；
nl -n rz file # 行号在自己栏位的最右方显示，且加 0 ；
nl -b a file # 表示不论是否为空行，也同样列出行号
```


```bash
history  # 返回所有的执行命令及其序号
!! 执行最后一次的命令
!n  # 执行第 n 个命令
```


---

#### tar

- 打包命令，不是压缩/解压缩命令（和其他压缩程序如 gzip、bzip2 等一起实现压缩/解压缩功能）
- `x`：从归档中提取文件；`c`：创建归档；`-f`：指定归档文件名称
- `z`：tar.gz 格式；`j`：tar.bz2 格式；`J`：tar.xz 格式；`--zstd`：tar.zst 格式
- 不同压缩格式的文件体积大小：`tar.gz` > `tar.bz2` > `tar.xz`

---

其他参数：

- `-v` - 显示详细信息
- `-t` - 显示归档文件中的内容，而非提取文件
- `-C` - 指定路径
- `--exclude` - 排除指定文件或目录
- `--remove-files` - 删除原始文件，谨慎使用

---

示例：

```bash
tar -xzvf file.tar.gz  # tar.gz 格式
tar --zstd -xvf file.tar.zst  # tar.zst 格式

tar -czvf ${fn}.tar.gz ${fn}  # 压缩

# 指定解压缩路径
tar -xzvf archive.tar.gz -C /path/destination

# 排除指定文件压缩
tar -czvf archive.tar.gz --exclude=exclude_file file1 file2

gzip -d all.gz  # 解压 .gz 文件
gunzip all.gz

unzip all.zip  # 解压 .zip 文件

zcat  # 查看 .gz 文件
bzcat  # 查看 .bz2 文件
```


---

#### ln

给文件/目录设置软/字符链接（**需绝对路径**）

```bash
ln -s path/src path/des
```


---

#### du

查看文件/目录大小

```bash
du -sh file/folder

# 按大小排序
du -sh file/folder | sort -h
```


---

#### dirs

显示目录堆栈，按照最近访问的目录排序（ohmyzsh 插件有关 dirs 的命令是 `d`）。

参数：

- `-l` - 展开 `~`
- `-p` - 每个目录按行显示
- `-v` - 每个目录按行显示并进行编号
- `-c` - 清空目录堆栈


---

#### curl

- 利用 URL 规则在命令行下工作的文件传输工具。

常用参数：

- `-o` 或 `--output` - 将下载的内容保存为指定的文件。
- `-O` 或 `--remote-name` - 将下载的文件保存为远程文件的名称。
- `--progress` - 显示进度条。
- `-L` 或 `--location` - 跟随重定向，如果服务器返回重定向响应，`curl` 将自动请求新的 URL。
- `-C` 或 `--continue-at` - 在下载中断的情况下，继续下载而不是重新开始，通常与 `-o` 参数一起使用。
- `-s` 或 `--silent` - 安静模式，减少输出信息，只显示错误信息。
- `-I` 或 `--head` - 仅获取远程文件的头部信息，而不下载实际内容。
- `-f` 或 `--fail` - 请求发生错误时，使命令返回一个非零的退出状态码，表示请求失败。
- `-S` 或 `--show-error` - 在发生错误时显示错误信息，这些错误信息通常被 `curl` 默认隐藏。

示例：
```bash
curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
```


---

#### wget

从网络下载文件。常用参数：

- `-P` - 指定下载文件的保存目录
- `-O` - 将下载的文件保存为指定的文件名

示例：

```bash
wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O install.sh

# wget -O - 将下载的内容输出到标准输出，而非将其保存为文件
```


---

#### find

- 查找文件。

---

常用参数：

- `-name` - 按照文件名查找
- `-iname` - 按照文件名查找，忽略大小写
- `-type` - 文件类型；`f` - 普通文件，`d` - 目录，`l` - 软链接
- `-maxdepth` - 目录最大深度
- `-mindepth` - 目录最小深度
- `-size` - 文件大小
- `-regex` - 正则表达式匹配
- `-iregex` - 正则表达式匹配，忽略大小写
- `-exec` - 执行指令
- `-ok` - 执行指令，但需确认

与另外两个命令对比：
- `whereis`：查找程序的二进制文件、源代码文件和 man 手册路径
- `locate`：通过数据库定位文件路径（可能需要自己安装，数据库更新慢）

示例：

```bash
# 查找 txt 或 pdf 文件
find . -type f -name "*.txt" -or -name "*.pdf"

# 查找 tar.gz 文件并删除
find . -type f -name "*.tar.gz" -exec rm {} +

# 找到含下划线的 python 脚本，并将其换成连字符输出
fes=$(find . -maxdepth 2 -type f -name "*_*.py"); for f in ${fes}; do echo ${f//_/-}; done
```


---

#### xargs

- 参数转化器，将输入数据转换为命令行参数并执行命令。常用于将管道或标准输入 (stdin) 的数据转换为命令的参数。

```bash
# 将 find 找到的文件删除
find . -name *.tmp | xargs rm -f

# 每行 3 个输出
echo "a b c d" | xargs -n 2 echo
```


---

#### tee

- 从标准输入读取数据并重定向到标准输出和文件（仍会输出到屏幕上；可用于 vasp 和 lammps 的提交命令，见 “ 拾梦的星星 “）

```python
echo linux | tee -a file
```

---

#### paste

`paste`: 可以用来进行多个（csv）文件之间的列合并

```bash
paste -d' ' file1 file2  # 以空格为间隔符来进行列合并文件
```



---

#### sed

sed 命令中引入变量
>[https://blog.csdn.net/qq_35445255/article/details/113750720](https://blog.csdn.net/qq_35445255/article/details/113750720)

```bash
# 双引号情况（常用）
sed -i "2s/node_base/$i/"  /etc/libvirt/qemu/$i.xml

# 单引号情况  先单引号，然后双引号
sed -i '2s/node_base/'"$i"'/' /etc/libvirt/qemu/$i.xml
```


```bash
sed [-nefr] [动作]

-i # 直接修改读取的文件内容，而不是屏幕输出

动作  [n1[,n2]]function
function
a  # 新增
c  # 取代
d  # 删除
i  # 插入
p  # 打印
s  # 取代


# 将INCAR文件中第3行的0.01字串替换为0.02，只会输出替换后的结果，不会更新INCAR文件
sed '3s/0.01/0.02/g' INCAR 

# 会更新INCAR文件（危险！注意备份）
sed -i '3s/0.01/0.02/g' INCAR 

# 指定文件中的行数，输出其内容
sed -n '1,4p' ../ex01_O_atom/OUTCAR

# 在文件最后一行添加内容
sed -i '$aENCUT = 400' INCAR  # 最后一行下方添加 ENCUT = 400

# 每行后面都添加内容
sed -i 'aENCUT = 400' INCAR   # 每一行下方添加 ENCUT = 400

sed 's/^1/Fe/g' test.xyz > out.xyz
# ^1指以1开头的字符


# 删除
# 删除第N~M行
sed -i 'N,Md' filename
# 删除最后一行
sed -i '$d' filename

# 插入行
# 在第二行后加上 ENCUT = 400这一行
sed -i '2a ENCUT = 400' INCAR
# 在第二行前加上 ENCUT = 400这一行
sed -i '2i ENCUT = 400' INCAR
# 插入多行，需要用 \ 
sed -i '2a ENCUT = 400 \
> NSW = 0' INCAR

# 显示第几行
sed -n 4,8p file # 打印file中的4-8行
sed -n 4p file # 打印file中的第4行
```



---

#### grep

```bash
-i 忽略大小写
```


---

#### awk

- 文本处理命令行工具
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
   // code
}

END {
   // code
}
```

---

常用功能 awk 命令实现

```bash
awk '{print NR, $0}' file  # 输出文件内容并显示行号 

awk 'END {print NR}' file  # 统计行数

awk '{ nf = nf + NF } END { print nf }' file  # 返回行列数乘积

awk '$3 == 0' file  # 输出第三列为 0 的行

awk 'NR % 2 == 1' file  # 打印奇数行

awk '{print $NF}' file  # 输出最后一列

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

bash tab 补全忽略大小写
>[linux下，按tab补全时，忽略大小写的配置\_linux命令行终端设置tab补全文件名或路径不区分大小写-CSDN博客](https://blog.csdn.net/lianshaohua/article/details/108710098)


alias 使用参数：以定义函数的方式进行
>[https://forsworns.github.io/zh/blogs/20190919/](https://forsworns.github.io/zh/blogs/20190919/)

```bash
alias ipynb2md="py2md(){jupyter nbconvert --to markdown $1}; py2md"
```




zsh 与 bash 之间的一些区别：

在 zsh 中，数组的索引是从 1 开始的，而 bash 是从 0 开始的
>[https://www.51cto.com/article/740743.html](https://www.51cto.com/article/740743.html)



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





configure、 make、 make install 相关区别
>[https://zhuanlan.zhihu.com/p/77813702](https://zhuanlan.zhihu.com/p/77813702)

linux configure `--prefix` 的作用是：编译的时候用来指定程序存放路径

若不指定 `--prefix`，则可执行文件默认放在 `/usr/local/bin`；库文件默认放在 `/usr/local/lib`；配置文件默认放在 `/usr/local/etc`；其它的资源文件放在 `/usr/local/share`，比较乱

>[https://blog.csdn.net/xiaojin21cen/article/details/90600284](https://blog.csdn.net/xiaojin21cen/article/details/90600284)


---

openmpi 编译
>[https://docs.open-mpi.org/en/v5.0.x/installing-open-mpi/quickstart.html](https://docs.open-mpi.org/en/v5.0.x/installing-open-mpi/quickstart.html)


```python
# 编译
wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.5.tar.bz2

tar xf openmpi-4.1.5.tar.bz2
cd openmpi-4.1.5.tar.bz2
./configure --prefix=$HOME/yangsl/src/openmpi
make -j 4 all && make install

# 添加PATH和LD_LIBRARY_PATH
export PATH=$HOME/yangsl/src/openmpi/bin:$PATH
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$HOME/yangsl/src/openmpi/lib
```



openmpi 编译、安装并配置好后，安装 mpi4py
```python
pip install mpi4py
```

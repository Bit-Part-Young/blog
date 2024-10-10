---
title: Shell 编程
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Shell 编程
description: Shell 编程
tags:
  - Shell
categories:
  - Linux
date: 2023-09-29 20:40:00
abbrlink: 493204
password:
---

# Shell 编程

## Shell 介绍

Shell 原意是 “外壳”，跟 kernel（内核）相对应，比喻内核外面的一层，即用户跟内核交互的对话界面。

首先，Shell 是一个程序，提供一个与用户对话的环境。这个环境只有一个命令提示符，让用户从键盘输入命令，所以又称为命令行环境（command line interface，CLI）。Shell 接收到用户输入的命令，将命令送入操作系统执行，并将结果返回给用户。

其次，Shell 是一个命令解释器，解释用户输入的命令。它支持变量、条件判断、循环操作等语法，所以用户可以用 Shell 命令写出各种小程序，又称为脚本（script）。这些脚本都通过 Shell 的解释执行，而不通过编译。

终端模拟器：terminal emulator，一个模拟命令行窗口的程序，让用户在一个窗口中使用命令行环境，并且提供各种附加功能，比如调整颜色、字体大小、行距等。

不同 Linux 发行版（准确地说是不同的桌面环境）带有的终端程序是不一样的，比如 KDE 桌面环境的终端程序是 konsole，Gnome 桌面环境的终端程序是 gnome-terminal，用户也可以安装第三方的终端程序。

主要的 Shell 有 sh、bash、csh、tcsh、ksh、zsh、fish；Bash 是目前最常用的 Shell。

```bash
# 查看 Shell
cat /etc/shells  # 查看当前的 Linux 系统安装的所有 Shell
echo $SHELL      # 当前设备的默认 Shell
ps               # 一般来说，ps 命令结果的倒数第二行是当前 Shell

# 切换默认 Shell 
chsh -s /bin/zsh
sudo chsh -s /usr/bin/zsh root

bash             # 进入 Shell
exit             # 退出 Shell，或 Crtl + D

# Shell 命令格式
# command 具体的命令或可执行文件
# arg1 ... argN 传递给命令的参数，可选
command [ arg1 ... [ argN ]]
# 参数的短长形式作用完全一样，前者便于输入，后者便于理解
-v                 # 短形式
--verbose          # 长形式
```

---

Shell 终端快捷键

```bash
TAB                   # 命令补全
Ctrl + C              # 中止命令
Ctrl + D              # 键盘输入结束，可用于退出 Shell 窗口
Crtl + A              # 光标移动到命令首
Crtl + E              # 光标移动到命令尾
Alt + B               # 光标向左移动一个单词
Ctrl + ←              # 同上
Alt + F               # 光标向右移动一个单词
Ctrl + →              # 同上
Crtl + W              # 删除光标左方的单词
Alt + D               # 删除光标右方的单词
Crtl + R              # 搜索之前输入过的命令
Crtl + G              # 退出历史搜索模式
Crtl + ↓              # 跳转至底部
Crtl + L              # 将底部内容移至最上方
Ctrl + Z              # 将当前正在运行的前台进程暂停（挂起）并放到后台

fg %n                 # n 为 job number；将挂起的进程回调到前台继续运行
bg %n                 # 将挂起的进程在后台继续运行（不占用终端的输入和输出）
```

注：Shell 脚本中，缩进的标准并没有一个严格的规定，常见的缩进宽度是 2 个或 4 个空格（个人现采用 2 个空格的缩进宽度）


---

### 参考资料

- [Bash 脚本教程 - 网道](https://wangdoc.com/bash/)
- 速查表：[Bash 备忘清单 & bash cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/bash.html)
- [shell脚本基础 - cherry](https://jaav.com.cn/posts/1b2.html)
- Shell 脚本案例：[GitHub - jacobproject/Shell\_Scripts: Shell Scripts examples](https://github.com/jacobproject/Shell_Scripts)
- [GitHub - bobbyiliev/introduction-to-bash-scripting: Free Introduction to Bash Scripting eBook](https://github.com/bobbyiliev/introduction-to-bash-scripting)
- Shell 代码优化：[Advanced Shell Scripting Techniques](https://omid.dev/2024/06/19/advanced-shell-scripting-techniques-automating-complex-tasks-with-bash/)

Bash 命令报错时，仍会继续执行后面的代码



---

## 工具

- 代码格式化：shfmt

```bash
# Go Module 镜像/代理
export GOPROXY=https://goproxy.cn,direct

# 安装
go install mvdan.cc/sh/v3/cmd/shfmt@latest

shfmt script.sh     # 打印格式化后的内容，不修改文件内容
shfmt -w script.sh  # 将格式化后的内容写入文件

# 参数
-i n                # 指定缩进空格
-mn                 # 启用最小化模式，通常删除不必要的空格和换行符
-ln                 # 指定方言 bash/posix/mksh/bats
```

- 代码检查：ShellCheck；Web 版本：[ShellCheck – shell script analysis tool](https://www.shellcheck.net/)

```bash
shellcheck [option] script.sh

# 参数
-s   # 指定方言 sh, bash, dash, ksh, busybox
-f   # 指定输出格式 checkstyle, diff, gcc, json, json1, quiet, tty
```

- VSCode 中的 shellcheck、shell-format 插件不是很好用（建议直接使用其命令行工具）

- Bash LSP：[GitHub - bash-lsp/bash-language-server](https://github.com/bash-lsp/bash-language-server)（依赖 ShellCheck 和 shfmt，可集成在 Vim 或 Neovim 中）

```bash
npm i -g bash-language-server
```

- 命令行解析：
    - `shift` 命令和 `while` 循环手动解析参数
    - [getoptions](https://github.com/ko1nksm/getoptions)、[argparse-bash](https://github.com/nhoffman/argparse-bash)（这两个感觉都一般）



---

## 语法

### 运行脚本

- 脚本第一行以 `#!` 字符（称为 Shebang）开头，指定解释器；`#!/bin/bash` 可写为 `#!/usr/bin/env bash`

```bash
#!/bin/bash

...
```

- 运行脚本

```bash
# 方式 1
bash script.sh      # 或 sh script.sh

# 方式 2 赋予可执行权限
chmod +x script.sh  # Linux 文件颜色变绿；macOS，变红
./script.sh
```


---

### 注释

```bash
# 单行注释

: '  多行注释
comment 1
comment 2
'
```


---

### 打印输出

-  `echo` 自动添加换行符， `printf` 不会

```bash
echo     # 输出一行空行

# 参数
-n       # 不自动换行
-e       # 转义字符
```


```bash
# 输出固定位数
printf "%05d\n" 123  # 输出 5 位数，00123
```


----

### 变量

- 定义变量：变量名和等号之间不能有空格
- 使用变量：在变量名前面加美元符号 `$`；可在变量名外面添加花括号，帮助解释器识别变量边界
- 删除变量：`unset`
- 输出变量：`export`

```bash
var="letter"      # 定义变量
echo $var         # 使用变量；或 echo ${var}
unset var         # 删除变量
export var=value  # 输出变量
```

- 特殊变量

```bash
$0   # 当前 Shell 的名称（在命令行直接执行时）或脚本名（在脚本中执行时）
$n   # n 为数字，第 n 个参数
$#   # 脚本的参数数量
$?   # 上一个命令的退出码（成功返回 0，失败返回非零数值）
$_   # 上一个命令的最后一个参数
$*   # 脚本的参数值；将所有参数视为一个整体
$@   # 脚本的参数值；所有参数是独立的
$$   # 当前 Shell 的进程 ID
$!   # 最近一个后台执行的异步命令的进程 ID
$-   # 当前 Shell 的启动参数


# 示例
mkdir directory && cd $_

# bash test.sh {2..4}
#!/bin/bash

echo "script name: $0"
echo "arg length: $#"
echo "arg1: $1"
echo "arg2: $2"
echo "arg3: $3"
for arg in "$*"; do
  echo '$* meaning:' "$arg"
done
for arg in "$@"; do
  echo '$@ meaning:' "$arg"
done
```

- `shift` 命令可以改变脚本参数，每次执行都会移除脚本当前的第一个参数，使得后面的参数向前一位

```bash
shift n         # 移除 n 个参数
```

- 环境变量

```bash
env            # 显示所有环境变量；或 printenv

printenv PATH  # 查看单个环境变量的值  
echo $PATH

export PATH=$PATH:$HOME/bin  # 方式 1
export PATH=$HOME/bin:$PATH  # 方式 2

# 常见环境变量
HOME           # 用户主目录
HOST           # 当前主机名称
PATH           # 由冒号分开的目录列表，当输入可执行程序名后，会搜索这个目录列表
RANDOM         # 生成 0~32767 之间的随机数
[RANDOM%num]   # 生成 0~num 之间的随机数
PWD            # 当前工作目录
PS1            # 命令提示符
DISPLAY        # 图形环境的显示器名字，通常是 :0，表示 X Server 的第一个显示器
IFS            # 内部字段分隔符，Internal Field Separator
```

---

### 引号

- 单引号不展开任何内容，全部原样输出
- 双引号会展开变量和命令，特殊字符保留（美元符号、反引号和反斜杠，星号会变成普通字符）；保存原始命令的输出格式

```bash
echo $'it\'s'    # 单引号中使用单引号，在最前面加 $
echo "it's"      # 在双引号之中使用单引号

echo $(cal)      # 单行输出
echo "$(cal)"    # 原始格式输出
```


---

### 字符串操作

```bash
# 获取字符串长度
echo ${#str}
echo ${#str[0]}

## 字符串切片
# 语法；offset 从 0 开始；该语法不能直接操作字符串
${str:offset:length}
# 示例
echo ${str:1:4}
echo ${str:1}      # 省略 length，表示到字符串结尾
echo ${str: -4}    # 从倒数第 4 个字符开始；负号前须有空格
echo ${str: -4:2}

## 字符串大小写转换
# 将字符串转换为小写
echo "Hello World" | tr '[:upper:]' '[:lower:]'
echo "HELLO WORLD" | awk '{ print tolower($0) }'
# 大写
echo "hello world" | tr '[:lower:]' '[:upper:]'
echo "hello world" | awk '{ print toupper($0) }'

# Bash 4.0 及更高版本中有效
${str,,}   # 小写
${str,}    # 首字母小写
${str^^}   # 大写
${str^}    # 首字母大写
```

---

- 大括号 `{}` 处理字符串：
    - 主要利用 Bash 的参数展开（parameter expansion）功能来实现
    - 参考：[Bash笔记](https://zhuanlan.zhihu.com/p/524196855)

```bash
# 基于模式匹配进行字符串剪裁
var="sample.bk.tar.gz"
# 常用于删除字符串前缀
${var#*.}       # 删除字符串开头部分，最短匹配；输出 "bk.tar.gz"
${var##*.}      # 删除字符串开头部分，最长匹配；输出 "gz"
# 常用于删除字符串后缀
${var%.*}       # 删除字符串末尾部分，最短匹配；输出 "sample.bk.tar"
${var%%.*}      # 删除字符串末尾部分，最长匹配；输出 "sample"

# 按字符位置截取字符串
${var:N:M}      # 从第 N 个位置开始，截取 M 个字符

# 字符串替换
${var/a/b}      # 把变量中的第一个 a 替换成 b
${var//a/b}     # 把变量中的所有 a 替换成 b

# 生成字符串列表、序列
echo beg{i,a,u}n  # 输出 begin began begun
echo {0..5}       # 等价于 seq 0 5
echo {00..8..2}   # 00 02 04 06 08

#复制文件夹中的多个文件到当前路径；可结合通配符使用
cp /path/{file1,file2,file3,file4} .
```


---

### 算术运算

- 简单数学运算：原生 bash 不支持，可通过 `expr` 命令实现

```bash
# 表达式和运算符之间要有空格
val=`expr 2 + 2`
 ​  
# 乘法运算：须加反斜杠
val=`expr 2 \* 3`
```

---

- 算术扩展：`(())`
    - 只能计算整数；会自动忽略内部的空格；支持常用运算符；指出逻辑运算符；支持赋值运算
    - `++` 和 `--` 这两个运算符有前缀和后缀的区别。作为前缀是先运算后返回值，作为后缀是先返回值后运算
    - 在 `$((...))` 里面使用字符串，Bash 会认为那是一个变量名

```bash
# 运算符
a=5; b=10; c=$(( a * b )); echo $c

# 逻辑运算符
if (( a < b )); then echo "$a is less than $b"; fi

# 赋值运算
echo $(( a=1 ))
```

---

- 浮点数运算
    - bash 不支持浮点运算，需借助 bc（basic calculator）, awk 处理
    - [linux shell 实现 四则运算（整数及浮点） 简单方法 - 程默 - 博客园](https://www.cnblogs.com/chengmo/archive/2010/09/30/1839556.html)

```bash
echo "5.01-4*2.0" | bc

awk 'BEGIN { print 7.01*5-4.01 }'

# scale 指定保留小数位数
echo "scale=4; 0.05*0.1" | bc

# 除法，只取整数部分
echo "10/3" | bc
echo "scale=2; 10/3" | bc | cut -d "." -f1
```

---

- `let` 命令：用于将算术运算的结果，赋予一个变量

```bash
# 整型变量自增
a=1; echo $a
# 方式1
let a++; echo $a
# 方式2
let a+=1; echo $a
```


---

### 数组

```bash
# 元素用空格分割开
array=(value0 value1)  # 写法 1

array=(                # 写法 2
  value0
  value1
)

# 添加元素
array+=(value2)

# 删除元素
unset array[1]

# 获取数组元素
echo ${array[*]}   # 所有元素；* 或 @
echo ${array}      # 第一个元素
echo ${array[0]}   # 第一个元素

# 获取数组长度
echo ${#array[*]}  # * 或 @
echo ${#array[0]}  # 第一个元素的长度

# 提取数组序号
${!array[*]}       # * 或 @

# 切片
${array[@]:position:length}

# 数组合并
array1=(xxx); array2=(xxx)
array_merge=(${array1[*]} ${array2[*]})

```

---

关联数组：使用字符串而不是整数作为数组索引；可等效为字典

```bash
declare -A sounds      # 创建

sounds[dog]="bark"     # 添加键值对
sounds[cow]="moo"

echo "${sounds[dog]}"  # 根据键访问值

# 遍历
for key in "${!sounds[@]}"; do 
    echo "$key: ${sounds[$key]}"
done
```


---

### 条件控制

#### if 条件语句

```bash
# 语法
# then 可以另起一行，删除分号
if condtion1; then
    commands
elif condition2; then
    commands
fi

# 写成一行
if condition; then commands; fi
```

---

`if` 结构的判断条件写法：`[[]]` 是扩展条件判断，相比 `[]`，支持更多的操作符（如正则表达式匹配）

```bash
test expression      # 写法一
[ expression ]       # 写法二
[[ expression ]]     # 写法三


# 字符串条件
[[ -z STR ]]         # 空字符串
[[ -n STR ]]         # 非空字符串 
[[ STR1 == STR2 ]]   # 相等 
[[ STR1 = STR2 ]]    # 相等（同上）
[[ STR1 =~ STR2 ]]   # 正则表达式

# 文件条件
[[ -f FILE ]]        # 文件
[[ -d FILE ]]        # 目录
[[ -e FILE ]]        # 文件/目录是否存在

# 整数条件
[[ NUM1 -eq NUM2 ]]  # 等于
[[ NUM1 -lt NUM2 ]]  # 小于
[[ NUM1 -gt NUM2 ]]  # 大于
```


---

#### case 分支语句

`case` 结构用于多值判断，可用到命令行解析中

```bash
# 语法
# ;; 可以另起一行
#  ) 前后面的内容可以在一行
# *)：匹配任意输入，通常作为 case 结构的最后一个模式
case expression in
  pattern1)
    commands ;;
  pattern2)
    commands ;;
  ...
esac
```


---

### 循环

#### for 循环

```bash
# 语法
# do 可以另起一行，删除分号
for variable in list; do
    command
done


# 示例
for i in 1 2 3 4 5; do 
    echo $i
done

for i in {1..5}; do 
    echo $i
done

for i in {1..5..2}; do 
    echo $i
done

for i in $(seq 1 2 5); do 
    echo $i
done

# 小数序列
for i in $(seq 1 0.2 2); do 
    echo $i
done

# C 语言风格
for(( i=1; i<=20; i++ )); do
    echo $i
done

# 99 乘法表
for i in {1..9}; do
    for j in $(seq $i); do 
        echo -n -e "$j*$i=$[j*i]\t"
    done
    echo
done
```


---

#### while 循环

```bash
# 语法
while condition; do
  command
done

# 读取文件内容的每一行
cat file.txt | while read line; do 
    echo $line
done
```


---

### 函数

- Bash 函数体内直接声明的变量，属于全局变量，整个脚本都可以读取
- 函数里面可以用 `local` 命令声明局部变量

```bash
# 函数定义语法
# 第一种
fn() {
    commands
}

# 第二种
function fn() {
    commands
}

fn  # 函数调用
```


---

### set 命令

`set` 命令：用于执行脚本时进行调试和错误处理

- `set -u`：执行脚本时，若遇到不存在的变量，Bash 默认忽略它；在脚本头部加上 `set -u`，遇到不存在的变量就会报错，并停止执行

- `set -x`：在运行结果之前，先输出执行的那一行命令

- `set -e`：若脚本中有运行失败的命令，Bash 默认会继续执行后面的命令；在脚本头部加上 `set -e`，使得脚本只要发生错误，就终止执行；`set +e` 表示关闭 `-e` 选项；不适用于管道命令（`set -o pipefail` 可解决该问题）

- `set -E`：纠正 `set -e` 导致的函数内的错误不会被 `trap` 命令捕获的行为

- `set -n`：不运行命令，只检查语法是否正确

- `set -f`：表示不对通配符进行文件名扩展

- `set -o noclobber`：防止使用重定向运算符 `>` 覆盖已经存在的文件

```bash
set      # 显示所有的环境变量和 Shell 函数

# 放在一起使用
set -Eeuxo pipefail  # 写法一

set -Eeux            # 写法二
set -o pipefail
```


---

### 重定向

```bash
command > file        # 标准输出重定向到文件
command >> file       # 标准输出追加到文件
command 2> file       # 标准错误重定向到文件 
command 2>&1          # 标准错误重定向到标准输出 
command 2> /dev/null  # 标准错误重定向到空
command &> /dev/null  # 标准输出和标准错误同时重定向到空
command < file        # 将文件内容作为标准输入
```

---

- Here 文档、字符串：
    - Here 文档：一种输入多行字符串的方法；本质是重定向
    - Here 文档内部会发生变量替换，同时支持反斜杠转义，但是不支持通配符扩展，双引号和单引号也失去语法作用，变成了普通字符
    - Here 字符串：将字符串通过标准输入，传递给命令

```bash
# 语法 token 一般为 EOF
<< token
text
token

# 语法
<<< string

cat <<< 'hi there'  # 等同于 echo 'hi there' | cat
```



---

## 其他

- 子命令扩展： `$()` 和\`\`；将命令的输出作为返回值

```bash
echo $(date)
echo `date`
```

---

- 重复输出字符：[How to repeat a character 'n' times in Bash - nixCraft](https://www.cyberciti.biz/faq/repeat-a-character-in-bash-script-under-linux-unix/)

```bash
# 重复输出等号
printf '==%.0s' {1..20}; printf '\n'

# 定义函数
repeat(){
    for i in {1..20}; do echo -n "$1"; done
}

repeat '-'; echo
repeat '='; echo
```

---

- 检查命令是否存在

```bash
COMMANDS=("git" "vi")

for COMMAND in $COMMANDS; do
  # if [ -x "$(command -v $COMMAND)" ]; then
  if ! command -v "$COMMAND" &> /dev/null; then
    echo "Please install $COMMAND";
  fi
done
```

- 输入

```bash
# 语法
read [-options] [variable...]

# 示例
echo "What is your name?"
read NAME  # 输入
echo "Hello, $NAME"
```

---

- 操作历史
    - 退出当前 Shell 的时候，Bash 会将用户在当前 Shell 的操作历史写入 `~/.bash_history` 文件
    - `Ctrl + R` 快捷键，可以搜索操作历史，选择以前执行过的命令

```bash
echo $HISTFILE

history         # 输出操作历史
history-c       # 清除操作历史

## 环境变量
# 设置 history 输出结果格式
# %F 相当于 %Y - %m - %d（年-月-日）
# %T 相当于 %H : %M : %S（时:分:秒）
export HISTTIMEFORMAT='%F %T  '
# 设置保存历史操作的数量
export HISTSIZE=10000
# 设置哪些命令不写入操作历史
export HISTIGNORE='pwd:ls:exit'


!n             # n 为行号，执行 .bash_history 文件中的第 n 条命令
!-n            # n 为数字，执行倒数第 n 条命令
!!             # 执行上一条命令，等同于 !-1
! + 搜索词      # 快速执行匹配的命令；只会匹配命令，不会匹配参数
!:p            # 输出上一条命令，而不是执行它
!$             # 上一个命令的最后一个参数，等同于 $_
!*             # 上一个命令的所有参数
!:n            # 匹配上一个命令的指定位置的参数
```

---

- 配置项参数终止符 `--`：`-` 和 `--` 开头的参数，会被 Bash 当作配置项解释；`--` 的作用是告诉 Bash，在它后面的参数开头的 `-` 和 `--` 不是配置项，只能当作实体参数解释

```bash
cat -- -f
cat -- --file
```

---

- 防止覆盖文件

```bash
set -o noclobber     # 防止覆盖已存在的文件；拒绝覆写操作并显示一个错误

echo "xxx" >| file   # 强制覆盖

set +o noclobber     # 临时关闭
```

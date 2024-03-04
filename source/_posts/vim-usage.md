---
title: Vim 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Vim 使用
description: Vim 使用
tags:
  - Vim
categories:
  - Linux
date: 2023-11-27 20:44:00
abbrlink: 
password:
---

# Vim 使用

## 介绍

>[GitHub - wsdjeg/vim-galore-zh\_cn: Vim 从入门到精通](https://github.com/wsdjeg/vim-galore-zh_cn)

>[GitHub - yyq123/learn-vim](https://github.com/yyq123/learn-vim)



---

## 快捷键

- [vim.txt - awesome-cheatsheets](https://github.com/skywind3000/awesome-cheatsheets/blob/master/editors/vim.txt)、[Vim Cheat Sheet](https://vim.rtorr.com/lang/zh_cn)


vim 中 j 和 gj 快捷键之间的区别：`j` 和 `gj` 都用于向下移动光标，但 `gj` 在处理折行文本时表现不同（前者不考虑，后者考虑），更视觉友好。


- 分命令模式（Command mode）**，**输入模式（Insert mode）和底线命令模式（Last line mode）三种模式
- 刚启动 vi/vim，便进入了命令模式；按 `i` 或 `a ` 或 `o` 进入输入模式，输入字符；`:` 切换到底线命令模式，以在最底一行输入命令；`x` 删除当前光标所在处的字符；`:wq` 保存文件并退出
- 输入模式下，按 `esc` 键退出输入模式，切换到命令模式
- 底线命令模式下：`q` 退出程序；`w` 保存文件


 命令模式下常用快捷键

- 光标移动
```shell
##-----光标移动-----##
h    # 光标向左移动一个字符
j    # 光标向下移动一个字符
k    # 光标向上移动一个字符
l    # 光标向右移动一个字符
0 / [Home]  # 数字0；移动到这一行行首(常用)
$ / [End]   # 移动到这一行行尾(常用)
gg   # 转到第一行(常用)
G    # 转到最后一行(常用)
nG   # n为数字；转到第n行
n<Enter> # n为数字；<Enter>表示<Enter>键；光标向下移动n行
H    # 光标移动到这个屏幕的最上方那一行的第一个字符
M    # 光标移动到这个屏幕的中央那一行的第一个字符
L    # 光标移动到这个屏幕的最下方那一行的第一个字符

##-----光标词间移动-----##
w       # 移动到下一个单词头部
b       # 移动到前一个单词头部
e       # 移动到下一个单词尾部
ge      # 移动到前一个单词尾部
```

- 搜索替换
```shell
/word    # 向光标之下寻找一个名称为 word 的字符串；按下<Enter>键后会显示所有的名称为 word 的字符串
?word    # 向光标之上寻找一个名称为 word 的字符串
n        # 英文按键；代表重复前一个搜寻的动作；向下搜寻
N        # 英文按键；代表重复前一个搜寻的动作；向上搜寻

:n1,n2s/word1/word2/g   # n1 与 n2 为数字；在第 n1 与 n2 行之间寻找 word1 这个字符串，并将该字符串取代为 word2；:1,6s/if/fi/g

:1,$s/word1/word2/g   # 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2
:%s/word1/word2/g     # 同上
:%s/word1/word2/gc    # 确认是否替代
```

- 复制、粘贴和删除
```shell
##-----复制-----##
yy     # 复制光标所在的那一行(常用)
nyy    # n为数字；复制光标所在的向下n行
y1G    # 复制光标所在行到第一行的所有内容
yG     # 复制光标所在行到最后一行的所有内容
y$     # 复制光标所在处，到该行的最后一个字符(常用)
y0     # 数字0；复制光标所在处，到该行的最前面一个字符(常用)
byw    # 复制光标所在的一个单词
nyl    # n为数字，复制光标向后的n个字符

##-----粘贴-----##
p      # 将已复制的数据在光标下一行贴上(常用)
P      # 大写；复制在上一行贴上
J      # 将光标所在行与下一行的内容结合成同一行

##-----删除-----##
dd     # 删除光标所在的那一整行(常用) 
ndd    # 删除光标所在的向下n行
dG
d1G
d$ / D   # 删除光标所在处到该行最后字符(常用)
d0
nd + ↑ # n为数字，删除光标所在行及其向上的n行
nd + ↓ # 删除光标所在行及其向下的n行（同ndd）
x      # 删除光标处的字符
X      # 删除光标的前一个字符
bdw    # b 让光标回退到单词开头的位置；dw 从光标当前的位置开始删除，直到删到单词最后
daw    # 直接删除光标所在的一个单词

##-----撤回/重复-----##
u      # 复原前一个动作(常用)
Ctrl + r      # 重做上一个动作(常用)
.      # 重复前一个动作(常用)
```

- 同时显示多个文件的分屏操作及切换操作
```shell
# 分屏
:split    # 上下分屏
:vsplit   # 左右分屏

# 文件转换
:bn       # 下一个文件
:bp       # 上一个文件

# 屏幕转换
Ctrl+ww   # 依次切换屏幕
Ctrl+w+h/j/k/l   # 切换上下左右窗口（按顺序分别为左/下/上/右）
```

- 大小写转换
```shell
# 字母大小写转换
shift + ~     # 光标所在位置字符转大小写

# 单词大小写转换
guw  gue      # 光标所在位置的单词转小写
gUw  gUe      # 光标所在位置的单词转大写
gu3w  gu3e    # 光标后面的3个单词转小写
gU3w  gU3e    # 光标后面的3个单词转大写

# 行大小写转换
guu           # 光标所在的行转小写
gUU           # 光标所在的行转大写
```

- 进入输入模式快捷键
```shell
i      # 从目前光标所在处输入(常用)
a      # 从目前光标所在的下一个字符处开始输入(常用)
o      # 在目前光标所在的下一行处输入新的一行(常用)
```

- 底线命令模式快捷键
```shell
:set nu    # 显示行号(常用)
:set nonu  # 显示行号

:q    # 文件没有任何改动，离开vi（常用）
:q!   # 文件有任何改动，但不想储存，强制退出vi
:wq   # 储存后离开
ZZ  # 大写；文件若无改动，不储存退出；若有改动，储存后离开
:w [filename]  # 将编辑的数据储存成另一个文件（类似另存新档）
```

- 可视化模式
```shell
v           # 字符可视化模式；以字符为单位
V           # 行可视化模式；行
ctrl + v    # 块可视化模式；可以选择一个矩形内的文本
```



---

## vimrc

vimrc 文件相关配置注释
>[https://github.com/yangyangwithgnu/use_vim_as_ide](https://github.com/yangyangwithgnu/use_vim_as_ide)

star 数很多的 vimrc 配置
>[GitHub - amix/vimrc: The ultimate Vim configuration (vimrc)](https://github.com/amix/vimrc)


---

`<silent>` - 用于控制在命令行中是否显示执行的命令
`<bar>` - 管道符


buffer 相关

|       命令       |                        说明                         |
|:----------------:|:---------------------------------------------------:|
|    `:e file`     |           打开文件并创建一个新的 buffer。            |
|      `:ls`       | 查看当前打开的所有 buffer，以及它们的状态和 buffer ID |
|     `:bnext`     |                 切换到下一个 buffer                 |
|     `:bprev`     |                 切换到上一个 buffer                 |
|     `:hide`      |      隐藏 buffer，但不会关闭文件，只是不再显示       |
| `:bdelete` / `:bd` |                     关闭 buffer                      |

---

- 个人 `~/.vimrc` 文件设置：[.vimrc · Falling Slowly/dotfiles](https://gitee.com/yangsl306/dotfiles/blob/main/.vimrc)

- 相对行号、高亮
- 缩进设置
- 打开文件返回到上次的编辑位置
- 插件安装与设置
- buffer 设置
- 删除行尾的空白符
- 块模式选中文本搜索
- 块模式选中文本添加括号


---

### Vim 插件

- vim 插件推荐：[Great VIM Plugins in 2023 | hacking C++](https://hackingcpp.com/dev/vim_plugins.html)
- [markdown-preview.nvim:](https://github.com/iamcco/markdown-preview.nvim)：预览 md 文件插件

- [plug](https://github.com/junegunn/vim-plug)：插件管理器；相关命令：
    - `:PlugInstall` - 安装插件；`:PlugClean` - 卸载插件；`:PlugUpdate` - 更新插件

- [airline](https://github.com/vim-airline/vim-airline.git)：状态栏美化；[vim-airline-themes](https://github.com/vim-airline/vim-airline-themes.git)
- [surround](https://github.com/tpope/vim-surround.git)
- [nerdtree](https://github.com/preservim/nerdtree.git)：目录树；
- [solarized8](https://github.com/lifepillar/vim-solarized8.git)：theme 美化
- [easymotion](https://github.com/easymotion/vim-easymotion.git)：快速移动
- [fzf.](https://github.com/junegunn/fzf.vim.git)：模糊搜索
- [ale](https://github.com/dense-analysis/ale.git)：异步代码检查和修复
- [coc.nvim](https://github.com/neoclide/coc.nvim)：提供代码自动补全、语法检查和语言服务器支持
- [ultisnips](https://github.com/SirVer/ultisnips)：代码片段（snippets）
- [lammps.vim](https://github.com/tommason14/lammps.vim.git)：LAMMPS 输入参数高亮
- [vasp.vim](https://github.com/Lattay/vasp.vim.git)：VASP 输入文件参数高亮



---

## neovim

### 安装

>直接安装 release，超算平台和服务器均正常（无需编译 source，pi 上编译失败）


```bash
wget https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz

tar -xvzf nvim-linux64.tar.gz

cd nvim-linux64/bin

ln -s ~/src/nvim-linux64/bin/nvim ~/bin
```


编译
```bash
make CMAKE_EXTRA_FLAGS="-DCMAKE_INSTALL_PREFIX=$HOME/src/neovim"

make install
```


---

### 设置

>[GitHub - bryant-video/neovim-tutorial](https://github.com/bryant-video/neovim-tutorial)

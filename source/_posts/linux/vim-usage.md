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
abbrlink: 749411
password:
---

# Vim 使用

## 介绍

文本编辑器。


---

### 参考资料

- Vim 相关汇总：[GitHub - akrawchyk/awesome-vim: The Vim plugin shortlist](https://github.com/akrawchyk/awesome-vim)
- [GitHub - wsdjeg/vim-galore-zh\_cn: Vim 从入门到精通](https://github.com/wsdjeg/vim-galore-zh_cn)
- [GitHub - yyq123/learn-vim](https://github.com/yyq123/learn-vim)
- [GitHub - yangyangwithgnu/use\_vim\_as\_ide: use vim as IDE](https://github.com/yangyangwithgnu/use_vim_as_ide)
- [Eric Wong / Learn Vim Zh Cn · GitLab](https://gitlab.com/wsdjeg/Learn-Vim_zh_cn)
- [GitHub - alexzhang1030/full-keyboard: 让你在日常开发中全键盘操作](https://github.com/alexzhang1030/full-keyboard)


---

## 使用

```bash
vimtutor    # 查看 Vim 教程
```

---

### 快捷键

- 快捷键 Cheat Sheet：
	- [Vim Cheat Sheet - 中文](https://vim.rtorr.com/lang/zh_cn)
	- [vim.txt - awesome-cheatsheets](https://github.com/skywind3000/awesome-cheatsheets/blob/master/editors/vim.txt)
	- [A Great Vim Cheat Sheet](https://vimsheet.com/)


vim 中 j 和 gj 快捷键之间的区别：`j` 和 `gj` 都用于向下移动光标，但 `gj` 在处理折行文本时表现不同（前者不考虑，后者考虑），更视觉友好。


- 三种模式：命令模式（Command mode）、输入模式（Insert mode）、底线命令模式（Last line mode）
- 启动时进入的是命令模式； `i/a/o` 进入输入模式；`esc` 键退出输入模式，切换到命令模式；`:` 切换到底线命令模式，以在最底行输入命令

---

进入输入模式快捷键

```bash
i          # 从光标所在处输入
a          # 从光标所在的下一个字符处输入
o          # 在光标所在的下一行处输入新的一行
```

---

底线命令模式快捷键

```bash
:q         # 退出（需文件没有改动）
:q!        # 强制退出（不保存文件改动)
:wq        # 保存后退出 
ZZ         # :q :wq 两个命令的结合
:w file    # 保存成另一个文件

:set nu    # 显示行号
:set nonu  # 显示行号

:term      # 在 vim 中打开终端
```

---

可视化模式

```bash
v          # 字符可视化模式
V          # 行可视化模式
Ctrl + v   # 块可视化模式
```

---

命令模式快捷键

```shell
# 光标移动
j/k/h/l     # 向下/上/左/右移动一个字符
0 / [Home]  # 移动到该行行首；数字 0
$ / [End]   # 移动到该行行尾
gg          # 移动到第一行
G           # 移动到最后一行
nG          # 移动到第 n 行；n 为数字
n<Enter>    # 向下移动 n 行；<Enter> 为 Enter 键
H           # 移动到屏幕的最上方
M           # 移动到屏幕的中央
L           # 移动到屏幕的最下方
e           # 移动到下一个单词尾部
ge          # 移动到前一个单词尾部
w           # 移动到下一个单词头部
b           # 移动到前一个单词头部

# 搜索
/word       # 向光标之下寻找 word 字符串
?word       # 向光标之上寻找 word 字符串
n           # 向下搜寻
N           # 向上搜寻

# 替换
:s/word1/word2/g   # 在该行将 word1 替换为 word2；gc 替换前询问
:n1,n2s...         # n1-n2 行
:1,$s...           # 第一行至最后一行
:%s...             # 同上

# 复制
yy          # 复制光标所在行
nyy         # n 为数字；复制光标所在向下 n 行
yG          # 复制光标所在行到最后一行
y1G         # 复制光标所在行到第一行
y$          # 复制光标所在处至该行行尾
y0          # 数字 0；复制光标所在处至该行行首
byw         # 复制光标所在的一个单词
nyl         # 复制光标向后的 n 个字符

# 粘贴
p            # 粘贴至光标下一行
P            # 粘贴至光标上一行
J            # 将光标所在行与下一行的内容结合成同一行

# 删除
dd           # 删除光标所在行
ndd          # 删除光标所在的向下 n 行
dG           # 删除光标所在行到最后一行
d1G          # 删除光标所在处至该行行尾
d$ / D       # 删除光标所在至行尾
d0           # 删除光标所在至行首
nd + ↑       # 删除光标所在行向上 n 行
nd + ↓       # 删除光标所在行向下 n 行（同 ndd）
x            # 删除光标处字符
X            # 删除光标处前一个字符
bdw          # 删除光标所在的一个单词（同 daw）

# 撤回/重复
u           # 恢复前一个动作
Ctrl + r    # 重做上一个动作
.           # 重复前一个动作（普通模式，替换操作无法重复）
&           # 重复前一个替换操作

# 分屏
:split      # 上下分屏
:vsplit     # 左右分屏
Ctrl + ww   # 切换屏幕
Ctrl +w + h/j/k/l  # 切换左/下/右/上窗口

# 大小写转换
shift + ~    # 光标所在位置字符转大小写
guw / gue    # 光标所在位置的单词转小写
gUw / gUe    # 光标所在位置的单词转大写
gu3w / gu3e  # 光标后面的3个单词转小写
gU3w / gU3e  # 光标后面的3个单词转大写
guu          # 光标所在行转小写
gUU          # 光标所在行转大写
```

---

其他快捷键

```bash
:5m3        # 将第 5 行剪切并粘贴到第 3 行下方
> + Enter   # 该行首右移一个 Tab 距离
>4 + Enter  # 4 行行首右移一个 Tab 距离


```


---

### 配置

- `.vimrc` 文件相关配置注释：[https://github.com/yangyangwithgnu/use_vim_as_ide](https://github.com/yangyangwithgnu/use_vim_as_ide)

- GitHub star 数很多的 `.vimrc` 配置：[GitHub - amix/vimrc: The ultimate Vim configuration (vimrc)](https://github.com/amix/vimrc)

- 交大同学 Neovim 配置：[GitHub - KinnariyaMamaTanha/KinanVim: My personal configuration for neovim on Ubuntu22.04(WSL2)](https://github.com/KinnariyaMamaTanha/KinanVim)

- 交大同学 Vim 配置：[GitHub - KinnariyaMamaTanha/KinaVim: My personal configuration of vim.](https://github.com/KinnariyaMamaTanha/KinaVim)

- 个人 `.vimrc` 配置文件：[.vimrc · Falling Slowly/dotfiles](https://gitee.com/yangsl306/dotfiles/blob/main/.vimrc)
	- 相对行号、高亮
	- 缩进设置
	- 打开文件返回到上次的编辑位置
	- 插件安装与设置
	- buffer 设置
	- 删除行尾的空白符
	- 块模式选中文本搜索
	- 块模式选中文本添加括号

```bash

# 按键映射


<silent>   # 不在命令行中显示执行（映射/命令）信息
<bar>      # 管道符
```



---

### 插件

- [Vim Awesome](https://vimawesome.com/)
- Vim 插件推荐：[Great VIM Plugins in 2023 - hacking C++](https://hackingcpp.com/dev/vim_plugins.html)
- 插件管理器：[plug](https://github.com/junegunn/vim-plug)
- [(neo)vim插件推荐：状态栏美化、代码格式化、markdown预览\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1sY411r78q/)

```bash
# plug 相关命令
:PlugInstall                  # 安装插件
:PlugClean                    # 卸载插件
:PlugUpdate                   # 更新插件


# 推荐插件
lifepillar/vim-solarized8     # theme 美化
vim-airline/vim-airline       # 状态栏美化
vim-airline/vim-airline-themes
ryanoasis/vim-devicons        # 图标

iamcco/markdown-preview.nvim  # 预览 md 文档
dkarter/bullets.vim           # md 列表
dhruvasagar/vim-table-mode    # 格式化 md 表格
mzlogin/vim-markdown-toc      # 生成 md 目录（对 GitHub 有用）

vim-autoformat/vim-autoformat # 代码格式化
preservim/nerdcommenter       # 代码注释

preservim/nerdtree            # 目录树
tpope/vim-surround            # 括号匹配
easymotion/vim-easymotion     # 快速移动
neoclide/coc.nvim             # 提供代码自动补全、语法检查和语言服务器支持
SirVer/ultisnips              # 代码片段
dense-analysis/ale            # 异步代码检查和修复
junegunn/fzf.vim              # 模糊搜索

tommason14/lammps.vim         # LAMMPS 输入参数高亮
Lattay/vasp.vim               # VASP 输入文件参数高亮


# nerdcommenter 相关命令
[count]<leader>cc             # 注释当前行
[count]<leader>cu             # 取消注释当前行
```


---

### 其他

>[vim缓冲区buffer\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Jf4y1g731)

缓冲区 buffer

```bash
:e file      # 打开文件并创建一个新的 buffer
:ls          # 列出所有 buffer（状态及 buffer ID）
:bn          # 切换到下一个 buffer :bnext
:bp          # 切换到上一个 buffer :bprev
:bID         # 根据 buffer ID 切换
:bdID        # 根据 buffer ID 删除 buffer
:hide        # 隐藏 buffer，但不会关闭文件，只是不再显示


# 在 .vimrc 中设置
set hidden   # 默认 buffer 未保存切换会警告；关闭该选项
```

---

寄存器

```bash
"ay       # 复制
"ap       # 粘贴
```

---

折叠

手动折叠：进入可视化模式，选中要折叠的行，`zf` 创建折叠

```bash
:set foldenable  # 开启折叠功能
:set fdm=...     # 设置折叠方法；manual、syntax、marker、indent 等
:mkview          # 保存文件的折叠状态
:loadview        # 加载折叠信息

# 快捷键
zo               # 打开折叠
zc               # 关闭折叠
za               # 切换折叠状态
zj               # 移动至下一折叠
zk               # 移动至上一折叠
zr               # 打开所有折叠
zR               # 打开所有折叠及其嵌套折叠
zm               # 关闭所有折叠
zM               # 关闭所有折叠及其嵌套折叠
zE               # 删除所有折叠
```


---

## Neovim 使用

### 安装

- 安装文档：[neovim/INSTALL.md at master · neovim/neovim · GitHub](https://github.com/neovim/neovim/blob/master/INSTALL.md)
- 安装二进制版本：[Releases · neovim/neovim](https://github.com/neovim/neovim/releases/)

```bash
brew install neovim   # macOS

# 源码编译安装
make CMAKE_EXTRA_FLAGS="-DCMAKE_INSTALL_PREFIX=$HOME/src/neovim"
make install
```


---

### 配置

[GitHub - bryant-video/neovim-tutorial](https://github.com/bryant-video/neovim-tutorial)

---

#### LazyVim

[轻松上手LazyVim：最强大功能的NeoVim编辑器！\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1868QeaEtm/)

- [LazyVim](https://github.com/LazyVim/LazyVim)：一键配置 Neovim（思源一号超算无法使用）

- 默认 `<leader>` 键是 `<space>` 空格键
- 点击 `<space>` 键，会弹出包含以 `<space>` 开头的所有可能的键盘映射的窗口

- Lazyvim 预装插件/工具

```bash
williamboman/mason.nvim         # LSP
folke/flash.nvim                # 代码导航（字符、单词跳转）
nvim-neo-tree/neo-tree.nvim     # 文件系统管理（树状视图显示文件和目录结构）
nvim-telescope/telescope.nvim   # 模糊查找（提供交互式界面）
jesseduffield/lazygit           # git UI，非插件
```

- 相关命令

```bash
:                 # 打开命令窗口
:LazyExtras       # 选择是否开启选定额外功能（如不同编程语言的插件推荐；开启会安装对应的插件）

# tree-sitter 插件命令
:TSInstall        # 安装编程语言 parser
:TSUpate          # 更新
```

- 键位映射

```bash
# 通用
<C-h>             # 跳转左侧窗口
<C-l>             # 跳转右侧窗口
<C-j>             # 跳转下方窗口
<C-k>             # 跳转上方窗口
<C-s>             # 保存文件
<leader>-         # 向下拆分窗口
<leader>|         # 向右拆分窗口
<leader>wd        # 删除窗口
<leader>bd        # 删除 buffer；b 指 buffer
<leader>bb        # 切换到其他 buffer
<leader>`         # 切换到其他 buffer
[w                # 上一个 Warning
]w                # 下一个 Warning
<leader>us        # 切换拼写；u 指 UI 界面
<leader>ul        # 切换行号
<leader>uL        # 切换相对行号
<leader>ub        # 切换背景
<leader>uw        # 切换自动换行
<leader>gg        # 打开 lazygit 窗口（根目录）；g 指 git
<leader>gG        # 打开 lazygit 窗口（当前工作路径）
<leader>ft        # 打开 Terminal
<C-/>             # 隐藏 Terminal
<leader>qq        # 退出所有（窗口、文件等）


# telescope 插件
<leader><space>   # 查找文件
<leader>,         # 切换 buffer
<leader>/         # Grep
<leader>sg        # Grep
<leader>:         # 命令历史
<leader>fr        # 显示最近文件 
<leader>gc        # 显示 git commit
<leader>gs        # 显示 git status
<leader>sc        # 命令历史

# neo-tree 插件
<leader>be        # 打开 buffer 目录树
<leader>e         # 打开文件目录树


# LSP
gd                # 转到定义
K                 # 悬停

# flash 插件
s                 # 字符查找
```

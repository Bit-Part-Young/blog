---
title: LaTeX 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: LaTeX 使用
description: LaTeX 使用
tags:
  - LaTeX
categories:
  - 排版语言
date: 2023-09-30 20:40:00
abbrlink: 119302
password:
---

# LaTeX 使用

## 介绍

本地 overleaf 程序：[NativeOverleaf](https://github.com/fjwillemsen/NativeOverleaf)

LaTeX 斜线表头 package（diagbox）：[CTAN: Package diagbox](https://ctan.org/pkg/diagbox/)

LaTeX 在线编辑器：[ScienHub, Online LaTex Editor](https://www.scienhub.com/)

[常用 LaTeX 代码](https://flowus.cn/latex/share/66110e84-b24a-4cd5-b8a7-2ba2afb35a30)

VSCode LaTeX Utilities 插件

texlive 2024 版本已有 sjtutex 包

- [ ] latex 如何在每个章节最后生成参考文献？

LaTeX 实现审阅效果：latexdiff（texlive 自带）

使用：`latexdiff old.tex new.tex > diff.tex`，编译 `diff.tex`

若 tex 多个文件嵌套，会复杂许多

```bash
# Ubuntu 安装
sudo apt install latexdiff

# macOS 安装
brew install latexdiff

```

LaTeX 中文写作：[Chinese - Overleaf, Online LaTeX Editor](https://www.overleaf.com/learn/latex/Chinese)


```latex
% 不显示日期
\date{}
```

```latex
摄氏度：$^\circ$C

波浪线：\~{}
```

TeX Live 跨版本升级：[Upgrade - TeX Live - TeX Users Group](https://tug.org/texlive/upgrade.html)

overleaf 的项目源码可以 push 到 Github 中，pull 到 overleaf，实现版本控制（交大版的 overleaf 无此功能)



---

### 模板

较为简洁的作业模板
>[hw1.tex](https://raw.githubusercontent.com/OrangeX4/NJUAI-Notes/master/%E4%BC%98%E5%8C%96%E6%96%B9%E6%B3%95/Homework/hw1.tex)

写论文模板
>[GitHub - ElegantLaTeX/ElegantPaper: Elegant LaTeX Template for Working Papers](https://github.com/ElegantLaTeX/ElegantPaper)

>[GitHub - ElegantLaTeX/ElegantBook: Elegant LaTeX Template for Books](https://github.com/ElegantLaTeX/ElegantBook)

>[上海交通大学 Beamer 模版](https://github.com/sjtug/SJTUBeamer)

>[上海交通大学 LaTeX 论文模板](https://github.com/sjtug/SJTUThesis)

---

LaTeX 课件（需设置网络代理）
>[LaTeX 科技文档排版](https://lvjr.bitbucket.io/latex.html)


>[LaTeX专栏 - 八一考研数学竞赛](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU1OTE2MDI4OA==&action=getalbum&album_id=1865901150256857095&scene=173&from_msgid=2247489314&from_itemidx=1&count=3&nolastread=1#wechat_redirect)

>[分类: LaTeX | 始终](https://liam.page/categories/LaTeX/)


markdown 宏包
>[以 Markdown 撰写文稿，以 LaTeX 排版 | 始终](https://liam.page/2020/03/30/writing-manuscript-in-Markdown-and-typesetting-with-LaTeX/)


>[GitHub - zousiyu1995/Study-LaTeX: LaTeX学习笔记](https://github.com/zousiyu1995/Study-LaTeX)


>[GitHub - xinychen/latex-cookbook: LaTeX论文写作教程 (中文版)](https://github.com/xinychen/latex-cookbook)


去除超链接、交叉引用中的方框
[hyperref - Remove ugly borders around clickable cross-references and hyperlinks - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/823/remove-ugly-borders-around-clickable-cross-references-and-hyperlinks)


[LaTeX 入门与进阶](https://latex.lierhua.top/zh/)



自定义 sty 文件
>[mystyle.sty](https://github.com/singularitti/PHYS6080-PS1/blob/main/tex/mystyle.sty)


---

### 参考资料

vscode latex workshop 设置
>[GitHub - EthanDeng/vscode-latex: LaTeX 编译环境配置：Visual Studio Code 配置简介](https://github.com/EthanDeng/vscode-latex)


cls 内容注释很详细
>[GitHub - CheckBoxStudio/BUAAThesis: 北航研究生学位论文模板（Word+LaTeX）.](https://github.com/CheckBoxStudio/BUAAThesis)



>[GitHub - wklchris/Note-by-LaTeX: 《简单粗暴 LaTeX》出版图书开源仓库 | The opensource repo for my published LaTeX book.](https://github.com/wklchris/Note-by-LaTeX)


>[GitHub - xinychen/latex-cookbook: LaTeX论文写作教程 (中文版)](https://github.com/xinychen/latex-cookbook)

>[LaTeX 备忘清单 & latex cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/latex.html)

lec4：LaTeX 排版简要介绍
>[lec4.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec4.md)


>[GitHub - Meiting-Wang/Awesome-LaTeX-cn: The LaTeX materials list I used](https://github.com/Meiting-Wang/Awesome-LaTeX-cn)
>[1.1 Awesome-LaTeX-cn - Meiting Wang](https://meiting-wang.github.io/latex/begin1)


>[GitHub - samcarter/tikzducks: A latex package to draw cute rubber ducks with TikZ](https://github.com/samcarter/tikzducks)

bib 文件写法
>[thesis.bib](https://github.com/thbtppl/latex-thesis-imperial/blob/main/utils/thesis.bib)


>[LaTeX技巧 | Feng's Blog](https://blog.windsky.tech/2022/01/29/LaTeX-Notes/)


自定义列表环境
>[LaTeX 自定义列表环境 | 智朋的个人博客](https://coffeelize.top/posts/18fc56c9.html)

LaTeX OCR
>[GitHub - lukas-blecher/LaTeX-OCR: pix2tex: Using a ViT to convert images of equations into LaTeX code.](https://github.com/lukas-blecher/LaTeX-OCR)


---

## texlive 安装

>[GitHub - OsbertWang/install-latex-guide-zh-cn: 一份简短的关于 LaTeX 安装的介绍](https://github.com/OsbertWang/install-latex-guide-zh-cn)

### Linux 端

CTAN 镜像：[CTAN - 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/CTAN/)

```bash
# 设置自定义安装路径 添加环境变量
export TEXLIVE_INSTALL_PREFIX=$HOME/src/texlive
export TEXLIVE_INSTALL_TEXDIR=$HOME/src/texlive/2023

# 下载
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz --no-check-certificate
tar -xzvf nstall-tl-unx.tar.gz
cd install-tl-*
perl ./install-tl --scheme=full  # 或 medium small
# perl ./install-tl --scheme=full --no-interaction # 不进行交互

# 安装完成后，添加环境变量
export MANPATH=$HOME/src/texlive/2023/texmf-dist/doc/man
export INFOPATH=$HOME/src/texlive/2023/texmf-dist/doc/info
export PATH=$HOME/src/texlive/2023/bin/x86_64-linux:$PATH
```

>注：texlive 不同版本需要安装的数目：medium 约 1395 项；full 约 4543 项。


basic small medium full 版本 texlive 之间的区别
>[https://tex.stackexchange.com/questions/397174/minimal-texlive-installation](https://tex.stackexchange.com/questions/397174/minimal-texlive-installation)


![different schemes of texlive](https://i.stack.imgur.com/Edat8.png)



---


tlmgr：texlive 包管理器

```bash
# 列出已安装的宏包
tlmgr list --only-installed
tlmgr list --only-installed | grep ctex

# 查看 package 信息
tlmgr info <package>

# 查找宏包
tlmgr search <package>

# 查看可升级的宏包
tlmgr update --list

# 安装宏包
tlmgr install <package>

# 升级全部宏包
# --self 选项用于更新 tlmgr 命令本身，而 --all 选项用于更新 TeX Live 系统中的所有宏包和字体
tlmgr update --self --all

# 查看 tlmgr 命令当前使用的源
tlmgr option repository

# 换源
# 清华镜像
# https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet
# 中科大镜像
# https://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet
tlmgr option repository url
```


查看已安装 texlive 的路径
```bash
kpsewhich -var-value=TEXMFMAIN
```


查看 texlive 安装版本
```bash
tex --version

tlmgr --version
```



---

### 在线 texlive

>[overleaf](https://www.overleaf.com/)
>
>[SJTU LaTeX 文档助手, 在线LaTeX编辑器](https://latex.sjtu.edu.cn/)

overleaf 可以使用 vim（**组合键**选项）


---

`texdoc` 是一个命令行程序，功能是查阅 TEX Live 中的文档。这些文档包括：发
行版的说明文档、宏包和文档类的手册，等等。
```bash
texdoc texlive

# 查看宏包文档
texdoc <package>
```




---

texlive 中的目录树（texmf-dist texmf-local），包管理（tlmgr），安装非官方的包

>《lshort-zh-cn.pdf》

>《texlive-zh-cn.pdf》


- [ ] tcolorbox 宏包使用




jupyter notebook 用 tex live+pandoc+nbconvert 转成含中文字符的 pdf（windows 端可以；linux 超算下安装较复杂）
>[https://blog.csdn.net/qq_39004117/article/details/106605076](https://blog.csdn.net/qq_39004117/article/details/106605076)

```bash
# 1. 转换成tex文件
jupyter nbconvert --to latex Week09.ipynb

# 2. 在tex文件中添加下面的三行命令
\usepackage{fontspec, xunicode, xltxtra}
\setmainfont{Microsoft YaHei}
\usepackage{ctex}

# 3. 转换成pdf
xelatex Week09.tex
```



---

## 使用

输出文件类型：

| 文件类型 |                                               说明                                               |
| :------: | :----------------------------------------------------------------------------------------------: |
|  `.sty`  |                                             宏包文件                                             |
|  `.cls`  |                                            文档类文件                                            |
|  `.aux`  | 用于储存交叉引用信息的文件；因此，在更新交叉引用（公式编号、纲级别）后，需要编译两次才能正常显示 |
|  `.log`  |                                     日志；记录上次编译的信息                                     |
|  `.toc`  |                                             目录文件                                             |
|  `.lof`  |                                             图形目录                                             |
|  `.lot`  |                                             表格目录                                             |
|  `.idx`  |                            如果文档中包含索引，该文件用于储存索引信息                            |
|  `.ind`  |                                           索引记录文件                                           |
|  `.ilg`  |                                           索引日志文件                                           |
|  `.bib`  |                                     bibtex 参考文献数据文件                                      |
|  `.bbl`  |                                    bibtex 生成的参考文献记录                                     |
|  `.bst`  |                                           bibtex 模板                                            |
|  `.blg`  |                                           bibtex 日志                                            |
|  `.out`  |                                 hyperref 宏包生成的 pdf 书签记录                                 |

---


 hologo 宏包，可以输出许多 $\TeX$ 家族标志
```bash
% 大写 H 表示符号的首字母也大写
\hologo{XeLaTeX} \Hologo{BibTeX}
```



文件结构

```tex
\documentclass{article} % 百分号为注释
% 导言区，调用宏包、定义命令、进行文档设置等
\begin{document}
% 正文
\end{document} % 后续忽略
```



章节和目录
```tex
\chapter{}
\section{}
\subsection{}
\subsubsection{}
```



命令

- 命令（控制序列）以 `\` 开头，对大小写敏感，如 `\LaTeX` -> $\LaTeX$
- 有些命令会对后续内容产生影响，可以用 `{}` 限定作用范围，如 {\\bf bold}
- 命令可以接收参数，\[\] 中为可选参数，{} 中为必选参数，逗号分隔



字体样式、字号

```tex
% 字体样式
\textbf{bold} \textit{italic} \texttt{typewriter}
\textsf{sans serif} \textsc{Small Caps} \textsl{slanted}

% 字号
{\tiny tiny} {\scriptsize scriptsize} {\footnotesize footnotesize}
{\small small} {\normalsize normalsize} {\large large}
{\Large Large} {\LARGE LARGE} {\huge huge} {\Huge Huge}
```


页眉页脚


列表

表格

浮动体

交叉引用


参考文献


数学公式




```markdown
$\TeX$

$\LaTeX$
```



```tex
\documentclass[options]{…} % 这里其中options可以有 Font size、Paper size、Page Formats、sides与openany等.  
\pagestyle{…} % 设定了页脚和页眉的参数  
\pagenumbering{…} % 页码的样式.默认参数是阿拉伯数字，可重置页码.  
  
\begin{document}  
% 标题部分:包含了 \title, \author, \date, \maketitle  
% 默认情况下内容自动居中，标题过长也会自动换行，这部分在book和report类型文章中会另起一页，而article则在文档的第一页.  
\title  
\author  
\date  
\maketitle  

%Abstract：只在article和report中可以调用\begin{abstract}来实现，在report类中这部分会另起一页，在article中这部分会在第一页的标题下方  
\begin{abstract}  
摘要部分  
\end{abstract}  

\chapter %\chapter*{章} 其写法不会产生编号  
\section  
\subsection  
\subsubsection  
\paragraph  
\subparagraph  
\end{document}
```




`\pagenumbering` 默认参数是阿拉伯数字
>arabic: 阿拉伯数字；roman: 小写罗马数字；Roman: 大写罗马数字；alpha: 小写英文字母 ；Alpha: 大写英文字母


假设在前言部分采用罗马数字，在剩余的正文部分用阿拉伯数字，则在前言部分使用命令 `\pagestyle{roman}`，随后在新的章节后面采用 `\chapter{…}\pagenumbering{arabic}`，还可以在后面接 `\setcounter{page}{number}` 来设定起始页码.

```text
\pagenumbering{arabic}\setcounter{page}{2}
```


---

### 数学公式

基本环境
- `equation，equation*` 单行单公式
- `multline multline*` 多行公式，没有对齐操作，只给一个公式编号
- `gather gather*` 多个公式，可添加多个公式编号
- `align align*` 多个公式对齐，但只能对齐公式内部的一个部分
- `flalign flalign*` 多个公式对齐，可对公式内的多个部分
- `split` 分割公式


>`gathered` 和 `gather` 的区别是放在了一个 `minipage` 里，`aligned` 也是 `minipage` 的问题


>若公式不要编号，在环境名加 `*` 即可实现


```tex
\usepackage{amsmath,amssymb,amsfonts}  % 常用数学宏包
```


- 在数学模式中输入普通文本：`\mbox{文本}` 或 `\text{文本}`
- 在数学模式中插入 空格：`\quad, \qquad, \hspace`，使用 `\,` 等价 `3/18 \quad`

- 数学公式书写：行内 `$ ··· $`，行间：`\[ ··· \]`，

- 常用数学字体命令：`\mathrm, \mathit, \mathtt, \mathsf, \mathbf, \mathcal，\mathbb`

- 数学公式中的函数名最好用正体, 一般通过函数名命令输入，`LaTeX` 中的函数命令都是斜杆 `\` 开始自定义新的函数名 (需 `amsmath` 宏包)，`\DeclareMathOperator{\函数名命令}{函数名}`：注意像这样的命令只能放置在导言区。



- 角标：上标 `ˆ{···}`, 下标 `_{···}`，若实现导数 → 可以直接使用右单引号 `'` 或 `\prime`

- 分式：`\frac → 普通分式， \tfrac → \textstyle， \dfrac → \displaystyle`。注意到 `\frac` 在行内公式中等价于 `\tfrac`, 在行间公式中等价于 `\dfrac`；二项式系数: `\binom, \tbinom, \dbinom`；根式:`\sqrt{···}或\sqrt[n]{···}`

- 求和与积分：求和 `\sum` ，积分 `\int`，针对于行内行间公式取不同的尺寸, 上下限位置也可能不同，这里举个例子，行间公式 `$$ \sum_{i=1}^{n} xˆi $$或\[\]` 可以等价于行内公式的 `$ \displaystyle\sum_{i=1}^{n} xˆi $或\(\)`

- 上、下划线：`\overline{…}，\underline{…}`；

- 上、下大括号：`\overbrace{…}，\underbrace{…}`

- 堆积：`\stackrel{上位符号}{基位符号}`，大家可能不懂，例下这样等号上有条件 `def`


- 定界符：`LaTeX` 中常用的定界符 `( ) [ ] | / \ { } ∥ ⌊ ⌋ ⌈ ⌉ ⟨ ⟩ ↑ ↓ ↕ ⇑ ⇓ ⇕`；定界符可以放大: `\big (1.5 倍), \Big (2 倍), \bigg (2.5 倍), \Bigg (3 倍)`

- 定界符的自适应放大：`\left, \right`，比如 `\left(, \right)` 产生小括号，中括号为 `\left[…\right]`，大括号为 `\left\{…\right\}`，尖括号为 `\left<…\right>`， 绝对值为 `\left|…\right|`， 范数为 `\left\|…\right\|`



自带定界符的矩阵环境，包括：
- 带圆括号 的 `pmatrix` 环境；
- 带方括号 的 `bmatrix` 环境；
- 带花括号 的 `Bmatrix` 环境；
- 带绝对值界的 `vmatrix` 环境与带范数界的 `Vmatrix` .


---


代码展示一般会选用 listings 或者 minted 宏包



```tex

% 页眉页脚设置
\usepackage{fancyhdr}
\pagestyle{fancy}
\lhead{\kaishu~课程报告~}
\rhead{\kaishu~xxx}
\cfoot{\thepage}

% 代码展示设置
\usepackage{listings}
% \lstset{...}
\lstset{tabsize=4, keepspaces=true,
    xleftmargin=2em,xrightmargin=0em, aboveskip=1em,
    %backgroundcolor=\color{gray!20},  % 定义背景颜色
    frame=none,                       % 表示不要边框
    extendedchars=false,              % 解决代码跨页时，章节标题，页眉等汉字不显示的问题
    numberstyle=\ttfamily,
    basicstyle=\ttfamily,
    keywordstyle=\color{blue}\bfseries,
    breakindent=10pt,
    identifierstyle=,                 % nothing happens
    commentstyle=\color{green}\small,  % 注释的设置
    morecomment=[l][\color{green}]{\#},
    numbers=left,stepnumber=1,numberstyle=\scriptsize,
    showstringspaces=false,
    showspaces=false,
    flexiblecolumns=true,
    breaklines=true, breakautoindent=true,breakindent=4em,
    escapeinside={/*@}{@*/},
}



% 自定义标题样式
\usepackage{titlesec}
\titleformat{\chapter}{\centering\zihao{2}\heiti}{第\chinese{chapter}章}{1em}{}


\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}

```


`comment` 是一个特殊的环境，用于将其中的文本视为注释，从而使这些文本不会在生成的文档中显示

```tex
\begin{comment}
...
\end{comment}
```


---

参考文献&文献引用

```tex
% 参考文献相关设置
\usepackage[
    defernumbers=true,
    backend=biber,
    % sorting=ymdnt,     % Year in descending order
    sorting=ynt,       % Year in ascending order
    maxbibnames=3,    % No. of listed names
    style = gb7714-2015,
    % style=ieee,
    % style=science,
    citestyle=numeric-comp,
    isbn=false,     % controls whether the fields isbn/issn/isrn are printed
    % block=par,
    doi=false,        % do not show doi
    giveninits=false,
]{biblatex}
\renewcommand*{\bibfont}{\small}
\setlength{\bibitemsep}{0pt}
\renewcommand{\bibname}{参考文献}
\addbibresource{reference.bib}


% 默认引用格式 
\cite{} 
% 右上角引用格式 
\upcite{} 
% 不出现在正文，出现在参考文献列表 
\nocite{} 

\supercite{}
\parencite{}

% 打印参考文献
\printbibliography
\printbibliography[heading=bibintoc]
```




---

### 表格

浮动体：浮动调整的环境
>因为有浮动体的存在，图片编排的位置是不确定的，所以要避免在文中使用「下图」、「上图」的说法，而是使用 `ref` 命令生成图表的编号。


```tex
\begin{table}[!htbp]
table
\end{table}
%%%%%%%%%%%%%%%%%%%%
\begin{figure}[!htbp]
figure
\end{figure}
```


! 表示忽略内部参数（比如内部参数对一页中浮动体数量的限制）；
h 当前位置 (here)，t 顶部 (top)，b 底部 (bottom)，p 单独成页 (p)。LATEX 的默认参数是 tbp。
另外需要注意的是 label 命令写在 caption 命令下方，否则交叉引用会出现问题。




三线表
```tex
\documentclass[UTF8]{ctexart}  
\usepackage{booktabs} % 需要加载宏包booktabs  

\begin{document}  

% 三线表
\begin{tabular}{ccc}  
\toprule        % 表格头部粗线  
姓名& 学号& 性别\\  
\midrule        % 表格中横线  
1& 2& 3\\  
4& 5& 6\\  
\bottomrule     %表格底部粗线  
\end{tabular}  
  
\end{document}
```


斜线表
```tex
\documentclass[UTF8]{ctexart}  
\usepackage{diagbox} % 需要加载宏包diagbox  

\begin{document}  

% 斜线表头
\centering
\begin{tabular}{|l|ccc|}
\hline
\diagbox{Time}{Room}{Day}
&Mon&Tue&Wed\\
\hline
Morning&used&used&\\
Afternoon& &used&used\\
\hline
\end{tabular}

\end{document}  
```

---

### 字体

```bash
# 查看已安装中英文字体
fc-list :lang=en
fc-list :lang=zh
```


中英文字体设置
```latex
% 新罗马字体设置
\usepackage{fontspec}
\setmainfont{Times New Roman}

% 中文字体设置
\usepackage{xeCJK}
\setCJKmainfont{Source Han Sans SC}
\setCJKmainfont{Smiley Sans}
```


---

### 编译

用 Makefile 编译 LaTeX 文档
>[GitHub - yhwu-is/Linear-Algebra-Left-Undone: 线性代数：未竟之美](https://github.com/yhwu-is/Linear-Algebra-Left-Undone)

>ctexart 需使用 xelatex 编译
>overleaf 默认使用 pdflatex 编译


pdflatex 表示使用 pdf$\TeX$ 作为引擎、使用 $\LaTeX$ 格式来编译文档（还有 xelatex、lualatex 等）。这些命令行命令通常称为 “ 编译方式 “；编译方式写成图标的形式


中文文档的编译方式：对于中文文档，推荐使用 xelatex 或 lualatex 编译并使用 ctex 宏集作为中文支持
```tex
\documentclass{ctexart}
```

>还需确保文档以 UTF-8 编码保存


中文支持
- 使用 ctexart ctexrep ctexbook 等文档类

```tex
\documentclass{ctexart}
\begin{document}
你好，世界！
\end{document}
```

- 引入 ctex 宏包

```tex
\documentclass{article}
\usepackage{ctex}
\begin{document}
你好，世界！
\end{document}
```




```bash
xelatex file.tex

xelatex -shell-escape file.tex

xelatex file

xelatex -shell-escape -synctex=1 %.tex
```

>编译命令启用了 -shell-escape 选项，从而可以使用一些依赖于外部工具的宏包（比如依赖于 Python 的 minted 宏包）。

>-shell-escape 选项开启 shell 转义，这一选项的直接应用就是允许使用 minted
宏包实现抄录代码高亮（见第 100 页）；-synctex=1 选项用于启用 SyncTEX 程序，编
辑器可以使用 SyncTEX 的输出来实现源代码和 PDF 之间的相互跳转。

使用命令行编译，若源文件的扩展名为.tex，则扩展名可以省略




![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310011726060.png)




```bash
latexmk -c

latexmk -C
```



---

#### latexmk

`.latexmkrc` 文件：latexmk 配置文件；通常包含以下内容
- 构建引擎的选择：如 pdfLaTeX、XeLaTeX 或 LuaLaTeX。
- 构建参数：设置构建过程中的各种参数，如输出文件类型、编译次数、文件清理选项等。
- 自定义构建规则：包括设置文件依赖关系、指定额外的编译步骤等。
- 输出文件命名规则：定义输出文件的命名规则，以确保生成的文件按照特定的方式命名。
- 文件监控选项：配置 latexmk 以在文件更改时自动重新构建文档，以提高工作效率。


[.latexmkrc](https://github.com/sjtug/SJTUThesis/blob/master/.latexmkrc)
```bash
# Latexmk configuration file.
#
#   WARNING: Only works with version 4.59 or higher of latexmk.
#

# reference: https://github.com/sjtug/SJTUThesis/blob/master/.latexmkrc

# Set timezone.
$ENV{'TZ'}='Asia/Shanghai';

# Ensure './texmf//' is in '$TEXINPUTS'.
ensure_path( 'TEXINPUTS', './texmf//' );

# PDF generate method
#   - 1 pdfLaTeX
#   - 3 LaTeX + DVIPDFMx
#   - 4 LuaLaTeX
#   - 5 XeLaTeX
$pdf_mode = 5;

# Add common patterns for tex engines.
set_tex_cmds( '-synctex=1 %O %S' );

# Always try to embed fonts, ignoring licensing flags, etc.
$xdvipdfmx = 'xdvipdfmx -E -o %D %O %S';

# Files to clean.
$clean_ext = 'bbl glo gls hd loa run.xml thm xdv synctex.gz';

```


---

#### 带参考文献

bibtex 引擎编译参考文献
>[LaTeX 参考文献输出](https://mp.weixin.qq.com/s/_comduqz-XOm7u6ArlP4KQ)

```bash
xelatex main.tex
bibtex main.aux
xelatex main.tex
xelatex main.tex
```


---

使用 biblatex 宏包，biber 作为后端，编译参考文献（使用 `latexmk` 或 `xe-biber-xe-xe`）
>[texstudio如何编译biblatex+biber？ - LaTeX问答](https://ask.latexstudio.net/ask/question/7509.html)

```bash
latexmk --xelatex main.tex
```


---

#### Github Actions 编译

用 github action 来编译 LaTeX
>[GitHub - xu-cheng/latex-action: :octocat: GitHub Action to compile LaTeX documents](https://github.com/xu-cheng/latex-action)

>[tex.yml](https://github.com/yhwu-is/Linear-Algebra-Left-Undone/blob/new/.github/workflows/tex.yml)

>不是很好用

```yaml
name: Build LaTeX document
on: [push]
jobs:
  build_latex:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Git repository
        uses: actions/checkout@v3
      - name: Compile LaTeX document
        uses: xu-cheng/latex-action@v3
        with:
          root_file: hello_latex.tex
          latexmk_use_xelatex: true
      - name: Upload PDF file
        uses: actions/upload-artifact@v3
        with:
          name: PDF
          path: hello_latex.pdf
		  
```


用 github action 进行 release 发布
[release.yml](https://github.com/sjtug/SJTUThesis/blob/master/.github/workflows/release.yml)
```yaml
name: Release

on:
  push:
    branches:
    - release
    tags:
    - "v*"

jobs:
  release-latexmk:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    steps: 
      - uses: actions/checkout@v2
        name: checkout code
      - uses: xu-cheng/texlive-action/full@v1
        name: build with latexmk
        with:
          run: |
            latexmk main.tex -halt-on-error -time -xelatex
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: ${{ github.ref }}
          body: "New release ${{ github.ref }}"
          draft: true
          prerelease: false
          files: |
            main.pdf
```



---


表格制作
>[https://www.tablesgenerator.com/](https://www.tablesgenerator.com/)



长竖线
>[https://www.zhihu.com/question/35119859](https://www.zhihu.com/question/35119859)

```latex
\frac{df}{dx}\bigg|_{x = x_0} 

\frac{df}{dx}\Bigg|_{x = x_0}
```



括号（大中小）大小控制
>[http://www.52souji.net/control-the-dimension-of-bracket-in-latex.html](http://www.52souji.net/control-the-dimension-of-bracket-in-latex.html)

方法一：在左右括号前分别添加 `\left` 和 `\right`（需要配对使用；能自动控制不同层次括号的大小）



---

## 自定义命令

命令使用 `\cmd{arg1}{arg2}` 来调用

`cmd` - 不能重名，必须符合命名规则。
`args` - 参数数量，0 ∼ 9，默认为 0。
`default` - 设定第⼀个参数的默认值，同时表示该参数是**可选参数**，新命令中最多只能有⼀个可选参数。
`def` - 定义，涉及到参数时使用 `#n` 表示第 n 个参数。


```tex
% 定义新命令
\newcommand{cmd}[args][default]{def}
\newcommand*{cmd}[args][default]{def}

% 修改已有命令
\renewcommand{cmd}[args][default]{def}
\renewcommand*{cmd}[args][default]{def}
```

>带星号的命令称为短命令，其中参数不能有换段或空行，否则编译报错，但是短命令有利排错


在命令中如果包含数学命令，那么这条命令只能⽤于⽂本模式，不能⽤于数学模式（因为
在数学模式中会被多加了⼀层 `$ $` 导致报错）。所以，在定义数学命令时，使⽤ `\ensuremath{code}` 来定义，这样的命令在数学模式中时 code 本⾝，在⽂本模式中时 `$ code $`。



---

### 宏包

写宏包
>[https://github.com/ustctug/ustcthesis/wiki/参与开发](https://github.com/ustctug/ustcthesis/wiki/%E5%8F%82%E4%B8%8E%E5%BC%80%E5%8F%91)



>[document.tex](https://github.com/Meiting-Wang/Article-template/blob/main/document.tex)
```latex
% 需使用 xelatex 编译
% 导言区
\documentclass[UTF8,hyperref,space=auto]{ctexart} %UTF8 编码，引入 hyperref 宏包 (可形成超链接及使用其自带的额外命令)，设置其处理空格的方式为 auto
\usepackage[a4paper,showframe]{geometry} % 设置纸张为 A4 大小
\usepackage[dvipsnames]{xcolor} % 扩展版的颜色宏包
\usepackage{cprotect} % 保护被抄录的语句
\usepackage{lipsum} % 形成一些随机的英语文字
\usepackage{zhlipsum} % 形成一些随机的中文文字
\usepackage{amsmath} % 数学命令及环境中最重要的宏包之一
\usepackage{amssymb} % 输出更多的数学符号
\usepackage{mathtools} % 提供了 dcases 环境
\usepackage{extarrows} % 提供了更多的数学长箭头
\usepackage{multirow} % 提供可跨行的处理表格的命令
\usepackage{array} % 提供了更多的表格列说明符，以及修正了一些表格显示上的问题
\usepackage{booktabs} % 以使用学术上常见的三线表命令
\usepackage{graphicx} % 插图专用宏包
\graphicspath{{figures/}} % 图片在当前目录的 figures 目录下
\usepackage{caption,subcaption} % 输出子图表专用
\usepackage{float} % 其 H 参数可以让浮动环境不再浮动
\usepackage{titlesec,titletoc} % 可分别设置目录和正文中的标题样式
\usepackage{natbib} % 专门用来排版文献的宏包
\usepackage[nottoc]{tocbibind} % 默认可将参考文献、索引等放入 tableofcontents
\usepackage[amsmath,thmmarks]{ntheorem} % 定理类环境宏包，如果前面使用 amsmath 宏包，则需加上 amsmath 宏包选项以避免出现未知问题，若需在定理环境末尾加上特定符号 (如证毕符号)，则需使用 thmmarks 宏包选项以使用\theoremsymbol{}命令。

\usepackage[bf,small,raggedright,indentafter,pagestyles]{titlesec}
% 其中 bf 设置章节标题的字体为黑体，这也是默认值，此外可以设为 rm(罗马体), sf(无衬线体), tt(打字机体), md(中等黑度),up(直立体), it(意大利斜体), sl(机械斜体), sc(小体大写字母)。
% small 设置标题字体的尺寸，还可设为 big(默认), medium, tiny。
% center 使标题居中，还可以设为 raggedleft(居左，默认),raggedright(居右)
% indentafter 相当于宏包 indentfirst 的作用，使标题下面的第一个段落正常缩进
% pagestyles 是申明后面要自定义页面样式

```



---

## 问题

下划线 `\newcommand` 及粗细设置
>[underline - Why does \\uline sometimes render thicker and darker (inconsistent with underlining in the rest of the text)? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/537907/why-does-uline-sometimes-render-thicker-and-darker-inconsistent-with-underlini)
>
>[Fixing the length of underline text - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/482835/fixing-the-length-of-underline-text)



简历

latex 版本
>[GitHub - jankapunkt/latexcv: :necktie: A collection of cv and resume templates written in LaTeX. Leave an issue if your language is not supported!](https://github.com/jankapunkt/latexcv)

用的是 tectonic latex 引擎
>[GitHub - philipempl/modern-latex-cv: A professional and modern CV in LaTex](https://github.com/philipempl/modern-latex-cv)
>[GitHub - AntObi/academicCV: LaTeX template for academic CV](https://github.com/AntObi/academicCV)



>[GitHub - sinaatalay/rendercv: LaTeX CV generator from a YAML/JSON input file.](https://github.com/sinaatalay/rendercv)



---

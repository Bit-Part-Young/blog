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

- TeX 是高德纳 (Donald E. Knuth) 为排版文字和数学公式而开发的软件
- LaTeX 是一种使用 TeX 程序作为排版引擎的格式（format），可以粗略地将它理解成是对 TeX 的一层封装；与汉字 “拉泰赫” 或 “雷泰赫” 的发音相近

- 优缺点：
	- 优点：专注于内容本身，排版（typesetting）效果好，数学公式排版强大，跨平台开源...
	- 缺点：学习成本高，不容易排错，不容易定制样式，不所见即所得...

- TeX 发行版：TeX Live / MacTeX（macOS 下定制的 TeX Live 版本）
- TeX 编辑器：TeXstudio、TeXShop（MacTeX 自带）


---

### 参考资料

- 现代 LaTeX 入门讲座：[GitHub - stone-zeng/latex-talk](https://github.com/stone-zeng/latex-talk)
- 《如何使用 LaTeX 排版论文》讲稿：[GitHub - tuna/thulib-latex-talk](https://github.com/tuna/thulib-latex-talk)
- [lshort-zh-cn.pdf](https://github.com/CTeX-org/lshort-zh-cn)
- [GitHub - wklchris/Note-by-LaTeX: 《简单粗暴 LaTeX》出版图书开源仓库](https://github.com/wklchris/Note-by-LaTeX)
- [LaTeX 备忘清单 & latex cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/latex.html)
- LaTeX 排版简要介绍：[lec4.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec4.md)
- 需设置网络代理：[LaTeX 科技文档排版](https://lvjr.bitbucket.io/latex.html)
- [LaTeX专栏 - 八一考研数学竞赛](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU1OTE2MDI4OA==&action=getalbum&album_id=1865901150256857095&scene=173&from_msgid=2247489314&from_itemidx=1&count=3&nolastread=1#wechat_redirect)
- [分类: LaTeX - 始终](https://liam.page/categories/LaTeX/)
- [GitHub - zousiyu1995/Study-LaTeX: LaTeX学习笔记](https://github.com/zousiyu1995/Study-LaTeX)
- [GitHub - xinychen/latex-cookbook: LaTeX论文写作教程 (中文版)](https://github.com/xinychen/latex-cookbook)
- [LaTeX 入门与进阶](https://latex.lierhua.top/zh/)
- [GitHub - xinychen/latex-cookbook: LaTeX论文写作教程 (中文版)](https://github.com/xinychen/latex-cookbook)
- [GitHub - Meiting-Wang/Awesome-LaTeX-cn: The LaTeX materials list I used](https://github.com/Meiting-Wang/Awesome-LaTeX-cn)
- [1.1 Awesome-LaTeX-cn - Meiting Wang](https://meiting-wang.github.io/latex/begin1)
- [GitHub - samcarter/tikzducks: A latex package to draw cute rubber ducks with TikZ](https://github.com/samcarter/tikzducks)
- [LaTeX技巧 | Feng's Blog](https://blog.windsky.tech/2022/01/29/LaTeX-Notes/)
- [常用 LaTeX 代码](https://flowus.cn/latex/share/66110e84-b24a-4cd5-b8a7-2ba2afb35a30)

- [分类: LaTeX - 智朋的个人博客](https://coffeelize.top/categories/LaTeX/)

- 自定义列表环境：[LaTeX 自定义列表环境 - 智朋的个人博客](https://coffeelize.top/posts/18fc56c9.html)

- Overleaf LaTeX 教程：[Learn LaTeX in 30 minutes - Overleaf, Online LaTeX Editor](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
- Overleaf LaTeX 中文写作教程：[Chinese - Overleaf, Online LaTeX Editor](https://www.overleaf.com/learn/latex/Chinese)



---

## TeX Live 安装

### 介绍

- 安装参考：
	- [GitHub - OsbertWang/install-latex-guide-zh-cn: 一份简短的关于 LaTeX 安装的介绍](https://github.com/OsbertWang/install-latex-guide-zh-cn)
	- [GitHub - AlphaZTX/LaTeX-tutorials](https://github.com/AlphaZTX/LaTeX-tutorials)（含 TeXstudio 使用）

- TeX Live 2024 版本已有 sjtutex 文档类
- TeX Live 不同版本（basic small medium full）之间的区别：[installing - Minimal TeXLive installation - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/397174/minimal-texlive-installation)
- TeX Live 跨版本升级：[Upgrade - TeX Live - TeX Users Group](https://tug.org/texlive/upgrade.html)


![different schemes of texlive](https://i.stack.imgur.com/Edat8.png)

```bash
# 查看 TeX Live 指南
texdoc texlive-en
texdoc texlive-zh

# 查看宏包、文档类帮助文档
texdoc package/class
```


---

### Linux

CTAN 镜像：[CTAN - 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/CTAN/)

```bash
# 设置自定义安装路径 添加环境变量
export TEXLIVE_INSTALL_PREFIX=$HOME/src/texlive
export TEXLIVE_INSTALL_TEXDIR=$HOME/src/texlive/2023

# 下载
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz --no-check-certificate

tar -xzvf nstall-tl-unx.tar.gz

cd install-tl-*

# 安装
perl ./install-tl --scheme=full  # 或 medium small
# --no-interaction 参数：不进行交互
# -gui  启用 GUI 安装程序

# 安装完成后，添加环境变量
export MANPATH=$HOME/src/texlive/2023/texmf-dist/doc/man
export INFOPATH=$HOME/src/texlive/2023/texmf-dist/doc/info
export PATH=$HOME/src/texlive/2023/bin/x86_64-linux:$PATH
```


---

### macOS

- 不建议用 brew 下载安装（体积太大），而是手动下载安装包
- 安装：[MacTeX - TeX Users Group](https://www.tug.org/mactex/mactex-download.html)；在官网上下载最新 pkg 包，双击，按照提示安装
- 卸载：[Uninstalling - MacTeX - TeX Users Group](https://tug.org/mactex/uninstalling.html)；卸载 GUI，直接将 TeX 移入废纸篓；卸载 TeX Distribution；卸载 Ghostscript（删除较复杂；通常在 `/usr/local/share` 或 `/usr/local/bin` 目录）

```bash
sudo rm -rf /Library/TeX
sudo rm -rf /usr/local/texlive
```

- MacTeX 本质上就是 TeXLive，只不过捆绑了 Ghostscript（处理 PS 图片文件转换成 pdf 文件） 和一些 GUI 程序，做成了便于安装的 pkg 包而已。pkg 包内的安装脚本会帮你设置好环境变量

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405070921146.png)


---

### TeX 目录结构

TeX 目录结构（TeX Directory Structure, TDS）：TeX 发行版中宏包、字体、帮助文档等文件的组织结构；有时也称为 TEXMF 树

```bash
texlive/XXXX/texmf-dist/  # TEXMF 树根目录

tex/latex       # LaTeX 宏包
doc/latex       # LaTeX 宏包的帮助文档
source/latex    # LaTeX 宏包的源代码
bibtex/         # BibTeX 工具相关文件，许多宏包配套的 BibTeX 格式文件位于子目录 bst 中
fonts/tfm       # TeX 使用的字体文件，TFM 格式
fonts/type1     # PostScript 字体文件（Type1），PFB 格式
fonts/opentype  # OpenType 格式的字体文件
```

需要手动安装的宏包，一般已经按照上述目录结构打包完成。手动安装时，尽量不要拷贝到系统的 TEXMF 树，而是拷贝到发行版提供的用户 TEXMF 树，如 `texlive/texmf-local`。安装完成后，还需**刷新 TeX 发行版的文件名数据库**，令新安装的宏包文件能够被系统找到。

```bash
mktexlsr
```


---

### tlmgr 使用

tlmgr：TeX Live 包管理器

- 清华镜像：https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet
- 中科大镜像：https://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet
- 交大镜像：https://mirrors.sjtug.sjtu.edu.cn/CTAN/systems/texlive/tlnet

```bash
# 列出已安装的宏包和文档类
tlmgr list --only-installed

tlmgr info <package>  # 查看宏包信息
tlmgr search <package>  # 查找宏包
tlmgr update --list  # 查看可升级的宏包
tlmgr install <package>  # 安装宏包

# 升级全部宏包
# --self 更新 tlmgr 命令本身
# --all 更新 TeX Live 系统中的所有宏包和字体
tlmgr update --self --all

# 查看当前使用的源
tlmgr option repository
# 换源
tlmgr option repository url
tlmgr repository set <CTAN mirrors>/systems/texlive/tlnet
```

```bash
# 查看已安装 Tex Live 的路径
kpsewhich -var-value=TEXMFMAIN

# 查看文档类路径
kpsewhich <classname>.cls

# 查看 texlive 安装版本
tex --version
tlmgr --version
```

---

## LaTeX 编辑器

- Windows 端：TeXstudio
- Mac 端：TeXShop

- 在线 LaTeX 编辑器
	- [overleaf](https://www.overleaf.com/)；本地 overleaf 软件：[NativeOverleaf](https://github.com/fjwillemsen/NativeOverleaf)
	- [SJTU LaTeX 文档助手, 在线LaTeX编辑器](https://latex.sjtu.edu.cn/)
	- LaTeX 在线编辑器：[ScienHub, Online LaTex Editor](https://www.scienhub.com/)

---

overleaf 使用：

- overleaf 的项目源码可以 push 到 GitHub 中，pull 到 overleaf，实现版本控制（交大版的 overleaf 无此功能)
- overleaf 可以使用 vim（**组合键**选项）

---

TeXstudio：工具 - 清理辅助文件


---

## 使用

### 工具

- VSCode LaTeX Workshop 设置：[GitHub - EthanDeng/vscode-latex: LaTeX 编译环境配置：Visual Studio Code 配置简介](https://github.com/EthanDeng/vscode-latex)

- VSCode LaTeX Utilities 插件

- LaTeX OCR：[GitHub - lukas-blecher/LaTeX-OCR: pix2tex: Using a ViT to convert images of equations into LaTeX code.](https://github.com/lukas-blecher/LaTeX-OCR)

- Markdown 宏包：[以 Markdown 撰写文稿，以 LaTeX 排版](https://liam.page/2020/03/30/writing-manuscript-in-Markdown-and-typesetting-with-LaTeX/)

---

`texdoc`：查阅 texlive 中的文档，包括发行版的说明文档、宏包和文档类的手册等。

```bash
texdoc texlive
texdoc <package>  # 查看宏包文档
```

---

BibTeX 相关：

- 格式化 bib 文件：[GitHub - FlamingTempura/bibtex-tidy: Cleaner and Formatter for BibTeX files](https://github.com/FlamingTempura/bibtex-tidy)
- [GitHub - Nickydusk/BibTeX-Formatter: Format your bibtex (.bib) file to help standardize citations for conference and journal submissions](https://github.com/Nickydusk/BibTeX-Formatter)

```bash
npm install -g bibtex-tidy

bibtex-tidy refs.bib

# 常用参数
bibtex-tidy refs.bib \
    --sort=-year,title \
    --sort-fields \
    --omit=abstract,keywords \
    --blank-lines \
    --duplicates \
    --escape \
    --strip-comments \
    --trailing-commas \
    --no-wrap \
    --remove-empty-fields \
    --remove-dupe-fields \
    --tidy-comments
```

[GitHub - njzjz/tushuguan: A template to create a BibTeX Library](https://github.com/njzjz/tushuguan)

doi 转 bib 格式：

- [GitHub - njzjz/wenxian: A tool to generate BibTeX files from given identifiers (DOI, PMID, or arXiv ID).](https://github.com/njzjz/wenxian)（效果比较好）
- [doi2bib](https://www.doi2bib.org/)（最直接方便；无摘要参数；中国人名的姓名前后顺序问题；article 后面的信息与官方期刊生成的 BibTeX 不一致）
- [GitHub - thchr/DOI2BibTeX.jl](https://github.com/thchr/DOI2BibTeX.jl)（只能在 REPL 下输出格式才美观）
- [GitHub - bibcure/doi2bib: get the bibtex string given a doi](https://github.com/bibcure/doi2bib)

```bash
# doi
julia> using DOI2BibTeX
julia> doi = "10.1103/PhysRevLett.45.494"
julia> doi2bib(doi)

# arxiv
julia> arxiv = "arxiv:1710.10324"
julia> arxiv2bib(arxiv)

# wenxian 安装与使用
pip install -U pipx
pipx run wenxian from 10.1063/5.0155600

# bib 中一些不需要的条目
sed -i '/abstract = {/d' xxx.bib
sed -i '/doi = {/d' xxx.bib
sed -i '/keywords = {/d' xxx.bib
```

ris（Zotero）转 bib 格式：

- [GitHub - harrisonlabollita/ris-2-bib: A command line tool to convert RIS files into bib files for LaTeX bibliographies](https://github.com/harrisonlabollita/ris-2-bib)
- [GitHub - janberges/ris2bib: Convert bibliographies from RIS to BibTeX format](https://github.com/janberges/ris2bib)

---

LaTeX 实现审阅效果：latexdiff（texlive 自带）

使用：`latexdiff old.tex new.tex > diff.tex`，编译 `diff.tex`

若 tex 多个文件嵌套，会复杂许多

```bash
# Ubuntu 安装
sudo apt install latexdiff

# macOS 安装
brew install latexdiff
```

---

[GitHub - chazeon/revtex2docx: Wrapper scripts and pandoc filters to convert LaTeX documents to Word docx files](https://github.com/chazeon/revtex2docx)

生成多种格式文献引用：[BibGuru - A New FREE APA, Harvard, & MLA Citation Generator](https://www.bibguru.com/)


---

### 编译

- pdflatex 表示使用 pdfTeX 作为引擎、使用 LaTeX 格式来编译文档（还有 xelatex、lualatex 等）。这些命令行命令通常称为 “编译方式”；编译方式写成图标的形式
- 英文文档：用 pdflatex、xelatex、lualatex 编译
- 中文文档：用、xelatex、lualatex 编译编译
- ctexart 文档类需使用 xelatex 编译；overleaf 在线编辑器默认使用 pdflatex 编译



![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310011726060.png)

```bash
# .tex 扩展名可以省略
xelatex file.tex
xelatex file

xelatex -shell-escape file.tex

xelatex -shell-escape -synctex=1 %.tex
```

- 参数 `-shell-escape`：开启 shell 转义，允许使用依赖于外部工具的宏包（如 minted 宏包实现代码高亮）
- 参数 `-synctex=1`：启用 SyncTEX 程序，编辑器可以使用 SyncTEX 的输出来实现源代码和 PDF 之间的相互跳转

---

含参考文献的文档编译

- BibTeX 后端：[LaTeX 参考文献输出](https://mp.weixin.qq.com/s/_comduqz-XOm7u6ArlP4KQ)
	- `xe-bib-xe-xe` 编译顺序

```bash
# 可以略去扩展名
xelatex main.tex
bibtex main.aux
xelatex main.tex
xelatex main.tex
```

- biber 后端 + biblatex 宏包：[texstudio如何编译biblatex+biber？ - LaTeX问答](https://ask.latexstudio.net/ask/question/7509.html)
	- 使用 `latexmk` 或 `xe-biber-xe-xe` 编译顺序

```bash
latexmk --xelatex main.tex
```

---

用 Makefile 编译 LaTeX 文档

- [GitHub - yhwu-is/Linear-Algebra-Left-Undone: 线性代数：未竟之美](https://github.com/yhwu-is/Linear-Algebra-Left-Undone)
- [Makefile](https://github.com/mage-tianxie/latex-/blob/master/Makefile)

使用 Github Actions 自动编译

- [GitHub - xu-cheng/latex-action: :octocat: GitHub Action to compile LaTeX documents](https://github.com/xu-cheng/latex-action)
- [tex.yml](https://github.com/yhwu-is/Linear-Algebra-Left-Undone/blob/new/.github/workflows/tex.yml)（不是很好用）

使用 GitHub Actions 将编译的 pdf 文档作为 release 发布：[release.yml](https://github.com/sjtug/SJTUThesis/blob/master/.github/workflows/release.yml)


---

#### latexmk

`.latexmkrc` 文件：latexmk 配置文件；通常包含以下内容

- 构建引擎的选择：如 pdfLaTeX、XeLaTeX 或 LuaLaTeX。
- 构建参数：设置构建过程中的各种参数，如输出文件类型、编译次数、文件清理选项等。
- 自定义构建规则：包括设置文件依赖关系、指定额外的编译步骤等。
- 输出文件命名规则：定义输出文件的命名规则，以确保生成的文件按照特定的方式命名。
- 文件监控选项：配置 latexmk 以在文件更改时自动重新构建文档，以提高工作效率。

.latexmkrc 含义
>[.latexmkrc](https://github.com/cohsh/.dotfiles/blob/main/latex/.latexmkrc)

```bash
latexmk -c  # 删除编译过程中的临时文件
latexmk -C  # 会删除 pdf 文件
```

[.latexmkrc](https://github.com/sjtug/SJTUThesis/blob/master/.latexmkrc)

```bash
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

### 语法

- 注释：以 `%` 开头

- 命令：以 `\` 开头，区分大小写；`\command[...]{...}`：必选参数放在 `{...}` 中，可选参数放在 `[...]`，多个参数以逗号分隔

- 有些命令会对后续内容产生影响，可以用 `{}` 限定作用范围，如 `{\bf bold}`

- 环境：常用环境：列表与枚举、图片、表格、定理等

- 特殊符号需转义，如 `\%`、`\$` 等

```latex
\begin{env}
   ...
\end{env}
```

- 相关术语与概念：引擎、格式、编译命令


---

### 文档类和宏包

#### 文档类

- 文档类：英文排版：article、report、book；中文排版 ctexart、ctexrep、ctexbook；幻灯片：beamer
- 可选参数：为文档类指定选项，以全局地规定一些排版的参数，如字号、纸张大小、单双面等；三个标准文档类可指定的选项如下

```latex
\documentclass[options]{classname}
\documentclass[12pt,twoside,a4paper]{article}
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407191928496.png)


---

#### 宏包

- 宏包：在使用 LaTeX 时，时常需要依赖一些扩展来增强或补充 LaTeX 的功能，比如排版复杂的表格、插入图片、增加颜色甚至超链接等
- 可一次性调用多个宏包，逗号隔开，这种用法一般不要指定选项

```latex
\usepackage[options]{packagename}
```


---

### 文件类型

- LaTeX 模板相关文件格式：`.sty`、`.cls`、`bst`、`bib`
- LaTeX 编译过程中生成相当多的辅助文件和日志，一些功能如交叉引用、参考文献、目录、索引等，需要先通过编译生成辅助文件，然后再次编译时读入辅助文件得到正确的结果，所以复杂的 LaTeX 源代码可能要编译多次

|  文件类型  |                 说明                  |
| :----: | :---------------------------------: |
| `.sty` |           宏包文件；宏包名称与文件名一致           |
| `.cls` |          文档类文件；文档类名称与文件名一致          |
| `.bst` |         BibTeX 用到的参考文献格式模板          |
| `.bib` |          BibTeX 参考文献数据库文件           |
| `.log` |         排版引擎生成的日志文件，供排查错误使用         |
| `.aux` |      主辅助文件，记录交叉引用、目录、参考文献的引用等       |
| `.toc` |               目录记录文件                |
| `.lof` |              图形目录记录文件               |
| `.lot` |              表格目录记录文件               |
| `.bbl` |         BibTeX 生成的参考文献记录文件          |
| `.blg` |           BibTeX 生成的日志文件            |
| `.idx` |        供 makeindex 处理的索引记录文件        |
| `.ind` | makeindex 处理 `.idx` 生成的用于排版的格式化索引文件 |
| `.ilg` |          makeindex 生成的日志文件          |
| `.out` |      hyperref 宏包生成的 pdf 书签记录文件      |

---

### 文件结构

#### 文件结构

```tex
\documentclass{article}  % 指明文档类型

% 导言区：设置文档样式
\usepackage{...}     % 调用宏包
\newcommand{...}         % 自定义命令

\begin{document}
% 正文
    ...
\end{document}
% 后续忽略
```


---

#### 中文排版

- 使用 ctexart ctexrep ctexbook 等 ctex 文档类（源代码需保存为 UTF-8 编码）
- 引入 ctex 宏包

```latex
\documentclass{ctexart}

\documentclass{article}
\usepackage{ctex}
```

---

- 中文文档简略测试

```latex
% 用 XeLaTeX 或 LuaLaTeX 编译
\documentclass{ctexart}
\begin{document}
\TeX{} 你好！
\end{document}
```

---

#### 文档部件

- 标题：`\title`、`\author`、`\date` → `\maketitle`
- 摘要：`abstract` 环境
- 目录：`\tableofcontents`
- 章节：`\chapter`、`\section`、`\subsection` 等
- 文献：`\bibliography`

注：`abstract` 环境只在 article 和 report 文档类有，report 文档类会单独成页，article 文档类会在标题下方


---

#### 文档划分

- 分文件编译：`\include`、`\input`
- 两者区别在于 `\include` 命令将会插入 `\clearpage` 再读取文件（即另起一页）

```latex
\input{filename.tex}
\include{filename}
```


---

### 字符

- 空格：空格键和 Tab 键输入的空白字符视为“空格”。连续的若干个空白字符视为一个空格。一行开头的空格忽略不计。

- 换行：行末的换行符视为一个空格；但连续两个换行符，也就是空行，会将文字分段。多个空行被视为一个空行。也可以在行末使用 `\par` 命令分段。

- 中文的标点符号（绝大多数为非 ASCII 字符）使用中文输入法输入即可，一般不需要过多留意；而输入西文标点符号时，有不少地方需要留意
	- 西文排版中经常会出现连字（ligatures），常见的有 ff/fi/fl/ffi/ffl
	- 单引号 ' 和 ' 分别用 \` 和 ' 输入；双引号 “ 和 ” 分别用 \`\` 和 '' 输入
	- 三种长度的横线：连字号 `-` 用来组成复合词；短破折号 `--` 用来连接数字表示范围；长破折号 `---` 用来连接单词，语义上类似中文的破折号
	- 英文省略号用 `\ldots`

- 拉丁文扩展与重音

```latex
% 加一对花括号的写法相当于提供了空的参数
% 否则它们可能会将后面的字符作为参数，形成重音效果
\# \$ \% \& \{ \} \_
\^{}  \~{}  \textbackslash

dif{}f{}icult  f{}ind  % 连字

``Please press the `x' key.''  % 单引号、双引号

\ldots  \ldots{}  % 省略号

% 三种长度的横线
daughter-in-law, X-rated \\
pages 13--67 \\
yes---or no?

% 特殊字符
Å  \AA % 埃
```


---

### 断行和换页

- 单词间距：西文排版中，断行的位置优先选取在两个单词之间，即“空格”；文字在单词间的“空格”处断行时，“空格”生成的间距随之舍去。可使用字符 `~` 输入一个不会断行的空格，通常用在英文人名、图表名称等上下文环境

- 断行：`\\` 可在表格、公式等地方用于换行，而 `\newline` 只用于文本段落中

- 换页：`\newpage`、`clearpage`

- 命令 `\newline` 和 `\newpage` 会在断行/断页位置填充适当的间距，但 `\linebreak` 和 `\pagebreak` 不能，使用这些命令强行断行/断页可能会制造出糟糕的排版效果，并导致 LaTeX 报 `Underfull \hbox` 等警告

- 手动断词：对于绝大多数单词，LaTeX 能够找到合适的断词位置，在断开的行尾加上连字符 `-`。手动使用 `\-` 命令指定断词的位置

```latex
% 不会断行的空格
Fig.~2a \\
Donald~E. Knuth

% 断行
\\[length]  \newline

% 换页
\newpage  \clearpage

% 数字 n 代表适合/不适合的程度；0-4，缺省为 4
\linebreak[n] \nolinebreak[n]
\pagebreak[n] \nopagebreak[n]
```


---

### 章节和目录

- 命令 `\chapter` 只在 report 和 book 文档类有定义
- article 文档类带编号的层级为 `\section`、`\subsection`、`\subsubsection` 三级
- report 和 book 文档类带编号的层级为 `\chapter`、`\section`、`\subsection` 三级
- article 文档类的 section 标题默认左对齐，ctexart 文档类的 section 标题默认居中，article 文档类 + ctex 宏包的 section 标题是左对齐的
- 正确生成目录项，一般需要编译两次源代码

```latex
\chapter
\section
\subsection
\subsubsection

% 定制章节标题的样式
\usepackge{titlesec}

\tableofcontents

\renewcommand{\contentsname}{目录}

% 定制目录的样式
\usepackge{titletoc}
```


---

### 标题页

- `\title` 和 `\author` 必需（不用 `\title` 会报错；不用 `\author` 会警告），`\date` 若省略或 `\date{\today}` 会生成当天日期，`\date{}` 不显示日期

- 在 `\title`、`\author` 等命令内可以使用 `\thanks` 命令生成标题页的脚注，用 `\and` 隔开多个人名

- `\title`、`\author`、`\date` 可放在导言区或正文

- article 文档类的标题默认不单独成页，book 和 report 文档类默认单独成页；可在 `\documentclass` 命令调用文档类时指定 `titlepage` 或 `notitlepage` 选项以修改默认的行为

- titlepage 环境，生成不带页眉页脚的一页；生成自定义的标题页以替代 `\maketitle` 命令

```latex
\title  \author  \date
\date{\today}  \date{}

\maketitle
```


---

### 引用与参考文献

- 参考文献由文献数据库（即 `.bib` 文件，条目会包含 key，用于引用）生成
- 注意特殊符号、公式等常常需要人工检查
- 需多次编译，推荐 latexmk

- 传统方法：BibTeX 后端（gbt7714 宏包）

```latex
\bibliographystyle{<style>}  % 指定样式
\renewcommand{\bibname}{参考文献}

\cite{key1, key2}            % 引用文献
\nocite{}                    % 列出未引用的文献 
\nocite{*}                   % 列出所有未被引用的文献

\bibliography{bibfile}       % 打印参考文献列表
```

- 现代方法：biber 后端 + biblatex 宏包（国家标准：biblatex-gb7714-2015 宏包）

- biblatex 宏包：支持以 `key=value` 形式指定选项，包括参考文献样式 style、参考文献著录排序的规则 sorting
	- biblatex 使用的参考文献样式分为著录样式（bibliography style）和引用样式（citation style），分别以 `.bbx` 和 `.cbx` 为扩展名。参考文献的样式在调用宏包时使用 style 选项指定，或者使用 bibstyle 或 citestyle 分别指定

```tex
% 参考文献相关设置
\usepackage[
    backend       = biber,
    defernumbers  = true,
    sorting       = ymdnt,          % Year in descending order
    sorting       = ynt,            % Year in ascending order
    maxbibnames   = 3,              % No. of listed names
    style         = gb7714-2015,
    citestyle     = numeric-comp,
    isbn          = false,          % controls whether the fields isbn/issn/isrn are printed
    block         = par,
    doi           = false,          % do not show doi
	url           = false,
	eprint        = false,
    giveninits    = false,
]{biblatex}
\renewcommand*{\bibfont}{\small}
\setlength{\bibitemsep}{0pt}
\addbibresource{refs.bib}  % 需要加文件名后缀


\cite{key1, key2}   % 默认引用参考文献条目 
\upcite             % 右上角引用格式 
\nocite             % 列出未引用的参考文献 

\citeauthor  \citeyear  \textcite   \footcite
\supercite   \parencite 

% 打印参考文献列表
\printbibliography
\printbibliography[heading=bibintoc]
```

- natbib 宏包：可以生成用人名——年份的引用方式

```latex
% 连续引用多篇文献时，会生成形如 (3–7) 的引用
\usepackage[numbers,sort&compress]{natbib}

\citep{}
\citet{}
```


---

### 列表

- 无序列表，有序列表

```latex
\begin{itemize}
    ...
\end{itemize}
```

---

### 图片

WIP...

```latex
\usepackage{graphicx}
% 指定图片目录
\graphicspath{{figures/}}
% 指定图片扩展名
\DeclareGraphicsExtensions{.pdf,.eps,.png,.jpg,.jpeg}
```

---

### 表格

- LaTeX 表格生成（可生成三线表）：[Create LaTeX tables online](https://www.tablesgenerator.com/)

```latex
\begin{tabular}
    ...
\end{tabular}
```

- 三线表：`booktabs` 宏包

```tex
\usepackage{booktabs}

% 三线表
\begin{tabular}{ccc}  
\toprule        % 表格头部粗线  
姓名& 学号& 性别 \\  
\midrule        % 表格中横线  
1 &2 &3 \\  
4 &5 &6 \\  
\bottomrule     % 表格底部粗线  
\end{tabular}  
```

- 斜线表：`diagbox` 宏包；[CTAN: Package diagbox](https://ctan.org/pkg/diagbox/)

```tex
\usepackage{diagbox}

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
```


---

### 浮动体

- 图片和表格有时会很大，在插入的位置不一定放得下，因此需要浮动调整；两类浮动体环境 figure 和 table
- 避免在文中使用「下图」、「上图」的说法，而是使用图表的编号，如：图 `~\ref{fig:fig1}`
- `h` 当前位置 (here)，`t` 顶部 (top)，`b` 底部 (bottom)，`p` 单独成页 (p)。LaTeX 的默认参数是 tbp。
- `!h` 表示忽略一些限制，H 表示强制（强烈不建议）
- 图标题一般在下方，表标题一般在上方，即 `\caption{...}` 应放在 `\begin{tabular}` 前
- `\label` 需写在 `\caption` 后面，否则交叉引用会出现问题
- 可通过修改 `\figurename` 和 `\tablename` 的内容来修改标题的前缀，标题样式的定制功能由 caption 宏包提供
- table 和 figure 两种浮动体分别有各自的生成目录的命令：`\listoftables` 和 `\listoffigures`


```latex
\label{name}     % 添加标签：图片、表格、公式、章节等
\label{eq:name}  % 有意义的标签
```

```latex
\begin{table}[!htbp]
   ...
\end{table}

\begin{figure}[!htbp]
   ...
\end{figure}

% 修改标题的前缀
\renewcommand{\tablename}{newname}
\renewcommand{\figurename}{newname}
```


---

### 页面设置

页边距：geometry 宏包

通过 geometry 宏包设置的纸张大小是输出 PDF 文件的真实大小，而在文档类选项中设置的参数实际上只影响输出区域。

 LaTeX 默认将页面内容在垂直方向分散对齐。

```latex
% geometry-settings 多以 key = value 的形式组织
% 方式 1
\usepackage{geometry}
\geometry{geometry-settings}
% 方式 2
\usepackage[geometry-settings]{geometry}

% Microsoft Word 习惯的页面设定：A4 纸张，上下边距 1 英寸，左右边距 1.25英寸
% 方式 1
\geometry{a4paper,left=1.25in,right=1.25in,top=1in,bottom=1in}
% 方式 2
\geometry{a4paper,hmargin=1.25in,vmargin=1in}

% 书籍等双面文档，习惯上奇数页右边、偶数页左边留出较大的页边距，而靠近书脊一侧的奇数页左边、偶数页右边页边距较小
\geometry{inner=1in,outer=1.25in}

\raggedbottom  % 页面在垂直方向向顶部对齐
\flushbottom   % 页面在垂直方向分散对齐
```





页眉页脚：fancyhdr 宏包，`\pagestyle`，将页眉页脚分为左中右三个部分，页眉页脚处的横线粗细可以定义，默认页眉为 0.4pt、页脚为 0pt

页码：`\pagenumbering` 命令，有 arabic，\[Rr\]oman，\[Aa\]lph 五种页码形式

```latex
% 页眉页脚设置
\usepackage{fancyhdr}
\pagestyle{fancy}
    \fancyhf{}  % 清空页眉页脚的设置
	\fancyhead[position]{}  % 设置页眉
	\fancyfoot[position]{}  % 设置页脚
    \lhead{}  % 分别设置页眉左中右内容
    \chead{}
    \rhead{}
    \lfoot{}  % 分别设置页脚左中右内容
    \cfoot{\thepage}
    \rfoot{}
\renewcommand{\headrulewidth}{0.4pt}  % 修改页眉横线宽度
\renewcommand{\footrulewidth}{0pt}    % 去掉页脚横线
```


---

### 公式

>[LaTeX Math Wikibook](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

amsmath 允许用户在导言区用 `\DeclareMathOperator` 定义自己的算符，其中带星号的命令定义带上下限的算符

```latex
\DeclareMathOperator{\diff}{d\!} % 定义微分运算符
```

---

#### 数学模式

- 空格不起作用；不能有空行
- 行内（inline）公式：`$...$`
- 行间（display 独显）公式：
	- 无编号：`\[...\]` 或 `equation*` 环境
	- 编号：`equation` 环境
	- 不要用 `$$...$$$`（为什么？）


---

#### 括号与定界符

- 基本括号：
	- `(...)`、`[...]`、`{...}`
	- 绝对值、范数：`|...|` 或 `\vert...\vert`、`\Vert...\Vert`
	- Dirac 符号：`\langle...\rangle`、`|...\rangle`
- 自动调节大小：`\left(...\right)`
- 手动调节大小：`\big`、`\Big`、`\bigg`、`\Bigg`；声明左中右，在命令后添加 `l`、`m` 或 `r`，如 `\bigl`

---

#### 符号与数学字体

- 符号
	- 最常用的额外字体包：amssymb

- 数学字体
	- 「Times New Roman」：newtxmath 宏包
	- 不要用 times 和 mathptmx 宏包
	- 加粗：使用 bm 宏包的 `\bm` 命令（`\mathbf` 只有直立的字母）

- 新方案：unicode-math 宏包

---

#### 多行公式

- `multline multline*` 多行公式，没有对齐操作，只给一个公式编号
- `gather gather*` 多个公式，可添加多个公式编号
- `align align*` 多个公式对齐，但只能对齐公式内部的一个部分
- `flalign flalign*` 多个公式对齐，可对公式内的多个部分
- `split` 分割公式

- 取消公式编号，在环境名加 `*` 即可实现

>`gathered` 和 `gather` 的区别是放在了一个 `minipage` 里，`aligned` 也是 `minipage` 的问题

```latex
\usepackage{amsmath,amssymb,amsfonts}  % 常用数学宏包

```

```latex
texdoc symbols % 查看符号表
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

### 字体

- 宏包：`fontspec`

```tex
% 字体样式
\textbf{bold} \textit{italic} \texttt{typewriter}
\textsf{sans serif} \textsc{Small Caps} \textsl{slanted}

% 字号
{\tiny tiny} {\scriptsize scriptsize} {\footnotesize footnotesize}
{\small small} {\normalsize normalsize} {\large large}
{\Large Large} {\LARGE LARGE} {\huge huge} {\Huge Huge}
```

```bash
# 查看已安装中英文字体 zh/en
fc-list :lang=zh
```

中英文字体设置

```latex
% 中文字体设置
\usepackage{xeCJK}
\setCJKmainfont{Source Han Sans SC}
\setCJKmainfont{Smiley Sans}

% 英文字体设置
\usepackage{fontspec}
\setmainfont{Times New Roman}  % 新罗马字体
\setmainfont{Tex Gyre Termes}  % 会报没有该字体的错
\setmainfont{PingFang SC}      % 苹方字体

% 检查字体是否存在；不存在则使用默认字体
\usepackage{fontspec}
\IfFontExistsTF{Times New Roman}{
  \setmainfont{Times New Roman}
}{
  \typeout{Times New Roman font not found. Using default font.}
}
```

- 解决 Tex Gyre Termes 字体报错问题：
	- 在当前项目路径下创建 tutgtermes.fd 和 texgyretermes.fontspec 文件
	- 参考：[texlive - How to install font Tex Gyre Termes - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/470456/how-to-install-font-tex-gyre-termes)


- NewComputerModern：[NewComputerModern 字体](https://mp.weixin.qq.com/s/McLeFYLOxygRoXyqDgdF7A)
- Linux Libertine（衬线体）：简历、公式字体优选；[Linux Libertine 字体介绍](https://mp.weixin.qq.com/s/Lr304vav4gy27sjKAlKf7g)

```latex
\usepackage{newcomputermodern}  % 会报错

\usepackage{libertine}
% 数学模式下使用 Linux Libertine
\usepackage[libertine]{newtxmath}
```


---

### 常用宏包

- 常用宏包简介：见 lshort-zh-cn.pdf 文件中附录 B.3 的内容

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407182134632.png)

- hyperref 宏包：超链接、引用，由于它经常与其他宏包冲突，一般把它放在导言区的最后

```latex
\usepackage{hyperref}
\hypersetup{
	pdftitle=...,            % PDF 标题
	pdfauthor=...,           % PDF 作者
	pdfsubject=...,          % PDF 主题 
	pdfborder={0 0 0},
	bookmarks=true,          % 显示书签
    bookmarksopen=true,      % 书签展开  
    bookmarksnumbered=true,  % 书签编号
    hidelinks=true,          % 隐藏链接方框
    colorlinks=true,
    urlcolor=...,            % 外部链接颜色
    linkcolor=...,           % 内部链接颜色
    citecolor=...,           % 文献引用颜色
    filecolor=...,
}
```

- xcolor 宏包：调用颜色

```latex
\usepackage{xcolor}

% 自定义颜色
\definecolor{keywordcolor}{RGB}{34,34,250}

% 文本颜色
{\color{color-name}{text}}
\textcolor{red!70}{百分之70红色}
```

- hologo 宏包：可以输出许多 $\TeX$ 家族标志

```latex
\usepackage{hologo}

% 大写 H 表示符号的首字母也大写
\hologo{XeLaTeX} \Hologo{BibTeX}
\providecommand{\XeTeX}{\hologo{XeTeX}}
\providecommand{\BibLaTeX}{\textsc{Bib}\LaTeX}

% LaTeX 标志
\TeX  \LaTeX \LaTeXe
```

- comment 宏包：用于将其中的文本视为注释，从而使这些文本不会在生成的文档中显示

```latex
\usepackage{comment}

\begin{comment}
    ...
\end{comment}
```

- lipsum、zhlipsum 宏包：生成随机的英文、中文文本，主要用途是填充文档以便测试文档的版面布局

```latex
\usepackage{lipsum}
\usepackage{zhlipsum}

\lipsum        % 插入默认的第一段到第七段的 Lorem Ipsum 文本
\lipsum[2-4]   % 第 2-4 段
```

- tcolorbox 宏包：创建彩色盒子

```latex
\usepackage{tcolorbox}

% 接受一串 key-value 的参数列表
\begin{tcolorbox}[
title=..., % 盒子标题
colframe=...,
colback=...,
...
]
    \tcblower  % 增加了一条虚线，将盒子内容分成了上下两部分
    ...
\end{tcolorbox}
```


```latex
% 文字、公式和符号
amsmath       % AMS数学公式扩展
mathtools     % 数学公式扩展宏包，提供了公式编号定制和更多的符号、矩阵等
amsfonts      % AMS 扩展符号的基础字体支持
amssymb       % 在 amsfonts 基础上将 AMS 扩展符号定义成命令
bm            % 提供将数学符号加粗的命令 \bm
unicode-math  % 使用 Unicode 数学字体
siunitx       % 以国际单位规范排版物理量的单位
mhchem        % 排版化学式和方程式

% 排版元素
ulem          % 提供排版可断行下划线的命令 \uline 以及其它装饰文字的命令
multicol      % 提供将内容自由分栏的 multicols 环境
multitoc      % 生成多栏排版的目录
minitoc       % 为章节生成独立的小目录
verbatim      % 对原始的 verbatim 环境的改善。提供了命令 \verbatiminput 调用源文件
fancyvrb      % 提供了代码排版环境 Verbatim 以及对版式的自定义
listings      % 提供了排版关键字高亮的代码环境 lstlisting 以及对版式的自定义。类似宏包有 minted 等
algorithmic   % 一个简单的实现算法排版的宏包。如果要生成浮动体的话，需要搭配 algorithm 宏包使用
algorithm2e   % 较为复杂的、可定制的算法排版宏包。类似宏包有 algorithmicx 等
amsthm        % 定制定理环境。类似宏包 theorem、ntheorem、thmtools 等

% 图表和浮动体
array         % 对表格列格式的扩展
booktabs      % 排版三线表
tabularx      % 提供 tabularx 环境排版定宽表格，支持自动计算宽度的 X 列格式
diagbox       % 排版斜线表头
longtable     % 提供排版跨页长表格的 longtable 环境
graphicx      % 支持插图
caption       % 控制浮动体标题的格式。类似宏包有 keyfloat 等
subcaption    % 提供子图表和子标题的排版。类似宏包有 subfigure 和subfig 等
float         % 为浮动体提供不浮动的 H 模式；提供自定义浮动体结构的功能

% 修改版式
geometry      % 修改页面尺寸、页边距、页眉页脚等参数
fancyhdr      % 修改页眉页脚格式，令页眉页脚可以左对齐、居中、右对齐
titlesec      % 修改章节标题 \chapter、\section 等的格式
titletoc      % 修改目录中各条目的格式。类似宏包有 tocloft 等
tocbibind     % 支持将目录、参考文献、索引本身写入目录项
```


---

### 抄录

- 抄录：指将键盘输入的字符（包括保留字符和空格）不经过 TeX 解释，直接输出到文档；默认字体是等宽字体
- 命令：`\verb` 后用两个同样的符号将抄录内容括住（不能是星号）
- 环境：`verbatim`
- `\verb` 以及 `verbatim` 环境很脆弱，不能隐式地用于自定义环境，也一般不能用作命令的参数。
	- 宏包 `verbatim` 提供了更多的抄录支持
	- 宏包 `fancyvrb` 提供 `\SaveVerb`, `\UseVerb` 命令，以及便于实现居中的 `BVerbatim` 环境（置于 `center` 环境内即可）
	- 宏包 `shortverb` 支持以一对符号代替 `\verb` 命令


```latex
% 抄录命令
\verb|\date \author \title|

% 抄录环境
\begin{verbatim}
    ...
\end{verbatim}
```


---

### 代码

一般使用 listings 或者 minted 宏包

```tex
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
```


---

### 排除错误

- 常见的 LaTeX 错误信息：见 lshort-zh-cn.pdf 文件中附录 B.1 的内容

```bash
! Undefined control sequences.
# 使用了未定义的命令。拼写错误是原因之一；
# 也有可能是没有调用某个宏包，但用了该宏包定义的命令。

! LaTeX Error: Can be used only in preamble.
# 由于将必须用于导言区的命令在 \begin{document} 之后使用而产生。
```


---

### 其他

- 文本上下标

```latex
% 不需要额外的宏包
\newcommand{\tsub}[1]{\textsubscript{#1}}
\newcommand{\tsuper}[1]{\textsuperscript{#1}}
```

---

```latex
\documentclass[options]{...} % 这里其中options可以有 Font size、Paper size、Page Formats、sides与openany等.  
```

`\pagenumbering` 默认参数是阿拉伯数字
>arabic: 阿拉伯数字；roman: 小写罗马数字；Roman: 大写罗马数字；alpha: 小写英文字母 ；Alpha: 大写英文字母


假设在前言部分采用罗马数字，在剩余的正文部分用阿拉伯数字，则在前言部分使用命令 `\pagestyle{roman}`，随后在新的章节后面采用 `\chapter{…}\pagenumbering{arabic}`，还可以在后面接 `\setcounter{page}{number}` 来设定起始页码.

```latex
\pagenumbering{arabic}\setcounter{page}{2}
```


```latex
% 附录部分的标题和编号设置
% 会报该命令弃用的错
\CTEXsetup[name={附录},number={\Alph{section}}]{appendix}

30$\,^{\circ}$ 三角形     % 角度

37$\,^{\circ}\mathrm{C}$ % 摄氏度
```

LaTeX 默认在 `\chapter`、`\section` 等章节标题命令之后的第一段不缩进（和 Typst 一样）；ctex 宏包和文档类默认按照中文习惯保持标题后第一段的首行缩进

```latex
\textgreat  \textless  % 大于号，小于号

% 弹性长度
12pt plus 2pt minus 3pt % 表示基础长度为 12pt，可以伸展到 14pt，也可以收缩到 9pt

\\[6pt]  \\*[6pt]  % 在段落内的两行之间增加垂直间距
```


---

## 进阶

### 自定义命令

- 自定义命令使用 `\name{arg1}{arg2}` 来调用

- LaTeX 不允许使用 `\newcommand` 定义一个与现有命令重名的命令。如果需要修改命令定义的话，使用 `\renewcommand` 命令，其语法与 `\newcommand` 相同。

- 带星号的命令称为短命令，其中参数不能有换段或空行，否则编译报错，但是短命令有利排错

- 在命令中如果包含数学命令，那么这条命令只能⽤于⽂本模式，不能⽤于数学模式（因为在数学模式中会被多加了⼀层 `$ $` 导致报错）。所以，在定义数学命令时，使⽤ `\ensuremath{code}` 来定义，这样的命令在数学模式中时 code 本⾝，在⽂本模式中时 `$ code $`。

```latex
% 定义新命令
\newcommand{name}[num]{def}
\newcommand*{name}[num]{def}

% name - 带反斜线，必须符合命名规则
% num - 命令参数数量，最多 9 个，默认为 0，即不带任何参数
% def - 命令具体定义，涉及到参数时使用 `#n` 表示第 n 个参数。

% 修改已有命令
\renewcommand{name}[num]{def}
\renewcommand*{name}[num]{def}

% 命令未定义时，相当于 \newcommand；命令已定义时，沿用已有定义
\providecommand{name}[num]{def}

% 在常宏包和类文件的开发中
% \DeclareRobustCommand 与 name 间可以不用花括号
\DeclareRobustCommand{name}[num]{def}


% https://github.com/0382/util/blob/main/latex/physics.tex
% 摄氏度
\newcommand{\celsius}{\mathrm{^o\! C}}

% 量子力学 bra ket 符号
\newcommand{\bra}[1]{\langle{#1}|}
\newcommand{\ket}[1]{|{#1}\rangle}
\newcommand{\braket}[2]{\langle{#1}|{#2}\rangle}

% 尖括号平均值
\newcommand{\anglemean}[1]{\langle{#1}\rangle}

% 实数虚数
\renewcommand{\Re}[1]{\mathfrak{Re}(#1)}
\renewcommand{\Im}[1]{\mathfrak{Im}(#1)}

% 三种矩阵简写
\newcommand{\pmat}[1]{\begin{pmatrix}#1\end{pmatrix}}
\newcommand{\bmat}[1]{\begin{bmatrix}#1\end{bmatrix}}
\newcommand{\Bmat}[1]{\begin{Bmatrix}#1\end{Bmatrix}}

% 绝对值和范数
\newcommand{\abs}[1]{\vert #1 \vert}
\newcommand{\norm}[1]{\Vert #1 \Vert}
```


---

### 自定义宏包/文档类

- 门槛较高

- 如果定义了很多新的环境和命令，文档的导言区将变得很长，在这种情况下，可以建立一个新的 LaTeX 宏包来存放所有你自己定义的命令和环境，然后在文档中使用 `\usepackage` 命令来调用自定义的宏包。

- 写一个宏包的基本工作就是将原本在你的文档导言区里很长的内容拷贝到另一个文件中去，这个文件需要以 `.sty` 作扩展名。你还需要加入一个宏包专用的命令

- 在宏包中调用其它宏包：LaTeX 允许你在自己编写的宏包中调用其它宏包

- 自定义文档类：以 `.cls` 作扩展名，可以像调用宏包那样调用一个基本的文档类

```latex
% 该命令应该放在你的宏包的最前面
% package-name 需要和宏包的文件名一致
\ProvidesPackage{package-name}

\RequirePackage[...]{package-name}

\ProvidesClass{class-name}

\RequireClass[...]{class-name}
```


写宏包

- [https://github.com/ustctug/ustcthesis/wiki/参与开发](https://github.com/ustctug/ustcthesis/wiki/%E5%8F%82%E4%B8%8E%E5%BC%80%E5%8F%91)
- [document.tex](https://github.com/Meiting-Wang/Article-template/blob/main/document.tex)


自定义 sty 文件：[mystyle.sty](https://github.com/singularitti/PHYS6080-PS1/blob/main/tex/mystyle.sty)


---

### LaTeX 可定制的一些命令和参数

- 标题名称/前后缀：可以用 `\renewcommand` 来修改
	- 使用 ctex 宏包或文档类时，表中的标题会修改为中文标题
- 长度：可用 `\setlength` 来修改

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407191919074.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407191921567.png)



---

## 模板

- 作业模板（较为简洁）：[hw1.tex](https://raw.githubusercontent.com/OrangeX4/NJUAI-Notes/master/%E4%BC%98%E5%8C%96%E6%96%B9%E6%B3%95/Homework/hw1.tex)
- [上海交通大学 Beamer 模版](https://github.com/sjtug/SJTUBeamer)
- [上海交通大学 LaTeX 论文模板](https://github.com/sjtug/SJTUThesis)
- [GitHub - ElegantLaTeX/ElegantPaper](https://github.com/ElegantLaTeX/ElegantPaper)
- [GitHub - ElegantLaTeX/ElegantBook](https://github.com/ElegantLaTeX/ElegantBook)
- cls 文档类文件内容注释很详细：[GitHub - CheckBoxStudio/BUAAThesis: 北航研究生学位论文模板（Word+LaTeX）.](https://github.com/CheckBoxStudio/BUAAThesis)

- 简历
	- [GitHub - jankapunkt/latexcv: :necktie: A collection of cv and resume templates written in LaTeX. Leave an issue if your language is not supported!](https://github.com/jankapunkt/latexcv)
	- 用的是 tectonic 引擎：[GitHub - philipempl/modern-latex-cv: A professional and modern CV in LaTex](https://github.com/philipempl/modern-latex-cv)
	- [GitHub - AntObi/academicCV: LaTeX template for academic CV](https://github.com/AntObi/academicCV)
	- [GitHub - sinaatalay/rendercv: LaTeX CV generator from a YAML/JSON input file.](https://github.com/sinaatalay/rendercv)
	- 部分格式可作为参考将其转换成 Typst 写法：[GitHub - Troublor/curriculum-vitae: My Curriculum Vitae (CV)](https://github.com/Troublor/curriculum-vitae)

- 国自然基金 LaTeX 模板：
	- [GitHub - Ruzim/NSFC-application-template-latex: 国家自然科学基金申请书正文（面上项目）LaTeX 模板（非官方）](https://github.com/Ruzim/NSFC-application-template-latex)
	- 青基：[GitHub - QijingZheng/QZ\_ExcellentYoungScientistsFund\_2024](https://github.com/QijingZheng/QZ_ExcellentYoungScientistsFund_2024)
	- [NSFC - overleaf 版](https://www.overleaf.com/project/6372028b9049e7ce5ea603fc)




---

## 问题

- 下划线 `\newcommand` 及粗细设置
	- [underline - Why does \\uline sometimes render thicker and darker (inconsistent with underlining in the rest of the text)? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/537907/why-does-uline-sometimes-render-thicker-and-darker-inconsistent-with-underlini)
	- [Fixing the length of underline text - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/482835/fixing-the-length-of-underline-text)

- 去除超链接、交叉引用中的方框：[hyperref - Remove ugly borders around clickable cross-references and hyperlinks - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/823/remove-ugly-borders-around-clickable-cross-references-and-hyperlinks)

- [ ] LaTeX 如何在每个章节最后生成参考文献？


---

```latex
% 使参考文献字符居中
\titleformat{\section}{\centering\Large\bfseries}{\thesection}{1em}{}

% 添加 "附录" 字符
% 该操作并不能使目录中也添加 "附录" 字符
\titleformat{\section}{\centering\Large\bfseries}{附录~\Alph{section}}{1em}{}

% 使 section 标题左对齐
\titleformat{\section}{\raggedright\Large\bfseries}{\thesection}{1em}{}
```

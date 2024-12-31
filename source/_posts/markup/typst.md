---
title: Typst 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Typst 使用
description: Typst 使用
tags:
  - Typst
categories:
  - 排版语言
date: 2023-10-29 10:30:00
abbrlink: 337619
password:
---

# Typst 使用

## 介绍

- Typst 是一门用于文档排版的标记语言

- Typst 优势：语法简单、编译速度快（毫秒级别）、环境搭建简单，详细使用体验，参见：[Typst 中文用户使用体验 - OrangeX4 - 知乎](https://www.zhihu.com/question/591143170/answer/3304601296)


```rust
// 页脚设置
// 方式 1
#set page(numbering: "1/1")

// 方式 2
#set page(
  footer: context {
    set align(center)
    set text(9pt)
    counter(page).display()
  }
)
```


---

### 参考资料

- 官方 Doc：[Typst Documentation](https://typst.app/docs)

- [Changelog – Typst Documentation](https://staging.typst.app/docs/changelog/)
    - 0.12 版本更新内容：
        - 设置每行的行号（论文写作中有用）
        - layout 布局增强
        - Typst 命令行增强

- 实用：
    - [Typst 中文用户使用体验 - OrangeX4 - 知乎](https://www.zhihu.com/question/591143170/answer/3304601296)
    - Typst 示例：[Typst Examples Book](https://sitandr.github.io/typst-examples-book/book)
    - [GitHub - OrangeX4/typst-talk: 并不复杂的 Typst 讲座 Typst is Simple](https://github.com/OrangeX4/typst-talk)
    - [GitHub - typst-doc-cn/tutorial: Typst中文教程](https://github.com/typst-doc-cn/tutorial)
    - [The Raindrop-Blue Book (Typst中文教程) - 网页版](https://typst-doc-cn.github.io/tutorial/)
    - [GitHub - qjcg/awesome-typst: Awesome Typst Links](https://github.com/qjcg/awesome-typst)
    - [GitHub - typst-cn/awesome-typst-cn: Awesome Typst 列表中文版](https://github.com/typst-cn/awesome-typst-cn)

- Typst 讨论（较活跃）：[typst/typst · Discussions · GitHub](https://github.com/typst/typst/discussions)

- [Typst Forum](https://forum.typst.app/)

- [LaTeX 用户指南 – Typst 中文文档](https://typst-doc-cn.github.io/docs/guides/guide-for-latex-users/)

- [Typst 中文社区](https://typst.cn/#/)



---

## 安装

- 二进制文件： [Releases · typst/typst](https://github.com/typst/typst/releases)

- 包管理器：

```bash
brew install typst         # macOS
scoop install main/typst   # Windows
```

- 在线编辑器：[Web - Typst](https://typst.app/)

- Mac 端 Typst 编辑器（还在开发中）：[Textique](https://textique.app/)

- iPad 端 Typst 编辑器：[GitHub - iXORTech/Typstify: A Typst Editor for iPad](https://github.com/iXORTech/Typstify)



---

## 使用

### 工具

- VSCode 插件：
    - Typst LSP：具有语言服务器 + 代码格式化（不再继承）等功能
    - Tinymist Typst：语法高亮，代码补全，代码格式化，即时预览、单词统计等功能
    - 两者不兼容：[Faitl to activate typst-lsp: command 'typst-lsp.pinMainToCurrent' already exists · Issue #513 · nvarner/typst-lsp · GitHub](https://github.com/nvarner/typst-lsp/issues/513)
    - Tinymist 查看实时更新编译的预览 PDF：点击窗口 + 放大镜的图标（而非 PDF 的图标），源码和 PDF 可互相跳转
    - 导出 PDF 设置：设置 'Tinymist Export PDF' 为 'onSave' 或 'onType'

- [typst-upgrade](https://github.com/Coekjan/typst-upgrade)：检查并升级 Typst packages

```bash
cargo install typst-upgrade  # 安装

# file.typ 可改成 .
typst-upgrade file.typ       # 更新 packages 并覆写文件
# 参数
-d                           # --dry-run 不实际运行
```

- 代码格式化：
    - [GitHub - astrale-sharp/typstfmt](https://github.com/astrale-sharp/typstfmt)（效果感觉一般）
    - [GitHub - Enter-tainer/typstyle: Beautiful and reliable typst code formatter](https://github.com/Enter-tainer/typstyle)
    - [GitHub - antonWetzel/prettypst: Formatter for Typst](https://github.com/antonWetzel/prettypst)

- Jupyter Notebook 转 Typst pdf：[GitHub - 8LWXpg/jupyter2typst: Jupyter to Typst converter with template support](https://github.com/8LWXpg/jupyter2typst)

- 将文献标题超链接化：[GitHub - alexanderkoller/typst-blinky: Creates bibliographies in Typst with URL/DOI links](https://github.com/alexanderkoller/typst-blinky)

- 数学公式 OCR：[GitHub - ParaN3xus/typress: Typst Mathematical Expression OCR](https://github.com/ParaN3xus/typress)

- 预览 Typst 的 Neovim 插件：[GitHub - chomosuke/typst-preview.nvim: Low latency typst preview for Neovim](https://github.com/chomosuke/typst-preview.nvim)

- 将 Typst 公式渲染成 svg 或 png：[GitHub - xingjian-zhang/typst2img: A fast script to render your Typst formulas to svg and png. Integrate formulas to your slides in seconds!](https://github.com/xingjian-zhang/typst2img/?tab=readme-ov-file)

- [GitHub - Thumuss/utpm: A package manager for typst](https://github.com/Thumuss/utpm)

- [GitHub - mkpoli/tyler: Typst package (libraries, templates) publishing utilty CLI tool](https://github.com/mkpoli/tyler)

- [GitHub - frozolotl/muchpdf: Include PDF images in your Typst document](https://github.com/frozolotl/muchpdf)


---

### 命令

```bash
# 编译
typst compile file.typ  # 或 typst c

# 跟踪文档实时编译
typst watch file.typ    # 或 typst w

# 指定字体搜索路径
typst compile file.typ --font-path path/to/fonts

# 列出系统和给定目录中发现的所有字体
typst fonts --font-path path/to/fonts

# 设置字体环境变量
TYPST_FONT_PATHS=path/to/fonts typst fonts

# 指定 project 路径
typst compile file.typ --root ..

# 更新 typst 版本
typst update
```


---

函数定义及使用


---

命令影响范围

`#text(weight: "bold")[bold text]` 将只对其参数加粗， 而 `#set text(weight: "bold")` 将对当前块或直到文件结尾之前的所有文本加粗。



---

### 基础

- 基础语法概览：[Syntax – Typst Documentation](https://typst.app/docs/reference/syntax/)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405081110856.png)



![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405081110728.png)


三种语法模式：标记、数学和脚本

Typst 为常用文档元素内置了语法标记，大多只是对应函数的快捷表达方式

**标记模式**：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405081112457.png)


---

**数学模式**：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405081113305.png)

---

**脚本模式**：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405081114713.png)


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405081114195.png)


---

- 图片插入及引用：figure 及 image 函数
    - image 函数支持的图片格式：png、jpg、gif、svg，不支持 tiff
    - 不支持根目录的绝对路径？

```rust
@fig  // 图片引用

#figure(
   image("fig.png"),
   caption: [ Caption ],
) <fig>
```


```rust
// 多图排列
#figure(
  grid(
    columns: 2,
    row-gutter: 2mm,
    column-gutter: 1mm,
    image("assets/Nb5Si3_1.png"), image("assets/Nb5Si3_1.png"), 
    image("assets/Nb5Si3_3.png"), image("assets/Nb5Si3_4.png"), 
  ),
  caption: "Caption"
) <Nb5Si3_plot>
```



---

- [x] 强调和加粗对中文字体不起作用（可使用 cuti 包）
- 有序列表无法使用 markdown 的 `1. ` 格式

- 换行与转义（Escaping）：使用 `\`

- 目录

```rust
#outline()
```

- 注释

```rust
// 单行注释

/*
多行注释
多行注释
*/
```

- 内联代码与代码块：和 markdown 一样，编程语言改成 `typ`

- 参考文献及引用

```rust
// 方式 1
@ZHU2023119062

// 方式 2
#cite(<ZHU2023119062>) \
#cite(<ZHU2023119062>, form: "prose") \
#cite(label("ZHU2023119062"))

#bibliography(
  "refs.bib",
  title: "参考文献",
  style: "gb-7714-2015-numeric",
  // style: "american-physics-society",
  // style: "nature",
)
```

- 参考文献 style 推荐：
    - `gb-7714-2015-numeric`（**暂无自定义不显示参考文献特定内容，如 doi 的功能，BibTeX 可以**）
    - `american-physics-society`
    - `nature`
    - `ieee`
    - `american-chemical-society`

---

### 字体

```rust
// reference: https://github.com/lucifer1004/pkuthss-typst/blob/main/template.typ
#let 字号 = (
  初号: 42pt,
  小初: 36pt,
  一号: 26pt,
  小一: 24pt,
  二号: 22pt,
  小二: 18pt,
  三号: 16pt,
  小三: 15pt,
  四号: 14pt,
  中四: 13pt,
  小四: 12pt,
  五号: 10.5pt,
  小五: 9pt,
  六号: 7.5pt,
  小六: 6.5pt,
  七号: 5.5pt,
  小七: 5pt,
)

#let 字体 = (
  仿宋: ("Times New Roman", "FangSong"),
  宋体: ("Times New Roman", "SimSun"),
  黑体: ("Times New Roman", "SimHei"),
  楷体: ("Times New Roman", "KaiTi"),
  代码: ("New Computer Modern Mono", "Times New Roman", "SimSun"),
  得意黑: ("Smiley Sans",),
)


// https://github.com/OrangeX4/Chinese-Resume-in-Typst/blob/main/template.typ
#let font = (
  main: "IBM Plex Serif",
  mono: "IBM Plex Mono",
  cjk: "Noto Serif CJK SC",
)

set text(font: (font.main, font.cjk), size: 10pt, lang: "zh")
```

字体 stroke 指字体的描边，含描边颜色、宽度、线条样式和透明度

TeX Gyre Termes：基于 Times Roman 的衬线字体，Noto Serif CJK SC：专为简体中文设计的衬线字体

1em：quad，相对单位；定义为当前字体大小的宽度；常用场景：缩进，段落、表格间距

1ex：相对单位，等于当前字体中小写字母 `x` 的高度；常用于垂直方向上的间距调整

1pt：point，绝对单位；在 TeX 系统中，1pt = 1/72.27 英寸（大约 0.35146 毫米）；常用场景：字体大小，精确间距，线条和边框

Word 中的字符度量单位：1 磅值 = 1/72 in = 1bp = 1.00375 pt

>[浅谈LaTeX与Word度量单位对应关系\_letex和word页边距转换-CSDN博客](https://blog.csdn.net/Null_0_lluN/article/details/107097236)


smartquote（智能引号）：根据文本语言（英、德、法语等）自动选择适当的开闭引号形式

smallcaps(small capitals)：小型大写字母的字体格式，小写字母以小号的大写字母形式显示，但与真正的大写字母相比，它们的尺寸稍微小一些；LaTeX 对应命令为 `\textsc{}`


---

对齐 `align` 函数
可选参数值：start、end、left、right、center、top、horizon、bottom
可以使用两个参数值，用 `+`

```rust
#set align(center + horizon)  // 在表格中，位于单元格中心位置
```


direction

```text
ltr: Left to right.
rtl: Right to left.
ttb: Top to bottom.
btt: Bottom to top.
```



```rust
fr // 分数
h() // 水平间距
v() // 垂直间距

// 水平或垂直排列内容和间距
stack()

//网格
grid()

// 段落
par()

// 容器
block()

// 表格
table()

pagebreak()

// 文本对齐
align()

// 页面
page()

rect()
// 线条
#line()

// 盒子
box()

// 文本上下标
#sub[]    // 下标
#super[]  // 上标
```

---

- 用法

```rust
// 当天日期
#datetime.today().display("[year]年[month]月[day]日")

// reference: https://typst.app/project/rI2NZaeIAMwgmyBXnz6tdF
#set par(
  justify: true,
  first-line-indent: 2em,  // 首行缩进
  leading: 20pt,   // 行距 20 磅
)

#show par: set block(spacing: 20pt) // 段间距 20 磅

#set text(
  // 正文小四号字，英文用 Times Roman，中文用宋体
  size: 12pt,
  font: (
    "TeX Gyre Termes", 
    "Noto Serif CJK SC",
  ),
  lang: "zh"
)
```


---

### 表格

```rust
#table()


// 导入 cell header，可单独控制其对齐方式
#import table: cell, header
```


---

### 数学公式

- 公式中的文本：若涉及到 typst 中的关键字，可以用 `""` 包裹文本
- 数学公式设置：等式：`#set math.equation()`；矩阵：`#set math.mat()`
- 与 LaTeX 不同，symbols 前不需加 `\`
- 分数：`1/2` 或 `frac(a, b)`
- root 根：平方根：`sqrt(2)`，非平方根：`root(N, x)`
- 分隔符匹配：分隔符大小与内容保持一致，类似 LaTeX 中的 `\left`、`\right`；`lr()`、`mid()`、`abs()`、`ceil()`、`floor()`、`round()`、`norm()`
- 向量：`vec()`，矩阵：`mat()`
- 箭头：`arrow()`
- 上、下划线：`underline()`、`overline()`、`underbrace()`、`overbrace()`
- [Typst 符号 General Symbols](https://typst.app/docs/reference/symbols/sym/)

- 数学字体中的替换字体：[Variants Functions – Typst Documentation](https://typst.app/docs/reference/math/variants/)


```rust
// 设置 math 字体
#show math.equation: set text(font: "Times New Roman")
// 设置 code 字体
#show raw: set text(font: "Fira Code")

// 数学公式编号，在引用的编号之前添加 supplement 内容
#set math.equation(numbering: "(1)", supplement: [Eq.])

// 行内公式 公式与 $$ 之间无空格
$Q = rho A v + C$

// 行间公式 公式与 $$ 之间有空格 <eq1> 公式标签
$ 7.32 beta + sum_(i=0)^nabla Q_i / 2 $ <eq1>

@eq1                   // 公式引用

lr()                   // 分隔符匹配
mid()
abs()
norm()
floor()
ceil()
round()

vec()                 // 向量

// 矩阵
$
mat(
    1, 2, ..., 10;
    2, 2, ..., 10;
    dots.v, dots.v, dots.down, dots.v;
    10, 10, ..., 10; // `;` in the end is optional
)
$
```



---

### Set 规则

Set 规则可以设置样式，为函数设置参数默认值


Set 规则中常用的一些函数的列表：

- [`text`](https://typst-doc-cn.github.io/docs/reference/text/text/) 用于设置文本的字体、大小、颜色和其他属性
- [`page`](https://typst-doc-cn.github.io/docs/reference/layout/page/) 用于设置页面大小、边距、页眉、启用栏和页脚
- [`par`](https://typst-doc-cn.github.io/docs/reference/layout/par/) 用于对齐段落、设置行距等
- [`heading`](https://typst-doc-cn.github.io/docs/reference/meta/heading/) 用于设置标题的外观与启用编号
- [`document`](https://typst-doc-cn.github.io/docs/reference/meta/document/) 用于设置 PDF 输出中包含的元数据，例如标题和作者


```rust
#set text(font: "")
```


---

### Show 规则

Show 规则用于全局替换

```rust
#show
```

---


代码块：Code block

内容块：Content block


---

### 函数

```rust
#let function(args) = {}
```


---

### 包管理

```rust
#include "file.typ"      // 导入子文件
```

- 包可以是 package，也可以是 template
- 已在官网上的 [packages](https://typst.app/universe)，以 `#import "@preview/pkg:1.0.0"` 格式导入，编译时会自动下载和自动导入 packages

```rust
#import "@preview/tablex:0.0.6": tablex, hlinex
```

- 未在官网上的，需下载模块源码，以相对路径形式导入（或等待其被官方接受）

```rust
#import "mdtable.typ": mdtable
```

---

#### 推荐 packages

- outline 目录：outrageous
- 绘图（类似 LaTeX 中的 PGF/TikZ）：cetz
- box 盒子（类似 LaTeX 中的 colorbox）
    - showybox
    - [GitHub - marc-thieme/frame-it](https://github.com/marc-thieme/frame-it)
- math 数学：physica
- table 表格：tablex、tablem
- code 代码：codly
- note 做笔记：drafting
- word count 字数统计：wordometer
- 图片排版：wrap-it（环绕效果）
- checklist：cheq
- 在 Typst 中使用 LaTeX 公式：MiTeX
- 中文伪粗体、伪斜体：cuti
- presentation 制作：[touying](https://github.com/touying-typ/touying)、[polylux](https://github.com/andreasKroepelin/polylux)
- 自动调整 content 尺寸：[GitHub - jdpieck/oasis-align: A Typst package to cleanly place content side by side with equal heights using automatic content sizing.](https://github.com/jdpieck/oasis-align)
- 表格中的科学计数格式化（小数点自动对齐）：[GitHub - Mc-Zen/zero: Advanced scientific number formatting for Typst.](https://github.com/Mc-Zen/zero)
- 生成 Typst package 的文档：[tidy](https://github.com/Mc-Zen/tidy)
- 使用 Font Awesome 图标：[GitHub - duskmoon314/typst-fontawesome](https://github.com/duskmoon314/typst-fontawesome)
- admonitions：[GitHub - jomaway/typst-gentle-clues: Simple admonishment for typst](https://github.com/jomaway/typst-gentle-clues)


---

### 其他

- Typst Logo：[fenjalien/Typst Logo](https://gist.github.com/fenjalien/1463a19ba2b91d061ed35e295494e0b3)

- 将 Typst Documentation 网页内容下载到本地：[Offline Documentation PDF? - Discord](https://discord.com/channels/1054443721975922748/1295417383938428998)

```text
wget --recursive --no-parent --convert-links https://typst.app/docs/
```



---

## 模板

- 简历 CV
    - [GitHub - gaoachao/uniquecv-typst: A simple resume template written in Typst](https://github.com/gaoachao/uniquecv-typst)
    - [GitHub - OrangeX4/Chinese-Resume-in-Typst: 使用 Typst 编写的中文简历, 语法简洁, 样式美观, 开箱即用, 可选是否显示照片](https://github.com/OrangeX4/Chinese-Resume-in-Typst)
    - [GitHub - memset0/my-resume](https://github.com/memset0/my-resume)（repo 现为 private 状态）
    - [GitHub - pavelzw/moderner-cv: moderncv in typst](https://github.com/pavelzw/moderner-cv)
    - [GitHub - stuxf/basic-typst-resume-template: A basic resume for typst, designed to work well with ATS systems.](https://github.com/stuxf/basic-typst-resume-template)
    - [GitHub - skyzh/chicv: A minimal and fully-customizable CV template for Typst.](https://github.com/skyzh/chicv)
    - [GitHub - DawnEver/typst-academic-cv: Typst Template for Academic CV](https://github.com/DawnEver/typst-academic-cv)

- 作业模板
    - [GitHub - gRox167/typst-assignment-template](https://github.com/gRox167/typst-assignment-template)
    - [GitHub - OriginCode/typst-homework-template: Homework Template for Typst](https://github.com/OriginCode/typst-homework-template)

- 试题模板（英文）：[GitHub - diquah/OpenBoard: Typst template and framework for creating professional and clean exams of any kind.](https://github.com/diquah/OpenBoard)

- 论文模板
    - [GitHub - lucifer1004/pkuthss-typst: Typst template for dissertations in Peking University (PKU).](https://github.com/lucifer1004/pkuthss-typst)
    - [GitHub - nju-lug/nju-thesis-typst: 南京大学学位论文 Typst 模板 nju-thesis-typst](https://github.com/nju-lug/nju-thesis-typst)
    - [GitHub - howardlau1999/sysu-thesis-typst: 中山大学学位论文 Typst 模板](https://github.com/howardlau1999/sysu-thesis-typst)
    - [简易上海交通大学学位论文 Typst 模板](https://typst.app/project/rI2NZaeIAMwgmyBXnz6tdF)
    - [GitHub - tzhTaylor/typst-sjtu-thesis-master: SJTU Master Thesis Typst Template](https://github.com/tzhTaylor/typst-sjtu-thesis-master/)
    - 机器学习领域的系列论文模板：[GitHub - daskol/typst-templates: A list of paper templates in the area of machine learning.](https://github.com/daskol/typst-templates)

- Typst 文档编译 Github Actions：
    - [build.yml](https://github.com/howardlau1999/sysu-thesis-typst/blob/master/.github/workflows/build.yml)
    - [GitHub - lvignoli/typst-action: Typst GitHub action](https://github.com/lvignoli/typst-action)

- 论文海报 poster：
    - [Kevin Bonham, PhD / bbm-poster-2024 · GitLab](https://gitlab.com/kescobo/bbm-poster-2024/)
    - [GitHub - pncnmnp/typst-poster: An academic poster template for Typst](https://github.com/pncnmnp/typst-poster)

- Elsevier 期刊模板
    - 预印版：
        - [GitHub - maucejo/elsearticle](https://github.com/maucejo/elsearticle)
        - [elsarticle preprint - Typst.app](https://typst.app/project/rFAXkf0lxIp1Paj1l-gKTr)
    - 正式出版：[elsarticle formal - Typst.app](https://typst.app/project/rrn_CcZC2mSFvKWd9vuVgT)

- 创建 Online Books：[GitHub - Myriad-Dreamin/shiroa: shiroa is a simple tool for creating modern online books in pure typst.](https://github.com/Myriad-Dreamin/shiroa)

- 将 Typst 内容渲染成网页
    - [GitHub - Myriad-Dreamin/typst-book: A simple tool for creating modern online books in pure typst.](https://github.com/Myriad-Dreamin/typst-book/)



---

## 相关问题

- [x] 目前的大语言模型都没有学习 Typst 内容（Claude 3.5 pro、GPT-o1 有） ✅ 2024-10-19

- [ ] Typst 中暂无 latexdiff 替代工具

- [x] Mac 中的 VSCode Typst 相关插件无法处理相对路径情况，会报错；Windows 上的正常
    - 解决方法：在子目录下创建根目录模板文件的符号链接（暂时解决方法）

```rust
#import "../template.typ": *   // 报错
```

- [x] 标题后首段无法正确缩进：
    - [Behavior of first line indentation in paragraphs seems limiting · Issue #311 · typst/typst · GitHub](https://github.com/typst/typst/issues/311)
    - [首段无法自动缩进 · Issue #12 · shuosc/SHU-Bachelor-Thesis-Typst · GitHub](https://github.com/shuosc/SHU-Bachelor-Thesis-Typst/issues/12)

```rust
#set par(
  first-line-indent: 2em,
  justify: true,
)

// 解决标题后首段无法正确缩进问题
// 在标题后面添加空白段 使得首段不再是首段
#show heading: it => {
  it
  par(leading: 1.5em)[#text(size:0.0em)[#h(0.0em)]]
}
```

- [ ] 上述方法会出现：列表后的首个段落无法正常缩进


---

- [x] 中文目录设置

```rust
#import "@preview/outrageous:0.1.0"

// 目录设置
#let ChineseOutline() = {
  set align(center)
  set text(font: 字体.宋体, size: 字号.小四)
  set page(numbering: "I")
  counter(page).update(1)
  set par(
    justify: true,
    first-line-indent: 2em,
  )

  // 一级目录字体、间距设置
  show outline.entry.where(
    level: 1
  ): it => {
    set text(size: 字号.中四)
    v(2pt)
    strong(it)
  }

  // outrageous 目录设置
  show outline.entry: outrageous.show-entry.with(
    ..outrageous.presets.typst,
    fill: (none, auto),
  )

  outline(
    title: text("目录"), 
    indent: 1em,
  )

  pagebreak(weak: true)

}
```


- [ ] 自己电脑的中文字体在 Typst 已是加粗 bold 状态，如何恢复 regular

[GitHub - csimide/cuti: Cuti: A simple typst package simulates fake bold / fake italic characters. | Cuti：在 typst 中便捷使用伪粗体/伪斜体](https://github.com/csimide/cuti)

[Fake text weight and style (synthesized bold and italic) · Issue #394 · typst/typst · GitHub](https://github.com/typst/typst/issues/394)

[Skew transform · Issue #2749 · typst/typst · GitHub](https://github.com/typst/typst/issues/2749)

[Emphasis does not work for Chinese · Issue #725 · typst/typst · GitHub](https://github.com/typst/typst/issues/725)

[lexer change: Allow emphasis in CJK text without spaces by peng1999 · Pull Request #2648 · typst/typst · GitHub](https://github.com/typst/typst/pull/2648)

---


- [ ] 生成的 pdf 如何也有对应的编号（暂无法实现）：[Include numbering in PDF bookmark · Issue #2416 · typst/typst · GitHub](https://github.com/typst/typst/issues/2416)

- [ ] Typst 如何让公式中的单个字符不斜体

- [ ] 数学公式中的两个及以上字符如何使其斜体

- [ ] Typst page 函数中 margin 页边距参数如何使水平方向全部填充？

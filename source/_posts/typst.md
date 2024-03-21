---
title: typst 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: typst 使用
description: typst 使用
tags:
  - typst
categories:
  - 排版语言
date: 2023-10-29 10:30:00
abbrlink: 
password:
---

# typst 使用

## 介绍

WIP…


相关问题：

- [ ] 段落缩进问题：
- [Behavior of first line indentation in paragraphs seems limiting · Issue #311 · typst/typst · GitHub](https://github.com/typst/typst/issues/311)
- [首段无法自动缩进 · Issue #12 · shuosc/SHU-Bachelor-Thesis-Typst · GitHub](https://github.com/shuosc/SHU-Bachelor-Thesis-Typst/issues/12)



---

### 参考资料

官方 Doc：[Typst Documentation](https://typst.app/docs)

很有用：

- [Typst 中文用户使用体验 | OrangeX4's Blog](https://orangex4.cool/post/typst-for-chinese/)
- [About - Typst Examples Book](https://sitandr.github.io/typst-examples-book/book)

>[GitHub - OrangeX4/typst-talk: 并不复杂的 Typst 讲座 Typst is Simple](https://github.com/OrangeX4/typst-talk)

>[GitHub - typst-doc-cn/tutorial: Typst中文教程](https://github.com/typst-doc-cn/tutorial)

>[GitHub - qjcg/awesome-typst: Awesome Typst Links](https://github.com/qjcg/awesome-typst)

>[LaTeX 用户指南 – Typst 中文文档](https://typst-doc-cn.github.io/docs/guides/guide-for-latex-users/)

>[Typst 中文社区](https://typst.cn/#/)

>[GitHub - typst-cn/awesome-typst-cn: Awesome Typst 列表中文版](https://github.com/typst-cn/awesome-typst-cn)



---

## 安装

- 下载 [预构建二进制文件](https://github.com/typst/typst/releases)（pre-built binaries）
- 不同 Linux 发行版 + macOS(`brew install typst`) + Win(`scoop install main/typst`)



---

## 使用

VSCode 插件：

- typst-lsp，具有语言服务器 + 代码格式化等功能
- typst-preview：实时编译预览


- [ ] 暂无法指定图片路径，图片无法是链接的形式


---

### 相关命令

```bash
# 编译
typst compile file.typ  # typst c file.typ

# 跟踪文档实时编译
typst watch file.typ    # typst w file.typ

# 指定字体搜索路径
typst compile file.typ --font-path path/to/fonts

# 列出系统和给定目录中发现的所有字体
typst fonts --font-path path/to/fonts

# 设置字体环境变量
TYPST_FONT_PATHS=path/to/fonts typst fonts

# 更新版本
typst update
```


---

基础语法概览：[Syntax – Typst Documentation](https://typst.app/docs/reference/syntax/)


---

函数定义及使用



---

命令影响范围

`#text(weight: "bold")[bold text]` 将只对其参数加粗， 而 `#set text(weight: "bold")` 将对当前块或直到文件结尾之前的所有文本加粗。



---

### 模块导入

已在官网上的 packages（官网：[Packages – Typst Documentation](https://typst.app/docs/packages/)），可直接通过以下的形式导入，编译时，会自动下载所需的 packages

```typst
#import "@preview/tablex:0.0.6": tablex, hlinex
```

不在官网上的，需下载其 typ 源代码，以相对路径形式导入（或者等待其被官方接受）
```typst
#import "mdtable.typ": mdtable
```


推荐 package：

- outline 目录设置：outrageous
- 绘图（类似 LaTeX 中的 PGF/TikZ）：cetz
- box 盒子（类似 LaTeX 中的 colorbox）：showybox
- math 数学：physica
- table 表格：tablex、tablem
- code 代码：codly
- note 做笔记：drafting
- word count 字数统计：wordometer
- 图片排版：wrap-it（环绕效果）



---

目录
```typ
#outline()
```


图片插入及引用

```typ
#figure(
   image("badge_sjtu.png"),
   caption: [
    上海交通大学校徽
   ],
) <badge_sjtu>

引用图片 @badge_sjtu
```

---

文本
```typ
普通文本 
_下划线_
```


---


标题
```typ
= 一级标题
== 二级标题
```


---

有序列表
```typ
#set enum(numbering: "a)")

+ item 1
+ item 2
+ item 3
```


无序列表
```typ
Normal list.
- Text
- Math
- Layout
- ...

Multiple lines.
- This list item spans multiple
  lines because it is indented.

Function call.
#list(
  [Foundations],
  [Calculate],
  [Construct],
  [Data Loading],
)
```

---

超链接
```typ
#show link: underline

https://example.com \

#link("https://example.com") \
#link("https://example.com")[
  See example.com
]
```

---

线条
```typ
#line()
```



---


数学公式
```typ
行内公式 $Q = rho A v + C$

行间公式

$ 7.32 beta + sum_(i=0)^nabla Q_i / 2 $

```


---

Set 规则

输入 `set` 关键字编写 Set 规则，后面跟随着你要设置属性的函数的名称， 并在括号中输入你需要的新默认参数列表

Set 规则中常用的一些函数的列表：

- [`text`](https://typst-doc-cn.github.io/docs/reference/text/text/) 用于设置文本的字体、大小、颜色和其他属性
- [`page`](https://typst-doc-cn.github.io/docs/reference/layout/page/) 用于设置页面大小、边距、页眉、启用栏和页脚
- [`par`](https://typst-doc-cn.github.io/docs/reference/layout/par/) 用于对齐段落、设置行距等
- [`heading`](https://typst-doc-cn.github.io/docs/reference/meta/heading/) 用于设置标题的外观与启用编号
- [`document`](https://typst-doc-cn.github.io/docs/reference/meta/document/) 用于设置 PDF 输出中包含的元数据，例如标题和作者


```typ
#set text(font: "")
```


---

Show 规则


---


文献及引用

```typ
文献引用@ZHU2023119062

#bibliography(
  "refs.bib",
  title: "参考文献",
  style: "gb-7714-2015-numeric",
  )
```


---


代码块：Code block

内容块：Content block





---

### 函数

```typst
#let function(args) = {}
```




---

## 相关 project

- 简历 CV
	- [GitHub - gaoachao/uniquecv-typst: A simple resume template written in Typst](https://github.com/gaoachao/uniquecv-typst)
	- [GitHub - OrangeX4/Chinese-Resume-in-Typst: 使用 Typst 编写的中文简历, 语法简洁, 样式美观, 开箱即用, 可选是否显示照片](https://github.com/OrangeX4/Chinese-Resume-in-Typst)
	- [GitHub - memset0/my-resume](https://github.com/memset0/my-resume)（repo 变成 private）

- 将 typst 内容渲染成网页：[GitHub - Myriad-Dreamin/typst-book: A simple tool for creating modern online books in pure typst.](https://github.com/Myriad-Dreamin/typst-book/)

- 作业模板
	- [GitHub - gRox167/typst-assignment-template](https://github.com/gRox167/typst-assignment-template)
	- [GitHub - OriginCode/typst-homework-template: Homework Template for Typst](https://github.com/OriginCode/typst-homework-template)

- 论文模板
	- [GitHub - lucifer1004/pkuthss-typst: Typst template for dissertations in Peking University (PKU).](https://github.com/lucifer1004/pkuthss-typst)
	- [GitHub - nju-lug/nju-thesis-typst: 南京大学学位论文 Typst 模板 nju-thesis-typst](https://github.com/nju-lug/nju-thesis-typst)
	- [GitHub - howardlau1999/sysu-thesis-typst: 中山大学学位论文 Typst 模板](https://github.com/howardlau1999/sysu-thesis-typst)

- typst 文档编译 Github Actions：[build.yml](https://github.com/howardlau1999/sysu-thesis-typst/blob/master/.github/workflows/build.yml)、[GitHub - lvignoli/typst-action: Typst GitHub action](https://github.com/lvignoli/typst-action)

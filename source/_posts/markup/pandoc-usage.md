---
title: Pandoc 使用
top: false
cover: 
toc: true
mathjax: true
summary: Pandoc 使用
description: Pandoc 使用
tags:
  - Pandoc
categories:
  - 排版语言
date: 2024-07-09 09:00:00
abbrlink: 160709
password:
---

# Pandoc 使用

[纯文本做笔记 --- 使用 Pandoc 把 Markdown 转为 PDF 文件 · Blowfish](https://jdhao.github.io/2017/12/10/pandoc-markdown-with-chinese/)

效果一般：[GitHub - Wandmalfarbe/pandoc-latex-template: A pandoc LaTeX template to convert markdown files to PDF or LaTeX.](https://github.com/Wandmalfarbe/pandoc-latex-template)

Pandoc 默认使用的 `pdflatex` 命令无法处理 Unicode 字符，如果要把包含中文的 Markdown 文件转为 PDF，在生成 PDF 的过程中会报错。需使用 `xelatex` 来处理中文，并使用 `CJKmainfont` 选项指定支持中文的字体。

Pandoc 支持 front matter

`--highlight-style`：指定语法高亮主题，`zenburn`，`tango`, `zenburn` 或 `breezedark`

调整页边距

含中文字符的 markdown / Jupyter Notebook 转 pdf

```bash
# input.md 或 input.ipynb
pandoc --pdf-engine=xelatex -V CJKmainfont="SimHei" --highlight-style zenburn input.md -o output.pdf
```

Jupyter Notebook 转 Markdown：[Jupyter Notebook文件转markdown](https://zhuanlan.zhihu.com/p/371132826)

```bash
jupyter nbconvert --to markdown input.ipynb
```

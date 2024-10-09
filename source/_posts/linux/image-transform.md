---
title: 图片格式转换
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: 图片格式转换
description: 图片格式转换
tags:
  - 图片处理
categories:
  - Linux
date: 2024-07-22 10:00:00
abbrlink: 427020
password:
---

# 图片格式转换

## 图片、PDF 互相转换

- eps 转 pdf：
    - ps2pdf，Linux 自带，将 ps/eps 格式转成 pdf
    - epstopdf，Tex Live 中的 tool（生成的 pdf 文件相比 ps2pdf 生成的空白较少）

- pdf 转 jpg/png 等格式：[GitHub - Belval/pdf2image: A python module that wraps the pdftoppm utility to convert PDF to PIL Image object](https://github.com/Belval/pdf2image)

```bash
brew install poppler

pip install -U pdf2image
```

- svg 转 pdf：[GitHub - typst/svg2pdf: Converts SVG files to PDF.](https://github.com/typst/svg2pdf)（没有 convert 效果好）

```bash
cargo install svg2pdf-cli

svg2pdf file.svg
```

- jpg/png 转 svg：[PNG to SVG - FreeConvert.com](https://www.freeconvert.com/png-to-svg)

- svg 生成及格式转换：[Text to SVG AI Generator : Create unique SVG illustration from text](https://svg.la/text-to-svg/)



---

## ImageMagick 使用

>[利用Linux/shell中的命令编辑图片/视频和pdf文件](https://zhuanlan.zhihu.com/p/397857009)

- ImageMagick 中的 convert 命令行工具，可实现多种图片格式转换
    - 图片格式包括：tiff、png、jpg、svg、pdf 等
    - pdf 转 png 的图片质量没有 pdf2image 工具 高
    - tiff 图片转换，会将 tiff 的所有图层输出出来（只要编号最小的即可）
    - ImageMagick V7 版本 `magick` 替换 `magick convert` 或 `convert` 命令

- ghostscript：处理 PDF 文件，可执行命令为 `gs`

- Docker 部署在线操作 PDF：[GitHub - Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)（

- pdftk M1 芯片安装：[pdftk MacOs M1 · GitHub](https://gist.github.com/u1i/d8d4422ce770ffaad4619eb7e9d040f4)

```bash
# 下载链接
https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/pdftk_server-2.02-mac_osx-10.11-setup.pkg
```

- 图片操作

```bash
# 创建 ImageMagick 默认 logo 图片
convert logo: logo.png

# 格式转换
convert input.* output.*

# pdf 转图片；添加 -density 参数不使其变糊
convert -density 1000 input.pdf -quality 100 output.png

# TIFF 格式压缩
convert input.tif -compress LZW -quality 75 output.tif

# 裁切图片白边
convert -trim input.png output.png

# 左右堆叠图片 +
convert image1.png image2.png +append stack.png
# 上下堆叠图片 -
convert image1.png image2.png -append stack.png

# 图片分割
convert input.jpg -crop 3x3@ +repage +adjoin output_%d.jpg
```

- PDF 操作

```bash
# PDF 合并
# 方式 1；会变模糊
convert input1.pdf input2.pdf merged.pdf
# 方式 2；不会变模糊
pdfunite input1.pdf input2.pdf merged.pdf

# PDF 抽取
pdftk input.pdf cat 5-10 output out.pdf

# PDF 压缩
ps2pdf input.pdf output.pdf
ps2pdf -dPDFSETTINGS=/screen input.pdf output.pdf
ps2pdf -dPDFSETTINGS=/ebook -dColorImageResolution=500 input.pdf output.pdf
# -dPDFSETTINGS 参数有 /screen, /ebook, /prepress, /printer
# /screen 压缩效果最好（很糊）
# 组合使用 可产生介于 /ebook 和 /prepress 的效果
# https://www.ghostscript.com/doc/current/VectorDevices.htm#distillerparams
```



---

## 图片压缩

- [Squoosh](https://squoosh.app/)
- [GitHub - joye61/pic-smaller: Pic Smaller – Compress JPEG, PNG, WEBP, AVIF and GIF images intelligently](https://github.com/joye61/pic-smaller)
- [GitHub - Lymphatus/caesium-image-compressor](https://github.com/Lymphatus/caesium-image-compressor)
- [GitHub - richhost/pixzip-lite: Easy to use batch image compression software. Powered by Svelte 🧡 Electron. 简单易用的批量图片压缩软件，使用 Svelte、Electron 构建。](https://github.com/richhost/pixzip-lite)
- [iLoveIMG - 图像文件在线编辑工具](https://www.iloveimg.com/zh-cn)
- [Compress JPG: Free Online Image Compressor | PNG, WebP & More - No Sign Up](https://compressjpg.io/)
- 优化 PDF 文件体积：[GitHub - pts/pdfsizeopt: PDF file size optimizer](https://github.com/pts/pdfsizeopt)

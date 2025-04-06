---
title: TeX Live 安装
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: TeX Live 安装
description: TeX Live 安装
tags:
  - LaTeX
categories:
  - 排版语言
date: 2024-11-23 15:59:58
abbrlink: 851955
password:
---

# TeX Live 安装

## 介绍

- 安装参考：
    - [GitHub - OsbertWang/install-latex-guide-zh-cn: 一份简短的关于 LaTeX 安装的介绍](https://github.com/OsbertWang/install-latex-guide-zh-cn)
    - [GitHub - AlphaZTX/LaTeX-tutorials](https://github.com/AlphaZTX/LaTeX-tutorials)（含 TeXstudio 使用）

- TeX Live 2024 版本已有 sjtutex 文档类

- TeX Live 不同版本（basic small medium full）之间的区别：[installing - Minimal TeXLive installation - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/397174/minimal-texlive-installation)

- TeX Live 跨版本升级：[Upgrade - TeX Live - TeX Users Group](https://tug.org/texlive/upgrade.html)


![different schemes of texlive](https://i.stack.imgur.com/Edat8.png)

- 信息查看

```bash
tex --version                    # 查看 TeX Live 安装版本
tlmgr --version                  # 同上

kpsewhich -var-value=TEXMFMAIN   # 查看已安装 Tex Live 的路径

kpsewhich <classname>.cls        # 查看文档类路径
```


---

## Linux

- CTAN 镜像：[CTAN - 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/CTAN/)

```bash
# 设置自定义安装路径，添加环境变量
export TEXLIVE_INSTALL_PREFIX=$HOME/src/texlive
export TEXLIVE_INSTALL_TEXDIR=$HOME/src/texlive/2023

# 下载安装包
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz --no-check-certificate

tar -xzvf nstall-tl-unx.tar.gz

cd install-tl-*

# 安装
perl ./install-tl --scheme=full    # 或 medium small
--no-interaction    # 不进行交互
-gui                #  启用 GUI 安装程序

# 安装完成后，添加环境变量
export MANPATH=$HOME/local/texlive/2023/texmf-dist/doc/man
export INFOPATH=$HOME/local/texlive/2023/texmf-dist/doc/info
export PATH=$HOME/local/texlive/2023/bin/x86_64-linux:$PATH
```

- 跨版本更新

```bash
rm 2023/tlpkg/backups        # 删除包的备份
cp -a 2023 2024              # 耗时较久

# 更新 ~/.{bash,zsh}rc 中 TeX Live 环境变量的年份

# 下载 update-tlmgr-latest.sh
wget https://mirror.ctan.org/systems/texlive/tlnet/update-tlmgr-latest.sh
sh update-tlmgr-latest.sh -- --upgrade

tlmgr update --self --all    # 更新
```



---

## macOS

- 不建议用 brew 下载安装（体积太大），而是手动下载安装包

- 安装：[MacTeX - TeX Users Group](https://www.tug.org/mactex/mactex-download.html)；在官网上下载最新 pkg 包，双击，按照提示安装

- 卸载：[Uninstalling - MacTeX - TeX Users Group](https://tug.org/mactex/uninstalling.html)
    - 卸载 GUI 应用（`/Applications/TeX`），直接将 TeX 移入废纸篓
    - 卸载 TeX Distribution
    - 卸载 Ghostscript（删除较复杂；通常在 `/usr/local/share` 或 `/usr/local/bin` 目录）

```bash
brew install --cask mactex-no-gui  # brew 安装；不建议

sudo rm -rf /Library/TeX
sudo rm -rf /usr/local/texlive
sudo rm -rf /usr/local/share/ghostscript
```

- MacTeX 本质上就是 TeX Live，只不过捆绑了 Ghostscript（处理 PS 图片文件转换成 pdf 文件） 和一些 GUI 程序（BibDesk、TeXShop、Tex Live Utility 等），做成了便于安装的 pkg 包而已。pkg 包内的安装脚本会设置好环境变量

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202405070921146.png)



---

## TeX 目录结构

- TeX 目录结构（TeX Directory Structure, TDS）：TeX 发行版中宏包、字体、帮助文档等文件的组织结构；有时也称为 TEXMF 树

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

- 需要手动安装的宏包，一般已经按照上述目录结构打包完成。手动安装时，尽量不要拷贝到系统的 TEXMF 树，而是拷贝到发行版提供的用户 TEXMF 树，如 `texlive/texmf-local`。安装完成后，还需**刷新 TeX 发行版的文件名数据库**，令新安装的宏包文件能够被系统找到

```bash
mktexlsr   # 更新 TeX 目录（通常是 TEXMF）的文件数据库
```


---

## tlmgr 使用

- tlmgr：TeX Live 包管理器

- 镜像
    - 清华镜像：https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/tlnet
    - 中科大镜像：https://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet
    - 交大镜像：https://mirrors.sjtug.sjtu.edu.cn/CTAN/systems/texlive/tlnet

```bash
# 列出已安装的宏包和文档类
tlmgr list --only-installed

tlmgr info <package>                # 查看宏包信息
tlmgr search <package>              # 查找宏包
tlmgr install <package>             # 安装宏包
tlmgr update --list                 # 查看可升级的宏包

texlive/XXXX/tlpkg/backups          # tlmgr 升级的包的备份；可删除
sudo tlmgr backup --all --clean=0   # 删除上述目录中的备份

tlmgr update --self --all           # 升级全部宏包
--self      # 更新 tlmgr 命令本身
--all       # 更新 TeX Live 系统中的所有宏包和字体

tlmgr option repository             # 查看当前使用的源
tlmgr option repository url         # 换源
tlmgr repository set url            # 同上
```

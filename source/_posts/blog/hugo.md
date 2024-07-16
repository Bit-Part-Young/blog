---
title: Hugo 框架
top: false
cover: 
toc: true
mathjax: true
summary: Hugo 框架
description: Hugo 框架
tags:
  - Hugo
categories:
  - 博客
date: 2024-07-08 22:30:00
abbrlink: 782024
password:
---

# Hugo 框架

## 介绍

- 主题：
	- [hextra](https://github.com/imfing/hextra)
	- [stack](https://github.com/CaiJimmy/hugo-theme-stack)
	- [PaperMod](https://github.com/adityatelange/hugo-PaperMod/)、[modified-papermod](https://github.com/xyming108/sulv-hugo-papermod)
		- [我的博客搭建经验 - 有意栽花花满枝](https://blog.hjroyal.top/posts/tools/2022-09-myblog/)
		- [GitHub - hjroyal/hugo-papermod-flowers: 博客源码](https://github.com/hjroyal/hugo-papermod-flowers)
		- [🧱 建站 - Sulv's Blog](https://www.sulvblog.cn/posts/blog/)
		- [Hugo博客添加相册功能 - Sulv's Blog](https://www.sulvblog.cn/posts/blog/hugo_gallery/)



---

## 使用

### Hugo 安装

```bash
# 安装 golang
curl -sS https://webi.sh/golang | sh

# 安装 prebuilt Dart Sass（一般用不到）

# 安装 Hugo
curl -sS https://webi.sh/hugo | sh
```


---

### 快速搭建

- 快速搭建

```bash
# 初始化项目
hugo new site hugo-demo

cd hugo-demo

# 克隆主题
git clone git@github.com:biaslab/hugo-academic-group.git themes/hugo-academic-group

# 删除主题 git
rm -rf themes/hugo-academic-group/.git

cp -av themes/hugo-academic-group/exampleSite/* .

cp config.toml hugo.toml

# 本地预览
hugo server --watch

# 构建
hugo --minify
```

- 若 GitHub Pages 已绑定域名，可在 `./static` 目录中添加含域名的 `CNAME` 文件

- 设置 `hugo.toml` 配置文件中的 `baseurl` 的参数值为 `https://username.github.io/repo`

---

- 目录结构

```text
.
├── archetypes/
│   └── default.md
├── content/
├── hugo.toml    # 配置文件
├── static/
└── themes/
```


---

### 部署

- GitHub Actions 示例

```yaml
name: Hugo deploy

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true
          fetch-depth: 0
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: 'latest'
          # extended: false
      - name: Build
        run: hugo --minify
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

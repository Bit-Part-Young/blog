---
title: MkDocs 框架
top: false
cover: 
toc: true
mathjax: true
summary: MkDocs 框架
description: MkDocs 框架
tags:
  - MkDocs
categories:
  - 博客
date: 2023-10-21 18:00:00
abbrlink: 182123
password:
---

# MkDocs 框架

## 介绍

MkDocs：文档、笔记、博客框架。


---

### 参考资料

- MkDocs 相关 projects 和插件列表：[GitHub - mkdocs/catalog: :trophy: A list of awesome MkDocs projects and plugins.](https://github.com/mkdocs/catalog)
- MKDocs 设置：[Setup - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/setup/)
- [mkdocs 源码剖析 - 鹤翔万里的笔记本](https://note.tonycrane.cc/cs/analysis/mkdocs/)
- 课题组 MKDocs Wiki 参考：[GitHub - ChiahsinChu/chenggroup.github.io: XMU Chenglab Wiki](https://github.com/ChiahsinChu/chenggroup.github.io)
- Mkdocs 首页写法参考：[notebook/docs/index.md at main · IsshikiHugh/notebook · GitHub](https://github.com/IsshikiHugh/notebook/blob/main/docs/index.md)

- 配置文件参考：
	- 官方配置文件：[mkdocs.yml - mkdocs-material - squidfunk - GitHub](https://github.com/squidfunk/mkdocs-material/blob/master/mkdocs.yml)
	- [mkdocs.yml - notebook - HobbitQia - GitHub](https://github.com/HobbitQia/notebook/blob/note1/mkdocs.yml)
	- [mkdocs.yml - note - TonyCrane](https://github.com/TonyCrane/note/blob/master/mkdocs.yml)
	- [mkdocs.yml - TuringCourses - ZJU-Turing - GitHub](https://github.com/ZJU-Turing/TuringCourses/blob/master/mkdocs.yml)
	- [mkdocs.yml | chenggroup.github.io - chenggroup - GitHub](https://github.com/chenggroup/chenggroup.github.io/blob/master/mkdocs.yml)

- 参考笔记站点搭建 repo：
	- [GitHub - IsshikiHugh/zju-cs-asio: 收集各类与 ZJU-CS 有关的网站形式的资料。](https://github.com/IsshikiHugh/zju-cs-asio)
	- [鹤翔万里的笔记本](https://note.tonycrane.cc/)
	- [Welcome to HobbitQia's Notebook! - HobbitQia的笔记本](https://note.hobbitqia.cc/)
	- [图灵班学习指南](https://zju-turing.github.io/TuringCourses/)
	- [GitHub - CS-ZIJI/F-MkDocs-Template: The uniform MkDocs template for course notes/tutorials.](https://github.com/CS-ZIJI/F-MkDocs-Template)



---

## 使用

### 快速搭建

- 常用主题：[mkdocs-material](https://github.com/squidfunk/mkdocs-material)

- 快速搭建

```bash
# 创建、激活虚拟环境
conda create -n mkdocs python=3.11
conda activate mkdocs

# 安装主题
pip install mkdocs-material

mkdir mkdocs-demo && cd $_

mkdocs new .      # 创建 mkdocs 项目
mkdocs serve      # 预览
mkdocs build      # 构建
mkdocs gh-deploy  # 部署
```

---

- 目录结构

```text
 ├── docs/       # 存放文档源码
 │     └── index.md
 └── mkdocs.yml  # 配置文件
```


---

### 部署

>[Publishing your site - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/publishing-your-site/)

- 手动：`mkdocs gh-deploy --force`

- GitHub Actions：示例如下

```yaml
name: MKDocs deploy 
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```


---

### 插件

- MkDocs 自带插件
- 文档统计的插件：[GitHub - TonyCrane/mkdocs-statistics-plugin](https://github.com/TonyCrane/mkdocs-statistics-plugin)
- changelog 插件：[GitHub - TonyCrane/mkdocs-changelog-plugin](https://github.com/TonyCrane/mkdocs-changelog-plugin)
- 内容加密插件：[GitHub - unverbuggt/mkdocs-encryptcontent-plugin](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin)
- 渲染 jupyter notebook：[mknotebooks](https://github.com/greenape/mknotebooks)、[mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter)（公式会无法正确渲染？）
- 导出 pdf：[mkdocs-exporter](https://github.com/adrienbrignon/mkdocs-exporter)（不好用，会报错）
- 版本控制：[Setting up versioning - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)


---

### 自定义设置

```yaml
theme:
  icon: 
    logo: material/notebook-outline  # 自定义 logo
    repo: fontawesome/brands/github-alt
    admonition: # 自定义 admonition
	# https://github.com/IsshikiHugh/notebook/blob/main/mkdocs.yaml
      info: fontawesome/solid/anchor
      note: fontawesome/solid/pen-nib
      abstract: fontawesome/solid/list
      tip: fontawesome/solid/lightbulb
      success: fontawesome/solid/check
      question: fontawesome/solid/circle-question
      warning: fontawesome/solid/triangle-exclamation
      failure: material/alien
      danger: fontawesome/solid/virus
      bug: fontawesome/solid/robot
      example: fontawesome/solid/flask
      quote: fontawesome/solid/link

  font:  # 文本及代码字体设置
    text: LXGW WenKai Screen GB Screen
    code: JetBrains Mono

  # https://github.com/HobbitQia/notebook/blob/note1/mkdocs.yml
  palette:  # 浅色/深色模式切换
    - media: "(prefers-color-scheme: light)" 
      scheme: default  # 配色方案：浅色模式
      # primary: brown  # 原色，用于标题、侧边栏、文本链接和其他几个组件
      # accent: brown  # 强调色，可以交互的元素如悬停链接、按钮和滚动条
      toggle:
        icon: material/weather-sunny # 太阳
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"  
      scheme: slate  # 配色方案：深色模式
      toggle:
        icon: material/weather-night  # 月亮
        name: Switch to light mode
		
  features:
    - navigation.footer  # 页面底部显示 “上一页、下一页”
    - navigation.tabs    # 导航栏
	
  custom_dir: overrides  # 指定自定义模板和静态文件的目录路径

plugins:  # 插件

extra_css:

extra_javascript:

markdown_extensions:  # 可直接添加，无需额外安装相关依赖；参考设置
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.emoji:
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
      emoji_index: !!python/name:material.extensions.emoji.twemoji
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.magiclink:
      normalize_issue_symbols: true
      repo_url_shorthand: true
      user: squidfunk
      repo: mkdocs-material
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.snippets:
      auto_append:
        - includes/mkdocs.md
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
      combine_header_slug: true
      slugify: !!python/object/apply:pymdownx.slugs.slugify
        kwds:
          case: lower
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde
  
extra:  # 添加 social link
  social:
    - name: GitHub
      icon: fontawesome/brands/github
      link: https://github.com/user
    - name: Home
      icon: fontawesome/solid/house-chimney
      link: url
	  
nav:
  - Home: 
    - index.md

  - XXX:
    - XXX/index.md
```

---

- 不同代码块的互相切换

```text
=== "Python"

    ```python
    print("Hello, Python!")
    ```

=== "JavaScript"

    ```javascript
    console.log("Hello, JavaScript!");
    ```
```


- i18n 设置：[mkdocs.yml](https://github.com/jiegec/kb/blob/main/mkdocs.yml)

- MKDocs Admonitions 写法：[Admonitions - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#usage)

---

## To Do

- [ ] 字体修改（暂无必要）：TonyCrane 有 heti repo；[Changing the fonts - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/#additional-fonts-mkdocsyml)
- [ ] 将 docs 目录用脚本的形式写入到 mkdocs.yml 中的 nav 中：[weekly/main.py at main · howie6879/weekly · GitHub](https://github.com/howie6879/weekly/blob/main/main.py)（参考代码）
- [x] 添加 RSS 订阅功能（Cloudflare 会失败）：[GitHub - Guts/mkdocs-rss-plugin: MkDocs plugin to generate a RSS feeds for created and updated pages, using git log and YAML frontmatter (page.meta).](https://github.com/guts/mkdocs-rss-plugin/)
- [ ] 添加给部分笔记内容设置密码的功能（涉及课题组内部内容需要；必要性不是很大）


---

## 问题

- i18n 含义：国际化（Internationalization）的缩写，在网页搭建中的主要作用是为了支持多语言和国际化。

- MkDocs Material 未来会支持 Algolia 搜索

- [x] MkDocs 中的 md 文档只能有一个一级标题，Hexo 可以多个（正常的 md 文档结构应是一个一级标题）
- [x] 任务列表渲染成了圆圈样式（mkdocs 特殊方式）
- [x] MKDocs 中连续两行都是分割线，其中的一行分割线会被当作某级标题（为兼容所有博客框架，只添加一行分割线）

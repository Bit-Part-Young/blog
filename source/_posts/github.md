---
title: GitHub 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: GitHub 使用
description: GitHub 使用
tags:
  - GitHub
categories:
  - 科研工具
date: 2023-10-30 09:00:00
abbrlink: "5928"
password:
---

# GitHub

## 介绍

全球最大的代码托管平台

提供免费的静态网站托管服务 GitHub Pages

团队协作开发平台：有完善的协作功能 (Fork, Issue, Pull Request) 等功能

GitHub 每个仓库的总体积限制是 1GB（Gitee 是 500MB），每个仓库中每个 release 的最大文件体积限制是 2GB（Gitee 是 1GB）；release 数量没有明确的限制；对于普通用户，仓库（Repo 代码 + release 文件）的总体积限制为 100 GB

- [x] 之前留言过的 GitHub issue，仍会收到后续通知， 如何关闭（在 Github 个人主页的 Notifications 处关闭）


---

显示/自定义 GitHub 通知：
- [GitHub - qiweiii/github-custom-notifier: Web Extension - Allows you to customize GitHub notifications](https://github.com/qiweiii/github-custom-notifier)
- [Fetching Title#wex5](https://github.com/0x2E/GitStatus)

生成 changelog
[GitHub - github-changelog-generator/github-changelog-generator: Automatically generate change log from your tags, issues, labels and pull requests on GitHub.](https://github.com/github-changelog-generator/github-changelog-generator)

GitHub 命令行形式的 dashboard
[GitHub - dlvhdr/gh-dash: A beautiful CLI dashboard for GitHub 🚀](https://github.com/dlvhdr/gh-dash)

[GitHub - maboloshi/github-chinese: GitHub 汉化插件，GitHub 中文化界面。 (GitHub Translation To Chinese)](https://github.com/maboloshi/github-chinese)



GitHub README 生成 TOC
>[GitHub - ekalinin/github-markdown-toc: Easy TOC creation for GitHub README.md](https://github.com/ekalinin/github-markdown-toc)

>[GitHub - ekalinin/github-markdown-toc.go: Easy TOC creation for GitHub README.md (in go)](https://github.com/ekalinin/github-markdown-toc.go)


skill 图标
>[GitHub - tandpfun/skill-icons: Showcase your skills on your Github readme or resumé with ease ✨](https://github.com/tandpfun/skill-icons)


用 GitHub Actions 实现 github 与 gitee 之间同步：[GitHub - Yikun/hub-mirror-action: 一个Github Action，用于在Github和Gitee之间同步代码。Action for mirroring repos between Hubs (like Github and Gitee).](https://github.com/Yikun/hub-mirror-action)


---

### 参考资料

>[GitHub 简易指南 - OrangeX4's Blog](https://orangex4.cool/post/github-tutorials-for-beginner/)

lec2：Git/GitHub 基础介绍
>[lec2.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec2.md)

>[GitHub - tiimgreen/github-cheat-sheet: A list of cool features of Git and GitHub.](https://github.com/tiimgreen/github-cheat-sheet)

>[GitHub - jasineri/gitartwork: Gitartwork on user's contribution graph](https://github.com/jasineri/gitartwork)



---

## 使用

### Repo 基本使用

Repo 页面

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images202403011048507.png)




---

Issues 页面

![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202309111638624.png)

---

Pull requests 页面（简称 PR）

![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202309111638625.png)


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081114184.png)


Pull Requests 流程:

- Fork 该 Repo；
- git clone fork 的 Repo 到本地，进行代码修改并提交，会出现提交的 commit 相对原 Repo 的前后关系；
- 点击 “Contribute”，提 一个 Pull Request 给原来的 Repo；
- 点击 “Sync fork”，同步原 Repo 最新代码。

---


改变 Repo 公开，隐藏的属性：
该 Repo 的 Settings - Danger Zone

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081130359.png)

---


设置自己的 activity 为 private：
Settings - Public profile - Contributions & activity


![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202309111638621.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081150607.png)



Github Pages

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images202403011049337.png)



---

### alert 语法

>[basic-writing-and-formatting-syntax.md](https://github.com/github/docs/blob/main/content/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax.md)

>和 Obsidian 中的 Admonition 插件的 alert 语法一样

```text
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081122804.png)



---

### 自定义 GitHub profile

创建名为 username 的 repo，在 README.md 文档中添加内容即可形成 profile，可以添加 GitHub 统计信息以丰富并自定义 profile。

可获取动态生成的 GitHub 统计信息的 repo：

- [GitHub - anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats)
- [GitHub - lowlighter/metrics](https://github.com/lowlighter/metrics)
- [GitHub - jstrieb/github-stats](https://github.com/jstrieb/github-stats)

使用 github-readme-stats repo 部署的 vercel app API 会有次数限制，且只能访问公开 repo 的相关数据，导致统计信息不全。因此更建议 fork 该 repo，部署自己的 vercel app API（可以访问私有 repo 数据，参见 [deploy-on-your-own](https://github.com/anuraghazra/github-readme-stats#deploy-on-your-own)；添加 PAT_1 环境变量时，注意需点击 Save 保存）

github-stats repo：使用 Github Acitons 生成 GitHub 统计信息卡片（生成速度较慢）；克隆该 repo，删除 `.git`，创建自己的 repo（非 fork），根据需要添加 EXCLUDED、EXCLUDED_LANGS 和 EXCLUDE_FORKED_REPOS secrets（创建这些 secrets 的方法：进入该 repo 的设置页面中的 “Secrets” 部分，创建新 secret）

profile 参考：

- [GitHub - TonyCrane/TonyCrane](https://github.com/TonyCrane/TonyCrane)
- [sudoskys (Jasmine) · GitHub](https://github.com/sudoskys)


标准 README.md 文件写法：[GitHub - RichardLitt/standard-readme: A standard style for README files](https://github.com/RichardLitt/standard-readme)


---

### shield.io

数据牌

>[GitHub - badges/shields](https://github.com/badges/shields)


---

Python 相关

```text
[![PyPi](https://img.shields.io/pypi/v/spt?logo=pypi&logoColor=white&label=PyPI)](https://pypi.org/project/spt/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/spt?logo=pypi&logoColor=white&color=blue&label=PyPI%20downloads)](https://pypi.org/project/spt)
[![Requires Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg?logo=python&logoColor=white)](https://python.org/downloads)
```

```text
[![GitHub](https://img.shields.io/github/license/jzhang-github/PyFunction)](https://github.com/jzhang-github/PyFunction/blob/main/LICENSE)

[![Pypi](https://img.shields.io/pypi/v/zjpf.svg)](https://pypi.org/project/zjpf/)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/zjpf)](https://pypi.org/project/zjpf/)

[![PyPI - Wheel](https://img.shields.io/pypi/wheel/zjpf)](https://pypi.org/project/zjpf/)
```

---

Repo 相关

```html
<div align="center">
<h1>Data Structures & Algorithms for Coding Interview</h1>
<p align="center">
<a href=" ">  
< img alt="Stars" src="https://img.shields.io/github/stars/SamirPaulb/DSAlgo"> 
< img alt="Forks" src="https://img.shields.io/github/forks/SamirPaulb/DSAlgo"> 
< img alt="Size" src="https://img.shields.io/github/repo-size/SamirPaulb/DSAlgo"> 
< img alt="Hits" src="https://hitsofcode.com/github/SamirPaulb/DSAlgo?branch=main">
< img alt="language" src="https://user-images.githubusercontent.com/77569653/227633223-43014974-ac8f-4cf9-8605-93d08cb2d5fd.svg">
</a >
</p >
```


---

一些编程语言及排版语言的 shields logo
>[README.md](https://github.com/frostming/marko/blob/master/README.md?plain=1)

```text
### Skills
#### Programming language
![Python](https://img.shields.io/badge/-Python-3776ab?style=flat-square&logo=python&logoColor=fff)
![Shell](https://img.shields.io/badge/-Shell-4eaa25?style=flat-square&logo=gnu%20bash&logoColor=fff)
![C++](https://img.shields.io/badge/-C%2b%2b-00599c?style=flat-square&logo=C%2b%2b&logoColor=fff)
![Fortran](https://img.shields.io/badge/-Fortran-734f96?style=flat-square&logo=fortran&logoColor=fff)
![Julia](https://img.shields.io/badge/-Julia-9558b2?style=flat-square&logo=julia&logoColor=fff)

#### Markup language
- ![LaTeX](https://img.shields.io/badge/-LaTeX-008080?style=flat-square&logo=latex&logoColor=fff)
- typst


#### 其他
![C](https://img.shields.io/badge/-C-a8b9cc?style=flat-square&logo=C&logoColor=fff)
![HTML5](https://img.shields.io/badge/-HTML5-e34f26?style=flat-square&logo=HTML5&logoColor=fff)
![CSS3](https://img.shields.io/badge/-CSS3-1572b6?style=flat-square&logo=CSS3&labelColor=1572b6)
![JavaScript](https://img.shields.io/badge/-JavaScript-f7df1e?style=flat-square&logo=JavaScript&labelColor=f7df1e&logoColor=000)
![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=Node.js&logoColor=fff)
```

>“4eaa25” 表示颜色的十六进制代码

---

github CI 状态
>[GitHub Workflow Status (with event) | Shields.io](https://shields.io/badges/git-hub-workflow-status-with-event)

>badge 的名称是 yml 文件中的 name 键对应的值

```text
# repo 需要 public
[![CI Status](https://github.com/materialsproject/pymatgen/actions/workflows/test.yml/badge.svg)](https://github.com/materialsproject/pymatgen/actions/workflows/test.yml)
```

---

### pre-commit

[pre-commit](https://pre-commit.com/)：用于管理和维护 git 钩子的框架。允许配置多种钩子，这些钩子会在代码提交到仓库之前自动运行，以检查代码风格、格式化代码、检查语法错误（可用于 Python Markdown Shell 等）等。配置文件：.pre-commit-config.yaml


```bash
# 安装 pre-commit
pip install -U pre-commit

# 安装钩子
pre-commit install

# 手动运行钩子
pre-commit run
pre-commit run --all-files
```


格式：
```yaml
repos:
  - repo:  # 钩子 repo url
    rev:  # 版本
    hooks:  # 列出要使用的具体钩子
      - id:  # 钩子唯一标识
	    args:  # 可选 传递给钩子的额外参数
		language_version: # 编程语言版本 如 python3.11
```


示例：[.pre-commit-config.yaml](https://github.com/CederGroupHub/smol/blob/main/.pre-commit-config.yaml)

```yaml
exclude: '.git|.tox'
default_stages: [commit]
fail_fast: true

repos:
  - repo: https://github.com/psf/black-pre-commit-mirror
    rev: 24.4.2
    hooks:
      - id: black  # black-jupyter
        # language_version: python3.11

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.2
    hooks:
	  # Run the linter.
      - id: ruff
        args: [ --fix ]
        types_or: [ python, pyi, jupyter ]
      # Run the formatter.
      - id: ruff-format
        types_or: [ python, pyi, jupyter ]

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
    - id: isort
      name: isort (python)
      args:
      - --profile=black
```




---

### GitHub Actions

>[github自动化 | 我是谁](https://yuhldr.github.io/posts/dabdcea.html)

>[使用 Github Action 自动部署 | 安知鱼](https://blog.anheyu.com/posts/asdx.html)

>[GitHub Actions 入门教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)

>[GitHub Actions工作流自动化的入门核心\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1aT421y7Ar/)


GitHub Actions 可以有多个 `.yml` 文件


同步到 gitee 的 GitHub Actions
>[gitee.yml](https://github.com/howardlau1999/sysu-thesis-typst/blob/master/.github/workflows/gitee.yml)

GitHub 自动发布 release
>[release.yml](https://github.com/frostming/marko/blob/master/.github/workflows/release.yml)


以网页文件夹的形式分享文件，需 repo 状态为 public
[GitHub - linyuxuanlin/File-host: 资源共享仓库](https://github.com/linyuxuanlin/File-host)

网页文件夹（需在每个文件夹目录下创建 index.html 文件）：[GitHub - pranabdas/drive](https://github.com/pranabdas/drive)


---

### GitHub CLI

>[GitHub - cli/cli: GitHub’s official command line tool](https://github.com/cli/cli)

- 安装

```bash
sudo apt install gh  # Ubuntu

sudo pacman -S github-cli  # Arch Linux

brew install gh  # Mac

conda install gh --channel conda-forge  # Conda
```

- 源码编译安装

```bash
# 安装 golang
curl -sS https://webi.sh/golang | sh

git clone https://github.com/cli/cli.git gh-cli
cd gh-cli

make install prefix=$HOME/src/gh

ln -s ~/src/gh/bin/gh ~/bin
```

- 验证登录：按照提示进行

```bash
gh auth login
```

- 创建 release 并上传文件：file 格式可以是压缩文件，`pdf`，`md` 等，`txt` 不行

```bash
gh release create v0.0.1  # 创建 release

gh release upload v0.0.1 file  # 上传附加文件

gh release list  # 列出 releases
```

- 创建 issue

```bash
gh issue create --title "gh issue test" --body "create an issue by gh"
```

- Github Copilot CLI 使用

```bash
# 安装
gh extension install github/gh-copilot

gh copilot explain  # 解释
gh copilot suggest  # 建议

# 设置别名 ghcs 和 ghce
echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc
```



---

### 其他

github star history
>[GitHub Star History](https://star-history.com/)

```text
< img alt="Star History" loading="lazy"  src="https://api.star-history.com/svg?repos=SamirPaulb/DSAlgo&type=Date">
```

---

contribution 可视化
>[GitHub - yoshi389111/github-profile-3d-contrib: This GitHub Action creates a GitHub contribution calendar on a 3D profile image.](https://github.com/yoshi389111/github-profile-3d-contrib)

>[Leticia-maria/.github/workflows/profile-3d.yml at main · Leticia-maria/Leticia-maria · GitHub](https://github.com/Leticia-maria/Leticia-maria/blob/main/.github/workflows/profile-3d.yml)

github contribution 贪吃蛇
>[github-contribution-grid-snake.yml](https://github.com/hotoo/hotoo/blob/main/.github/workflows/github-contribution-grid-snake.yml)

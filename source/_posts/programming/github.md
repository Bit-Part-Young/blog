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
  - 编程
date: 2023-10-30 09:00:00
abbrlink: 592810
password:
---

# GitHub

## 介绍

- 全球最大的代码托管平台，也是一个社区

- 也可以托管 Gist 代码片段

- 团队协作开发平台：有完善的协作功能 (Fork, Issue, Pull Request) 等功能

- 提供免费的静态网站托管服务 GitHub Pages

- GitHub 每个仓库的总体积限制是 1GB（Gitee 是 500MB），每个仓库中每个 release 的最大文件体积限制是 2GB（Gitee 是 1GB）；release 数量没有明确的限制；对于普通用户，仓库（仓库代码 + release 文件）的总体积限制为 100 GB


---

### 参考资料

- [GitHub 简易指南 - OrangeX4's Blog](https://orangex4.cool/post/github-tutorials-for-beginner/)

- Git/GitHub 基础介绍：[lec2.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec2.md)

- [GitHub - tiimgreen/github-cheat-sheet: A list of cool features of Git and GitHub.](https://github.com/tiimgreen/github-cheat-sheet)

- [GitHub - phodal/github: GitHub 漫游指南](https://github.com/phodal/github)



---

## 使用

### 工具

- 管理 GitHub Star（Star 的仓库数一多，5k+，无法查看 star 页面，老是出错）
    - 移动端 GitHub App（可识别用户已创建的分类 tag）
    - [【工具自荐】starflare 又一个管理 github star 的 web app · Issue #4732 · ruanyf/weekly · GitHub](https://github.com/ruanyf/weekly/issues/4732)
    - [GitHub - cfour-hi/gitstars: Github Starred Repositories Manager](https://github.com/cfour-hi/gitstars)（无法识别）
    - [Starflare](https://starflare.app/)（无法识别）
    - [Organize Your GitHub Stars With Ease - Astral](https://astralapp.com/)
    - [GitHub - raythunder/github-stars-manager: 这是一个用来管理你的github stars的网页工具，它通过标签来管理和分类你的stars。所有的数据保存在你自己的github gists.](https://github.com/raythunder/github-stars-manager)

- [GitHub - WCY-dt/my-github-2024: Statistics of your activities on GitHub in 2024. 统计2024年你在GitHub上的活动.](https://github.com/WCY-dt/my-github-2024)

- [GitHub Cards - Showcase Your GitHub Contributions in 2024 into Stunning Visual Cards](https://github.cards/)

- 在仓库所在链接后添加 `stargazers`（**实用**）：[查看GitHub仓库被谁star · Issue #15 · oneone1995/blog · GitHub](https://github.com/oneone1995/blog/issues/15)

- 汉化插件（无必要）：[GitHub - maboloshi/github-chinese: GitHub 汉化插件，GitHub 中文化界面。 (GitHub Translation To Chinese)](https://github.com/maboloshi/github-chinese)

- 命令行版本的 GitHub Dashboard：[GitHub - dlvhdr/gh-dash: A beautiful CLI dashboard for GitHub 🚀](https://github.com/dlvhdr/gh-dash)

- 隐藏仓库中 `Compare & pull request` 的提示插件：[GitHub - liuliangsir/compare-and-pull-request-prompt-box-killer-for-github: Automatically hides the "Compare & pull request" prompt box on GitHub repository pages](https://github.com/liuliangsir/compare-and-pull-request-prompt-box-killer-for-github)

- 显示/自定义 GitHub 通知：
    - [GitHub - qiweiii/github-custom-notifier: Web Extension - Allows you to customize GitHub notifications](https://github.com/qiweiii/github-custom-notifier)
    - [GitHub - 0x2E/GitStatus: Show GitHub notifications on menubar (macOS 13.0+)](https://github.com/0x2E/GitStatus)

- 生成 changelog：[GitHub - github-changelog-generator/github-changelog-generator: Automatically generate change log from your tags, issues, labels and pull requests on GitHub.](https://github.com/github-changelog-generator/github-changelog-generator)

- 浏览、打开、预览 GitHub 仓库中的 ipynb 文件
    - [nbviewer](https://nbviewer.org/)
    - [欢迎使用 Colaboratory - Colab](https://colab.research.google.com/)

- [【工具自荐】一键查看 github 仓库树形图 · Issue #5272 · ruanyf/weekly · GitHub](https://github.com/ruanyf/weekly/issues/5272)（一般）

- [GitHub - zanjie1999/githubBackup: 备份Github所有仓库（包括私仓）纯shell实现](https://github.com/zanjie1999/githubBackup)

- 生成最近的 PR 为网页：[GitHub - leon-fong/prs: Explore historic Open Source Contributions](https://github.com/leon-fong/prs)

- [GitHub - hunshcn/gh-proxy: github release、archive以及项目文件的加速项目](https://github.com/hunshcn/gh-proxy)

- [GitHub - antfu-collective/sponsorkit: 💖 Toolkit for generating sponsors images 😄](https://github.com/antfu-collective/sponsorkit)


---

### GitHub Markdown

- [GitHub - jerry1100/github-markdown-printer: Print GitHub Flavored Markdown exactly as it appears on GitHub](https://github.com/jerry1100/github-markdown-printer)

- 生成 TOC：
    - [GitHub - ekalinin/github-markdown-toc: Easy TOC creation for GitHub README.md](https://github.com/ekalinin/github-markdown-toc)
    - [GitHub - ekalinin/github-markdown-toc.go: Easy TOC creation for GitHub README.md (in go)](https://github.com/ekalinin/github-markdown-toc.go)

- alert 语法

```markdown
> [!NOTE]
> [!TIP]
> [!IMPORTANT]
> [!WARNING]
> [!CAUTION]
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081122804.png)


---

### GitHub 基本使用

- Repo 页面

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images202403011048507.png)

---

- Issues 页面

![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202309111638624.png)

---

- Pull requests 页面（简称 PR）

![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202309111638625.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081114184.png)

- Pull Requests 流程:

    - Fork（复刻） 该 Repo；
    - git clone fork 的 Repo 到本地，进行代码修改并提交，会出现提交的 commit 相对原 Repo 的前后关系；
    - 点击 “Contribute”，提一个 Pull Request 给原来的 Repo；
    - 点击 “Sync fork”，同步原 Repo 最新代码。

---

- 改变 Repo 的 public private 状态：该 Repo 的 Settings - Danger Zone

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081130359.png)

---

- 设置自己的 activity 为 private：Settings - Public profile - Contributions & activity


![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202309111638621.png)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081150607.png)


---

### GitHub Pages

GitHub Pages 介绍

- GitHub 提供的免费静态网页托管服务，类似的还有 Gitee Pages 和 GitLab Pages；商用：Vercel、Netlify、Cloudflare Pages 等
- GitHub 会为每个用户/组织分配一个二级域名 `username.github.io`
- 创建一个名为 `username.github.io` 的 repo，会作为主页，通过 `username.github.io` 即可访问 repo 内存放的静态网页
- 对于其他 repo（可无限创建），也可以开启 Pages 功能，通过 `username.github.io/repo-name` 访问，静态页面来源也需要指定
- 部署时自动创建 gh-pages 分支：[GitHub - peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images202403011049337.png)


---

### GitHub 个人首页

参考：美化 GitHub profile 教程：[GitHub - rzashakeri/beautify-github-profile](https://github.com/rzashakeri/beautify-github-profile)

创建名为 username 的 repo，在 README.md 文档中添加内容即可生成个人首页（profile），可以添加 GitHub 统计信息以丰富并自定义 profile。

可获取动态生成的 GitHub 统计信息的 repo：

- [GitHub - anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats)
- [GitHub - lowlighter/metrics](https://github.com/lowlighter/metrics)（形式丰富，可使用 GitHub Actions）
- [GitHub - jstrieb/github-stats](https://github.com/jstrieb/github-stats)
- [GitHub - vn7n24fzkq/github-profile-summary-cards](https://github.com/vn7n24fzkq/github-profile-summary-cards)
- 生成并更新 WakaTime 统计数据：[GitHub - matchai/waka-box](https://github.com/matchai/waka-box)

使用 github-readme-stats repo 部署的 vercel app API 会有次数限制，且只能访问公开 repo 的相关数据，导致统计信息不全。因此更建议 fork 该 repo，部署自己的 vercel app API（可以访问私有 repo 数据，参见 [deploy-on-your-own](https://github.com/anuraghazra/github-readme-stats#deploy-on-your-own)；添加 PAT_1 环境变量时，注意需点击 Save 保存）

github-stats repo：使用 Github Acitons 生成 GitHub 统计信息卡片（生成速度较慢）；克隆该 repo，删除 `.git`，创建自己的 repo（非 fork），根据需要添加 EXCLUDED、EXCLUDED_LANGS 和 EXCLUDE_FORKED_REPOS secrets（创建这些 secrets 的方法：进入该 repo 的设置页面中的 “Secrets” 部分，创建新 secret）

profile 实例参考：

- [GitHub - TonyCrane/TonyCrane](https://github.com/TonyCrane/TonyCrane)
- [sudoskys (Jasmine) · GitHub](https://github.com/sudoskys)
- [XYCode-Kerman (XYCode Kerman) · GitHub](https://github.com/XYCode-Kerman)
- [GitHub - Wybxc/metrics: 忘忧北萱草大合集！](https://github.com/Wybxc/metrics/)
- [ayaka-icu/README.md at main · ayaka-icu/ayaka-icu · GitHub](https://github.com/ayaka-icu/ayaka-icu/blob/main/README.md)


标准 README.md 文件写法：[GitHub - RichardLitt/standard-readme: A standard style for README files](https://github.com/RichardLitt/standard-readme)

优秀 README.md 文件：[GitHub - matiassingers/awesome-readme: A curated list of awesome READMEs](https://github.com/matiassingers/awesome-readme)

---

GitHub Star history：[GitHub Star History](https://star-history.com/)

```markdown
< img alt="Star History" loading="lazy" src="https://api.star-history.com/svg?repos=SamirPaulb/DSAlgo&type=Date">
```

---

GitHub contribution 可视化：

- [GitHub - yoshi389111/github-profile-3d-contrib: This GitHub Action creates a GitHub contribution calendar on a 3D profile image.](https://github.com/yoshi389111/github-profile-3d-contrib)
- [Leticia-maria/.github/workflows/profile-3d.yml at main · Leticia-maria/Leticia-maria · GitHub](https://github.com/Leticia-maria/Leticia-maria/blob/main/.github/workflows/profile-3d.yml)
- 贪吃蛇（只能使用 public contributions，见 [Issue #88](https://github.com/Platane/snk/issues/88)）：[snk](https://github.com/Platane/snk)
    - 实例：[github-contribution-grid-snake.yml](https://github.com/hotoo/hotoo/blob/main/.github/workflows/github-contribution-grid-snake.yml)
- （未测试）[GitHub - jasineri/gitartwork: Gitartwork on user's contribution graph](https://github.com/jasineri/gitartwork)


---

### 徽章

通常在 GitHub 的 README 文件或其他在线文档中显示以展示各种信息，如构建状态、测试覆盖率、包版本、许可证信息等。

徽章/ icon 相关 repo：

- [GitHub - badges/shields](https://github.com/badges/shields)
- [GitHub - inttter/md-badges: An extensive list of Shields.io badges.](https://github.com/inttter/md-badges)
- [GitHub - ziadOUA/m3-Markdown-Badges: 🏅 A Material You inspired markdown badge collection.](https://github.com/ziadOUA/m3-Markdown-Badges)
- skill 图标 icon：[GitHub - tandpfun/skill-icons: Showcase your skills on your Github readme or resumé with ease ✨](https://github.com/tandpfun/skill-icons)
- 统计 GitHub 中的 REDME、Issue、PR visitor 数量：[Visitor Badge](https://visitor-badge.laobi.icu/)
- 可参考：[README.rst](https://github.com/charmoniumQ/charmonium.cache/blob/main/README.rst?plain=1)
- [Notes-for-Data-Structure/README.md at master · OE-Heart/Notes-for-Data-Structure · GitHub](https://github.com/OE-Heart/Notes-for-Data-Structure/blob/master/README.md?plain=1)


---

Python 相关（使用 pypi）

```markdown
<!-- package 版本 -->
![PyPi](https://img.shields.io/pypi/v/spt?logo=pypi&logoColor=white&label=PyPI)
<!-- package 下载量 -->
![PyPI Downloads](https://img.shields.io/pypi/dm/spt?logo=pypi&logoColor=white&color=blue&label=PyPI%20downloads)
<!-- Python 版本 -->
![Requires Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg?logo=python&logoColor=white)
<!-- package wheel -->
![PyPI - Wheel](https://img.shields.io/pypi/wheel/spt)
```

---

GitHub Repo 相关（使用 github）

```markdown
<!-- star 数目 -->
![GitHub Repo stars](https://img.shields.io/github/stars/Bit-Part-Young/spt)
<!-- license 证书 -->
[![GitHub](https://img.shields.io/github/license/jzhang-github/PyFunction)](https://github.com/jzhang-github/PyFunction/blob/main/LICENSE)
<!-- 点击量 -->
![Hits-of-Code](https://hitsofcode.com/github/Bit-Part-Young/spt?branch=master)
<!-- CI 状态 方式 1 -->
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Bit-Part-Young/github-stats/main.yml)
<!-- 方式 2 -->
![Generate Stats Images - passing](https://github.com/Bit-Part-Young/github-stats/actions/workflows/main.yml/badge.svg)
```

---

编程语言 logo（使用 badge）

```markdown
![Python](https://img.shields.io/badge/-Python-3776ab?style=flat-square&logo=python&logoColor=fff)
![Shell](https://img.shields.io/badge/-Shell-4eaa25?style=flat-square&logo=gnu%20bash&logoColor=fff)
![C++](https://img.shields.io/badge/-C%2b%2b-00599c?style=flat-square&logo=C%2b%2b&logoColor=fff)
![Fortran](https://img.shields.io/badge/-Fortran-734f96?style=flat-square&logo=fortran&logoColor=fff)
![Julia](https://img.shields.io/badge/-Julia-9558b2?style=flat-square&logo=julia&logoColor=fff)
![LaTeX](https://img.shields.io/badge/-LaTeX-008080?style=flat-square&logo=latex&logoColor=fff)
```


---

### pre-commit

>[Git项目管理，代码规范pre-commit使用详解 - 夏冬](https://amos-x.com/index.php/amos/archives/pre-commit/)

[pre-commit](https://pre-commit.com/)：用于管理和维护 git 钩子的框架。允许配置多种钩子，这些钩子会在代码提交到仓库之前自动运行，以检查代码风格、格式化代码、检查语法错误（可用于 Python、Markdown、Shell）等。配置文件：`.pre-commit-config.yaml`

```bash
# 安装
pip install -U pre-commit
# 安装钩子
pre-commit install
# 生成默认配置
pre-commit sample-config
# 手动运行钩子
pre-commit run
pre-commit run --all-files

# 删除钩子
rm .git/hooks/pre-commit
```

---

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

---

示例：
- [.pre-commit-config.yaml](https://github.com/CederGroupHub/smol/blob/main/.pre-commit-config.yaml)
- https://github.com/jupyter/docker-stacks/blob/main/.pre-commit-config.yaml
- [ZnFrame/.pre-commit-config.yaml at main · zincware/ZnFrame · GitHub](https://github.com/zincware/ZnFrame/blob/main/.pre-commit-config.yaml)

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

- GitHub 提供的 CI/CD 服务：CI（Continuous Integration）：持续集成；CD（Continuous Delivery）：持续交付
- 即配置一些自动化任务，在特定事件发生时自动执行：如每次 push 后自动测试，release 时自动构建部署
- 配置文件：`.github/workflows/workflow_name.yml`；可以有多个 `.yml` 文件

参考资料：

- [github自动化 - 我是谁](https://yuhldr.github.io/posts/dabdcea.html)
- [使用 Github Action 自动部署 - 安知鱼](https://blog.anheyu.com/posts/asdx.html)
- [GitHub Actions 入门教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)
- [GitHub Actions工作流自动化的入门核心\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1aT421y7Ar/)
- 内含 Github Action 计划任务语法：[GitHub - xlc520/AutoGreen: 保持GitHub一直绿](https://github.com/xlc520/AutoGreen)

具体示例：

- [GitHub - sdras/awesome-actions: A curated list of awesome actions to use on GitHub](https://github.com/sdras/awesome-actions)
- 同步到 Gitee：[gitee.yml](https://github.com/howardlau1999/sysu-thesis-typst/blob/master/.github/workflows/gitee.yml)、[hub-mirror-action](https://github.com/Yikun/hub-mirror-action)
- 自动发布 Release：[release.yml](https://github.com/frostming/marko/blob/master/.github/workflows/release.yml)
- 自动化发布 release：[GitHub - release-it/release-it: 🚀 Automate versioning and package publishing](https://github.com/release-it/release-it)
- Wakatime GitHub Actions 设置：[OE-Heart/.github/workflows/main.yml at master · OE-Heart/OE-Heart · GitHub](https://github.com/OE-Heart/OE-Heart/blob/master/.github/workflows/main.yml)

---

### GitHub CLI

- 官网：[GitHub - cli/cli: GitHub’s official command line tool](https://github.com/cli/cli)

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

- GitHub Copilot CLI 使用（效果一般）

```bash
# 安装
gh extension install github/gh-copilot

gh copilot explain  # 解释
gh copilot suggest  # 建议

# 设置别名 ghcs 和 ghce
echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc
```



---

## 相关问题

- GitHub feed 最新消息时间与电脑时间差 12 小时（移动端、网页均是次情况）

- GitHub 桌面端不好用；移动端有探索功能

- [x] 之前留言过的 GitHub issue，仍会收到后续通知， 如何关闭（在 GitHub 个人主页的 Notifications 处关闭）

- [ ] GitHub Organization 删除后，90 天内该名字无法被使用

- [ ] GitHub 添加 organization 成员（弄成课题组）

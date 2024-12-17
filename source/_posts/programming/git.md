---
title: Git 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Git 使用
description: Git 使用
tags:
  - Git
categories:
  - 编程
date: 2023-09-18 09:00:00
abbrlink: 242349
password:
---

# Git 使用

## 介绍

分布式版本控制系统。


```bash
# 查看文件每行最后一次的提交相关信息
git blame [options] <file>
```



---

### 相关概念

Git 中的 4 个位置：工作目录 Working Directory、暂存区 Staging Area、本地存储库 Local Repository、远程存储库 Remote Repository

暂存区（stage）：已经修改、等待后续提交的文件
文件三个类别：未跟踪（Untracked）、已追踪（Tracked）、被忽略（Ignored）
HEAD：当前工作区在提交历史中的**指针**
detached HEAD：HEAD 指向某个历史提交，而不是某个 “分支”


```bash
# 让当前文件夹变成 git 仓库（创建 .git 文件夹）
git init
# 创建一个新的文件夹并初始化为 git 仓库
git init folder

# 查看某个文件是否被忽略，以及匹配的规则
git check-ignore -v file

# 同时删除本地和版本库中的文件
# 等价于 rm + git add
git rm
# 将一个已暂存的新文件取消暂存
git rm --cached

# 重命名文件
# 等价于 mv + git rm + git add
git mv
```


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images202403011046838.png)



---

### .git 结构

WIP...


---

### 参考资料

- [图解Git](https://marklodato.github.io/visual-git-guide/index-zh-cn.html)
- [Git 备忘清单 & git cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/git.html)
- 可视化 git 学习：[GitHub - pcottle/learnGitBranching](https://github.com/pcottle/learnGitBranching)
- [git-flight-rules](https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md)
- Git/GitHub 基础介绍：[lec2.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec2.md)
- [Oh Shit, Git!?!](https://ohshitgit.com/zh)
- [GitHub - twtrubiks/Git-Tutorials: Git-Tutorials GIT基本使用教學:memo:](https://github.com/twtrubiks/Git-Tutorials)
- [Git Commands - Isshiki修's Notebook](https://note.isshikih.top/tech_accu/tool/Git/Commands/)
- [git.txt](https://github.com/skywind3000/awesome-cheatsheets/blob/master/tools/git.txt)
- [GitHub - jaywcjlove/git-tips: 这里是我的笔记，记录一些git常用和一些记不住的命令。](https://github.com/jaywcjlove/git-tips)
- [GitHub - 521xueweihan/git-tips: :trollface:Git的奇技淫巧](https://github.com/521xueweihan/git-tips)
- [Git • Linux tutorial](https://pranabdas.github.io/linux/git)
- [十分钟学会正确的github工作流，和开源作者们使用同一套流程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV19e4y1q7JJ/)
- [GitHub - hongiii/gitNotes\_from\_Liao: 从廖老师网站上总结的Git笔记，对常见命令进行了总结。](https://github.com/hongiii/gitNotes_from_Liao)
- [Git 重学指南 - Git 重学指南](https://git-remake.wybxc.cc/index.html)
- [Git 和 Github 秘籍](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md)
- [GitHub - k88hudson/git-flight-rules: Flight rules for git](https://github.com/k88hudson/git-flight-rules)
- [Git - 茂茂物语](https://notes.fe-mm.com/workflow/git/)
- 解决 git 合并冲突：[解决冲突 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/896043488029600/900004111093344)
- [Git常用操作清单](https://blog.sbyu.top/post/8)
- [常用 Git 命令清单 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)
- [git cherry-pick 教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2020/04/git-cherry-pick.html)
- [个人心得：Git使用与开发规范 - AllenY's blog](https://alleny.xyz/post/development-standards/)
- [Getting Started with: Git, GitHub, and GitHub pages - howtos](https://www.wgilpin.com/howto/howto_github.html)
- Git 游戏：[Oh My Git!](https://ohmygit.org/)
- [GitHub - hanyujie2002/wyag-zh: 自己动手写 Git 的中文翻译](https://github.com/hanyujie2002/wyag-zh)


---

## 使用

### 工具

- VSCode 插件 GitLens：增强 Git 使用

- Git 操作 TUI 工具：[gitui](https://github.com/extrawurst/gitui)、[lazygit](https://github.com/jesseduffield/lazygit)

- [onefetch](https://github.com/o2sh/onefetch)：获取本地 Git 仓库的项目详情和代码统计、仓库大小等内容

- [gita](https://github.com/nosarthur/gita)：管理多个 Git 仓库

- 统计本地 Git 仓库大小：[GitHub - github/git-sizer](https://github.com/github/git-sizer)

- 查看 Git repo 的统计信息：[GitHub - arzzen/git-quick-stats](https://github.com/arzzen/git-quick-stats)

- 以 SQL 的方式查询 Git 仓库相关内容：[Git Query language](https://amrdeveloper.github.io/GQL/)

- 根据 commit 记录生成 changelog：[GitHub - orhun/git-cliff: A highly customizable Changelog Generator that follows Conventional Commit specifications ⛰️](https://github.com/orhun/git-cliff)

```bash
brew install lazygit  # macOS
go install github.com/jesseduffield/lazygit@latest  # go 安装

cargo install onefetch

pip install -U gita

brew install coreutils
export PATH="$HOMEBREW_PREFIX/opt/coreutils/libexec/gnubin:$PATH"
brew install git-quick-stats

brew install git-delta
```

- [delta](https://github.com/dandavison/delta)：主要用于 Git 相关命令（diff、blame、show 等）的语法突出显示分页器
    - 安装包为 git-delta，可执行命令为 delta
    - 使用：在 `~/.gitconfig` 中添加以下设置

```bash
[core]
    pager = delta
[interactive]
    diffFilter = delta --color-only
[delta]
    features = side-by-side line-numbers decorations
    navigate = true
[merge]
    conflictstyle = diff3
[diff]
    colorMoved = default
```

- Git 扩展：[GitHub - tj/git-extras](https://github.com/tj/git-extras)
    - git extras 命令功能中文翻译：[git-extras-zh/Commands.zh.md](https://github.com/chinanf-boy/git-extras-zh/blob/master/Commands.zh.md)

```bash
# 安装
brew install git-extras  # macOS

# 编译安装
git clone [https://github.com/tj/git-extras.git](https://github.com/tj/git-extras.git)
cd git-extras
git checkout $(git describe --tags $(git rev-list --tags --max-count=1))
make install PREFIX=$HOME/local/git-extras

# 设置环境变量
export PATH=$HOME/local/git-extras/bin:$PATH
source $HOME/local/git-extras/git-extras-completion.zsh

# 常用命令
git setup            # 初始化项目（等同于 git init + add + commit）
git summary          # 输出 repo 总结
git changelog        # 生成 History.md
git commits-since    # 列出（默认为上周）date 以来的提交记录；与 --since 参数用法一致
git count            # 统计提交总数
git count --all      # 依据作者统计提交总数
git undo N           # 删除最新的 N 条提交记录
```


---

### 基本使用

- 注册 GitHub 或 Gitee 账户
- 配置 GitHub 或 Gitee 的 SSH
- 配置 Git

---

- 新建本地 Git 仓库

```bash
git init
git add .
git commit -m "first commit"

# GitHub
git remote add origin git@github.com:user/repo.git
# git remote add origin https://github.com/user/repo.git

# Gitee
git remote add origin git@gitee.com:user/repo.git
# git remote add origin https://gitee.com/user/repo.git

git push -u origin main
```

---

- 已有本地 Git repo

```bash
git remote add origin git@github.com:user/repo.git
git push -u origin main
```


---

### 开发使用

- [GitHub - DeepSourceCorp/good-first-issue: Make your first open-source contribution.](https://github.com/DeepSourceCorp/good-first-issue)

- [GitHub - firstcontributions/first-contributions: 🚀✨ Help beginners to contribute to open source projects](https://github.com/firstcontributions/first-contributions)

```bash
# 对于二次开发 repo 人员，在新分支上进行操作

git clone url            # 克隆仓库
git checkout -b feature  # 切换至新分支 feature
git add .                # 修改代码
git commit -m "message"  # 添加提交信息
git push origin feature  # 将本地的 feature 分支 push 至远程分支

###########################################################

# 对于二次开发 repo 人员，开发过程中，main 主分支有更新

# 方式 1
git checkout main      # 切换回主分支
git pull origin main   # pull 远程主分支
git checkout feature   # 切换至 feature 分支
git rebase main        # 将 main 分支合并到 feature 分支
# 方式 2
git pull origin main:feature

# 中途可能会出现 rebase conflict，手动选择保留哪段代码

git push origin feature -f  # 推送更新

###########################################################

# 对于 repo 所有者，将 feature 分支合并到 main 主分支
git pull origin feature:feature  # 将远程 feature 分支 pull 到 本地 feature 分支
git merge feature                # 将 feature 合并到主分支
git rebase feature               # 同上
```


---

### 特殊文件

#### .gitconfig

- git 配置文件
- 路径：Linux `~/.gitconfig`；Windows `git\etc\gitconfig`
- 内容示例：

```bash
[user]
    name = XXX
    email = XXX@email.com
[init]
    defaultBranch = main
[credential]
    helper = cache --timeout 300000
    # optional
    # helper = store --file ~/.git-credentials
[core]
    quotepath = false
[help]
    autocorrect = 1
[push]
    # 自动设置远程追踪分支；git push 后可省略 origin BRANCH
    autosetupremote = true
```


---

#### .gitignore

- 忽略文件：写入在 `.gitignore` 文件中的文件/目录会被忽略掉
- 可在 repo 根目录及其子目录分别创建
- 常用 `.gitignore` 模板：
    - [GitHub - github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore)
    - [gitignore.io - 为你的项目创建必要的 .gitignore 文件](https://www.toptal.com/developers/gitignore)


---

#### `.gitattributes`

用于配置 Git 在处理不同类型文件时的行为：定义行结束符（Line Endings）、指定语言统计等（linguist-language）等。

示例 1：[.gitattributes- simpy](https://github.com/esemble/simpy/blob/master/.gitattributes)
示例 2：[md - .gitattributes - note](https://github.com/TonyCrane/note/blob/master/.gitattributes)

```bash
# 自动检测文本文件，并执行 LF（Line Feed）规范化操作
* text=auto
*.txt eol=lf

*.jpg binary
*.pdf binary
*.png binary

# 配置特定文件类型的差异（diff）显示策略
# 并非将文件转换为文本文件，只是尝试以文本方式进行显示
*.doc   diff=astextplain
*.DOC   diff=astextplain
*.docx  diff=astextplain
*.DOCX  diff=astextplain
*.dot   diff=astextplain
*.DOT   diff=astextplain
*.pdf   diff=astextplain
*.PDF   diff=astextplain
*.rtf   diff=astextplain
*.RTF   diff=astextplain

*.md linguist-documentation=false linguist-detectable=true
*.md linguist-language=Markdown
*.html linguist-detectable=false
*.js linguist-detectable=false
*.css linguist-detectable=false

linguist-documentation=false  # 不将文件统计为文档类型
linguist-detectable=true      # 开启检测
linguist-language=...         # 记为 ... 编程语言
linguist-vendored             # 将目录/文件视为外部引入的代码，不计入语言统计中
```


---

#### `.gitmodules`

Git 子模块（submodule）：允许将一个 Git repo 嵌套在另一个 Git repo 中，以便在一个项目中使用其他项目的代码。

`.gitmodules` 写法及示例：[.gitmodules - ZJU-UGCourse](https://github.com/yujincheng08/ZJU-UGCourse/blob/master/.gitmodules)

```bash
[submodule "submodule"]  # 子模块名称
    path = submodule  # 子模块在 repo 中的相对路径
    url = git@github.com:user/submodule.git  # 子模块 url
    branch = main  # 分支名
    # 浅克隆
    shallow = true
    depth = 1
```

添加子模块

```bash
git submodule add git@github.com:user/repo.git

# 初始化和更新子模块
git submodule update --init --recursive
```

克隆含子模块的 GitHub repo

```bash
# 方式 1
git clone --recurse-submodules git@github.com:user/repo.git

# 方式 2
git clone git@github.com:user/repo.git
cd repo

git submodule init    # 初始化子模块
git submodule update  # 更新子模块
# 以上两个命令可以等效为以下命令
git submodule update --init --recursive
```


---

#### `.git-credential`

>[Git - 凭证存储](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%87%AD%E8%AF%81%E5%AD%98%E5%82%A8)

凭证存储；非标准 git 配置文件。

- 默认所有都不缓存。 每一次连接都会询问用户名和密码
- “cache” 模式会将凭证存放在内存中一段时间。 密码不会被存储在磁盘中，且 15 分钟后从内存中清除
- “store” 模式可接受 `--file <path>` 参数，自定义存放密码的文件路径（默认 `~/.git-credentials` ）

```bash
git config --global credential.helper cache

git config --global credential.helper 'store --file ~/.my-credentials'
```


---

### 多账号 ssh 配置

>[配置同时使用 Gitlab、Github、Gitee(码云) 共存的开发环境 - 简书](https://www.jianshu.com/p/68578d52470c)

- 多账号 ssh 配置作用：
    - 多账号管理：通过配置 config 文件，可以方便地管理访问多个仓库时使用的不同账号
    - 通过 ssh 协议，免密克隆远程仓库及 git 操作

- 生成密钥，将 `id_rsa.gitee.pub` 和 `id_rsa.github.pub` 文件中的内容添加到 Github 和 Gitee 中的 SSH keys（SSH 公钥）中

```bash
ssh-keygen -t rsa -f ~/.ssh/id_rsa.gitee -C "XXX@email.com"

ssh-keygen -t rsa -f ~/.ssh/id_rsa.github -C "XXX@email.com"
```

- `~/.ssh/config` 文件配置

```bash
# GitHub
Host github.com
    Port 22
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa.github

# Gitee
Host gitee.com
    Port 22
    HostName gitee.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitee

# GitLab
Host gitlab.com
    Port 22
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitlab
```

- 测试

```bash
ssh -T git@github.com

ssh -T git@gitee.com

ssh -T git@gitlab.com
```

- 若返回信息，则配置成功

```text
Hi XXX! You've successfully authenticated, but GitHub does not provide shell access.

Hi XXX! You've successfully authenticated, but GITEE.COM does not provide shell access.

Welcome to GitLab, XXX!
```

- **注意事项**：
    - `~/.ssh/config` 文件出现 `Bad owner or permissions` 错误的解决办法：文件权限问题，设置 config 文件权限为 `600`
    - 超算平台中的登陆节点禁止对外的 ssh，无法使用 git 交互环境，建议在本地或者实验室工作站（Manager 和 Master）使用；超算平台进行以上设置会出现以下报错：

```bash
ssh: connect to host github.com port 22: Network is unreachable
```


---

### 将 repo 的 remote origin 由 https 改为 ssh 或 token 形式

- 之后进行 push、pull 等操作时，将默认通过 SSH 协议，并使用 SSH keys 进行身份验证，不需再输入用户名和密码

- 在该 repo 目录中的 `.git/config` 文件找到 `[remote "origin"]` 选项，将 URL 后的 https 地址改成 ssh 形式或带 token 的地址

```bash
# https 形式
url = https://github.com/user/repo.git

# ssh 形式
url = git@gitee.com:user/repo.git
url = git@github.com:user/repo.git

# https + token 形式
url = https://user:token@github.com/user/repo.git
url = https://user:token@gitee.com/user/repo.git
```


---

### GitHub Token

- GitHub 从 2021 年开始不再支持输入账号和密码的形式进行验证，密码改为 Token（Gitee 验证仍是账号和密码）

- 具体设置：Settings - Developer settings - Personal access tokens - Tokens(classic)


---

### Gitee 与 GitHub、GitLab 之间互相同步

- Gitee 可以直接从 GitHub 和 GitLab 中导入 repo

- 参考：
    - [仓库镜像管理（Gitee<->Github 双向同步） - Gitee 产品文档](https://help.gitee.com/repository/settings/sync-between-gitee-github)
    - [Gitlab、Github、Gitee之间的代码同步\_gitea 和gitee能同步吗\_李·逍遥的博客-CSDN博客](https://blog.csdn.net/lianwen1314/article/details/106384595)


---

### Git LFS

- Git LFS(Git Large File Storage)：GitHub 推出的大文件存储服务，让 Git 只保存二进制文件的 hash，而二进制文件将会存在 Git LFS 服务器中。以减小 Git 仓库体积，加快仓库的克隆和拉取

- GitHub 的免费存储空间为 1G，限带宽 1GB/月，超过需升级；Gitee 只对付费企业开放

```bash
# 安装
sudo apt-get install git-lfs  # Ubuntu
brew install git-lfs          # macOS

git lfs install               # 初始化

git lfs track "*.pdf"         # 跟踪大文件 会生成 .gitattributes 文件
git add .gitattributes
git commit -m "add .gitattributes"

git lfs track                 # 查看当前已跟踪的 Git LFS File 类型

git lfs pull                  # 拉取 LFS 文件

git lfs clone repo_url        # 克隆

git lfs ls-files              # 列出当前已通过 LFS 跟踪的所有文件

git lfs untrack "*.pdf"       # 取消跟踪并删除
git rm --cached "*.pdf"

# 将历史文件迁移到 LFS
git lfs migrate import --include="*.dmg" --everything
git push --force             # 强制推送
```


---

### git-filter-repo

- Git 历史重写工具

- 执行 `git filter-repo` 命令后，会改变 `.git/config` 文件，只保留 `[core]` 参数信息，需重新添加远程 repo url 并强制推送

```bash
# 安装
brew install git-filter-repo    # macOS
pip install -U git-filter-repo  # pip

# 使用
--dry-run  # 模拟运行

# 删除文件（及包含该文件的 commit 历史）
git filter-repo --path-glob '*.jpg' --invert-paths

# 重命名文件/目录
git filter-repo --path old_path --to-path new_path

# 替换作者信息
git filter-repo --name-callback 'return name.replace(b"Old Name", b"New Name")'

# 删除大文件
git filter-repo --strip-blobs-bigger-than 10M

# 提取子目录
git filter-repo --subdirectory-filter path

# 强制推送至远程 repo
git push -f origin main
```



---

## 常用命令

### clone

```bash
git clone  <url>           # 完整克隆（fresh/full clone）
git clone --depth 1 <url>  # 浅克隆（shallow clone）；只 clone 最新提交
git fetch --unshallow      # 更新本地仓库，使其包含完整的历史记录

git clone -b <branch1> -b <branch2> <url>  # clone 多个分支
```


---

### config

```bash
git config --list           # 列出 repo 配置
git config --global --list  # 列出全局配置
git config --list --show-origin  # 列出配置即对应配置文件路径

# 全局设置
git config --global user.name "username"
git config --global user.email "user@email.com"
# 其他
color.ui 1                  # git 命令输出里加上颜色
core.editor "vim"           # 配置默认编辑器
core.fileMode false         # 忽略文件的权限变化
core.quotepath false        # 解决 git status 中文乱码 问题
help.autocorrect 1          # 开启自动纠错功能

# 取消全局配置 --global 后添加 --unset
```


---

### add

```bash
git add file

git add --patch  # 或 -p；对于所有的修改依次进行添加确认

git add -i  # 交互式
```


---

### commit

- [commit-messages-guide/README\_zh-CN.md at master · RomuloOliveira/commit-messages-guide · GitHub](https://github.com/RomuloOliveira/commit-messages-guide/blob/master/README_zh-CN.md)

- [创建没有任何改动的提交](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md#%E6%B2%A1%E6%9C%89%E4%BB%BB%E4%BD%95%E6%94%B9%E5%8A%A8%E7%9A%84%E6%8F%90%E4%BA%A4)

```bash
# 根据当前时间进行 commit
git commit -m "$(date '+%Y-%m-%d %H:%M:%S')"

# 将改动添加进最近一次的 commit 中
git commit --amend --no-edit  
git push --force  # 不加 --force 会出现问题

# 修改 commit 信息
git commit --amend --no-edit -m 'xxx'

# 创建没有任何改动的提交
git commit -m 'empty' --allow-empty
```


---

### push

```bash
git push

# 删除远程分支
git push origin :<remote-branch>
git push origin --delete <remote-branch>

# 删除远程分支已经不存在而本地还保留的跟踪记录
git remote prune origin
```


---

### pull

```bash
git pull

git pull --rebase
```


---

### branch

```bash
git branch       # 查看本地分支
git show-branch  # 更详细
git branch -r    # 查看远程分支
git branch -a    # 查看所有分支（本地 + 远程）

git branch -u origin/main  # 设置本地分支与远程分支之间的追踪关系
git branch -m <NewBranch>  # 重命名为新分支
git branch -d <Branch>     # 删除本地分支（会提醒是否进行分支合并）
git branch -D <Branch>     # 强制删除
git branch -vv             # 列出 repo 所有分支信息

# 示例
* master 8b700ba [origin/master] vault backup: 2024-04-01 19:11:49
```


---

### checkout

```bash
git checkout <Branch>      # 切换分支
git checkout -b <Branch>   # 创建并切换新分支
git checkout -             # 迅速切换到上一个分支
git checkout -- file       # 撤回对某个文件的修改
```


---

### remote

```bash
git remote show origin  # 查看远程 repo 所有分支
git ls-remote origin    # 列出远程仓库的引用（分支和标签）

# 使本地的跟踪分支列表与远程保持一致，删除远程分支已经不存在而本地还保留的跟踪记录
git remote prune origin
git remote prune origin --dry-run  # 不实际删除

git remote rm origin    #
```


---

### status

```bash
git status

git status --short --branch

# 删除未跟踪的文件
gsb | grep -E '^\s*[?][?]' | awk '{print $2}' |  xargs rm -rf
```


---

### reset

```bash
git reset               # 撤销整个暂存区的 add 操作
git reset HEAD~         # 撤回最新的 commit，保留代码修改
git reset --hard HEAD~  # 不保留修改
git reset commit_hash   # 撤回到指定的 commit id 版本
git reset file          # 撤销指定文件 add 操作
```


---

### tag

- 版本号命名一般规范：v 主版本号.次版本号.修订号\[- 预发布版本号\]
    - 主版本号：不兼容的 API 修改；为 0 时表示还在开发阶段，不保证稳定性
    - 次版本号：添加新功能，但是保持兼容
    - 修订号：兼容修改，修正不正确的行为
    - 示例：v1.0.0、v1.0.0-beta

```bash
# 拉取标签
git pull --all                     # 拉取远程所有内容包括标签
git fetch --tags                   # 拉取标签

# 查看标签
git tag -ln                        # 列出标签及其注释
git ls-remote --tags origin        # 列出远程仓库标签
git show v1.0.0                    # 查看具体标签信息

# 新建标签
git tag -a v1.0.0 -m 'comment'     # 带注释

# push 标签
git push origin v1.0.0             # 特定标签
git push origin --tags             # 所有标签

# 删除标签
git tag -d v1.0.0                  # 本地
git push origin :refs/tags/v1.0.0  # 远程
```


---

### log

查看 commit 记录/日志

```bash
git log           # 查看提交日志
git reflog        # 查看所有分支的所有操作记录

git shortlog -s -n             # 统计作者提交次数
# 在作者后面添加邮箱
git log --pretty=format:'%an <%ae>' | sort | uniq -c | sort -nr
git rev-list --count --all     # 统计 repo 中的总提交次数
git rev-list --count [branch]  # 统计 repo 中指定分支的提交总数

# 较为简洁美观的 git log 输出样式
git log --oneline --graph --all
git log --oneline --graph --stat
# 参考 zsh git alias
git log --graph --pretty="%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset" --stat

# 获取文件最后一次修改的时间
git log -1 --pretty="%ci" file
# 获取文件第一次添加到 repo 的时间
git log -1 --diff-filter=A --follow --pretty="%ci" file

# git log 常用参数
-p                   # --patch；显示详细修改内容
--graph              # 显示分支结构
--stat               # 统计
--oneline            # 一行显示；commit id 8 个字符
--pretty=oneline     # 一行显示；完整 commit id
        =%B          # 只显示 commit message
        =%s          # commit message
        =%H          # 完整 commit hash
        =%h          # 缩写 commit hash
        =%ci         # 提交日期（不受作者限制）
        =%ad         # 作者提交日期（绝对时间）
        =%ar         # 作者提交日期（相对时间）
        =%an         # 作者名称
        =%ae         # 作者邮箱
        =%d          # 分支信息
-n N / HEAD~N        # 显示最新的前 N 条提交记录
--grep=pattern       # 筛选指定 pattern 的提交记录
--date=short         # 日期格式
--since="midnight"   # 当天一天
--since="2024-09-17 00:00" --until="2024-09-18 00:00"  # 具体某一天
--since="1 day ago"  # 一天以前；week month year
```


---

### diff

```bash
git diff                      # 比较工作区和暂存区
git diff <Branch>             # 比较工作区和分支
git diff <Branch1> <Branch2>  # 比较两个分支
git diff HEAD~N -- file       # 查看某个文件当前工作区与 HEAD~N 的差异

# 查看工作区文件改动统计（个数，增加、删除行数）
git diff --stat
git diff --stat file

# 查看两次提交之间的差异
git diff <commit_id_1> <commit_id_2> --stat

# 查看特定提交的所有改动统计
git show <commit_id> --stat
git diff-tree <commit_id> --stat

# 查看暂存区文件的改动统计
# staged cached 同义词
# --word-diff 忽略空行
git diff --staged --stat
git diff --cached --stat

# 常用参数
--name-only         # 只显示发生变化的文件名
--diff-filter=M     # 筛选只显示被修改的文件
```


---

### stash

- 用于临时保存暂存区的未提交更改，返回工作区

- 暂存项（stashes）遵循栈结构，即最近暂存的更改（编号为 `stash@{n}`）会被放置在栈的顶部（索引为 0）

```bash
git stash                 # 将当前修改暂存到 stash 栈中
git stash -u              # 包括新增 untracked 文件
git stash push -- file    # 指定单个文件
git stash save 'message'  # 添加备注

git stash list     # 列出所有 stash
git stash pop      # 恢复 stash 中的最近一次暂存，并从 stash 栈中删除
git stash apply    # 恢复 stash 中的最近一次暂存，不从 stash 栈中删除
git stash show -p  # 查看 stash 修改内容
git stash show --name-only  # 查看 stash 文件名
git stash apply stash@{n}   # 恢复特定 stash
git stash drop stash@{n}    # 删除特定 stash
git stash clear             # 清空 stash
git stash branch <branch>   # 从 stash 中创建一个新的分支
```


---

### rm

>[从工作区批量去除已删除文件](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md#%E4%BB%8E%E5%B7%A5%E4%BD%9C%E5%8C%BA%E5%8E%BB%E9%99%A4%E5%A4%A7%E9%87%8F%E5%B7%B2%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6)

```bash
git rm $(git ls-files -d)     # 从工作区批量去除已删除文件
git rm --cached file          # 删除远程 repo 的文件
git rm -r --cached folder     # 删除远程 repo 的目录
```


---

### git 命令自定义别名

- [git-命令自定义别名](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md#git-%E5%91%BD%E4%BB%A4%E8%87%AA%E5%AE%9A%E4%B9%89%E5%88%AB%E5%90%8D)
- [查看历史 - Git 重学指南](https://git-remake.wybxc.cc/%E5%82%A8%E5%AD%98%E5%BA%93/%E6%9F%A5%E7%9C%8B%E5%8E%86%E5%8F%B2.html)
- [GitHub - GitAlias/gitalias: Git alias commands for faster easier version control](https://github.com/GitAlias/gitalias)

```bash
# 方式 1 命令行设置
git config --global alias.p 'push'

# 方式 2 直接在 ~/.gitconfig 添加
[alias]
  p = push

# oh-my-zsh 中的内置 git 插件定义了 许多 git 命令的 alias
alias | grep 'git subcommand'
```



---

## 其他用法

- 提交空文件夹：在空文件夹中创建 `.gitkeep` 文件

- push 到多个远程 repo（**不能是浅克隆**）
    - 参考： [文件推向3个git库 - git-tips](https://github.com/jaywcjlove/git-tips#%E6%96%87%E4%BB%B6%E6%8E%A8%E5%90%913%E4%B8%AAgit%E5%BA%93)
    - 只能从 `origin` 里的一个 repo url pull 代码，默认为添加到 `origin` 的第一个地址，可在 `.git/config` 文件中直接调整 repo url 顺序
    - 可用此方法替代 Gitee 与 GitHub 之间互相同步的设置

```bash
# 添加远程 repo url
git remote add origin url
git remote set-url --add origin url

# 删除远程 repo url
git remote set-url --delete origin url

# 也可直接在 .git/config 添加/删除远程 repo url
url = XXX
```

浅克隆时，push 到多个远程 repo 会出现如下报错：

```bash
remote: fatal: did not receive expected object XXX
error: remote unpack failed: index-pack failed
To github.com:user/repo.git
 ! [remote rejected] main -> main (failed)
error: failed to push some refs to 'github.com:user/repo.git'
```

---

- git clone 部分内容：[如何使用 Git 只克隆部分文件 | 猎人杂货铺](https://hunterx.xyz/git-sparse-checkout.html#more)
    - `git sparse-checkout` - 可实现只克隆或检出指定文件夹，不下载所有内容
    - `--filter=blob:none` - 只获取元数据，不下载原始数据部分

```bash
# 方式 1 速度更快
git clone --filter=blob:none --sparse <repo>
git sparse-checkout set <file> <folder>

# 方式 2
git clone --filter=blob:none --no-checkout <repo>
git checkout origin/main -- <file> <folder>
```

---

- 下载单个文件：打开文件，点击 “Raw”，用 `wget` 下载，示例：

```bash
# gitee
wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O install.sh

# github
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O install.sh

# gist
wget https://gist.githubusercontent.com/user/GIST_ID/raw/filename -O filename
```

---

- GitHub 加速下载：[Github 增强 - 高速下载](https://greasyfork.org/zh-CN/scripts/412245-github-%E5%A2%9E%E5%BC%BA-%E9%AB%98%E9%80%9F%E4%B8%8B%E8%BD%BD)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401082135895.png)

---

- 规范式提交

gitmoji-cli：git commit 时使用 emoji
>[GitHub - carloscuesta/gitmoji-cli: A gitmoji interactive command line tool for using emojis on commits. 💻](https://github.com/carloscuesta/gitmoji-cli)

>[gitmoji 速查表 - Git 重学指南](https://git-remake.wybxc.cc/%E9%99%84%E5%BD%95/gitmoji-%E9%80%9F%E6%9F%A5%E8%A1%A8.html)


---

- 创建 Releases：Create a new release - Choose a tag，之后填写相关信息，必要时上传附件

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081713870.png)

---

- 新建空分支：
    - GitHub 中的 gh-pages 分支为特殊分支，可与主分支无关联（push 时会自动启用 Github Actions）
    - **其他命名的分支暂无法实现与主分支无关联**；[git - Create empty branch on GitHub - Stack Overflow](https://stackoverflow.com/questions/34100048/create-empty-branch-on-github)

```bash
git switch --orphan <new branch>
git commit --allow-empty -m "init"
git push -u origin <new branch>
```

---

- 其他

```bash
# 查看两星期内的改动
git whatchanged --since='2 weeks ago'


# 只保留最新的一次提交以减小 repo 体积
git checkout --orphan <NewBranch> <commit-hash>  # 基于最后的 commit 创建新分支
git commit -m 'init'          # 提交
git branch -D main            # 删除分支
git branch -m main            # 新分支重命名为 main 主分支
git push origin main --force  # 强制 push


# 列出大文件
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -5 | awk '{print$1}')"


# 列出 repo 所有文件
git ls-tree --full-tree -r --name-only HEAD
```

- 拷贝自水源

```bash
# 忽略本地文件系统的优化
git clone --no-local

# 把所有已跟踪的文件的修改添加到暂存区，无需 git add 命令
# 不包括新文件或被删除的文件
git commit -am 'message'

# 修改最后一次提交，不改变提交信息
git commit --amend --no-edit

# 拉取时删除在远程仓库中已被删除的远程跟踪分支的引用
git pull --prune

# 合并两个没有共同历史的 Git 分支
git merge --allow-unrelated-history

# 所有的 reflog 记录将被标记为过期，并且在下一次垃圾回收时被清理
# reflog 引用日志
git reflog expire --expire=now --all

# 遍历所有提交，将每个提交的提交者日期修改为作者日期
# git filter-repo 需单独安装
git filter-repo -f --commit-callback 'commit.committer_date = commit.author_date'
```



---

## 相关问题

- GitHub 和 Gitee 中的 md 文档无法渲染 `\begin{}` 等复杂 LaTeX 公式命令

- GitHub 可以渲染 Front-Matter，Gitee 和 Typora 暂不行，但会将其包裹起来

- 无法 SSH 连接 GitHub：[坑：ssh: connect to host github.com port 22: Connection refused - 知乎](https://zhuanlan.zhihu.com/p/521340971)

```bash
# 方式 1
# 修改 ~/.ssh/config 内容
Host github.com
  Hostname ssh.github.com
  Port 443

# 方式 2
# 打开仓库中的 .git/config 文件
git config --local -e
# 将 url 的 SSH 形式 改成 HTTPS
```

- Git 报错

```bash
# 报错内容
error: RPC failed; Failed to connect to github.com port 443: Couldn't connect to server

# 解决方法
# 若有 VPN 代理，设置代理
git config --global http.proxy 127.0.0.1:7890
git config --global https.proxy 127.0.0.1:7890
```

- Git 报错

```bash
# 报错内容
error: cannot pull with rebase: You have unstaged changes.
error: please commit or stash them.

# 解决方法
git config pull.rebase false
```

- [ ] 交大 VPN 打开，会使得 SSH 连接 Git 失效（已水源提问，暂无法解决）

- [x] Git 如何忽略空行的变化（忽略的话，对同步会不利，不建议）

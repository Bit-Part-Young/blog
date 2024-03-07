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
  - 版本控制
categories:
  - 编程
date: 2023-09-18 09:00:00
abbrlink: 24234
password:
---

# Git 使用

## 介绍

分布式版本控制工具。

```bash
# 列出本地 repo 所有文件
git ls-tree --full-tree -r HEAD
git ls-tree --full-tree -r --name-only HEAD
```

```bash
git filter-branch
```

```bash
# 可以线性化提交历史
git rebase --root
```

[线性化提交历史 | Argvchs の小窝](https://argvchs.github.io/2023/02/26/linearize-commit-history/)

- [x] git 如何忽略空行的变化（忽略的话，对同步会不利，不建议）


---

### 相关概念

暂存区 stage
Untracked 未追踪的


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images202403011046838.png)




Git LFS 是一个开源的 Git 扩展，用于管理大型文件，例如音频样本、视频、数据集和图形。它通过在 Git 内部使用文本指针，同时将文件内容存储在像 GitHub.com 或 GitHub Enterprise 这样的远程服务器上，来替换大型文件。

```bash
sudo apt-get install git-lfs

brew install git-lfs
```


会生成 .gitattributes 文件

```bash
git lfs track "*.pdf -maxsize=100M"
```


---

### 参考资料

lec2：Git/GitHub 基础介绍
>[lec2.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec2.md)

>[Git 备忘清单 & git cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/git.html)

>[git.txt](https://github.com/skywind3000/awesome-cheatsheets/blob/master/tools/git.txt)

>[GitHub - jaywcjlove/git-tips: 这里是我的笔记，记录一些git常用和一些记不住的命令。](https://github.com/jaywcjlove/git-tips)

>[GitHub - 521xueweihan/git-tips: :trollface:Git的奇技淫巧](https://github.com/521xueweihan/git-tips)

>[Git • Linux tutorial](https://pranabdas.github.io/linux/git)

>[十分钟学会正确的github工作流，和开源作者们使用同一套流程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV19e4y1q7JJ/)

>[GitHub - hongiii/gitNotes\_from\_Liao: 从廖老师网站上总结的Git笔记，对常见命令进行了总结。](https://github.com/hongiii/gitNotes_from_Liao)

>[Git 重学指南 - Git 重学指南](https://git-remake.wybxc.cc/index.html)

>[Git 和 Github 秘籍](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md)

>[GitHub - k88hudson/git-flight-rules: Flight rules for git](https://github.com/k88hudson/git-flight-rules)

以 SQL 的方式查询 repo 的 git 相关内容
>[Git Query language](https://amrdeveloper.github.io/GQL/)



---

## 使用

### 基本使用

- 注册 gitee 或 github 账户
- 配置 gitee 或 github 的 SSH（id_rsa.gitee、id_rsa.github）
- 配置 git（.gitconfig）

---

- 新建 repo

```bash
git init
git add README.md
git commit -m "first commit"

# github
git remote add origin git@github.com:username/repo.git
# git remote add origin https://github.com/username/repo.git

# gitee
git remote add origin git@gitee.com:username/repo.git
# git remote add origin https://gitee.com/username/repo.git

git push -u origin main
```

---

- 本地已有 git repo

```bash
git remote add origin git@github.com:username/repo.git
git push -u origin main
```


---

### 开发使用

>[GitHub - firstcontributions/first-contributions: 🚀✨ Help beginners to contribute to open source projects](https://github.com/firstcontributions/first-contributions)


```bash
# 对于二次开发 repo 人员
git clone git@github.com:username/repo.git

# 切换至新分支 shend_dev
git checkout -b shend_dev

# 修改或者添加本地代码

git add file
git commit -m "message"

# 将本地的 shend_dev 分支上传至 git repo 对应远程分支
git push origin shend_dev  

###########################################################

# 对于 repo 所有者，将 shend_dev 合并到主分支
# 将远程的 shend_dev branch pull 到 本地的 shend_dev 分支
git pull origin shend_dev:shend_dev

# 将 shend_dev 合并到主分支
git merge shend_dev
# 或 git rebase shend_dev

###########################################################

# 对于二次开发 repo 人员，开发过程中，主分支有更新
# 切换回主分支
git checkout main

# pull远程主分支
git pull origin main

# 切换至 shend_dev 分支
git checkout shend_dev

# 将main分支合并到 shend_dev 分支，根据自己的 commit 来修改成新的内容
git rebase main
# 以上步骤也可以 git pull origin main:shend_dev
# git pull origin remote-branch-a : local-branch-b

# 中途可能会出现 rebase conflict 手动选择保留哪段代码

# 把 rebas 后并且更新过的代码再 push 到 remote repo；-f 强行
git push -f origin shend_dev

```


---

### 配置文件

#### `.gitconfig`

git 配置文件。

`.gitconfig` 路径：windows - `git\etc\gitconfig`； linux - `~/.gitconfig`

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
```


---

#### `.gitignore`

忽略文件；可在 repo 根目录及其子目录创建多个 `.gitignore` 文件


若在 `.gitignore` 添加忽略文件后不起作用，可使用如下命令：
```bash
git rm --cached file
```


不同编程语言的 `.gitignore` 模板
>[GitHub - github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore)


---

#### `.gitattributes`

用于配置 Git 在处理不同类型文件时的行为


>[.gitattributes](https://github.com/esemble/simpy/blob/master/.gitattributes)

```text
# Auto detect text files and perform LF normalization
# 指示 Git 自动检测文本文件，并在处理它们时执行 LF（Line Feed）规范化操作
* text=auto

# Custom for Visual Studio
# 自定义一些与 Visual Studio 相关的文件的差异显示和合并策略
*.cs     diff=csharp
*.sln    merge=union
*.csproj merge=union
*.vbproj merge=union
*.fsproj merge=union
*.dbproj merge=union

# Standard to msysgit
# 配置一些特定文件类型的差异（diff）显示策略，特别是针对 MSYSGit（旧版Git for Windows）
*.doc	 diff=astextplain
*.DOC	 diff=astextplain
*.docx diff=astextplain
*.DOCX diff=astextplain
*.dot  diff=astextplain
*.DOT  diff=astextplain
*.pdf  diff=astextplain
*.PDF	 diff=astextplain
*.rtf	 diff=astextplain
*.RTF	 diff=astextplain
```

>ChatGPT 生成

- `* text=auto` 的设置会让 Git 尝试自动检测文件类型，将其标记为文本文件，并在需要时执行 LF 规范化（一种处理换行符的方式，通常用于确保在不同操作系统上的文本文件中的行尾都使用相同的行尾字符），以确保文件在版本控制系统中的一致性。这是一种非常常见的设置，特别是在跨平台开发中。
- `astextplain` 是一种 Git 的差异显示策略，它会尝试将二进制文件（如 Word 文档、PDF、RTF 等）视为文本文件，以便更好地显示差异。这对于希望查看这些二进制文件的差异时可能非常有用，**但请注意，它并不会将这些文件真正地转换为文本文件，只是尝试以文本方式进行显示**。
- `*.cs diff=csharp` - 对扩展名为 `.cs` 的文件使用 `csharp` 差异显示策略。这意味着 Git 会尝试以 C# 代码的方式来显示这些文件的差异。
- `union` 合并策略通常用于合并文本文件，它会尝试合并两个不同的版本，并在可能的情况下保留双方的更改。


>[.gitattributes](https://github.com/TonyCrane/note/blob/master/.gitattributes)

```text
*.md linguist-documentation=false linguist-detectable=true
```

>由 ChatGPT 生成

- Linguist - GitHub 中的一种工具，用于自动检测和标识存储库中的代码文件以及其编程语言
- `linguist-documentation=false` - 告诉 Linguist 不要将扩展名为 `.md` 的 文件统计为 documentation(文档) 类型的文件。
- `linguist-detectable=true` - 告诉 Linguist 要将扩展名为 `.md` 的 Markdown 文件标记为可以检测的（detectable）。这表示 Linguist 会尝试检测这些文件的编程语言。虽然 Markdown 通常不是编程语言，但这个规则会让 Linguist 识别它以查找任何可能的代码片段。


---

#### `.gitmodules`

定义子模块（submodule）的相关信息。子模块是一个独立的 Git 仓库，被包含在另一个 Git 仓库中，允许将一个 Git 仓库嵌套在另一个 Git 仓库中，以便在一个项目中使用其他项目的代码。

`git submodule init`、`git submodule update` - 初始化和更新子模块


>[.gitmodules](https://github.com/yujincheng08/ZJU-UGCourse/blob/master/.gitmodules)

```bash
[submodule "simplex"] # 子模块名称
	path = simplex # 子模块在 repo 中的相对路径
	url = git@github.com:yao-zou/simplex.git # 子模块的远程 Git repo url
	branch = master # 分支名
```

添加子模块
```bash
git submodule add https://github.com/username/reop.git
```


---

#### `.git-credential`

>[Git - 凭证存储](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%87%AD%E8%AF%81%E5%AD%98%E5%82%A8)

非标准 git 配置文件。

凭证存储
- 默认所有都不缓存。 每一次连接都会询问用户名和密码。
- “cache” 模式会将凭证存放在内存中一段时间。 密码永远不会被存储在磁盘中，并且在 15 分钟后从内存中清除。
- “store” 模式可以接受一个 `--file <path>` 参数，可以自定义存放密码的文件路径（默认是 `~/.git-credentials` ）

```bash
git config --global credential.helper cache

git config --global credential.helper 'store --file ~/.my-credentials'
```


---

### 多账号 ssh 配置

多账号 ssh 配置作用：
- 多账号管理：通过配置 config 文件，可以方便地管理访问多个仓库时使用的不同账号；
- 通过 ssh 协议，可以免密访问、克隆远程仓库，以及 git 操作（clone、pull 和 push 等）。


生成密钥，将 `id_rsa.gitee.pub` 和 `id_rsa.github.pub` 文件中的内容添加到 github 和 gitee 中的 SSH keys（SSH 公钥）中；
```bash
ssh-keygen -t rsa -f ~/.ssh/id_rsa.gitee -C "XXX@email.com"

ssh-keygen -t rsa -f ~/.ssh/id_rsa.github -C "XXX@email.com"
```


`~/.ssh/config` 文件配置
```bash
# github
Host github.com
    Port 22
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa.github

# gitee
Host gitee.com
    Port 22
    HostName gitee.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitee

# gitlab
Host gitlab.com
    Port 22
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_rsa.gitlab
```


测试
```bash
ssh -T git@github.com

ssh -T git@gitee.com

ssh -T git@gitlab.com
```


若返回信息，则配置成功
```text
Hi XXX! You've successfully authenticated, but GitHub does not provide shell access.

Hi XXX! You've successfully authenticated, but GITEE.COM does not provide shell access.

Welcome to GitLab, XXX!
```


**注：**
- 超算平台中的登陆节点禁止对外的 ssh，无法使用 git 交互环境，建议在 pc 本地或者实验室工作站（manager 和 master）使用。
- 超算平台进行以上设置会出现以下报错：

```bash
ssh: connect to host github.com port 22: Network is unreachable
```

- `~/.ssh/config` 文件出现 `Bad owner or permissions` 错误的解决办法：文件权限位问题，设置 config 文件权限为 `600` （chmod 命令）。


---

### 将 repo 的 remote origin 由 https 改为 ssh 或 token 形式

之后进行 push、pull 等操作时，将默认通过 SSH 协议,并使用 SSH keys 进行身份验证，不需要再输入用户名和密码。

在该 repo 目录中的 `.git/config` 文件找到 `[remote "origin"]` 选项，将 URL 后的 https 地址改成 ssh 形式或带 token 的地址

```bash
# 原
url = https://github.com/user/repo.git

# ssh形式
url = git@gitee.com:user/repo.git
url = git@github.com:user/repo.git

# 带token形式
url = https://user:token@github.com/user/repo.git
url = https://user:token@gitee.com/user/repo.git
```


---

### github 需要用到 token 的地方

github 从 2021 年开始不再支持输入账号和密码的形式进行验证，密码改为 token（gitee 仍是账号和密码验证）。

- git 操作（push）
- 图床
- 与 gitee 进行 repo 同步

具体设置：
Settings - Developer settings - Personal access tokens - Tokens(classic)

---

### 为 repo 创建 gh-pages 分支并 deploy

一般通过第三方的 Github Actions repo
>[GitHub - peaceiris/actions-gh-pages: GitHub Actions for GitHub Pages 🚀 Deploy static files and publish your site easily. Static-Site-Generators-friendly.](https://github.com/peaceiris/actions-gh-pages)

>[GitHub Marketplace · Actions to improve your workflow · GitHub](https://github.com/marketplace?type=actions)


---

### gitee 与 github、gitlab 之间互相同步

**gitee 可以直接从 github 和 gitlab 中导入 repo**

>[仓库镜像管理（Gitee<->Github 双向同步） | Gitee 产品文档](https://help.gitee.com/repository/settings/sync-between-gitee-github)
>[Gitlab、Github、Gitee之间的代码同步\_gitea 和gitee能同步吗\_李·逍遥的博客-CSDN博客](https://blog.csdn.net/lianwen1314/article/details/106384595)


---

## 常用命令

### clone

```bash
# clone 深度
git clone --depth 1 url

# clone 多个分支
git clone -b <branch1> -b <branch2> <url>
```

>提交数量增加，提交过大文件，会使得 `.git/object` 体积增加，可通过 `--depth` 选项来进行浅克隆

---

### config

```bash
# 列出 repo 配置
git config --list
# 列出全局配置
git config --global --list

# 全局设置 
git config --global user.name "username"
git config --global user.email "user@email.com"

# 取消全局配置
git config --global --unset user.name
git config --global --unset user.email
# 取消代理
git config --global --unset http.proxy 
git config --global --unset https.proxy

# git 命令输出里加上颜色
git config --global color.ui 1

# 配置默认编辑器
git config --global core.editor "vim"

# 忽略文件的权限变化
git config core.fileMode false

# 解决 git status 中文乱码 问题
git config --global core.quotepath false

# 开启自动纠错功能
git config --global help.autocorrect 1

# 列出配置即对应配置文件路径
git config --list --show-origin
```


---

### add

```bash
git add file
```


---

### commit

```bash
# 根据当前时间进行 commit
git commit -m "$(date '+%Y-%m-%d %H:%M:%S')"

# 修改 commit 信息
git commit --amend --no-edit -m "xxx"

# 创建没有任何改动的提交
git commit -m "empty" --allow-empty
```

>[创建没有任何改动的提交](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md#%E6%B2%A1%E6%9C%89%E4%BB%BB%E4%BD%95%E6%94%B9%E5%8A%A8%E7%9A%84%E6%8F%90%E4%BA%A4)


---

### push

```bash
git push
```


---

### pull

```bash
git pull
```


---

### branch

```bash
git branch 

# 查看所有分支（本地+远程分支）
git branch -a

# 查看远程分支
git branch -r

git brach -u

git branch -m

# 删除本地分支前，会提醒是否进行分支的合并
git branch -d <branch_name>

# 强制删除本地分支
git branch -D <branch_name>

# 列出当前仓库中所有分支的信息，包括每个分支的名称、关联的远程分支、远程分支的提交和本地分支的提交
git branch -vv

# 示例
* master f6423c9 [origin/master] update
```


---

### checkout

```bash
# 切换到新分支
git checkout <branch_name>

# 创建并进入新分支
git checkout -b <branch_name>

# 迅速切换到上一个分支
git checkout -

# 关联分支
git checkout -b <branch_name> origin/<branch_name>  
```


---

### remote

```bash
# 使本地的跟踪分支列表与远程保持一致，删除远程分支已经不存在而本地还保留的跟踪记录
git remote prune origin
# 不实际删除
git remote prune origin --dry-run

# 查看远程 repo 的所有分支
git remote show origin

# 列出远程仓库的引用（分支和标签）
git ls-remote origin

# 
git remote rm origin
```


---

### status

```bash
git status

git status --short --branch
```


---

### reset

```bash
# 撤销整个暂存区的 add 操作
git reset

# 撤回最后一次 commit 保留代码修改
git reset HEAD~
# --hard 不保留代码修改
git reset HEAD~ --hard

# 撤销指定文件 add 操作
git reset <file>

# 退回到指定的 commit hash 值所在版本
git reset --hard <commit_hash>
```


---

### fetch

```bash
# 从远程仓库（所有分支）获取最新版本到本地仓库，但不会自动 merge 或 rebase 到当前分支
git fetch origin
```


---

### merge

```bash
# 合并时使用 vim 编辑器
GIT_EDITOR=vim git merge tmp
```


---

### tag

```bash
# 查看本地标签
git tag

# 查看远程标签
git ls-remote --tags origin

# 新建标签
git tag v1.0.0

# 新建带注释标签
git tag -a v1.0.0 -m 'Nb-Si projects scripts until on 20230723'

# push 标签
git push origin v1.0.0
# push 所有标签
git push origin --tags

# 删除本地标签
git tag -d v0.0.1

# 删除远程标签
git push origin :refs/tags/v0.0.1
# 删除所有远程标签
git push origin --delete $(git tag -l)

# pull 远程所有内容包括标签
git pull --all

# 列出标签
git tag -l
# 列出标签及其注释
git tag -ln

# 查看具体标签信息
git show v1.0.0
```


---

### log

日志 log
```bash
# 查看提交日志
git log

# 以一行的形式显示提交日志，commit_id 为 8 个字符
git log --oneline
# 完整的 commit_id
git log --pretty=oneline

# 显示倒数第几条 log
git log -n N
git log HEAD~1 --oneline

# 查看含有 "update" 关键字的提交日志
git log --grep=update

# 查看所有分支的所有操作记录
git reflog

# 较为美观的 git log 输出样式 参考 zsh git alias
git log --oneline --graph --stat
git log --graph --pretty="%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset" --stat
```


---

### diff

```bash
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
```

---

### stash

用于临时保存当前工作目录和暂存区的未提交更改，从而获得一个干净的工作状态。这个功能在需要快速切换任务或分支时特别有用，因为它允许保存当前进度而不必进行提交，然后在适当的时候再恢复这些更改。

---

暂存项（stashes）是按照它们被创建的时间顺序排序的，遵循一个栈的结构（后进先出）。这意味着最近暂存的更改会被放置在栈的顶部（索引为 0），而之前的暂存项则按照它们被添加的顺序依次排列。

- `stash@{0}`: 这代表着栈顶的暂存项，即最近一次的暂存。
- `stash@{1}`: 这是紧随其后的暂存项，即倒数第二次的暂存。

---

```bash
# 将当前修改暂存到 stash 栈中
git stash

# 显示 stash 中的所有暂存
git stash list

# 恢复 stash 中的最近一次暂存，并从 stash 栈中删除
git stash pop

# 恢复 stash 中的最近一次暂存，但不从 stash 栈中删除
git stash apply

# 恢复特定的 stash
git stash apply stash@{n}

# 删除 特定的 stash
git stash drop stash@{n}

# 清空 stash 中的所有暂存
git stash clear

# 包括 untracked 的文件
git stash -u

# 从 stash 中创建一个新的分支
git stash branch <branch> 
```


---

### rm

>[从工作区批量去除已删除文件](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md#%E4%BB%8E%E5%B7%A5%E4%BD%9C%E5%8C%BA%E5%8E%BB%E9%99%A4%E5%A4%A7%E9%87%8F%E5%B7%B2%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6)

```bash
# 从工作区批量去除已删除文件
git rm $(git ls-files -d)

# 删除 push 到远程 repo 的文件/目录
git rm --cached file
git rm -r --cached folder
```



---

### oh-my-zsh 中 git 命令相关 alias

查看 - `alias | grep 'git'`

---

```bash
# git add 相关
ga='git add'
gaa='git add --all'
gapa='git add --patch'
gau='git add --update'
gav='git add --verbose'
gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign --message "--wip-- [skip ci]"'


# git commit 相关
gc='git commit --verbose'
'gc!'='git commit --verbose --amend'
gca='git commit --verbose --all'
'gca!'='git commit --verbose --all --amend'
gcam='git commit --all --message'
'gcan!'='git commit --verbose --all --no-edit --amend'
'gcans!'='git commit --verbose --all --signoff --no-edit --amend'
gcas='git commit --all --signoff'
gcasm='git commit --all --signoff --message'
gcmsg='git commit --message'
'gcn!'='git commit --verbose --no-edit --amend'
gcs='git commit --gpg-sign'
gcsm='git commit --signoff --message'
gcss='git commit --gpg-sign --signoff'
gcssm='git commit --gpg-sign --signoff --message'
gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign --message "--wip-- [skip ci]"'


# git push 相关
ggpush='git push origin "$(git_current_branch)"'
git-svn-dcommit-push='git svn dcommit && git push github $(git_main_branch):svntrunk'
gp='git push'
gpd='git push --dry-run'
gpf='git push --force-with-lease'
'gpf!'='git push --force'
gpoat='git push origin --all && git push origin --tags'
gpod='git push origin --delete'
gpsup='git push --set-upstream origin $(git_current_branch)'
gpsupf='git push --set-upstream origin $(git_current_branch) --force-with-lease'
gpu='git push upstream'
gpv='git push --verbose'


# git pull 相关
ggpull='git pull origin "$(git_current_branch)"'
gl='git pull'
gluc='git pull upstream $(git_current_branch)'
glum='git pull upstream $(git_main_branch)'
gpr='git pull --rebase'
gup='git pull --rebase'
gupa='git pull --rebase --autostash'
gupav='git pull --rebase --autostash --verbose'
gupom='git pull --rebase origin $(git_main_branch)'
gupomi='git pull --rebase=interactive origin $(git_main_branch)'
gupv='git pull --rebase --verbose'


# git checkout 相关
gcb='git checkout -b'
gcd='git checkout $(git_develop_branch)'
gcm='git checkout $(git_main_branch)'
gco='git checkout'
gcor='git checkout --recurse-submodules'


# git reset相关
gpristine='git reset --hard && git clean --force -dfx'
grh='git reset'
grhh='git reset --hard'
groh='git reset origin/$(git_current_branch) --hard'
gru='git reset --'
gunwip='git rev-list --max-count=1 --format="%s" HEAD | grep -q "\--wip--" && git reset HEAD~1'


# git status 相关
gsb='git status --short --branch'
gss='git status --short'
gst='git status'


# git diff 相关
gd='git diff'
gdca='git diff --cached'
gdcw='git diff --cached --word-diff'
gds='git diff --staged'
gdt='git diff-tree --no-commit-id --name-only -r'
gdup='git diff @{upstream}'
gdw='git diff --word-diff'


# git tag 相关
gtl='gtl(){ git tag --sort=-v:refname -n --list "${1}*" }; noglob gtl'
gts='git tag --sign'
gtv='git tag | sort -V'


# git remote 相关
gr='git remote'
gra='git remote add'
grmv='git remote rename'
grrm='git remote remove'
grset='git remote set-url'
grup='git remote update'
grv='git remote --verbose'


# git config 相关
gcf='git config --list'


# git rm 相关
grm='git rm'
grmc='git rm --cached'


# git rebase 相关
grb='git rebase'
grba='git rebase --abort'
grbc='git rebase --continue'
grbd='git rebase $(git_develop_branch)'
grbi='git rebase --interactive'
grbm='git rebase $(git_main_branch)'
grbo='git rebase --onto'
grbom='git rebase origin/$(git_main_branch)'
grbs='git rebase --skip'


# git merge 相关
gm='git merge'
gma='git merge --abort'
gmom='git merge origin/$(git_main_branch)'
gms='git merge --squash'
gmtl='git mergetool --no-prompt'
gmtlvim='git mergetool --no-prompt --tool=vimdiff'
gmum='git merge upstream/$(git_main_branch)'


# git fetch 相关
gf='git fetch'
gfa='git fetch --all --prune --jobs=10'
gfo='git fetch origin'


# git submodule 相关
gsi='git submodule init'
gsu='git submodule update'


# git reset 相关
gpristine='git reset --hard && git clean --force -dfx'
grh='git reset'
grhh='git reset --hard'
grhk='git reset --keep'
grhs='git reset --soft'
groh='git reset origin/$(git_current_branch) --hard'
gru='git reset --'
gunwip='git rev-list --max-count=1 --format="%s" HEAD | grep -q "\--wip--" && git reset HEAD~1'


# git clone 相关
gcl='git clone --recurse-submodules'


# git stash 相关
gsta='git stash push'
gstaa='git stash apply'
gstall='git stash --all'
gstc='git stash clear'
gstd='git stash drop'
gstl='git stash list'
gstp='git stash pop'
gsts='git stash show'


# git revert 相关
grev='git revert'

# git show 相关
gsh='git show'
gsps='git show --pretty=short --show-signature'

# git switch 相关
gsw='git switch'
gswc='git switch --create'
gswd='git switch $(git_develop_branch)'
gswm='git switch $(git_main_branch)'

```



---

## 其他用法

### push 到多个远程 repo

>[git-tips#文件推向3个git库](https://github.com/jaywcjlove/git-tips#%E6%96%87%E4%BB%B6%E6%8E%A8%E5%90%913%E4%B8%AAgit%E5%BA%93)

```bash
# 添加远程 repo url
git remote add origin git@gitee.com:username/repo.git
git remote set-url --add origin git@github.com:username/repo.git
git remote set-url --add origin git@gitlab.com:username/repo.git

# 删除远程 repo url
git remote set-url --delete origin git@github.com:username/repo.git
```

>只能从 `origin` 里的一个 repo url pull 代码，默认为添加到 `origin` 的第一个地址；若需调整 repo url 顺序，可在 `./.git/config` 文件中直接调整

>可用此方法替代 gitee 与 github 之间互相同步的设置

---

### 删除本地及对应的远程分支

```bash
# 删除本地分支
git branch -D <local-branch>

# 删除远程分支
git push origin :<remote-branch>
git push origin --delete <remote-branch>

# 删除远程分支已经不存在而本地还保留的跟踪记录
git remote prune origin
```


---

### 提交空文件夹

在空文件夹中创建 `.gitkeep` 文件。


---

### git clone 部分内容

>[如何使用 Git 只克隆部分文件 | 猎人杂货铺](https://hunterx.xyz/git-sparse-checkout.html#more)


```bash
# 方式 1 速度更快
git clone --filter=blob:none --sparse <repo>
git sparse-checkout set <file> <folder>

# 方式 2
git clone --filter=blob:none --no-checkout <repo>
git checkout origin/main -- <file> <folder>
```

>`git sparse-checkout` - 可实现只克隆或检出指定文件夹，不下载所有内容

>`--filter=blob:none` - 只获取元数据，不下载原始数据部分


---

### 下载单个文件

打开文件，点击 “Raw”，用 `wget` 下载，示例：

```bash
# gitee
wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O install.sh

# github
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O install.sh

# gist
wget https://gist.githubusercontent.com/user/GIST_ID/raw/filename -O filename
```


---

### git 自定义别名

>[查看历史 - Git 重学指南](https://git-remake.wybxc.cc/%E5%82%A8%E5%AD%98%E5%BA%93/%E6%9F%A5%E7%9C%8B%E5%8E%86%E5%8F%B2.html)

>[git-命令自定义别名](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md#git-%E5%91%BD%E4%BB%A4%E8%87%AA%E5%AE%9A%E4%B9%89%E5%88%AB%E5%90%8D)

```bash
# 设置之后直接使用 git ls
git config --global alias.ls "log --no-merges --color --graph --date=format:'%Y-%m-%d %H:%M:%S' --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cd) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

或在 `~/.gitconfig` 添加如下内容
```bash
[alias]
  co = checkout
  cm = commit
  p = push
  tags = tag -l
  branches = branch -a
  remotes = remote -v
```


---

### GitHub 加速下载

>[Github 增强 - 高速下载](https://greasyfork.org/zh-CN/scripts/412245-github-%E5%A2%9E%E5%BC%BA-%E9%AB%98%E9%80%9F%E4%B8%8B%E8%BD%BD)

安装 GitHub 增强插件

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401082135895.png)



---

### 规范式 commit

gitmoji-cli：git commit 时使用 emoji
>[GitHub - carloscuesta/gitmoji-cli: A gitmoji interactive command line tool for using emojis on commits. 💻](https://github.com/carloscuesta/gitmoji-cli)
>[gitmoji 速查表 - Git 重学指南](https://git-remake.wybxc.cc/%E9%99%84%E5%BD%95/gitmoji-%E9%80%9F%E6%9F%A5%E8%A1%A8.html)


---

### 查看两个星期内的改动

```bash
git whatchanged --since='2 weeks ago'
```


---

### 创建发行版（Releases）

#### 手动

Create a new release - Choose a tag，之后填写相关信息，必要时附加文件

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081713870.png)


---

#### 通过 GitHub CLI

>[GitHub - cli/cli: GitHub’s official command line tool](https://github.com/cli/cli)

- 安装

```bash
# Ubuntu
sudo apt update
sudo apt install gh

# Arch Linux
sudo pacman -S github-cli

# Mac
brew install gh

# Conda
conda install gh --channel conda-forge
```

- 手动编译安装

```bash
# 安装 golang
curl -sS https://webi.sh/golang | sh

git clone https://github.com/cli/cli.git gh-cli
cd gh-cli

make install prefix=$HOME/src/gh

ln -s ~/src/gh/bin/gh ~/bin
```

- 验证登录 按照提示进行

```bash
gh auth login
```

- 创建 release 并上传文件

```bash
# 创建 release
gh release create v0.0.1

# 上传附加文件
gh release upload v0.0.1 file

# 列出 releases
gh release list

```

>file 格式可以是压缩文件，`pdf`，`md` 等，`txt` 不行

- 创建 issue

```bash
gh issue create --title "gh issue test" --body "create an issue by gh"
```


---

### 新建空分支

github 中的 `gh-pages` 分支为特殊分支，可与主分支无关联（push 时会自动启用 Github Actions），**其他命名的分支暂无法实现与主分支无关联**

>[git - Create empty branch on GitHub - Stack Overflow](https://stackoverflow.com/questions/34100048/create-empty-branch-on-github)
```bash
git switch --orphan <new branch> 
git commit --allow-empty -m "Initial commit on orphan branch" 
git push -u origin <new branch>
```



---

## 相关问题

- github 和 gitee 中的 md 文档无法渲染 `\begin{}` 等 LaTeX 命令
- github 可以渲染 Front-Matter，gitee 和 typora 暂不行，但会将其包裹起来

---

>[坑：ssh: connect to host github.com port 22: Connection refused - 知乎](https://zhuanlan.zhihu.com/p/521340971)

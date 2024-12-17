---
title: Linux 命令行工具
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Linux 命令行工具
description: Linux 命令行工具
tags:
  - CLI
  - 命令行工具
categories:
  - Linux
date: 2023-09-18 09:00:00
abbrlink: 168542
password:
---

# Linux 命令行工具

## 介绍

- 命令行工具安装方式：
    - 官网下载二进制文件
    - 包管理器
        - Linux：Ubuntu（apt、snap 等）、Arch Linux（pacman、yay 等）
        - Windows：Scoop、Winget、Chocolatey 等
        - macOS：Homebrew
        - 程序端：Python（pip、pipx、conda），Rust（cargo），Nodejs（npm），Go（go）
    - 从 [webinstall.dev](https://webinstall.dev/) 网站安装（后三者可以在无 root 权限情况下安装）
    - 源码编译安装

- 参考资料：
    - [命令行常用工具的替代品 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2022/01/cli-alternative-tools.html)
    - [GitHub - ibraheemdev/modern-unix: A collection of modern/faster/saner alternatives to common unix commands.](https://github.com/ibraheemdev/modern-unix)
    - 有意思/搞笑的 GitHub repo：[GitHub - terremoth/awesome-hilarious-repos: Awesome hilarious github repositories](https://github.com/terremoth/awesome-hilarious-repos)
    - [My Favorite CLI Tools](https://switowski.com/blog/favorite-cli-tools/)



---

## 命令行工具

### 概览

>lsd、ripgrep、sd、bat、git-delta、gitui 等由 Rust 编写的 CLI 均可通过 cargo 安装

系统相关

- Shell（个人感觉没有 zsh 好用）
    - nushell
    - fish

- 快速跳转目录：[z - jump around](https://github.com/rupa/z)（可用于 Bash 和 zsh）

- 替代 `man`
    - [tldr](https://github.com/tldr-pages/tldr)（有时会失效）
    - [eg](https://github.com/srsudar/eg)
    - [navi](https://github.com/denisidoro/navi)（默认的 cheatsheet 很少，效果一般）

- `CTRL + R` 历史命令升级版：[mcfly](https://github.com/cantino/mcfly)

- 替代 `ls`
    - [lsd](https://github.com/lsd-rs/lsd)（可显示文件的 git 状态）
    - [eza](https://github.com/eza-community/eza)（exa 的维护版本；可显示文件的 git 状态）
    - [exa](https://github.com/ogham/exa)（已不再更新）

- 替代 `grep`
    - [ripgrep](https://github.com/BurntSushi/ripgrep)（命令 `rg`）
    - [peco](https://github.com/peco/peco)（交互式）
    - [ripgrep-all](https://github.com/phiresky/ripgrep-all)（命令 `rga`；可在 PDF、E-Books、Office 文档、压缩文件等查找内容）

- 替代 `sed`：[sd](https://github.com/chmln/sd)

- 替代 `cat`：[bat](https://github.com/sharkdp/bat)（可与 Git 结合使用）

- 替代 `find`：[fd](https://github.com/sharkdp/fd)（cargo 安装时为 `fd-find`）

- 替代 `diff`：[difftastic](https://github.com/Wilfred/difftastic)（命令 `difft`）

- 替代 `ps`：[procs](https://github.com/dalance/procs)

- 替代 `top`
    - [btop](https://github.com/aristocratos/btop)
    - [htop](https://github.com/htop-dev/htop)

- 查看系统资源：[glances](https://github.com/nicolargo/glances)

- 监测 GPU（Nvidia 和 AMD 等）
    - [nvtop](https://github.com/Syllo/nvtop#distribution-specific-installation-process)
    - [nvitop](https://github.com/XuehaiPan/nvitop)

- 监测 CPU 压力：[GitHub - amanusk/s-tui: Terminal-based CPU stress and monitoring utility](https://github.com/amanusk/s-tui)

- 显示系统信息
    - [neofetch](https://github.com/dylanaraps/neofetch)、[neofetch-themes](https://github.com/Chick2D/neofetch-themes)
    - [fastfetch](https://github.com/fastfetch-cli/fastfetch)（比 neofetch 更快）
    - [hyfetch](https://github.com/hykilpikonna/hyfetch)
    - macchina

- 磁盘分析
    - [ncdu](https://dev.yorhel.nl/ncdu)（有时较耗时）
    - dysk（仅限 Linux）

- 查看 coreutils 工具的进度条：[progress](https://github.com/Xfennec/progress)

- 安全替代 `rm` 
    - [trash.sh](https://github.com/qqAys/trash.sh)
    - [GitHub - MilesCranmer/rip2: A safe and ergonomic alternative to rm](https://github.com/MilesCranmer/rip2)

- [GitHub - theryangeary/choose: A human-friendly and fast alternative to cut and (sometimes) awk](https://github.com/theryangeary/choose)

- 带宽：[bandwhich](https://github.com/imsnif/bandwhich)

- Linux 经典命令增强（命令 help 含义汉化）：[X-CMD - 开源轻量级 POSIX 脚本，用于管理工具 (500+) 和提供经典命令扩展](https://cn.x-cmd.com/)


---

Markdown 相关

- 终端 Markdown 渲染
    - [frogmouth](https://github.com/Textualize/frogmouth)
    - [glow](https://github.com/charmbracelet/glow)
    - [GitHub - swsnr/mdcat: cat for markdown](https://github.com/swsnr/mdcat)
    - 以 PPT 形式查看 md 文档：[GitHub - maaslalani/slides: Terminal based presentation tool](https://github.com/maaslalani/slides)


---

文件相关

- 文件模糊查找：[fzf](https://github.com/junegunn/fzf)

- 终端文件管理器
    - [yazi](https://github.com/sxyazi/yazi)
    - [superfile](https://github.com/MHNightCat/superfile)
    - [nnn](https://github.com/jarun/nnn)
    - [joshuto](https://github.com/kamiyaa/joshuto)
    - [ranger](https://github.com/ranger/ranger)
    - [lf](https://github.com/gokcehan/lf)（效果一般）

- 文件传输
    - [GitHub - schollz/croc](https://github.com/schollz/croc)
    - TUI 版本，支持 SCP/SFTP/FTP/S3/SMB：[GitHub - veeso/termscp:](https://github.com/veeso/termscp)

- [f2](https://github.com/ayoisaiah/f2)：文件批量重命名

- 检测文件内容类型（文本、文档、代码等）：[GitHub - google/magika: Detect file content types with deep learning](https://github.com/google/magika)


---

编程相关

- 命令纠正：[thefuck](https://github.com/nvbn/thefuck)

- 统计代码行数：[cloc](https://github.com/AlDanial/cloc#quick-start-)

- 统计目录中的代码行数：[scc](https://github.com/boyter/scc)（类似 cloc）


---

图片相关

- 终端显示图片（效果一般）：[GitHub - SilinMeng0510/imgcatr: cat for images, by RUST 🦀️](https://github.com/SilinMeng0510/imgcatr)

- 将源代码生成美观图片
    - [silicon](https://github.com/Aloxaf/silicon)
    - [carbon](https://github.com/carbon-app/carbon)

- 将输入的图片，使用几何形状重新绘制：[GitHub - fogleman/primitive: Reproducing images with geometric primitives.](https://github.com/fogleman/primitive)


---

其他

- [sshx](https://github.com/ekzhang/sshx)：通过链接共享终端（可创建多个终端画布）

- 富文本：[rich](https://github.com/textualize/rich)

- 字符 logo 制作：figlet、toilet：[Linux 运维相关 — OnlineNote latest documentation](https://codenote.readthedocs.io/en/latest/linux.html#figlet)

- 文本编辑器（类似 Vim）：[helix](https://github.com/helix-editor/helix)

- 趣味小工具
    - cowsay（牛说）
    - sl（火车）
    - fortune（幸运饼干；格言）
    - lolcat
    - boxes
    - cmatrix（黑客帝国类似的矩阵效果）
    - asciiquarium（水族馆）


---

### 具体使用

- fzf 进阶用法
    - [fzf/ADVANCED.md at master · junegunn/fzf · GitHub](https://github.com/junegunn/fzf/blob/master/ADVANCED.md)
    - [Linux 上有哪些工具软件堪称精美？ - 知乎](https://www.zhihu.com/question/28596616/answer/3487536522)
    - 可将 find、grep、history 等查找命令与 fzf 通过管道符连接，实现前者命令的模糊查找

```bash
# 搜索整个 apt package；回车安装
apt-cache search '' | sort | cut --delimiter ' ' --fields 1 | fzf --multi --cycle --reverse \ --preview-window=right:70%:wrap \ --preview 'apt-cache show {1}' | xargs -r sudo apt install -y

# 用 bat 作为 previewer
fzf --preview "bat --color=always --style=numbers --line-range=:500 {}"
```

- 用 fzf-tab 替代 zsh 的自动补全：[GitHub - Aloxaf/fzf-tab](https://github.com/Aloxaf/fzf-tab)
    - 需将 fzf-tab 写在 zsh-autosuggestions、fast-syntax-highlighting 插件前，compinit 后

```bash
# 安装
git clone --depth 1 https://github.com/Aloxaf/fzf-tab ${ZSH_CUSTOM}/plugins/fzf-tab

# fzf-tab 配置；写入 ~/.zshrc
# disable sort when completing `git checkout`
zstyle ':completion:*:git-checkout:*' sort false
# set descriptions format to enable group support
# NOTE: don't use escape sequences here, fzf-tab will ignore them
zstyle ':completion:*:descriptions' format '[%d]'
# set list-colors to enable filename colorizing
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
# force zsh not to show completion menu, which allows fzf-tab to capture the unambiguous prefix
zstyle ':completion:*' menu no
# preview directory's content with eza when completing cd
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'eza -1 --color=always $realpath'
# switch group using `<` and `>`
zstyle ':fzf-tab:*' switch-group '<' '>'
```

---

```bash
# z 安装与配置
git clone https://github.com/rupa/z.git

# 将以下内容添加至 ~/.{bash,zsh}rc
. /path/to/z.sh


# turm 安装
cargo install turm

# peco 安装与使用
brew install peco  # 安装

cat file | peco    # 基本使用


ncdu -o ncdu.txt   # 输出信息到文件中


# navi 使用
navi repo browse   # 按需添加 cheatsheet git repo 以增加丰富性


# fzf 安装、升级
# 安装
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
# 升级
cd ~/.fzf && git pull && ./install


# rg 使用
# -g 过滤搜索
rg 'content' -g '!docs/'  # 排除
rg 'content' -g '*.py'    # 包含


# ripgrep-all 安装与使用
brew install pandoc poppler ffmpeg  # 需提前安装
brew install rga

rga 'XXX' file.pdf  # 使用；文件后缀可以是 docx、zip、epub 等

# 与 fzf 集成；写入 ~/.{bash,zsh}rc 中
rga-fzf() {
    RG_PREFIX="rga --files-with-matches"
    local file
    file="$(
        FZF_DEFAULT_COMMAND="$RG_PREFIX '$1'" \
            fzf --sort --preview="[[ ! -z {} ]] && rga --pretty --context 5 {q} {}" \
                --phony -q "$1" \
                --bind "change:reload:$RG_PREFIX {q}" \
                --preview-window="70%:wrap"
    )" &&
    echo "opening $file" &&
    xdg-open "$file"
}


# eg 安装
pip install -U eg
brew install eg-examples


# figlet toilet 相关用法
showfigfonts      # 查看可用字体
figlet spt        # 生成字符 logo
figlet -c spt     # 居中
figlet spt | toilet -f term --gay  # 彩色输出


# mcfly 安装与配置
brew install mcfly        # macOS
# Linux/macOS
curl -LSfs https://raw.githubusercontent.com/cantino/mcfly/master/ci/install.sh | sh -s -- --git cantino/mcfly

eval "$(mcfly init zsh)"  # 配置


# fastfetch Ubuntu 安装
sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt update

sudo apt install fastfetch


# starship
# 安装
curl -sS https://starship.rs/install.sh | sh  # Linux
brew install starship  # macOS

# 配置
eval "$(starship init zsh)"   # zsh
eval "$(starship init bash)"  # bash
Invoke-Expression (&starship init powershell) # PowerShell


# rename 文件重命名
brew install rename
sudo apt install rename


# primitive 安装与使用
go install github.com/fogleman/primitive@latest

export PATH=$(go env GOPATH)/bin:$PATH

primitive -i input.png -o output.png -n 100
```

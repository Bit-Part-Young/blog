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
categories:
  - Linux
date: 2023-09-18 09:00:00
abbrlink: 168542
password:
---

# Linux 命令行工具

## 介绍

命令行工具安装方式：

- Linux 端：Ubuntu（apt、snap 等）、Arch Linux（pacman、yay 等）
- Windows 端：scoop、winget 等
- Mac 端：brew；
- 程序端：Python（pip、pipx、conda），Rust（cargo），Nodejs（npm）
- 从 [webinstall.dev](https://webinstall.dev/) 网站安装（后三者可以在无 root 权限情况下安装）
- 源码编译安装

---

参考资料：

- [命令行常用工具的替代品 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2022/01/cli-alternative-tools.html)
- [GitHub - ibraheemdev/modern-unix: A collection of modern/faster/saner alternatives to common unix commands.](https://github.com/ibraheemdev/modern-unix)
- 有意思/搞笑的 GitHub repo：[GitHub - terremoth/awesome-hilarious-repos: Awesome hilarious github repositories](https://github.com/terremoth/awesome-hilarious-repos)



---

## zsh

- 提升终端使用体验
	- 插件丰富：可实现命令自动补全、高亮、建议；`x` 解压任意格式压缩文件；`z` 路径快速跳转等
	- 丰富的 git 命令 alias，git 状态可视化
- master、manager 上没有 zsh；Pi 和思源一号有 zsh，但版本较老
- zsh 系列插件：[awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins)
- 管理 zsh 配置：[ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)
- 管理 bash 配置：[oh-my-bash](https://github.com/ohmybash/oh-my-bash)（没 ohmyzsh 好用）


---

### 安装

- 通过 Package Managers

```bash
sudo apt install zsh  # Ubuntu
sudo pacman -S zsh    # Arch Linux
brew install zsh      # macOS
```

---

- 源码编译：依赖 ncurses；[Building Zsh from Source and Configuring It on CentOS - jdhao's digital space](https://jdhao.github.io/2018/10/13/centos_zsh_install_use/)

编译 ncurses（构建 TUI（文本用户界面）的库）

```bash
wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.4.tar.gz --no-check-certificate

./configure --prefix=${HOME}/local CXXFLAGS="-fPIC" CFLAGS="-fPIC"

make -j && make install
```

编译 zsh

```bash
wget https://sourceforge.net/projects/zsh/files/zsh/5.9/zsh-5.9.tar.xz/download -O zsh-5.9.tar.xz --no-check-certificate

./configure --prefix="${HOME}/local" CPPFLAGS="-I${HOME}/local/include" LDFLAGS="-L${HOME}/local/lib"

make -j && make install
```

---

- Windows：
	- 两种方式：WSL + zsh，Git Bash + zsh：[Windows高效开发环境配置（一） - 北鱼扶摇](https://ifuyao.com/blog/install-zsh-and-oh-my-zsh-in-windows-git-bash/)、[在 Windows 中使用 Bash shell - 北辞](https://northword.cn/code/bash-for-windows/)
	- Windows Terminal 以及 VSCode 本地设置默认终端为 Git Bash：[Windows Terminal添加Git Bash支持 - TruthHell - 博客园](https://www.cnblogs.com/cong-wang/p/15026535.html)

下载 zsh 包；复制 `etc/`、`usr/` 到 Git 安装目录中；打开 Git Bash，执行命令 `zsh`

```bash
wget https://mirror.msys2.org/msys/x86_64/zsh-5.9-2-x86_64.pkg.tar.zst

tar --zstd -xvf zsh-5.9-2-x86_64.pkg.tar.zst
```

设置 zsh 为默认 shell，在 `.bashrc` 添加：

```bash
 # Enable zsh
 if [ -t 1 ]; then
    exec zsh
 fi
```

修改 Windows Terminal 的 `settings.json` 内容：

```json
{
    // ...
    // 添加项 
    // 默认启动为 Git Bash
    "defaultProfile": "{5D1F95DF-36E8-56AD-C203-EA75CE06422C}",
    // "defaultProfile": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
    // ...
        "list": 
        [			
            // 添加项
	        {
                "guid" : "{5D1F95DF-36E8-56AD-C203-EA75CE06422C}",
                "name" : "Git Bash",
                "commandline" : "D:\\Scoop\\apps\\git\\current\\bin\\bash.exe --login -i",
                "icon" : "D:\\Scoop\\apps\\git\\current\\usr\\share\\git\\git-for-windows.ico",
                "startingDirectory": "C:\\Users\\XXX\\Desktop"
            },
		    // ...
        ],
    },
}
```

---

- 设置 zsh 为默认 shell

```bash
# 有 root 权限
chsh -s /bin/zsh

# 无 root 权限 在 ~/.bashrc_profile 添加以下内容（不建议）
export PATH=$HOME/bin:$PATH
export SHELL=`which zsh`
[ -f "$SHELL" ] && exec "$SHELL" -l
```


---

### 配置

- 安装 ohmyzsh

```bash
# gitee 源
sh -c "$(curl -fsSL https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh)"  # via curl
sh -c "$(wget https://gitee.com/Devkings/oh_my_zsh_install/raw/master/install.sh -O -)"  # via wget

# github 源
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"  # via curl
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"  # via wget
```

- 插件下载：
	- powerlevel10k（主题）
	- zsh-completions（自动补全）
	- zsh-syntax-highlighting（高亮）
	- zsh-autosuggestions（建议）
	- zsh prompt（可选）：[spaceship-prompt](https://github.com/spaceship-prompt/spaceship-prompt)

```bash
# github 源
git clone --depth=1 https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM}/plugins/zsh-completions && \
git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions && \
git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting && \
git clone --depth=1 https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/fast-syntax-highlighting && \
git clone --depth=1 https://github.com/jeffreytse/zsh-vi-mode ${ZSH_CUSTOM}/plugins/zsh-vi-mode && \
git clone --depth=1 https://github.com/MichaelAquilina/zsh-you-should-use.git ${ZSH_CUSTOM}/plugins/you-should-use && \
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM}/themes/powerlevel10k && \
# 可选
# git clone --depth=1 https://github.com/spaceship-prompt/spaceship-prompt.git ${ZSH_CUSTOM}/themes/spaceship-prompt && \
# ln -s ${ZSH_CUSTOM}/themes/spaceship-prompt/spaceship.zsh-theme ${ZSH_CUSTOM}/themes/spaceship.zsh-theme

# gitee 源
git clone --depth=1 https://gitee.com/yuhldr/zsh-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/zsh-syntax-highlighting && \
git clone --depth=1 https://gitee.com/yuhldr/zsh-autosuggestions ${ZSH_CUSTOM}/plugins/zsh-autosuggestions && \
git clone --depth=1 https://gitee.com/yuhldr/zsh-completions ${ZSH_CUSTOM}/plugins/zsh-completions && \
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM}/themes/powerlevel10k
```

- 备份 `~/.zshrc`（如果有）

- 重新登录，会进入配置 powerlevel10k 的交互，按照指示自定义设置即可

```bash
omz update      # 更新 ohmyzsh
p10k configure  # 配置 powerlevel10k
```


---

### 插件

- ohmyzsh 有用的内置与外置插件：[Plugins · ohmyzsh/ohmyzsh Wiki · GitHub](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)
- [GitHub - magicmonty/bash-git-prompt: An informative and fancy bash prompt for Git users](https://github.com/magicmonty/bash-git-prompt)
- zsh tips tricks examples: [ZSH-LOVERS(1)](https://grml.org/zsh/zsh-lovers.html)

```bash
# 内置插件
z    # 目录自动跳转，模糊匹配最近进入过的目录
git  # 丰富的 git alias

# 外置插件
zsh-syntax-highlighting
zsh-autosuggestions
zsh-completions
zsh-fast-syntax-highlighting
zsh-you-should-use
zsh-vi-mode  # Crtl + [ 进入 Normal mode
zsh-lovers
zsh-git-prompt

# bash 插件
bash-git-prompt       # 效果还不错
bash-language-server  # 有 Bash IDE 的 VSCode 插件
bash-completion
bash-snippets         # 有 cheat 等可执行命令
```


---

### 相关问题

- zsh 中的 `[nyae]` 的含义：[What does nyae mean in Zsh? - Stack Overflow](https://stackoverflow.com/questions/800182/what-does-nyae-mean-in-zsh)
- zsh 安装后，`Home / End` 键可能会失效，对应快捷键：`Home = Ctrl + A`，`End = Ctrl + E`。


---

## 数据处理相关命令行工具

- csv 命令行工具：csvkit（Python）

```bash
in2csv data.xlsx | csvlook  # excel 表格转 csv 表格查看

csvlook data.csv | head  # 以表格形式查看

csvcut -n data.csv  # 查看列名
csvscut -c 1,2,3 data.csv   # 查看特定列数据 1 2 3 也可以是具体列名

csvstat --count data.csv  # 统计行数
csvstat file.csv  # 统计所有列的情况
csvstat -c 1,2,3 data.csv  # 统计特定列
```

- josn 命令行工具：jq、[jnv](https://github.com/ynqa/jnv)（交互式）

```bash
cat data.json | jq .  # 输出 json 文件内容

cat data.json | jq '.user.name'  # 获取特定键值
```

- JSON、YAML、TOML、HCL 格式之间互相转换：[yj](https://github.com/sclevine/yj)

```bash
brew install yj          # macOS 安装

yj -jy < package.json    # JSON 转 YAML
yj -yj < deploy.yml      # YAML 转 JSON
yj -yy < deploy.yml      # 会删除 YAML 文件中多余的空行
```


---

## 其他命令行工具

>ripgrep、lsd、sd、bat、git-delta、gitui 等由 Rust 编写的 CLI 均可通过 cargo 安装

- shell：nushell、fish 体验（没有 zsh 好用）
- 替代 `man`：[tldr](https://github.com/tldr-pages/tldr)（有时会失效）、[eg](https://github.com/srsudar/eg)、[navi](https://github.com/denisidoro/navi)（默认的 cheatsheet 很少，效果一般）
- `CTRL + R` 历史命令升级版：[mcfly](https://github.com/cantino/mcfly)
- 替代 `ls`：[lsd](https://github.com/lsd-rs/lsd)（可下载 x86_64-unknown-linux-gnu 二进制版本）、[exa](https://github.com/ogham/exa)、[eza](https://github.com/eza-community/eza)（可以与.gitignore 结合）
- 替代 `grep`：[ripgrep](https://github.com/BurntSushi/ripgrep)（命令 `rg`）
- 替代 `sed`：[sd](https://github.com/chmln/sd)
- 替代 `cat`：[bat](https://github.com/sharkdp/bat)（可与 git 结合使用）
- 替代 `find`：[fd](https://github.com/sharkdp/fd)
- 替代 `ps`：[procs](https://github.com/dalance/procs)
- 替代 diff：[difftastic](https://github.com/Wilfred/difftastic)（命令 `difft`）
- 替代 top：[btop](https://github.com/aristocratos/btop)、[htop](https://github.com/htop-dev/htop)
- 文本编辑器：[helix](https://github.com/helix-editor/helix)
- 终端 Markdown 渲染：[frogmouth](https://github.com/Textualize/frogmouth)、[glow](https://github.com/charmbracelet/glow)
- 显示系统信息：[neofetch](https://github.com/dylanaraps/neofetch)、[neofetch-themes](https://github.com/Chick2D/neofetch-themes)、[fastfetch](https://github.com/fastfetch-cli/fastfetch)（比 neofetch 更快）、[hyfetch](https://github.com/hykilpikonna/hyfetch)
- 磁盘分析：[ncdu](https://dev.yorhel.nl/ncdu)（有时较耗时）
- 文件对比：[difftastic](https://github.com/Wilfred/difftastic)
- 文件搜索：[fzf](https://github.com/junegunn/fzf)
- 统计代码文件行数：[cloc](https://github.com/AlDanial/cloc#quick-start-)
- 终端文件管理器：[yazi](https://github.com/sxyazi/yazi)、[superfile](https://github.com/MHNightCat/superfile)、[ranger](https://github.com/ranger/ranger)、[lf](https://github.com/gokcehan/lf)（效果一般）
- 富文本：[rich](https://github.com/textualize/rich)
- 命令纠正：[thefuck](https://github.com/nvbn/thefuck)
- 将源代码生成美观图片：[silicon](https://github.com/Aloxaf/silicon)、[carbon](https://github.com/carbon-app/carbon)
- neovim 配置：[lazyvim](https://github.com/LazyVim/LazyVim)（siyuan 无法使用）
- 字符 logo 制作：figlet、toilet：[Linux 运维相关 — OnlineNote latest documentation](https://codenote.readthedocs.io/en/latest/linux.html#figlet)
- 查看 coreutils 工具的进度条：[progress](https://github.com/Xfennec/progress)
- Slurm TUI 版本（查看集群任务）：[GitHub - kabouzeid/turm: TUI for the Slurm Workload Manager](https://github.com/kabouzeid/turm)
- [starship](https://github.com/starship/starship): 美观、可自定义的 shell prompt（支持多种 shell，与 ohmyzsh 的主题不兼容）
- 安全替代 `rm` 的脚本：[trash.sh](https://github.com/qqAys/trash.sh)
- 终端显示图片（效果一般）：[GitHub - SilinMeng0510/imgcatr: cat for images, by RUST 🦀️](https://github.com/SilinMeng0510/imgcatr)
- [GitHub - theryangeary/choose: A human-friendly and fast alternative to cut and (sometimes) awk](https://github.com/theryangeary/choose)
- [GitHub - imsnif/bandwhich: Terminal bandwidth utilization tool](https://github.com/imsnif/bandwhich)
- [GitHub - swsnr/mdcat: cat for markdown](https://github.com/swsnr/mdcat)
- 检测 GPU（Nvidia 和 AMD 等）：[nvtop](https://github.com/Syllo/nvtop#distribution-specific-installation-process)
- 将输入的图片，使用几何形状重新绘制：[GitHub - fogleman/primitive: Reproducing images with geometric primitives.](https://github.com/fogleman/primitive)
- 其他小工具： cowsay、sl（火车）、fortune（幸运饼干；格言）、lolcat、boxes、cmatrix（黑客帝国）、asciiquarium（水族馆）


---

fzf 进阶用法

- [fzf/ADVANCED.md at master · junegunn/fzf · GitHub](https://github.com/junegunn/fzf/blob/master/ADVANCED.md)
- [Linux 上有哪些工具软件堪称精美？ - 知乎](https://www.zhihu.com/question/28596616/answer/3487536522)

```bash
# 搜索整个 apt package；回车安装
apt-cache search '' | sort | cut --delimiter ' ' --fields 1 | fzf --multi --cycle --reverse \ --preview-window=right:70%:wrap \ --preview 'apt-cache show {1}' | xargs -r sudo apt install -y

# 用 bat 作为 previewer
fzf --preview "bat --color=always --style=numbers --line-range=:500 {}"
```

---

```bash
# turm 安装
cargo install turm


ncdu -o ncdu.txt  # 输出信息到文件中


# navi 使用
navi repo browse  # 按需添加 cheatsheet git repo 以增加丰富性


# 升级 fzf
cd ~/.fzf && git pull && ./install


# rg 使用
# -g 过滤搜索
rg 'content' -g '!docs/'  # 排除
rg 'content' -g '*.py'    # 包含


# eg 安装
pip install -U eg
brew install eg-examples


# figlet toilet 相关用法
showfigfonts   # 查看可用字体
figlet spt
figlet -c spt  # 居中 
figlet spt | toilet -f term --gay  # 彩色输出


# mcfly 安装与配置
brew install mcfly

curl -LSfs https://raw.githubusercontent.com/cantino/mcfly/master/ci/install.sh | sh -s -- --git cantino/mcfly

eval "$(mcfly init zsh)"


# fastfetch Ubuntu 安装
sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt update

sudo apt install fastfetch


# starship
# 安装
curl -sS https://starship.rs/install.sh | sh
brew install starship  # macOS

# 配置
eval "$(starship init zsh)"   # zsh
eval "$(starship init bash)"  # bash
Invoke-Expression (&starship init powershell) # powershell


# primitive 安装与使用
go install github.com/fogleman/primitive@latest

export PATH=$(go env GOPATH)/bin:$PATH

primitive -i input.png -o output.png -n 100
```

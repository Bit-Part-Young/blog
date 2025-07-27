---
title: Tmux 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Tmux 使用
description: Tmux 使用
tags:
  - Tmux
categories:
  - Linux
date: 2024-09-09 16:17:18
abbrlink: 900924
password:
---

# Tmux 使用

## 介绍

- 将终端和会话分离

- 相关概念：后台服务 (server)，会话 (session)，窗口 (window)，窗格 (pane)

- 一个 session 可以包含多个 window，一个 window 可以被分割成多个 pane

- [Tmux 使用教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/10/tmux.html)



---

## 安装

```bash
brew install tmux      # macOS
sudo apt install tmux  # Ubuntu
```



---

## 使用

### 工具

- [GitHub - rothgar/awesome-tmux: A list of awesome resources for tmux](https://github.com/rothgar/awesome-tmux)

- [Tmux Cheat Sheet & Quick Reference](https://tmuxcheatsheet.com/)

- session 管理（实用）：
    - [GitHub - tmux-python/tmuxp: 🖥️ Session manager for tmux, build on libtmux.](https://github.com/tmux-python/tmuxp)
    - [GitHub - tmuxinator/tmuxinator: Manage complex tmux sessions easily](https://github.com/tmuxinator/tmuxinator)

- 替代工具：[GitHub - zellij-org/zellij: A terminal workspace with batteries included](https://github.com/zellij-org/zellij)


---

### 配置

- [Tmux 配置：打造最适合自己的终端复用工具 - zuorn - 博客园](https://www.cnblogs.com/zuoruining/p/11074367.html)

- tmux 配置：[GitHub - gpakosz/.tmux: Oh my tmux! My self-contained, pretty & versatile tmux configuration made with 💛🩷💙🖤❤️🤍](https://github.com/gpakosz/.tmux)

- 默认前缀键 prefix：`Ctrl + b`；ohmytmux 添加了 `Ctrl + a` 前缀键

- ohmytmux 安装

```bash
cd ~
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```

- 常用配置
    - `-n` 表示该按键绑定是“全局快捷键”，即不需要先按 prefix 键，直接按组合键就能触发
    - `M` 键表示表示 Meta 键，通常是 Alt/Option 键

```bash
# copy-mode 配置
# 设置快捷键为 vim 风格，默认是 Emacs 风格
setw -g mode-keys vi

# 智能分割窗格
bind i run-shell " \
if [ $(( \$(tmux display -p '8*#{pane_width}-20*#{pane_height}') )) -lt 0 ]; then \
  tmux splitw -v -c '#{pane_current_path}'; \
else \
  tmux splitw -h -c '#{pane_current_path}'; \
fi"

# 没有效果？
bind -n M-O next-layout

# 调整窗格大小
bind -n S-Up    resize-pane -U 5
bind -n S-Down  resize-pane -D 5
bind -n S-Left  resize-pane -L 5
bind -n S-Right resize-pane -R 5

# 移动窗口在底部状态栏的位置
bind -n M-S-Left swap-window -t -1\; select-window -t -1
bind -n M-S-Right swap-window -t +1\; select-window -t +1
```


---

### 快捷键

- 快捷键（含默认以及 ohmytmux 中的等价快捷键）

```bash
# session 快捷键
prefix + d           # 分离 session
prefix + s           # 列出所有 session
prefix + $           # 重命名当前 session
prefix + (           # 切换到上一个 session
prefix + )           # 切换到下一个 session

# window 快捷键
prefix + c           # 新建窗口
prefix + 0~9         # 切换窗口
prefix + w           # 打开窗口列表
prefix + f           # 定位窗口
prefix + &           # 关闭当前窗口

# pane 快捷键
prefix + - / "       # 垂直拆分当前窗格
prefix + _ / %       # 水平拆分当前窗格
prefix + x           # 关闭当前窗格
prefix + ; / o       # 光标切换到上/下一个窗格
prefix + > / <       # 交换窗格；或 { / }
prefix + H J K L     # 调整窗格大小
prefix + h j k l     # 导航窗格
prefix + + / z       # 将当前窗格最大化为新窗口和最小化
prefix + m           # 鼠标模式打开或关闭
prefix + Enter / [   # 进入 copy-mode 模式；按 q 退出；按 Space 开始复制
prefix + ] / p       # 粘贴 copy-mode 模式中复制的文本
prefix + q           # 显示窗格编号
```


---

### 命令

- session 相关命令

```bash
tmux source-file ~/.tmux.conf         # 刷新配置
tmux ls                               # list-sessions；列出所有 sessions
tmux new -s session_name              # 新建 session，默认从 0 开始
tmux detach                           # 分离 session
tmux a                                # attach；重新连接 session
tmux attach -t session_name          # 同上
tmux kill-session -t session_name    # 杀死
tmux kill-session -a                  # 杀死除当前 session 的其他
tmux switch -t session_name           # 切换
tmux rename-session -t 0 new_name    # 重命名

tmux capture-pane -pt session_name    # 将指定 session 的窗口内容保存到缓冲区


# 查看 tmux session 中的 pane 中的命令完成情况
# 若为 bash/zsh，则命令已完成；若为具体命令，则命令正在运行
tmux list-panes -a -F "#{session_name}:#{pane_id} #{pane_current_command}"
# # 查看 tmux session 中的 pane 中的进程 ID
tmux list-panes -a -F "#{session_name}:#{pane_id} #{pane_pid}"
# 根据 pane 的进程 ID 查看具体命令
ps f -o pid,cmd --ppid ${pane_pid}
```

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

将终端和会话分离

后台服务 (server)，会话 (session)，窗口 (window)，窗格 (pane)
一个 session 可以包含多个 window，一个 window 可以被分割成多个 pane

---

参考资料：

- [Tmux 使用教程 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2019/10/tmux.html)
- 替代工具：[GitHub - zellij-org/zellij: A terminal workspace with batteries included](https://github.com/zellij-org/zellij)



---

## 安装

```bash
brew install tmux      # macOS
sudo apt install tmux  # Ubuntu
```



---

## 使用

### 配置

- [Tmux 配置：打造最适合自己的终端复用工具 - zuorn - 博客园](https://www.cnblogs.com/zuoruining/p/11074367.html)
- [tmux + oh-my-tmux使用指北](https://ixjx.github.io/2020-04-14/tmux-+-oh-my-tmux%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8C%97/)
- tmux 配置：[GitHub - gpakosz/.tmux: 🇫🇷 Oh my tmux! My self-contained, pretty & versatile tmux configuration made with ❤️](https://github.com/gpakosz/.tmux)
- tmux 插件管理：[GitHub - tmux-plugins/tpm: Tmux Plugin Manager](https://github.com/tmux-plugins/tpm)

```bash
# ohmytmux 安装
cd ~
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```


---

### 快捷键

- 默认前缀键：`Ctrl + b`，oh-my-tmux 添加了 `Ctrl + a`（如何将其取消或换成别的）


```bash
# session 快捷键
prefix + d       # 分离 session
prefix + s       # 列出所有 session
prefix + $       # 重命名当前 session

# 窗格快捷键
prefix + %       # 划分左右两个窗格
prefix + "       # 划分上下两个窗格
```


---

### 命令

tmux session 管理：

- [GitHub - tmux-python/tmuxp: 🖥️ Session manager for tmux, build on libtmux.](https://github.com/tmux-python/tmuxp)
- [GitHub - tmuxinator/tmuxinator: Manage complex tmux sessions easily](https://github.com/tmuxinator/tmuxinator)

session 相关命令

```bash
tmux -V                               # 查看版本
tmux source-file ~/.tmux.conf         # 刷新配置
tmux new -s <session-name>            # 新建 session，默认从 0 开始
tmux detach                           # 分离 session
tmux ls                               # list-sessions；列出所有 sessions
tmux a                                # attach；重新连接 session
tmux attach -t <session-name>         # 同上
tmux kill-session -t <session-name>   # 杀死
tmux switchc -t <session-name>        # 切换
tmux rename-session -t 0 <new-name>   # 重命名
```

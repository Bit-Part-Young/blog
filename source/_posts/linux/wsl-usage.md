---
title: WSL 安装与使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: WSL 安装与使用
description: WSL 安装与使用
tags:
  - WSL
categories:
  - Linux
date: 2023-09-18 16:30:00
abbrlink: 113678
password:
---

# WSL 安装与使用

## 介绍

- WSL 全称为 Windows Subsystem for Linux，即「适用于 Linux 的 Windows 子系统」。WSL 的诞生让 Windows 用户（开发人员）按原样运行 GNU/Linux 环境：包括大多数命令行工具、实用工具和应用程序，且不会产生虚拟机开销

- WSL 2 相比 WSL 1，Linux 内核是完整的，且支持 Docker

- WSL 2 访问本机系统的文件速度比 WSL 1 慢

- 无法使用 KDE 和 GNOME 桌面


---

### 参考资料

- WSL 问题 Q&A：[关于适用于 Linux 的 Windows 子系统的常见问题解答 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows/wsl/faq)
- WSL 开发指南：[Dev on Windows with WSL](https://dowww.spencerwoo.com/)
- WSL GUI 图形化窗口：[GUI 图形化窗口 | Dev on Windows with WSL](https://dowww.spencerwoo.com/4-advanced/4-1-gui.html#%E5%AE%89%E8%A3%85-xserver-for-windows)
- WSL Windows Terminal 终端设置：[GitHub - tautomer/WSL\_Windows\_Terminal: A full guide on how to set up WSL/WSL2 and use Windows Terminal or Terminator as the terminal emulator. Some tricky X11 configuration is also included.](https://github.com/tautomer/WSL_Windows_Terminal)



---

## 安装

>[安装 | Dev on Windows with WSL](https://dowww.spencerwoo.com/1-preparations/1-1-installation.html#windows-10)


- 开启「适用于 Linux 的 Windows 子系统」的附加功能：以管理员身份打开 PowerShell；运行以下命令，按照提示重启电脑

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

- Microsoft Store 搜索 WSL，选择合适的分发版进行安装（若使用了网络代理，需关闭再打开 Microsoft Store）



---

## 使用

### 个人 WSL 开发配置

>[Linux 端安装配置 zsh - Linux 终端工具 - Seek Another Land](https://seekanotherland.xyz/hexo-demo/posts/16854.html#Linux-%E7%AB%AF%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE-zsh)

>[Miniconda3 安装与使用 - Seek Another Land](https://seekanotherland.xyz/hexo-demo/posts/43711.html)

>[多账号 ssh 配置 - git 使用 - Seek Another Land](https://seekanotherland.xyz/hexo-demo/posts/24234.html#%E5%A4%9A%E8%B4%A6%E5%8F%B7-ssh-%E9%85%8D%E7%BD%AE)


- 确定 WSL 版本（1 or 2），下载合适的发行版（不同版本的 Ubuntu，WSLArch 等），设置账号和密码
- 确认一些基本程序是否已安装，如 git、wget、curl 等；若未安装，需手动安装
- `git clone https://gitee.com/yangsl306/dotfiles.git`，进行配置
	- 换源（Ubuntu 为 `/etc/apt/sources.list`，WSLArch 等）
	- git 及 多账号 ssh 配置（`~/.gitconfig`、`~/.ssh/config`、`id_rsa.github`、`id_rsa.gitee`）
	- 安装、配置 zsh（`.zshrc`）
	- 配置 vim
	- 安装 Miniconda3，换源（`.condarc`）
	- 若安装的是 WSL 2，进行网络代理设置（`wslproxy`）


---

### WSL 迁移到 D 盘

>[Move WSL to another drive in Windows - Anmup HD](https://anmup.com.np/programming/move-wsl-to-another-drive-in-windows/)

- WSL 默认安装在 C 盘，若安装 Intel oneAPI 和 texlive 等体积较大的软件时，会占用 C 盘较多的空间，因此需进行迁移。
- WSL 迁移到非 C 盘后，MobaXterm 连接登录 WSL 会偶尔出现一次无法成功，需多次尝试的情况，总体影响不大

```powershell
# 终止
wsl -t Ubuntu-22.04
# 导出
wsl --export Ubuntu-22.04 "D:\Ubuntu-2204.tar"
# 卸载
wsl --unregister Ubuntu-22.04
# 导入
wsl --import Ubuntu-22.04 "D:\Ubuntu-2204" "D:\Ubuntu-2204.tar"
```


---

### WSL 2 网络代理

- Windows 和 WSL 2 算是在同一个局域网内，由 Hyper-V 创建；WSL 2 使用的网络适配器是 'Default Hyper-V Switch'，该适配器每次重启都会被删除重建（WSL 2 IP 不固定的原因）
- [WSL 2 的一些网络访问问题 - 野声](https://cat.ms/posts/wsl2-network-tricks/)

- [WSL 2 中访问宿主机 Windows 的代理 - ZingLix Blog](https://zinglix.xyz/2020/04/18/wsl2-proxy/)

- [WSL 2 中的网络访问问题](https://dowww.spencerwoo.com/2-cli/2-3-cli-tools.html#wsl-2-%E4%B8%AD%E7%9A%84%E7%BD%91%E7%BB%9C%E8%AE%BF%E9%97%AE%E9%97%AE%E9%A2%98)


---

流程：

- Windows 主机上的网络代理软件**允许局域网访问**
- 获取 Windows 主机 IP
- 设置 WSL 2 的代理
- shell 脚本：[proxywsl · Falling Slowly/dotfiles - Gitee.com](https://gitee.com/yangsl306/dotfiles/blob/main/proxywsl)

---

v2rayN 代理客户端允许局域网访问：设置 - 参数设置 - Core: 基础设置 - 勾选允许来自局域网的连接

```text
端口：本地:[socks:10808] | [http(系统代理):10809] 局域网:[socks:10810] | [http:10811]
```

---

较新版本的 WSL 2 网络代理设置：打开或创建 wsl 配置文件（位置：`%USERPROFILE%\.wslconfig`），添加以下内容

```bash
[experimental]
autoMemoryReclaim=gradual  # gradual  | dropcache | disabled
networkingMode=mirrored
dnsTunneling=true
firewall=true
autoProxy=true
```

>[wsl: 检测到 localhost 代理配置，但未镜像到 WSL。NAT 模式下的 WSL 不支持 localhost 代理。 · Issue #10753 · microsoft/WSL · GitHub](https://github.com/microsoft/WSL/issues/10753)


---

### 常用命令

```powershell
# 设置默认 WSL 版本为 2
wsl --set-default-version 2

# 设置 WSL 发行版版本为 2
wsl --set-version <Distro> 2

# 设置默认 WSL 发行版
wsl --set-default-version Ubuntu-22.04

# 列出 WSL 发行版及其信息
wsl -l -v

# 列出可安装的所有 WSL 发行版
wsl -l -o

# 卸载 WSL 发行版
wsl --unregister <Distro>

wslconfig
```


---

### 其他

WSL2 安装 cuda：[win11+wls2+ubuntu2004配置cuda+cudnn+pytorch - LandWind - 博客园](https://www.cnblogs.com/LandWind/p/wsl2-cuda-cudnn-first-start.html)

cuda 的 API 分为两种类型，一种是驱动（driver）API，另一种是运行（runtime）API。`nvidia-smi` 查看的 cuda 版本是驱动 API 版本，`nvcc -V` 是运行 API



---

## 问题

- 安装 WSL 2 报错：[WslRegisterDistribution failed with error: 0x800701bc · Issue #5393 · microsoft/WSL · GitHub](https://github.com/microsoft/WSL/issues/5393)

```bash
WslRegisterDistribution failed with error: 0x800701bc
```

解决方法：[更新 WSL 2 Linux kernel](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

---

- 默认用户设置：[WSL Ubuntu设置普通用户为默认用户 - 简书](https://www.jianshu.com/p/5bfeb5920fb1)

WSL Ubuntu 设置默认用户为普通用户：在 powershell 中输入以下命令

```powershell
ubuntu config --default-user <username>

ubuntu2204 config --default-user <username>
```

WSLArch 设置默认用户为普通用户：在 `/etc/wsl.conf` 添加以下内容，在 powershell 中输入 `wsl --shutdown` 关闭 WSL

```bash
[user] 
default=myuser
```

---

- WSL 可被分配的最大内存：WSL 2 在可用内存允许的情况下可以分配更大的内存量，而 WSL 1 的可用内存通常受到一定限制，约为 4 GB。

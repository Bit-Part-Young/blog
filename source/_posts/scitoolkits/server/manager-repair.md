---
title: 课题组服务器修理
top: true
pin: false
cover:
toc: true
mathjax: true
math: true
summary: 课题组服务器修理
description: 课题组服务器修理
tags:
  - 服务器
  - 课题组
categories:
  - 科研工具
date: 2023-03-04 18:30:30
abbrlink: 36420
password:
---

# 课题组服务器修理

Manager 服务器实拍图：

<img src="https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307091037879.jpg#pic_center" alt="Manager 服务器实拍图" width="60%" />



---

## Manager

### 介绍

- Manager 在断电重新来电时，节点不会重启，需到 312 机房手动重启

- 下方（node1-10）和最上方（node11）的是计算节点，中间的是 Manager 节点，也是计算节点，Manager 和 node1-10 均有 8 核，node11 有 12 核，共 100 核；将任务提交到 node11 的命令是 `gsub`，提交到其他节点的命令为 `submit -n 8 vasp`，无法指定具体节点进行计算

- node1-10 和 node11 的总开关在右侧，Manager 的开关在左侧

- node1-10 中有两个按钮，上方按钮是 node 开关按钮，下方按钮切换到该 node 屏幕显示按钮，按该按钮后会变成蓝色，正常都是绿色。若某节点上方按钮变成红色，说明该节点处于 down 状态，按该按钮将其重启，修理较为简单；若 Manager 节点处于 down 状态，则较难处理，建议找孔老师

- node1-10 中，其中 6 号节点经常 down，一般不修（目前共 node2，6，7，8 经常 down，其他偶尔会 down）

- 一般电脑屏幕的信号线（VGA 线 1 根，现在连在 Master 上，因此 Manager 上无法用屏幕查看 node 节点状态，后侧）和鼠标线（1 根蜂窝口，后侧）插在 Manager 上，键盘线（2 根，一根 USB 口（前侧），一根蜂窝口（后侧））分别插在 Manager 和 node1-10 上。检查 Manager 相关节点状态时需将信号线、鼠标线和键盘线插在对应的节点接口上（node1-10 公用一个接口线）

- 最下方的是存储硬盘，不用管


---

### 重启 SSH

- 服务器 SSH 登录严重卡顿时，可在 Manager/Master 上重启 SSH 服务

```bash
sudo systemctl restart ssh
```


---

### /dev/null 相关报错

- 出现 `/dev/null bad permissions` 报错

```bash
su manager                   # 切换至 manager 用户，需输入 manager 用户密码

ls -l /dev/null              # 查看 /dev/null 权限信息（此时大概率为 600）
sudo chmod 666 /dev/null     # 修改 /dev/null 权限，需输入 manager 用户密码
```


---

### 关闭、重启 Manager

关闭 Manager 操作：

- 先关闭 node1-10（节点全部关闭后再按其右侧的总开关）和 node11（node11 没有鼠标，通过键盘快捷键 `Ctrl+F10` 关闭），再关闭 Manager 节点

- **关闭对应节点需在图形界面上进行操作（需将相关的线连到对应的节点接口上，可将 Master 上的 VGA 线拔下来插到 Manager 上）**

---

重启 Manager 操作：

- 先重启 Manager，再重启 node1-10 和 node11，顺序相反

- 直接按开关即可，可以在图形界面上检查是否重启成功（非必要操作）



---

## Master

- 管理节点 Master，计算节点 node1、node2

- Master 在断电重新来电时，节点会自动重启

- 在计算节点中进出不会导致服务器负载过高而崩溃

- VSCode 远程连接 Manager（机子较老，10 余年历史），有时会导致其负载过高而崩溃，不建议长时间连接；VSCode 远程连接 Master（2023 年 5 月配置）暂无相关问题

- 计算节点出现带 \* 状态的情况（node2 节点经常出现这种情况）：
    - 检查 munge 服务是否是正常（ Slurm 节点间认证的核心服务；若它挂了或时间不同步，Slurm 就会出现一堆奇怪的 \* 状态）
    - 查看计算节点的时间是否和管理节点一致，时间很容易不一样导致问题
    - 检查计算节点的 slurmd 服务是否正常
    - 执行 `sync_slurm` 重启队列服务（同步配置文件）

- 运行 `nvidia-smi` 命令可解决没有正常识别到显卡的问题？（有时可以）

```bash
su -u                        # 切换至 root 用户

sudo reboot                  # 管理节点重启
sudo shutdown now            # 管理节点关机
sudo ssh node1 reboot        # 计算节点重启
sudo ssh node1 shutdown now  # 计算节点关机

sudo sync_slurm              # 同步 slurm 配置

# 检查 munge 服务是否是正常
systemctl status munge
systemctl is-active munge

munge -n | unmunge
munge -n | ssh node1 unmunge
munge -n | ssh node2 unmunge

# 查看节点的时间是否和管理节点一致，时间很容易不一样导致问题
date
ssh node2 date
ssh node1 date

# 检查计算节点的 slurmd 服务是否正常
systemctl status slurmd
systemctl restart slurmd

slurmd -Dvvvv                # 前台启动 slurmd 并输出非常详细的调试日志


# * 消失后，更新状态
# down
sudo scontrol update nodename=node2 state=resume
# drain
sudo scontrol update nodename=node2 state=idle
```



---

## 办公室打印机

- 306 办公室 HP 打印机 WiFi：DIRECT-da-HP M232 LaserJet（不是 DIRECT-14-HP M232 LaserJet、DIRECT-8E-HP M429fdw LJ）

- 新连接密码查看方式：按打印机旁边的 `i` 按钮（按 2 次），会打印其自身的一些信息，其中包括 'Wi-Fi Direct Password'，值为新的 WiFi 密码（**破折号也是密码的一部分**）



---

## 306 工位计算机资产编号

```text
程路遥  2020  3011099
任欣    华为主机，无编号
沈度    2019  313097（可以开机）; 2018  47087（已申请报废处理）
徐志涵  2022  3011894
李树彬  2022  3011895
杨伸炉  2021  3004729
王敏    2020  3015680（应该是李老师那边的资产）
刘瑞    2020  3022792
在墙边上有一台主机  2018  47086（已申请报废处理）
```

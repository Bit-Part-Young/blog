---
title: 课题组服务器修理
top: true
pin: false
cover: false
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

manager 服务器实拍图：

<img src="https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307091037879.jpg#pic_center" alt="manager 服务器实拍图" width="60%" />



---

## manager

manager 在断电重新来电时，节点不会重启，需到 312 机房手动重启。

- 下方（node1-10）和最上方（node11）的是计算节点，中间的是 manager 节点，也是计算节点，manager 和 node1-10 均有 8 核，node11 有 12 核，共 100 核；将任务提交到 node11 的命令是 `gsub`，提交到其他节点的命令为 `submit -n 8 vasp`，无法指定具体节点进行计算。

- node1-10 和 node11 的总开关在右侧，manager 的开关在左侧。

- node1-10 中有两个按钮，上方按钮是 node 开关按钮，下方按钮切换到该 node 屏幕显示按钮，按该按钮后会变成蓝色，正常都是绿色。若某节点上方按钮变成红色，说明该节点处于 down 状态，按该按钮将其重启，修理较为简单；若 manager 节点处于 down 状态，则较难处理，建议找孔老师。

- node1-10 中，其中 6 号节点经常 down，一般不修（目前共 node2，6，7，8 经常 down，其他偶尔会 down；更新日期：20230709）。

- 一般电脑屏幕的信号线（VGA 线 1 根，现在连在 master 上，因此 manager 上无法用屏幕查看 node 节点状态，后侧）和鼠标线（1 根 蜂窝口，后侧）插在 manager 上，键盘线（2 根，一根 USB 口（前侧），一根蜂窝口（后侧））分别插在 manager 和 node1-10 上。检查 manager 相关节点状态时需将信号线、鼠标线和键盘线插在对应的节点上（node1-10 公用一个接口线）的接口上。

- 最下方的是硬盘，不用管。


---

### 关闭、重启 manager

关闭 manager 操作：

- 先关闭 node1-10（节点全部关闭后再按其右侧的总开关）和 node11（node11 没有鼠标，通过键盘快捷键 `Ctrl+F10` 关闭），再关闭 manager 节点；

- **关闭对应节点需在图形界面上进行操作（需将相关的线连到对应的节点接口上，可将 master 上的 VGA 线拔下来插到 manager 上）。**

---

重启 manager 操作：

- 先重启 manager，再重启 node1-10 和 node11，顺序相反；

- 直接按开关即可，可以在图形界面上检查是否重启成功（非必要操作）。



---

## master

- master 在断电重新来电时，节点会自动重启。
- 在计算节点中进出不会导致服务器负载过高而崩溃。
- vscode 远程连接 manager（机子较老，10 余年历史） ，有时会导致其负载过高而崩溃，不建议长时间连接；vscode 远程连接 master（2023 年 5 月配置）暂无相关问题。



---

## 重启 SSH

服务器 SSH 登录严重卡顿时，可在 manager/master 上重启 SSH 服务

```bash
sudo systemctl restart ssh
```



---

## 办公室打印机

- 306 办公室 HP 打印机 WiFi：DIRECT-da-HP M232 LaserJet
- 新连接密码查看方式：按打印机旁边的 `i` 按钮，会打印其自身的一些信息，其中包括 “Wi-Fi Direct Password”，值为新的 WiFi 密码（**破折号也是密码的一部分**）。

---
title: Material Studio 安装与使用
top: false
cover: 
toc: true
mathjax: true
summary: Material Studio 安装与使用
description: Material Studio 安装与使用
tags:
  - Material-Studio
  - 结构建模
categories:
  - 科研工具
date: 2024-06-28 20:00:00
abbrlink: 202708
password:
---

# Material Studio 安装与使用

## 安装

注：

- 安装版本为 2019
- 需联网安装
- 安装路径及 license 文件路径不要有中文
- 计算机名必须由英文和数字组成，如果之前已经更改为中文，需要使用计算机的 IP 地址代替计算机名
- 许可文件所在的文件目录不能包含中文，所以将其复制到 C 盘根目录下，然后选择载入即可

---

- 打开 “BIOVIA Materials Studio 2019.msi” 或 “setup.exe” 文件，按照提示进行正常安装，直到安装完成。

- 安装成功后，以笔记本方式打开 “MS2019\\激活文件\\msi.lic”，将计算机名复制到许可文件中替换 “this_host”，然后保存即可。

![msi-lic.jpg](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310211448615.jpg)

- 在开始菜单页面，打开 BIOVIA 文件夹中的 “License Administrator 2019”，选择 Install License，然后点击 Browser 选择 msi.lic 许可文件

![install-license.jpg](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310211449950.jpg)

- 弹出如下提示，表明软件成功注册激活

![success-install.jpg](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202310211447160.jpg)

- 至此，Materials Studio 2019 完成破解。


---

## 卸载

- 点击安装包中的 Autorun.exe——install material studio——选择 remove
- 在设置中卸载 License Pack（先卸载它，后面的会自动卸载）和 License Pack (X64)


---

## 建模使用

- 文件保存路径不要有中文
- 出现很卡顿的情况
	- 解决方法：tool - option - graphhics，勾选 disable graphic（取消硬件加速）
	- 输入法的兼容性打开

---

复杂结构 Bulk 模型构建：

- 可通过其他程序构建（如 pymatgen、ase、pyxtal 等），使用 ase 保存成 xsd 格式文件，之后直接导入到 MS 中即可
- 在 MS 中手动构建


表面构建：表面构建过程中，可以调整 thickness（从最小值调整到 1.0），得到表面不同终端的数目和层间距

MS 中的构型文件可保存成 res 格式，之后使用 posconv 可转换成其他格式


---

## CASTEP

CASTEP 文件格式
![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202312262058798.png)


CASTEP 赝势路径
```text
BIOVIA\Materials Studio 19.1\share\Resources\Quantum\Castep\Potentials
```

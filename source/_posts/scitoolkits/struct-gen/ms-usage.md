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
categories:
  - 科研工具
  - 结构建模
date: 2024-06-28 20:00:00
abbrlink: 202708
password:
---

# Material Studio 安装与使用

## 介绍

建模工具；含 CASTEP 模块，可进行 DFT 计算。



---

## 安装与下载

### 安装

- 注意事项：
    - 安装版本为 2019
    - 需联网安装
    - 安装路径及 license 文件路径不要有中文
    - 计算机名必须由英文和数字组成，如果之前已经更改为中文，需要使用计算机的 IP 地址代替计算机名
    - 许可文件所在的文件目录不能包含中文，所以将其复制到 C 盘根目录下，然后选择载入即可

- 打开 “BIOVIA Materials Studio 2019.msi” 或 “setup.exe” 文件，按照提示进行正常安装，直到安装完成

- 安装成功后，以笔记本方式打开 “MS2019\\激活文件\\msi.lic”，将计算机名复制到许可文件中替换 “this_host”，然后保存即可

- 在开始菜单页面，打开 BIOVIA 文件夹中的 “License Administrator 2019”，选择 Install License，然后点击 Browser 选择 msi.lic 许可文件

- 弹出 “License file was insatlled successfully. License server has been started” 提示，表明软件成功注册激活

- 至此，Materials Studio 2019 完成破解


---

### 卸载

- 点击安装包中的 Autorun.exe -- install material studio -- 选择 remove
- 在设置中卸载 License Pack（先卸载它，后面的会自动卸载）和 License Pack (X64)



---

## 使用

### 建模

- 参考：
    - [Materials\_Studio建模锂电池材料Li3VO4\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1jL2EYBE23)
    - [Materials\_Studio构建石墨烯抗冲击结构\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1MY28YdEqv)
    - [14-3-Materials\_Studio建模\_哔哩哔哩\_bilibili](https://b23.tv/Ip9oPhw)
    - [VASP视频教程-搭建模型-用ms建模\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1QKt3e1E6p)
    - [Materials Studio学习](https://cndaqiang.github.io/2017/11/24/ms1/)
    - [如何采用Materials Studio切晶面和建立界面模型\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Av411H7PS)
    - [How to build and optimize crystal structure of a compound - Part 01 - Materials studio (CASTEP)](https://www.youtube.com/watch?v=IMvzznBhEns)
    - [关于Material Studio和Vesta导出来的cif文件的差别](https://zhuanlan.zhihu.com/p/417605545)
    - [合集·Materials Studio - 奕星模拟个人主页 - 哔哩哔哩视频](https://space.bilibili.com/662609827/channel/collectiondetail?sid=4089960)

- 复杂结构 Bulk 模型构建：
    - 可通过其他程序构建（如 pymatgen、ase、pyxtal 等），使用 ase 保存成 xsd 格式文件，之后直接导入到 MS 中即可
    - 在 MS 中手动构建
        - 构建晶体：Build -- Crystals, Build Crystal -- Space Group: Enter group、List; Lattice Parameters: Lengths
        - 添加原子：Build -- Add Atoms: Element、a、b、c

- 表面构建：表面构建过程中，可以调整 thickness（从最小值调整到 1.0），得到表面不同终端的数目和层间距

- 将晶体对称性降低至 P1，目的是方便对晶体结构进行修改（VESTA 和 Material Studio）

- MS 中的构型文件可保存成 res 格式（对称性设为 P1），之后使用 posconv 可转换成其他格式

- MS -- Build -- find symmetry 找到对称性

- 无定形模型：水溶液

- 构建界面模型：Build -- Build Layer（最多添加三个构型）


---

### CASTEP

- CASTEP (Cambridge Serial Total Energy Package)

- CASTEP 文件格式

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202312262058798.png)

- CASTEP 赝势路径

```text
BIOVIA\Materials Studio 19.1\share\Resources\Quantum\Castep\Potentials
```


---

### 相关问题

- 文件保存路径不要有中文

- 出现很卡顿的情况
    - 解决方法：Tool -- Option -- Graphhics，勾选 Disable Graphic（取消硬件加速）
    - 输入法的兼容性打开

---
title: atomsk 安装与使用
top: false
cover:
toc: true
mathjax: true
summary: atomsk 安装与使用
description: atomsk 安装与使用
tags:
  - atomsk
categories:
  - 科研工具
  - 结构建模
date: 2024-06-28 16:00:00
abbrlink: 162806
password:
---

# atomsk 安装与使用

## 介绍

- 强大的结构建模工具；同 latgen 相比，可生成孪晶、晶界、位错、层错等更多复杂构型

- 示例丰富，文档详细

- atomsk 中的 cfg 格式文件可用 OVITO 打开，VESTA 无法打开

- 暂时没有的功能：
    - 单胞转换成原胞
    - 无法直接构造八面体、四面体间隙的点缺陷
    - 可否建立 layer / 界面模型？


---

### 参考资料

- atomsk 官方教程：[Atomsk - Tutorials](https://atomsk.univ-lille.fr/tutorials.php)

- [Atomsk Cheat Sheet](https://atomsk.univ-lille.fr/data/Atomsk_Cheat-Sheet.pdf)

- 查看所有的 options 和 modes 及其用法：[Documentioin - Atomsk](https://atomsk.univ-lille.fr/doc/en/index.html)

- 层错构建：[Atomsk - Tutorial - Stacking fault](https://atomsk.univ-lille.fr/tutorial_stackingfault.php)

- VESTA 中如何变换点阵（六方转正交）：[crystallography - How to transform lattice in VESTA - Matter Modeling Stack Exchange](https://mattermodeling.stackexchange.com/questions/7263/how-to-transform-lattice-in-vesta)

- 六方胞的正交化（里面的示意图可供参考）：[Orthogonalization of a hexagonal unit cell of AlN](https://er-c.org/barthel/drprobe/example-orthcel-aln.html)

- 晶界构建（symmetric tilt、twist）：[Atomsk - Tutorial - Grain Boundaries](https://atomsk.univ-lille.fr/tutorial_grainboundaries.php)

- 位错构建（刃、螺位错）：
    - [Atomsk - Tutorial - Edge Dislocation in Aluminium](https://atomsk.univ-lille.fr/tutorial_Al_edge.php)
    - [Atomsk - Tutorial - Screw Dislocation in Aluminium](https://atomsk.univ-lille.fr/tutorial_Al_screw.php)



---

## 安装

- 安装教程：[Atomsk - Install - Pierre Hirel](https://atomsk.univ-lille.fr/doc/en/install.html)

- 下载二进制版本（最简单方式，无 macOS 版本）：[Download Atomsk](https://atomsk.univ-lille.fr/dl.php)

- 源码编译：依赖 LAPACK 库（Intel 套件有相关库）

```bash
# 编译 LAPACK
cp make.inc.example make.inc
make # 耗时较长

# 拷贝编译得到的静态库文件
make -p ${HOME}/local/lib/lapack
cp *.a ${HOME}/lib


# atomsk 编译、安装
# 下载 atomsk 源代码，进入 src 目录，修改 Makefile 文件
LAPACK=-L${HOME}/local/lib/lapack -llapack -lrefblas
INSTPATH=$HOME/local/atomsk
CONFPATH=${INSTPATH}/etc

# 编译
make atomsk     # 或 make -j4 atomsk

# 安装
make -p ${HOME}/local/atomsk/bin
# 方式 1
make install
# 方式 2
make INSTPATH=${HOME}/local/atomsk install

# 编译成功
\o/ Compilation was successful!

<i> To install Atomsk system-wide, you may now run:
      sudo make install
```

- 编译 ifort 版本

```bash
# 导入 Intel OneAPI 套件
module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

git clone https://github.com/pierrehirel/atomsk.git

cd atomsk/src

make -f Makefile.ifort atomsk

# 超算（思源）使用 atomsk 时
# 需设置 libiomp5.so 文件的软链接
# 或使用前 module load intel-oneapi-compilers/2021.4.0
ln -s /dssg/opt/icelake/linux-centos8-icelake/gcc-8.5.0/intel-oneapi-compilers-2021.4.0-rszhbg2vjwqqeddqqdryjwxromenbfmr/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libiomp5.so ~/lib/libiomp5.so
```

- macOS 编译 atomsk（详细编译说明查看 `Makefile.macos` 文件内容）

```bash
# 需安装 LAPACK 和 OpenMP（非必需）
# 修改 Makefile.macos 中的 LAPACK lib 路径
# 并将 -lrefblas 改为 -lblas，最后编译
make -f Makefile.macos atomsk
```



---

## 使用

- options：应用于体系的变换（transformations），用 `-` 区分

- modes：允许执行特定的操作，构造，分析或操纵多个数据文件（operations, constructions, analysis, manipulate），用 `--` 区分

- 常用 options

```bash
-orient                 # 晶体取向
-rmatom N               # 删除原子
-rotate Z 45            # 旋转轴
-orthogonal-cell        # 转变为正交胞
-fractional             # 分数坐标；VASP 格式下
-sort species pack      # 使相同元素在 POSCAR 中是连续的
-fix Z                  # 固定原子坐标轴；Z/all
-shift                  # 平移
-substitute 1 Cu        # 原子类型替换成某种元素
-wrap                   # 将胞外原子施加 PBC 移至胞内
-cell add 10 y          # 在 y 方向上增加 10 埃，原子位置不变；x y z 可分别写成 H1 H2 H3；作用相当于添加真空层；set 设置 某个方向的长度
-center 0/com           # 移动所有原子，使其质心在 box 中心；会使位于 box 边缘的原子位点稍微往胞里靠，和 ase Atoms 的 center 方法效果不同
-add-atom               # 添加原子；可添加笛卡尔坐标及分数坐标（0.5*box 形式）
-wrap                   # 将胞外原子通过 PBC 到胞内
-properties
-remove-doubles
-mirror
```

- 常用 modes

```bash
--create                # 构建晶体结构
--merge

# 报错内容：一次只能使用一个 mode
X!X ERROR: only one mode can be used at a time.
```

- atomsk 支持的构型文件格式

```bash
# atomsk 支持的构型文件格式
atsk abin bop bx cfg cel cif coo csv d12
dat dd dlp fdf gin imd jems lmp mol
pdb pos pw str vesta xmd xsf xv
xyz exyz sxyz
```

- 常用命令实例

```bash
# 构建晶体结构
atomsk --create fcc 4.02 Al vasp
atomsk --create hcp 2.92 4.61 Ti vasp  # 矢量：H1=[2-1-10], H2=[-12-10], H3=[0001]

# 构建不同晶体取向的构型
# zsh [] 中括号需添加引号
atomsk --create fcc 3.53 Ni -orient [1-10] [11-2] [111] vasp

# 构建超胞
atomsk POSCAR -duplicate 1 1 4 vasp

# 添加原子；box/BOX 可小写/大写
atomsk initial.xsf -add-atom Si at 0.25*box 0.33*box 0.5*box final.cfg

# 原子 z 轴坐标低于一定值，其 z 轴被固定
atomsk POSCAR -fix z below 4.05 z vasp

# 线性插值；用于 NEB
atomsk --interpolate initial.vasp final.vasp 7 vasp

# 将六方胞变成正交胞
atomsk POSCAR -orthogonal-cell -sort species pack vasp

# 笛卡尔、分数坐标互相转换
atomsk POSCAR vasp               # 笛卡尔坐标
atomsk POSCAR -fractional vasp   # 分数坐标

# 添加真空层
-cell add 15 z                   # 在 z 轴上半部分添加真空层
-shift 0 0 15 -cell add 30 z     # 在 z 轴两侧添加真空层
-shift 0 0 15 -cell add 15 z     # 在 z 轴下半部分添加真空层

# 格式转换
# 输出文件可以是具体的文件名，也可以是文件格式；输出文件可以是多个
# 写入 cif 文件时，总是假设空间群为 P1，写入所有原子位置
atomsk XXX.cfg xyz        # 常用：xyz lammps/lmp vasp/pos cif

# 常见表面的具体坐标轴
"[010]" "[001]" "[100]"          # BCC、FCC (100)
"[1-10]" "[001]" "[110]"         # BCC、FCC (110)
"[11-2]" "[-110]" "[111]"        # BCC、FCC (111)
```

- 多晶模型及界面模型（coating 模型）构建： [【计算材料学-从算法原理到代码实现】视频教程 | 7.17\_多元合金的atomsk手把手建模\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV13s421A735)

- 多晶模型：基于 Voronoi tessellation 算法生成

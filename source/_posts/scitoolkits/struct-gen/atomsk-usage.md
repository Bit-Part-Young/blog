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

- 只能构建 BCC、FCC、HCP 结构的特殊取向，其他结构不能（会报错）

- 参考资料
    - atomsk 官方教程：[Atomsk - Tutorials](https://atomsk.univ-lille.fr/tutorials.php)
    - [Atomsk Cheat Sheet](https://atomsk.univ-lille.fr/data/Atomsk_Cheat-Sheet.pdf)
    - VESTA 中如何变换点阵（六方转正交）：[crystallography - How to transform lattice in VESTA - Matter Modeling Stack Exchange](https://mattermodeling.stackexchange.com/questions/7263/how-to-transform-lattice-in-vesta)
    - 六方胞的正交化（里面的示意图可供参考）：[Orthogonalization of a hexagonal unit cell of AlN](https://er-c.org/barthel/drprobe/example-orthcel-aln.html)

- FCC 孪晶：
    - [Atomsk - Tutorial - Twin boundary](https://atomsk.univ-lille.fr/tutorial_twin.php)
    - [ATOMSK建模 Stacking Fault](https://mp.weixin.qq.com/s/o0ldM-87tGulOEIBFXSsSw)


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

- 配置文件（可选）：[Program behaviour: setting up a configuration file](https://atomsk.univ-lille.fr/doc/en/progbe_configfile.html)

```bash
# 配置文件路径
~/.config/atomsk.conf

# 内容
colour yes
colour_error red bold blink
```

- atomsk 中的变量可全小写/大写，如 box、z

- atomsk 支持的构型文件格式

```bash
atsk abin bop bx cfg cel cif coo csv d12
dat dd dlp fdf gin imd jems lmp mol
pdb pos pw str vesta xmd xsf xv
xyz exyz sxyz
```

- atomsk 支持的晶体结构构建类型：[Mode: create - Atomsk](https://atomsk.univ-lille.fr/doc/en/mode_create.html)

```bash
               <structure> | N.lattice cst. | N.at.sp.
              -------------+----------------+----------
CUBIC                  sc  |       1        |     1
LATTICES              bcc  |       1        |   1 or 2
                      fcc  |       1        |   1 or 2
                  diamond  |       1        |   1 or 2
                     L1_2  |       1        |     2
                 fluorite  |       1        |     2
                rock-salt  |       1        |     2
               perovskite  |       1        |     3
                      A15  |       1        |     2
                      C15  |       1        |     2
              -------------+----------------+----------
TETRAGONAL             st  |  2 (a and c)   |   1 or 2
LATTICES              bct  |  2 (a and c)   |   1 or 2
                      fct  |  2 (a and c)   |   1 or 2
              -------------+----------------+----------
HEXAGONAL             hcp  |  2 (a and c)   |   1 or 2
LATTICES         wurtzite  |  2 (a and c)   |     2
                 graphite  |  2 (a and c)   |   1 or 2
                       BN  |  2 (a and c)   |     2
                      C14  |  2 (a and c)   |     2
                      C36  |  2 (a and c)   |     2
```

- 常见模型构建
    - 晶界构建（symmetric tilt、twist）：[Atomsk - Tutorial - Grain Boundaries](https://atomsk.univ-lille.fr/tutorial_grainboundaries.php)
    - 位错构建（刃、螺位错）：
        - [Atomsk - Tutorial - Edge Dislocation in Aluminium](https://atomsk.univ-lille.fr/tutorial_Al_edge.php)
        - [Atomsk - Tutorial - Screw Dislocation in Aluminium](https://atomsk.univ-lille.fr/tutorial_Al_screw.php)
    - 层错构建：[Atomsk - Tutorial - Stacking fault](https://atomsk.univ-lille.fr/tutorial_stackingfault.php)
    - [atomsk多层碳纳米管建模示例](https://mp.weixin.qq.com/s/geQF9G9xC-f_90puwqI_tA)

- 查看所有的 options 和 modes 及其用法：[Documentioin - Atomsk](https://atomsk.univ-lille.fr/doc/en/index.html)

- options：应用于体系的变换（transformations），用 `-` 区分

- modes：允许执行特定的操作，构造，分析或操纵多个数据文件（operations, constructions, analysis, manipulate），用 `--` 区分

- 常用 options

```bash
-orient                     # 晶体取向
-duplicate                  # 或 -dup；扩胞
-rotate                     # 旋转轴
-orthogonal-cell            # 转变为正交胞
-reduce-cell                # 保持周期性的同时减小胞的大小；参数值 x/y/z/p
-fractional                 # 或 -frac；分数坐标（VASP 格式）
-sort                       # 根据 properties 对原子进行排序
-fix                        # 固定原子坐标轴
-shift                      # 移动原子
-substitute                 # 元素替换
-wrap                       # 将胞外原子施加 PBC 移至胞内
-cell                       # 修改 box 的 cell vector；可 add、set、rm
-center                     # 使体系移至 box 的中心
-add-atom                   # 添加原子
-wrap                       # 将胞外原子通过 PBC 到胞内
-properties                 # 设置 properties
-remove-doubles             # 删除重复的原子
-remove-atom                # 或 -rmatom；删除原子
-mirror                     # 施加镜像操作（mirror transformation）
-deform                     # 或 -def；通过施加正应变或切应变使体系变形（box 和 原子一起）
-disturb                    # 随机移动原子位置
-select                     # 根据准则选择原子
```

- 常用 modes

```bash
--create                # 构建晶体结构
--merge                 # 合并两个构型
--rdf                   # RDF 计算

# 报错内容：一次只能使用一个 mode
X!X ERROR: only one mode can be used at a time.
```

- Program behaviour

```bash
-ov            # overwrite；覆写文件
-v N           # verbosity；
# N 可选值
0              # 不会输出内容到屏幕/log 文件，Errors、warnings、questions 仍会输出到屏幕 
1              # 只输出内容到屏幕
0              # 只输出内容到 log 文件
0              # 输出内容到屏幕、log 文件
```

- 常用命令实例

```bash
# 构建晶体结构
--create fcc 4.02 Al               # FCC
--create hcp 2.92 4.61 Ti          # HCP，基矢: H1=[2-1-10], H2=[-12-10], H3=[0001]
--create perovskite 3.905 Sr Ti O  # 钙钛矿结构

# 支持的晶体结构类型
bcc
fcc
hcp
diamond
perovskite
rocksalt


# 构建晶体特定取向的构型
--create fcc 3.53 Ni -orient "[1-10]" "[11-2]" "[111]"

-reduce-cell p                     # 寻找原胞

-duplicate 1 1 4                   # 构建超胞

-sort species pack                 # 将相同的元素排在一起（写入 VASP POSCAR 有用）

# 笛卡尔、分数坐标互相转换（用于 VASP）
atomsk POSCAR vasp                 # 笛卡尔坐标
atomsk POSCAR -fractional vasp     # 分数坐标

# 添加真空层
-cell add 15 z                     # 在 z 轴上半部分添加真空层；x、y、z 可写成 H1-3
-shift 0 0 15 -cell add 30 z       # 在 z 轴两侧添加真空层
-shift 0 0 15 -cell add 15 z       # 在 z 轴下半部分添加真空层

# 固定原子坐标轴
-fix x -fix y                      # 固定所有原子的 x、y 轴
-fix x below 4.05 z                # 原子 z 轴坐标低于一定值，其 x 轴被固定

-def zx 5%                         # 使 z 轴沿 x 方向进行切应变

-center 0/com                      # 移动所有原子，使其质心在 box 中心；会使位于 box 边缘的原子位点稍微往胞里靠，和 ase Atoms 的 center 方法效果不同

# 添加原子（分数坐标）
-add-atom Si at 0.25*box 0.33*box 0.5*box

# 给定准则选择原子
# 选择矩形盒子内的原子；矩形盒子区域 X=[0;1.0*box], Y==[0.5*box;1.0*box], Z=[0.48*box;0.52*box]
-select in box 0 0.5*box 0.48*box 1.0*box 1.0*box 0.52*box
-select in box 0 0.48*box 0.48*box 1.0*box 0.52*box 0.52*box
# 多个 select 是 || 的效果，而不是 && 的效果
-select above 0.48*box z -select below 0.52*box z -select above 0.48*box y Ti -substitute Ti Al

# 线性插值；用于 NEB
--interpolate initial.vasp final.vasp 7 vasp


# 格式转换
# 输出文件可为具体文件名，也可为文件格式；输出文件可以是多个
# 写入 cif 文件时，总是假设空间群为 P1，写入所有原子位置
atomsk POSCAR xyz                  # 常用: xyz lammps/lmp vasp/pos cif
```

- RDF 计算：[Tutorial: Radial Distribution Functions (RDF)](https://atomsk.univ-lille.fr/tutorial_rdf.php)

- 多晶模型及界面模型（coating 模型，相对简单的）构建：[【计算材料学-从算法原理到代码实现】视频教程 | 7.17\_多元合金的atomsk手把手建模\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV13s421A735)

- 多晶模型：基于 Voronoi tessellation（泰森多边形镶嵌） 算法生成
    - [LAMMPS 笔记：Atomsk 生成多晶](https://zhuanlan.zhihu.com/p/617697569)

```bash
# 创建单晶的种子
atomsk --create fcc 4.041 Al Al.lmp

# polycrystal.txt
box 100 100 100      # 设置多晶模型盒子大小
random 6             # 设置晶粒数目（随机位置和方向）

# 生成多晶
atomsk --polycrystal Al.lmp polycrystal.txt -wrap Al_polycrystal.lmp

# 删除距离过近的原子
atomsk Al_polycrystal.lmp -remove-doubles 0.2 final.lmp


# 输出信息文件
*_size-dist.txt      # 晶粒大小的分布
*_param.txt          # 节点的位置和旋转信息
*_nodes.xsf          # 最终的节点位置
*_id-size.txt        # 晶粒中的原子数目和晶粒体积
*_grain-com.xsf      # 晶粒质心的位置
```

- 等原子比四元随机固溶体

```bash
a=3.254

# 替换比例 20% 25% 33.33% 50%
# 全部 -> 等原子比五元
# 后 3 个 -> 等原子比四元
# 后 2 个 -> 等原子比三元

atomsk --create bcc ${a} Nb -duplicate 20 20 20 tmp1.cfg
atomsk tmp1.cfg -select random 25% Nb -sub Nb Ti tmp2.cfg
atomsk tmp2.cfg -select random 33.33% Nb -sub Nb Al tmp3.cfg
# -sort species pack vasp 或 TiAlNbMo_random.lmp
atomsk tmp3.cfg -select random 50% Nb -sub Nb Mo -sort species pack vasp

rm -f *.cfg
```

---
title: LAMMPS 输入文件
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: LAMMPS 输入文件
description: LAMMPS 输入文件
tags:
  - LAMMPS
categories:
  - 科研工具
  - LAMMPS
date: 2024-10-25 19:36:01
abbrlink: 360191
password:
---

# LAMMPS 输入文件

- in 文件结构：[5.3. Input script structure — LAMMPS documentation](https://docs.lammps.org/Commands_structure.html)
    - 初始化（Initialization）
    - 系统定义（System definition）
    - 模拟设置（System definition）
    - 运行模拟（Run a simulation）

- 一般不建议通过 LAMMPS 的内置命令构建初始结构模型（简单的除外）

- `#` 注释；一行过长时，用 `&` 连接下一行

- LAMMPS in 文件比较好的注释写法

```bash
# --------------------- ATOM DEFINITION ---------------------

# --------------------- FORCE FIELDS ------------------------
```

```bash
# 最小化过程中控制最大移动距离
min_modify dmax

fix ave/time
fix ave/correlate
compute pressure            # 整体压强
compute stress/atoms        # 局部压强

compute chunk/atom
compute msd/chunk

compute cna/atom

compute vacf
```


---

## LAMMPS 常用命令

- [ ] 更新 LAMMPS 相关输入参数
    - lattice
    - create_box
    - create_atoms
    - print
    - atom_style
    - units
    - compute
    - variable（参考孔老师的 MSD 代码）
    - jump
    - label

- Command 类型：[5.4. Commands by category — LAMMPS documentation](https://docs.lammps.org/Commands_category.html)
    - 初始化（Initialization）：units、newton

    - box 设置（Setup simulation box）：boundary、change_box、create_box、dimension、lattice、region

    - 原子设置（Setup atoms）：atom_style、atom_style、create_atoms、delete_atoms、displace_atoms、group、mass、read_data、read_dump、read_restart、replicate、set、velocity

    - 势函数（力场 Force fields）：pair_style、pair_coeff、pair_modify、pair_write

    - Settings：timestep、reset_timestep、neighbor、neigh_modify、min_style、min_modify

    - fix 和 compute：fix、fix_modify、unfix、compute、compute_modify、uncompute

    - Actions：minimize、neb

    - 输出（Output）：thermo、thermo_style、tehrmo_modify、read_data、write_data、dump、dump_modify

    - 输入脚本控制（Input script control）：variable、clear、shell、if、jump、label、next、print

- 再细化分类
    - 蒙特卡洛 MC 相关命令：`fix gcmc`、`fix atom/swap`、`fix sgcmc`

- [LAMMPS 最重要的两种符号：引号与美元符号](https://mp.weixin.qq.com/s/q81ngjKF6cN2l4o_7d4sow)
    - `$()` 的作用和 `""` 很像（允许空格的出现），前者是立即计算转换成数值的（所有出现 `$` 的地方都如此），后者不会立即计算
    - `print` 命令把变量的值输出时，须用 `$` 而不能用引号。因为引号在 `print` 后面时字符串的作用会被强化，而传递参数的作用会被弱化

```bash
if 2>1 then "print yes!"

variable         var equal "1 / (lx*2 + lx^2 / (3-lx))"

# 若 foo 是未定义的变量
variable         var1 equal "(foo * 2)"   # 不会报错
variable         var2 equal $(foo * 2)    # 会报错
```

```bash
# 单循环
variable     i loop 3  # 声明变量
print        "$i"      # 命令块
next         i         # i 自增
jump         SELF      # 重新读取本脚本

# 嵌套循环
label        lp
variable     i loop 3
variable     j loop 5
print        "($i,$j)"
next         j
jump         SELF lp
next         i
jump         SELF lp
```


---

### atom_style

- 定义模拟过程中原子的类型，决定原子包括哪些属性（原子，键角，二面角、电荷等）

- 须在建立 simulaiton box（`read_data` 或 `read_restart` 或 `create_box` 等命令）前使用

- 不同样式对应的原子属性及适用体系： [atom-style-attributes - atom\_style command — LAMMPS documentation](https://docs.lammps.org/atom_style.html#atom-style-attributes)

- 默认值：atomic（典型物理体系：金属、固体、atomic liquids）

```bash
# 语法
atom_style style args

# style
atomic
body
hybrid

# atomic 对应属性（最基本属性）
tag                # atom-ID
type               # type
x                  # position
v                  # velocities
f                  # forces
image              # image flags；镜像 box ID；有时原子会跑到 box 外面，将其所处的镜像 box 进行编号
mask               # group membership；识别 group ID；LAMMPS 最多设置 32 个 group？

# 示例
atom_style atomic  # 默认设置
```


---

### boundary

- 用来设置模拟盒子的边界条件

```bash
# 语法
boundary x y z

x, y, z                 # 可取 p s f m 中的一个或两个字母的组合
p                       # 周期性边界条件 periodic
f                       # 非周期性；固定边界条件 fixed
s                       # 非周期性；该方向的大小会随着原子的运动而改变（以保证不丢失原子）
m                       # 非周期性；包覆最小值边界条件 minimum value

# 示例
boundary p p p
```


---

### dimension

- 定义模拟的维度

- 默认值：3

```bash
# 语法
dimension N

N                   # 2/3

# 示例
dimension 3         # 默认设置
```


---

### newton

- 用来开启或关闭对势或键相互作用中的第三运动定律

```bash
# 语法
newton flag
newton flag1 flag2

# flag： 开关对势和键相互作用[on/off]
# flag1：开关对势相互作用[on/off]
# flag2：开关键相互作用[on/off]

# 示例
newton on  # 默认设置
```


---

### units

- 用来定义模拟过程中使用的单位类型（单位制），它决定了所有输入脚本、数据文件和所有输出到屏幕、日志文件以及 dump 文件中物理量的单位；一般来说，该命令用在输入脚本最开始的位置

- 使用不当，会导致后期数据处理需要进行繁杂的单位换算

- eam、tersoff 势函数，使用 `units metal`

- 默认值：lj

- metal
    - 质量：g/mol
    - 长度：Å
    - 时间：ps
    - 能量：eV
    - 力：eV/Å
    - 应力：bars
    - 温度：K
    - 速度：Å/ps

- real
    - 质量：g/mol
    - 长度：Å
    - 时间：fs
    - 能量：kcal/mol
    - 力：(kcal/mol)/Å
    - 应力：atmospheres
    - 速度：Å/fs

```bash
# 语法
units style

# style
metal              # 金属体系常用
real               # 高分子常用
lj                 # 约化单位，无量纲
si                 # 国际单位制
cgs
electron

# 示例
units lj                # 默认设置
units metal
```


---

### read_data

- 读取 LAMMPS data 构型格式文件（可读取 gzip 格式）

```bash
# 语法
read_data file
```

- LAMMPS data 文件格式：[read\_data command — LAMMPS documentation](https://docs.lammps.org/read_data.html)

```bash
# header
# data 文件 开头内容 keywords
atoms                    # 原子数
bonds                    # 键数
angles                   # 键角数
dihedrals                # 二面角数
atom types               # 原子类型
bond types               # 键类型
angle types              # 键角类型
dihedral types           # 二面角类型
xlo xhi                  # x 轴边界（起始、终点坐标）
ylo yhi                  # y 轴边界
zlo zhi                  # z 轴边界
xy xz yz                 # 三斜体系的 tilt factors

# 正交盒子，x y z轴坐标
A = (xhi-xlo,0,0)
B = (0,yhi-ylo,0)
C = (0,0,zhi-zlo)

# 三斜盒子，x y z轴坐标
A = (xhi-xlo,0,0)
B = (xy,yhi-ylo,0)
C = (xz,yz,zhi-zlo)


# body
# data 文件 正文内容 keywords
# 原子性质部分
Atoms
Velocities
Masses

# 分子拓扑部分
Bonds
Angles
Dihedrals

# 力场部分
Pair Coeffs


# Atoms 内容写法；与 atom_style 相关
atomic atom-ID atom-type x y z           # atomic
atom-ID molecule-ID atom-type q x y z    # full
```


---

### write_data

- 写出 LAMMPS data 构型格式文件

- 使用 LAMMPS 内置命令构建模型后，需设置原子类型对应的相对原子质量（也可势函数），再使用 `write_data`，否则会报错

```bash
# 语法
write_data file
```


---

### read_restart

- 用来读入之前的模拟过程保存下的重启动文件；可以帮助你实现接着之前的模拟过程继续进行

- 这些重启动文件一般来说是不能拷贝到其他的机器使用的，但你可以使用工具 `restart2data` 将其转换成文本文件

```bash
# 语法
read_restart file
```


---

### read_dump

- （可读取 gzip 格式）

```bash

```


---

### lattice

- 定义晶格类型，晶格常数，以及晶向方向

- 默认值 `orient x 1 0 0 orient y 0 1 0 orient z 0 0 1`；改变晶向时，需满足**右手定则**（不推荐使用 LAMMPS 的内置命令构建特殊晶向的构型，生成的构型不正确）

```bash
# 语法
lattice style scale keyword values ...

# style：none bcc fcc hcp diamond hex sc custom

# scale：晶格与模拟盒子之间的比例因子

# keyword/value：没有或多个
# keyword = orient origin spacing a1 a2 a3 basis
# orient values = dim i j k
# dim = x y z
# i,j,k = 整数晶向方向

# 示例
lattice      none 1.0             # 默认设置
lattice      bcc 3.168
lattice      fcc 3.615
lattice      hcp 3.2              # 正交坐标轴
```


---

### region

- 用来构建拟盒子大小以及划分模拟区域（用于定义一个空间几何区域）

- 默认值：`units lattice`

- 一般 `box` 这个单词只用于与盒子相关的地方，只选取部分区域时，不要将其定义为 `box`

```bash
# 语法
region ID style args keyword args ...

ID                    # 为 regoin 命令分配的 ID

# style
block
sphere
plane
union
intersect

# block args
xlo xhi ylo yhi zlo zhi    # x y z 方向的起始、终点坐标；可以是变量
EDGE                       # 变量，box 边界的坐标值
INF                        # 变量，无穷大/小（截止到 box 最大/小坐标值）

# keyword
side
units
move
rotate

# units
lattice                    # 用晶格常数作为单位定义长度，box
box                        # 用模拟盒子单位定义几何结构


# 示例
# 构建 10a*10a*10a 大小的 box；units lattice为默认值，可不写出
lattice           fcc 3.615
region            box block 0 10 0 10 0 10 units lattice

# 构建 10*10*10 Å 大小的 box
region            box block 0 10 0 10 0 10 units box
```


---

### create_box

- 定义模型中有几类原子，几类键等

```bash
# 语法
create_box N region-ID keyword value ...

N                    # 原子种类数

# keyword
bond/types           # 键种类数
angle/types          # 键角种类数


# 示例
create_box        2 box              # box 中有 2 种原子
create_box        2 box bond/type 2  # box 中有 2 种原子及 2 种键长
```


---

### creat_atoms

- 在晶格阵点上创建原子，或创建一个单独的原子，或创建一些列随机原子（往模型中添加原子）

- 使用该命令之前，模拟盒子必须是存在的（使用 `create_box` 命令创建），同时晶格也必须已经被定义（使用 `lattice` 命令）

```bash
# 语法
create_atoms type style args keyword values ...

# type：要创建的原子类型（用1到N的数字代替）

# style：box region single random
# box arg：无
# region args：region-ID  只有在region内的原子才会被创建
# single args： x y z  x,y,z为要创建原子的坐标（以原胞为单位）

# keyword：basis reamp units 没有或多个
# units values：lattice box  lattice：以晶格距离作为单位；box：以模拟盒子作为单位

# 示例
create_atoms 1 box           # 将类型 1 的原子填满盒子
create_atoms 2 single 5 5 5  # 在坐标为（5a, 5a, 5a）添加一个类型 2 的原子
```

- **box 类型**：该命令在整个模拟盒子中所有的晶格阵点上创建原子


---

### pair_style

- 势函数类型

```bash
# 语法
pair_style style args

# 示例
# 默认设置，可用于只创建并输出构型文件
pair_style         none
# 只创建对势需要的近邻列表，不计算力和能量
pair_style         zero
# eam 势
pair_style         eam/alloy
```


---

### pair_coeff

- 给出势函数中的参数或者数值列表

```bash
# 语法
pair_coeff I J args


# 示例
# * * 表示 span 所有元素，考虑任意的两个原子间的相互作用
# 对于含多种元素的势函数，若只用到部分元素，其它元素可不写出
pair_coeff      * * ../../CuYM.eam.alloy Cu
```


---

### pair_modify

- WIP...


---

### pair_write

- 将原子对间所定义的势函数，以距离作为自变量，将对应的能量和受力写入到文件中

- 可用于绘制势函数曲线

```bash

```


---

### neighbor

- 此命令设置影响 pairwise neighbor lists 构建的参数。所有原子对的 neighbor cutoff 距离等于其力截止加上 skin 距离，都存储在列表中。通常，skin 距离越大，需要构建的 neighbor lists 就越少，但每个时间步都必须检查更多的对以确定可能的力相互作用。skin 的默认值取决于模拟的单位选择；请参见下面的默认值。

- style 的值表示选择构建近邻列表的算法。bin style 通过 binning 创建列表，binning 是一种与 N/P（每个处理器的原子数）线性缩放的操作，其中 N=原子总数，P=处理器数 (processors)。它几乎总是比缩放为 (N/P)^2 的 nsq style 快。

- 2.0 bin for units = real or metal, skin = 2.0 Angstroms

```bash
neighbor skin style

# skin = 超出力截止的额外距离(distance units)
# style = bin nsq multi multi/old

# 例子
neighbor 0.3 bin
neighbor 2.0 nsq
```


---

### neigh_modify

- 设置影响成对近邻列表建立和使用的参数；一次模拟可能需要多个近邻列表

- 默认值：delay = 0, every = 1, check = yes, once = no, cluster = no, include = all (same as no include option defined), exclude = none, page = 100000, one = 2000, and binsize = 0.0.

- 此命令设置影响 pairwise neighbor lists 的生成和使用的参数。根据定义的对相互作用和其他命令，模拟可能需要一个或多个邻居列表。

- *every*, *delay*, *check*, and *once*选项影响模拟运行时生成列表的频率。*delay*设置意味着在上一次构建之后至少 N 个步骤之前从不构建新列表。*every*设置意味着每 M 步尝试构建列表（after the delay has passed）。如果*check*设置为 no，则在满足延迟和每个设置的第一步上构建列表。如果*check*设置为 yes，则*every*和*delay*设置将确定何时可能执行构建，但只有在自上次邻居列表构建以来至少有一个原子移动了超过 neighbor skin 距离（在 neighbor 命令中指定）一半的情况下，才会进行实际构建。
- 如果*once*设置为 yes，则 neighbor lists 仅在每次运行开始时构建一次，并且从不重新构建，除非在写入重新启动文件时执行步骤，或在修复强制进行重建时执行步骤（例如，创建或删除原子的修复，如 fix deposit or fix evaporate）。只有当您确定原子移动的距离不够远，无法重建 neighbor lists 时，才能进行此设置，例如运行冷晶体模拟。请注意，检查是否应该重建邻居列表并不昂贵。

```bash
# 语法
neigh_modify keyword values ...

# keyword
delay           # 在上一次构建之后至少N步之前，永远不要构建新的列表
everry          # delay pass后，每M步建立列表
check           # yes/no
once            # yes/no


# 示例
neigh_modify every 2 delay 10 check yes page 100000
```


---

### group

- 确定一组原子属于一个组；可以在其他命令（如 fix compute dump velocity）使用 group ID，以共同作用于这些原子；若 group ID 已存在，group 命令将指定的原子添加到 group 中

```bash
# 语法
group ID style args

# ID

# style
# style = id  表示原子id
# style = type 表示原子种类

# 默认设置：所有的原子属于 "all" group

# 示例
group 1 type 1  # 表示将所有类型为1的原子设置为1组
group 2 region 2  # 表示将处于区域2中的所有原子设置为2组
group 3 union 1 2 # 表示将1，2组合并为3组
group water type 3 4
group sub id 10 25 50
```


---

### mass

- 为原子类型设置相对原子质量

- 只有在模拟盒子定义后，才能使用该命令

```bash
# 语法
mass I value

I                # 原子类型
value            # 相对原子质量值


# 示例
mass 1 1.0
```

---

### timestep

- 设置模拟时间步长

```bash
# 语法
timestep dt

dt            # 时间步长值；默认值取决于 units

# 示例
timestep 0.001

# 默认值
1 fs          # real
0.001 ps      # metal；等于 1 fs
```


---

### velocity

- 设置或改变原子的速度

```bash
# 语法
velocity group-ID style args keyword value ...

# style
create
set
scale
zero

# create
temp                 # 温度值
seed                 # 随机数

# keyword
dist
sum
mom
rot
temp
loop

# dist value；在 creat style 下使用
uniform
gaussian              # 原子速度分布满足高斯分布


# 示例
velocity           all create 300.0 4928459 dist gaussian
# 默认设置
dist = uniform
mom = yes
rot = no
```


---

### run

- 设置模拟运行步数

```bash
# 语法
run N keyword values ...

N                      # 运行步数

# 示例
run 10000
run 0            # 只计算系统的热力学量并输出，不需要时间步长
```


---

### fix

- 给原子施加约束；`fix` 是在时间步进或最小化期间应用于系统的任何操作；可能是在时间积分的过程中更新原子的位置和速度，或是控制温度，或是给原子施加约束力，或是强制某种边界条件，或计算过程诊断，等等

- `fix` 的 style 有很多，且大多是单独的命令

- fix 引用（compute references）：`f_ID`

```bash
# 语法
fix ID group-ID style args

ID             # 为 fix 命令分配 ID
group-ID       # 被施加约束的原子所属 group ID

# fix nvt  fix nve  fix npt

# fix print


# 示例
# 设置模拟系综（nve,nvt,npt等）
fix 1 all nvt temp 300 300 100.0

# 对原子进行操作
```


---

### fix setforce

```bash
fix ID group-ID setforce fx fy fz keyword value ...

fx fy fz            # 力分量值；可以是变量
NULL                # 变量，不改变（不额外设置）该方向的受力

# 示例
fix          1 all setforce 0.0 0.0 NULL
```


---

### fix nve

- 执行普通 (plain) 时间积分，以在每个时间步更新组中原子的位置和速度。这创建了与微正则系综（NVE）一致的系统轨迹，前提是存在（完全）周期性边界条件，并且没有系统的其他 “操纵 “（例如，修改力或速度的固定）

```bash
fix ID group-ID nve

# ID, group-ID与fix命令中定义相同
```


---

### fix nvt/npt/nph

- 用 Nose-Hoover 方法对时间积分，生成位置和速度

```bash
# 语法
fix ID group-ID style_name keyword value ...

# style_name = nvt/npt/nph

# keyword = temp iso等
# temp values = Tstart Tstop Tdamp
# iso values = Pstart Pstop Pdamp

# 示例
fix 1 all nvt temp 300.0 300.0 100.0
```

- fix nvt，温度不是保持不变，而是会有振荡（波动），振幅与 Tdamp 有关


---

### fix box/relax

```bash
fix ID group-ID box/relax keyword value ...
```

- 在能量最小化期间，将外部压力或应力张量应用于模拟盒。这允许盒子的大小和形状在最小化器的迭代过程中变化，从而最终构型将是原子势能的能量最小值，并且系统压力张量将接近指定的外部张量。从概念上讲，指定正压力就像挤压模拟盒；负压通常允许盒子膨胀。

- 外部压力张量用*iso*, *aniso*, *tri*, *x*, *y*, *z*, *xy*, *xz*, *yz*, and *couple*关键词。这些关键字使您能够指定外部应力张量的所有 6 个分量，并将这些分量耦合在一起，以便在最小化过程中与它们所表示的尺寸一起变化。
- 应力张量的 6 个分量中的每一个的目标压力 Ptarget 可以通过 x、y、z、xy、xz、yz 关键字独立指定，这些关键字对应于 6 个模拟盒维度。例如，如果使用 y 关键字，则在最小化期间 y 框长度将发生变化。如果使用 xy 关键字，xy 倾斜因子将更改。如果未指定该组件，长方体尺寸将不会更改。

- 关键字 iso 表示在计算压力（静水压力）时将所有三个对角分量连接在一起，并将尺寸放大/缩小在一起。value = Ptarget
- 关键词 aniso 意味着 x、y 和 z 维度是使用应力张量的 Pxx、Pyy 和 Pzz 分量作为驱动力和指定的标量外部压力独立控制的。
- vmax 关键字可用于限制在最小化器的一次迭代中可能发生的模拟盒体积的分数变化。如果在最小化期间压力没有稳定下来，这可能是因为体积波动太大。指定的分数必须大于 0.0，且应小于 1.0。值 0.001 表示当指定了 xyz 对时，体积在一次迭代中的变化不能超过 1/10。对于任何其他情况，这意味着模拟框的线性尺寸变化都不能超过 1/10。

- 默认值：dilate = all, vmax = 0.0001, nreset = 0


---

### fix print

- 每 N 步输出文本内容（用于调试）

```bash
# 语法
fix ID group-ID print N string keyword value ...

N                 # 每 N 步输出

# keyword
file              # 写入内容到文件
append            # 追加内容到文件
screen            # 是否输出到屏幕；yes/no


# 示例
fix        extra all print 100 "Coords of marker atom =$x $y $z" file coord.txt

# 输出文件中的默认标题行（# 号是自带的）
# Fix print output for fix-ID
```


---

### fix_modify

---

### fix atom/swap

- 执行 Monte Carlo 原子交换；需安装 MC package

```bash
# 语法


# 示例
```


---

### fix sgcmc

- 运行 parallel hybrid molecular dynamics/Monte Carlo (MD/MC) 模拟

- [LAMMPS 蒙特卡洛 MC 模拟案例](https://mp.weixin.qq.com/s/79qR5g0m9FlpgE-JAO7J-Q)

- LAMMPS 示例代码路径 `examples/mc/in.sgcmc.eam`

```bash
# 语法
fix ID group-ID sgcmc every_nsteps swap_fraction temperature deltamu ...

every_nsteps            # 每隔 every_nsteps MD 步执行一次 MC 循环
swap_fraction           # MC 循环中原子交换比例（1.0 表示所有原子都进行 trial moves）
temperature             # MC 温度（Metropolis criterion中的 T；通常和 MD 温度相同）
deltamu                 # 化学势差



```

---

### unfix

- 删除之前使用 `fix` 命令定义的约束；也会删除使用 `fix_modify` 命令对该约束所进行的修改

```bash
# 语法
unfix fix-ID


# 示例
unfix           2
```


---

### compute

- 为 group 原子定义一种计算

- compute 引用（compute references）：`c_ID`

- 计算出的量是瞬时值，也就是说它们只是原子在当前时间步或迭代步的信息。当然，compute 命令也可以在内部保存体系在之前一个状态的某些信息

- 定义 compute 命令的时候并不会执行计算。真正的计算过程是被其他 LAMMPS 命令激活的，比如某些 fix 命令需要计算温度的时候，或这需要产生热力学信息的时候，或者需要 dump 输出到文件中的时候

```bash
# 语法
compute ID group-ID style args

ID                    # 为 compute 命令分配 ID
group-ID              # 被 compute 的原子所属 group ID

# style
ke                    # 总动能
ke/atom               # 平均原子动能
pe                    # 总势能
pe/atom               # 平均原子势能
pressure
rdf                   # 计算 rdf
msd                   # 计算 MSD
temp
voronoi/atom


# 示例
compute        1 all temp
compute        1 all pe/atom
# 计算每个原子在 x y z方向上所受到的力
compute        1 all porperty/atom fx fy fz

# 将 W.xyz 导入 OVITO，Add Modification -- Color coding，在 input property 选项中选择 c_1 可得到以平均原子势能为 colorbar 的构型
compute        1 all pe/atom
dump           1 all custom 100 W.xyz id type x y z c_1
```

- style 中含有 “atom”，为单原子量；含有 “local”，为局域量；不包含前两者，为全局量

---

### compute_modify

- 用来修改过之前定义过的 `compute` 命令的一个或多个参数

```bash
# 语法
compute_modify compute-ID keyword value ...
```


---

### uncompute

- WIP...


---

### compute rdf

- [如何计算 rdf](https://mp.weixin.qq.com/s/2J5J1Mlw8pPeXJBh8E2Nbw)

```bash
compute ID group-ID rdf Nbin itype1 jtype1 itype2 jtype2 ... keyword/value ...

Nbin           # 0-截断半径的切片数
itype1         # 中心原子
jtype1         # 被统计的原子

# keyword
cutoff         # RDF 的截断半径
```


---

### compute msd

- [如何计算 msd](https://mp.weixin.qq.com/s/n15pAX-_9dewzLvgdJKPBA)

```bash
compute ID group-ID msd keyword values ...

# 有 4 个分量，前三个向量分别为 x，y，z 方向的 MSD，第四个是总 MSD

# keyword values
com                 # yes/no；yes 表示在计算每个原子的位移之前，将减去原子组质心中任何漂移的影响
average             # yes/no

# 示例
compute        1 all msd com yes
variable       msdx equal c_1[1]
variable       msdy equal c_1[1]
variable       msdz equal c_1[1]
variable       msdt equal c_1[4]
```

---

### dump

- 输出原子构型信息

- custom style 中的参数：c_ID/c_ID[I] = 允许输出由 compute 计算的每原子向量或数组 (per-atom vectors or arrays)，这里 ID 应替换为先前在 in 文件中定义的计算的实际 ID（**ID 类似于一种变量**）

- [LAMMPS学习系列（43） - dump输出坐标的几种格式](https://mp.weixin.qq.com/s/rEzHMkKAJk44hoKUcp_wtQ)

```bash
# 语法
dump ID group-ID style N file args

ID                    # 为 dump 命令分配的 ID
group-ID              # 被 dump 的原子所属 group ID
style                 # custom、one 等
N                     # 每 N 步输出一次构型
file                  # dump 文件名
args                  # style 参数

# custom 参数：原子属性列表
mass                  # 相对原子质量
id                    # 原子 ID
type                  # 原子类型
x, y, z               # 笛卡尔坐标
xu, yu, zu            # 笛卡尔坐标（不做 PBC 处理）
xs, ys, zs            # 分数坐标
xsu, ysu, zsu         # 分数坐标（不做 PBC 处理）
c_ID / c_ID[I]        # compute 命令计算的每原子向量或数组(per-atom vectors or arrays)

# 示例
dump            1 all custom 500 dump.lammpstrj id type x y z
```


---

### dump_modify

- 修改 dump 命令的预定义参数

```bash
# 语法
dump_modify dump-ID keyword values ...


# keyword
sort
append

# sort 值
off           # 乱序输出以提高性能；默认
id            # 通过原子 ID 对输出进行排序
N             # 通过第 N 列数据对输出进行升序排序
-N            # 通过第 N 列数据对输出进行降序排序


# 示例
# 用于中断后重算时，将构型数据追加到之前的同名 dump 文件中
dump_modify      1 append yes
```


---

### undump

- 关闭先前定义的 dump，使其不再处于活动状态。这将关闭与 dump 关联的文件。

```bash
undump dump-ID

dump-ID           # 先前定义的dump ID
```


---

### thermo

- 输出热力学信息（如温度、能量、压强）；可以是变量

```bash
# 语法
thermo N

N                  # 每 N 步输出一次热力学信息

# 示例
thermo          0         # 默认设置
thermo          100
```


---

### thermo_style

- 设置输出的热力学信息内容

```bash
# 语法
thermo_style style args

# style
custom                   # 最常用
one                      # 后三个 style args = none
multi
yaml

# custom args = list of keywords
atoms                    # 原子总数目
step                     # 输出运行的步数是多少
temp                     # 体系的温度
ke                       # 体系的动能
pe                       # 体系的总势能
etotal                   # 体系的总能量
pxx, pyy, pzz, pxy ...   # 表示体系各个方向的压强
count(all)               # 计算总原子数目
dt                       # 步长
lx,ly,lz                 # 盒子三个方向的长度
cpu                      #
tpcpu                    #
v_name                   # 变量

# 示例
thermo_style custom step temp ke pe etotal
```


---

### start

---

### write_restart

---

### delete_atoms

- 删除原子

```bash
# 语法
delete_atoms style args keyword value ...

# style
group
region
overlap               # 必须先定义 pair_style
random

# keyword，值均为 no/yes
compress
bond
mol


# 示例
delete_atoms     group 1
delete_atoms     region 2
```

- **如果 compress 关键字设置为 yes，那么在原子被删除后，原子 ID 将被重新分配，以便从 1 到系统中的原子数**。请注意，对于分子系统（请参见 atom_style 命令），无论压缩设置如何，都不会这样做，因为这会破坏已指定的键连接。但是，reset_atom_ids 命令可以在该命令之后使用，以完成相同的任务。

- 默认设置是：compress = yes, bond = no, mol = no


---

### displace_atoms

- 移动原子位置

```bash
```


---

### min_style

- 能量最小化算法

```bash
# 语法
min_style style

# style
cg            # 共轭梯度法；对于绝大多数的问题来说，被认为是效果最好的
sd            # 最速下降法；一般来说，没有cg算法收敛快
quickmin
spin

# 示例
min_style     cg  # 默认设置
```

---

### min_modify

- 设置所选择的能量最小化算法的参数；不同的设置参数会影响收敛速率和能量最小化过程中需要计算力的次数

```bash
# 语法
min_modify keyword values ...

# keyword/value = 一个或多个
# keyword = dmax line norm等

# 示例
min_modify dmax 0.2
```


---

### minimize

- 能量最小化

```bash
# 语法
minimize etol ftol maxiter maxeval

etol          # 能量收敛条件（无单位）
ftol          # 力收敛条件（力的单位）
maxiter       # 能量最小化的最大迭代次数
maxeval       # 计算力或能量的最大次数

# 示例
minimize 1.0e-4 1.0e-6 100 1000
```

- 能量最小化结束后，程序会打印一段统计摘要信息，介绍满足了何种收敛判据，以及能量、受力、最终的线性搜索和迭代次数等

```bash
Minimization stats:
  Stopping criterion = max iterations
  Energy initial, next-to-last, final =
       -0.626828169302     -2.82642039062     -2.82643549739
```


---

### neb

---

### temper

---

### set

- 设置原子性质

```bash
# 语法
set style ID keyword values ...

# style
atom                      # 原子 ID
type                      # 原子类型
mol                       # 分子 ID
group                     # group ID
region                    # region ID

# keyword
type/fraction             # 分数替换
type/ratio                # 同上
type/subset               # 具体数目替换


# 示例
# 按 type 替换
set        type 1 type/fraction 2 0.5 12393
set        type 1 type/ratio 2 0.5 12393
set        type 1 type/subset 2 100 1239

# 按 group 替换
region     top block INF INF INF INF 20 INF units box
group      top region top
set        group top type/fraction 2 1 23985

# 按 region 替换
region     mid block INF INF 18 32 INF INF units box
group      mid region mid
set        region mid type/fraction 2 0.3 23985
```


---

### variable

- variable 引用（variable references）：`v_ID`

- [LAMMPS 统计一个原子周围不同类型原子数量的方法](https://mp.weixin.qq.com/s/cyCPhlYuUXDQ-GyeDcIlaQ)

- [LAMMPS 计算固定区域内原子受力的方法](https://mp.weixin.qq.com/s/CpBP9Fnamnd7IrZl1M2kxg)

```bash
# 语法
variable name style args ...

name                    # 定义的变量名

# style
index                   # 可选值（字符串）
equal                   # 等于；数值，常量，数学操作，thermo 关键字，函数（数学、group、region），引用
loop                    # 循环；从 1 开始

# region functions
count(group)            # 统计 region 中 group 的原子数
fcm(group,dim)          # 计算 region 中 group 的总受力分量

# region functions
count(group,region)     # 统计 region 中 group 的原子数
fcm(group,dim,region)   # 计算 region 中 group 的总受力分量


# 示例
variable        x index run1 run2 run3
variable        iter equal 40
variable        n loop ${iter}
```


---

### jump

- 关闭当前输入脚本文件，打开命令中文件名所指定的文件，并从那个文件开始读入 LAMMPS 命令；与命令 `include` 不同的是，LAMMPS 不会再返回到之前的输入文件了

- 'SELF' 含义：重新打开当前 in 文件并再次读取

```bash
# 语法
jump file label

file          # 要跳转到的 in 文件名
label         # 可选；要跳转到的 in 文件中的设置的标签；从标签的位置开始向下执行


# 示例
jump        newfile
jump        in.run2 runloop
jump        SELF runloop
```


---

### label

- 设置标签

```bash

```

---

### clear

- 用来删除所有的原子、将所有的设置都设为默认值，并释放 LAMMPS 分配的所有内存

- 该命令可以让你在一个输入脚本中顺序运行多个作业

- 工作目录（命令 `shell`）、日志文件状态（命令 `log`）、echo 状态（命令 `echo`）以及输入脚本中的变量（命令 `variable`）不受 `clear` 影响

```bash
(commands for 1st simulation)
clear
(commands for 2nd simulation)
```

---

### next

- 该命令需要与使用命令 `variable` 定义的变量同时使用，用来从为该变量定义的一些列值中将下一个值赋给变量。在使用该命令之后，变量就是一个新值

```bash
# 语法
next variables

# 示例
next x
next a t x myTemp
```

---

### if

- 在输入文件中提供一个 if-then-else 功能

```bash
# 语法
if boolean then t1 t2 ... elif boolean f1 f2 ... elif boolean f1 f2 ... else e1 e2 ...

# 示例
if              "$i==1" then "shell rm data"
```

---

### print

- 打印一个文本字符串到屏幕和日志文件

```bash
# 语法
print string keyword value

# keyword
file         # 写入文件；无法用变量？
append       # 追加内容到文件
screen       # yes/no
universe     # yes/no
```


---

### shell

- 执行 Shell 命令

```bash
# 语法
shell command args

command        # cd mkdir mv rm rmdir 等 Shell 命令


# 示例
shell      ./script.sh     # 执行 Bash 脚本
shell      mkdir folder    # 创建目录
```

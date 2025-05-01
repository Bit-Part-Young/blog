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

## 介绍

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

# --------------------- Potential ------------------------
```



---

## LAMMPS 常用命令

- [ ] 更新 LAMMPS 相关输入参数
    - print
    - compute
    - variable（参考孔老师的 MSD 代码）
    - jump
    - label

- 命令类型：[5.4. Commands by category — LAMMPS documentation](https://docs.lammps.org/Commands_category.html)
    - 初始化（Initialization）：units、newton

    - 模拟盒子设置（Setup simulation box）：boundary、change_box、create_box、dimension、lattice、region

    - 原子设置（Setup atoms）：atom_style、create_atoms、delete_atoms、displace_atoms、group、mass、read_data、read_dump、read_restart、replicate、set、velocity

    - 势函数（力场 Force fields）：pair_style、pair_coeff、pair_modify、pair_write

    - Settings：timestep、reset_timestep、neighbor、neigh_modify、min_style、min_modify

    - fix 和 compute：fix、fix_modify、unfix、compute、compute_modify、uncompute

    - Actions：minimize、neb

    - 输出（Output）：
        - 热力学数据输出的频率和格式：thermo、thermo_style、tehrmo_modify、
        - 构型/轨迹读取、输出：read_data、write_data、dump、dump_modify

    - 输入脚本控制（Input script control）：variable、clear、shell、if、jump、label、next、print

- 再细化分类
    - 蒙特卡洛 MC 相关命令：`fix gcmc`、`fix atom/swap`、`fix sgcmc`

- [LAMMPS 最重要的两种符号：引号与美元符号](https://mp.weixin.qq.com/s/q81ngjKF6cN2l4o_7d4sow)
- [5.2. Parsing rules for input scripts — LAMMPS documentation](https://docs.lammps.org/Commands_parse.html)
    - `$()` 的作用和 `""` 很像（允许空格的出现），前者是立即计算转换成数值的（所有出现 `$` 的地方都如此），后者不会立即计算
    - `print` 命令把变量的值输出时，须用 `$` 而不能用引号。因为引号在 `print` 后面时字符串的作用会被强化，而传递参数的作用会被弱化

```bash
if 2>1 then "print yes!"

variable          var equal "1 / (lx*2 + lx^2 / (3-lx))"

# 若 foo 是未定义的变量
variable          var1 equal "(foo * 2)"   # 不会报错
variable          var2 equal $(foo * 2)    # 会报错
```

```bash
# 单循环
variable          i loop 3  # 声明变量
print             "$i"      # 命令块
next              i         # i 自增
jump              SELF      # 重新读取本脚本

# 嵌套循环
label             lp
variable          i loop 3
variable          j loop 5
print             "($i,$j)"
next              j
jump              SELF lp
next              i
jump              SELF lp
```


---

### atom_style

- 定义模拟过程中原子的类型，决定原子包括哪些属性（原子，键角，二面角、电荷等）

- 必须在建立模拟盒子（`read_data` 或 `read_restart` 或 `create_box` 等命令）前使用

- 不同样式对应的原子属性及适用体系： [atom-style-attributes - atom\_style command — LAMMPS documentation](https://docs.lammps.org/atom_style.html#atom-style-attributes)

```bash
# 语法
atom_style style args

# style
atomic                  # 默认设置；典型物理体系：金属、固体、atomic liquids
body
hybrid

# atomic 对应属性（最基本属性）
tag                     # atom-ID
type                    # type
x                       # position
v                       # velocities
f                       # forces
image                   # image flags；镜像 box ID；有时原子会跑到 box 外面，将其所处的镜像 box 进行编号
mask                    # group membership；识别 group ID；LAMMPS 最多设置 32 个 group？

# 示例
atom_style        atomic
```


---

### boundary

- 设置模拟盒子的边界条件

- `f` 非周期性边界条件，且是开放性的边界条件（即采用这种边界条件，当有原子运动到盒子以外的区域，该原子便会被系统删除，即丢失原子，但一般情况下 LAMMPS 在运行过程中是不允许丢失原子的，则若想采用该边界条件，需在 `thermo` 命令下添加 `thermo_modify lost ignore` 允许系统丢失原子）

```bash
# 语法
boundary x y z

x, y, z                 # 可取 p s f m 中的一个或两个字母的组合
p                       # 周期性边界条件 periodic
f                       # 非周期性；固定边界条件 fixed
s                       # 非周期性；该方向的大小会随着原子的运动而改变（以保证不丢失原子）
m                       # 非周期性；包覆最小值边界条件 minimum value；用得很少


# 示例
boundary          p p p
```


---

### dimension

- 定义模拟的维度

```bash
# 语法
dimension N

N                          # 2/3

# 示例
dimension         3        # 默认设置
```


---

### newton

- 用来开启或关闭对势或键相互作用中的牛顿第三运动定律

```bash
# 语法
newton flag
newton flag1 flag2

flag                       # 开关对势和键相互作用
flag1                      # 开关对势相互作用
flag2                      # 开关键相互作用


# 示例
newton            on       # 默认设置
```


---

### units

- 定义模拟过程中使用的物理量的单位制（一般该命令写在输入脚本最开始的位置）；使用不当，会导致后期数据处理需要进行繁杂的单位换算

- metal
    - 质量：g/mol
    - 长度：Å
    - 时间：ps
    - 能量：eV
    - 力：eV/Å
    - 压强：bars=0.1 MPa
    - 温度：K
    - 速度：Å/ps

- real
    - 质量：g/mol
    - 长度：Å
    - 时间：fs
    - 能量：kcal/mol
    - 力：(kcal/mol)/Å
    - 压强：atmospheres
    - 速度：Å/fs

```bash
# 语法
units style

# style
metal                      # 金属体系常用；eam、tersoff 势函数使用
real                       # 高分子常用
lj                         # 约化单位，无量纲；默认值
si                         # 国际单位制
cgs
electron

# 示例
units             metal
```



---

### read_dump

- （可读取 gzip 格式）

```bash

```


---

### lattice

- 定义点阵

- 改变晶向时，需满足**右手定则**（不推荐使用 LAMMPS 的内置命令构建特殊晶向的构型，生成的构型不正确）

```bash
# 语法
lattice style scale keyword values ...

# style
none
bcc
fcc
hcp                        # HCP 正交胞，4 个原子，c 默认为 sqrt(8/3)
diamond
hex
sc                         # 简单立方
custom                     # 自定义

# scale 点阵常数（除 LJ unit 外）

# keyword
orient                     # 位向
a1, a2, a3                 # 点阵矢量
basis                      # 胞内原子位置的分数坐标

# 默认值
origin = 0.0 0.0 0.0
orient = x 1 0 0, orient = y 0 1 0, orient = z 0 0 1
a1 = 1 0 0, a2 = 0 1 0, a3 = 0 0 1


# 示例
lattice           bcc 3.168

# 自定义正交 HCP 结构
variable          a equal 2.95
variable          b equal $a*sqrt(3.0)
variable          c equal 4.67
lattice           custom 1.0 &
                  a1  $a   0.0  0.0          &
                  a2  0.0  $b   0.0          &
                  a3  0.0  0.0  $c           &
                  basis 0.00  0.00000  0.00  &
                  basis 0.50  0.50000  0.00  &
                  basis 0.00  0.33333  0.50  &
                  basis 0.50  0.83333  0.50
```


---

### region

- 构建模拟盒子大小、划分模拟区域

- 默认值：`units lattice`

- 一般 `box` 这个单词只用于与盒子相关的地方，只选取部分区域时，不要将其定义为 `box`

```bash
# 语法
region ID style args keyword args ...

ID                         # 为 regoin 命令分配的 ID

# style
block                      # 矩形 region
sphere                     # 球形 region
prism                      # 非正交 region
union                      # 合并 region
intersect

# block args
xlo xhi ylo yhi zlo zhi    # x y z 轴的起始、终点坐标；可以是变量
EDGE                       # 变量，box 边界的坐标值
INF                        # 变量，无穷大/小（截止到 box 最大/小坐标值）

# keyword
units                      # lattice 以晶格常数作为单位；box 以模拟盒子距离作为单位
side
move
rotate


# 示例
lattice           fcc 3.615
# 构建 10a*10a*10a 的 box
region            box block 0 10 0 10 0 10
# 构建 10*10*10 Å 大 box
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
create_box        2 box
create_box        2 box bond/type 2
```


---

### create_atoms

- 生成/填充原子

- 使用该命令之前，模拟盒子必须是存在的（使用 `create_box` 命令创建），同时晶格也必须已经被定义（使用 `lattice` 命令）

```bash
# 语法
create_atoms type style args keyword values ...

type       # 原子类型

# style
box                 # 在盒子内填充原子
region              # 在 region 内填充原子
single              # 填充单个原子
random              # 随机生成原子

# keyword
units               # lattice 以晶格距离作为单位；box 以盒子距离作为单位
basis
reamp


# 示例
create_atoms      1 box
create_atoms      2 single 5 5 5 units box

# 创建 γ-TiAl 金属间化合物
lattice           custom 1.0 &
                  a1  $a   0.0  0.0      &
                  a2  0.0  $b   0.0      &
                  a3  0.0  0.0  $c       &
                  basis 0.00  0.00  0.00 &  # Al
                  basis 0.50  0.50  0.00 &  # Al
                  basis 0.50  0.00  0.50 &  # Ti
                  basis 0.00  0.50  0.50    # Ti

region            box block 0 10 0 10 0 10
create_box        2 box
# 这里 create_atoms 后 1/2 都可以
create_atoms      2 box basis 1 1 basis 2 1 basis 3 2 basis 4 2
```


---

### pair_style

- 势函数类型

- ZBL：[pair\_style zbl command — LAMMPS documentation](https://docs.lammps.org/pair_zbl.html)

```bash
# 语法
pair_style style args


# 示例
# 默认设置，可用于只创建并输出构型文件
pair_style        none

# 只创建对势需要的近邻列表，不计算力和能量
pair_style        zero

# EAM
pair_style        eam/alloy

# ZBL 势；inner outer 截断半径
pair_style        zbl 3.0 4.0
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
pair_coeff        * * CuYM.eam.alloy Cu
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

- 定义近邻列表；只计算与在该原子截断距离内的原子的相互作用；近邻列表就是为了更新每个原子截断距离内的原子位置而设定的


```bash
max neighbors/atom: 2000, page size: 100000

master list distance cutoff = 6.95

# 近邻列表的一些属性, 以及构建方法
# 永久/临时/额外
1 neighbor lists, perpetual/occasional/extra = 1 0 0
# 计算量减半
attributes: half, newton on
# bin：表明 LAMMPS 使用的是基于网格索引的近邻列表构建法, 时间复杂度为 O(N)
pair build: half/bin/atomonly/newton
stencil: half/bin/3d

bin: standard
```

一个原子能够拥有的最多的近邻原子数量是 2000（默认值）

构建的近邻列表的半径 = 势函数的截断半径 + skin 值

atomonly：表明当前模型中参与计算受力的只有原子, 无键, 角, 二面角

page size 则是表明 LAMMPS 里面存储了多少个近邻对；默认值 100000；page_size 至少大于一个原子的最大的近邻原子数量的 10 倍

需要在内存中记录下每个近邻对中的中心原子和近邻原子的 ID,以便于后续在模拟中使用这些 ID 进行数组索引. 而 page_size 就是 LAMMPS 为存储这些近邻对的原子 ID 而申请的内存空间.

Dangerous builds, 该数值表示的是存在潜在漏算风险的近邻列表的重构次数。在 LAMMPS 中, 若不使用 neighbor_modify 命令进行调整, 近邻列表的构建默认是每运行一步都检查一次近邻列表是否存在需要重构的风险, 若发现存在需要重构的近邻列表, 会延迟运行 10 步之后（非立即重构）, 再进行重构近邻列表

LAMMPS 采用的判定是否需要重构是非常保守的策略。自从上一次重构近邻列表之后, 一旦有某个原子的位移超过 skin 值的一半, LAMMPS 就判定需要进行邻居列表重构

Dangerous builds 的数量不为 0, 并不意味着模拟中就一定出现了漏算或者错算。但对于一个正确的模拟来说, 无论跑多少步, Dangerous builds 都应该保持为 0。也可使用 `neigh_modify every 1 delay 0 check yes` 命令, 以稍微增加一些计算量的代价, 确保每次需要更新近邻列表的时候都立即更新, 而不会有任何的延迟

并不是所有的势函数都支持使用 openMP 进行并行, 但是所有的势函数都绝对支持基于 MPI 的并行

- 此命令设置影响 pairwise neighbor lists 构建的参数。所有原子对的 neighbor cutoff 距离等于其力截止加上 skin 距离，都存储在列表中。通常，skin 距离越大，需要构建的 neighbor lists 就越少，但每个时间步都必须检查更多的对以确定可能的力相互作用。skin 的默认值取决于模拟的单位选择；请参见下面的默认值。

- style 的值表示选择构建近邻列表的算法。bin style 通过 binning 创建列表，binning 是一种与 N/P（每个处理器的原子数）线性缩放的操作，其中 N=原子总数，P=处理器数 (processors)。它几乎总是比缩放为 (N/P)^2 的 nsq style 快。

- 默认值：2.0 bin for units = real or metal, skin = 2.0 Angstroms

```bash
# 语法
neighbor skin style

skin                 # 超出势函数的截断半径的额外距离

# style
bin
nsq
multi
multi/old


# 示例
neighbor          0.3 bin
neighbor          2.0 nsq
```


---

### neigh_modify

- 设置近邻列表构建和使用的参数；一次模拟可能需要多个近邻列表

- *every*, *delay*, *check*, and *once*选项影响模拟运行时生成列表的频率。*delay*设置意味着在上一次构建之后至少 N 个步骤之前从不构建新列表。*every*设置意味着每 M 步尝试构建列表（after the delay has passed）。如果*check*设置为 no，则在满足延迟和每个设置的第一步上构建列表。如果*check*设置为 yes，则*every*和*delay*设置将确定何时可能执行构建，但只有在自上次邻居列表构建以来至少有一个原子移动了超过 neighbor skin 距离（在 neighbor 命令中指定）一半的情况下，才会进行实际构建

- `once` 只在开始运行时构建一次近邻列表，并且从不重新构建，除非在写入 restart 文件时，或使用 fix 相关命令（如 fix deposit、fix evaporate）。检查是否应该重构近邻列表耗时很少

- 默认值：delay=0, every=1, check=yes, once=no, page=100000, one=2000, binsize=0.0

```bash
# 语法
neigh_modify keyword values ...

# keyword
delay                # 在上一次构建之后至少N步之前，永远不要构建新的列表
everry               # delay pass后，每M步建立列表
check                # yes/no
once                 # yes/no；只在开始运行时构建一次近邻列表


# 示例
neigh_modify      every 2 delay 10 check yes page 100000
```


---

### group

- 对原子进行分组；group-ID 可被用于 velocity、fix、compute、dump 等命令中（最多支持 32 个 group）

- 即使不对原子进行分组，LAMMPS 也会设置一个默认的 `all` group-ID，即将所有的原子全部划分到 all 组内

```bash
# 语法
group ID style args

ID                         # 为 group 命令分配的 ID

# style
id                   # 原子 ID
type                 # 原子种类
region               # region
union                # 合并 group


# 示例
group             1 type 1
group             2 region 2
group             3 union 1 2
group             water type 3 4
group             sub id 10 25 50
```


---

### mass

- 设置原子类型的相对原子质量；只有在模拟盒子定义后，才能使用该命令

```bash
mass              1 26.982   # Al
```


---

### timestep

- 设置模拟时间步长

- 默认值：1 fs (real）、0.001 ps (metal；即 1 fs)

```bash
timestep          0.001
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
gaussian             # 原子速度分布满足高斯分布


# 示例
velocity          all create 300.0 4928459 dist gaussian
# 默认设置
dist = uniform
mom = yes
rot = no
```


---

### run

- 设置模拟运行步数

```bash
run               0  # 只计算系统的热力学量并输出
run               10000
```


---

### thermo

- 输出热力学信息频率

```bash
thermo            0     # 默认值 
thermo            100
```


---

### thermo_style

- [热力学信息 - 系统输出 - LAMMPS 中文站](https://lammpscnv2.vercel.app/zh/hello/novice/output.html#%E7%83%AD%E5%8A%9B%E5%AD%A6%E4%BF%A1%E6%81%AF)

- 设置输出的热力学数据参量（格式）：
    - LAMMPS 预定义的一些关键字（如 press、etotal 等）所代表的参量
    - 由 compute、fix 或 variable 三个命令所得到的参量值，具体可通过 `c_ID`、`f_ID` 或 `v_name` 关键字引用（必须是全局量）

- 热力学输出量既可以是“广度量”也可以是“强度量”。前者与系统中的原子数成比例，如体系总能，而后者则与系统中的原子数无关，如体系温度。thermo_modify 命令的 `norm` 参数用以决定是否对广度量进行归一化操作。compute 和 fix 命令既可以产生广度量也可以产生强度量。variable 命令的类型为 `equal` 时仅能产生强度量值，若需要将此时的强度量值转变为广度量值，可通过在公式中除原子数（natoms）的方式得到

- 若通过 fix ave/time 做时间平均，可用 `f_ID` 来输出相应的平均数据

```bash
# 语法
thermo_style style args

# style
custom               # 最常用
one                  # 后三个 style args = none
multi
yaml

# custom args = list of keywords
atoms                # 原子数
step                 # 输出运行的步数是多少
temp                 # 体系温度
ke                   # 体系动能
pe                   # 体系总势能
etotal               # 体系总能量
press                # 压强（静水压力）
pxx                  # 6 个自由度的压强张量
count(all)           # 计算原子总数
dt                   # 步长
lx,ly,lz             # 盒子三个方向的长度
xlo, xhi ...         # 盒子边界位置
cpu                  #
tpcpu                #
v_name               # 变量

# 示例
thermo_style      custom step temp ke pe etotal

# 非全局量，会报错
compute           1 all pe/atom
thermo_style      custom step temp pe etotal c_1
```


---

### thermo_modify

```bash
thermo_style custom step vol temp etotal pe press

# 格式化
thermo_modify     format 1 %12d
thermo_modify     format 2 %22.12f
thermo_modify     format 3 %22.12f
thermo_modify     format 4 %22.12f
thermo_modify     format 5 %22.12f
```


---

### min_style

- 能量最小化算法

```bash
# 语法
min_style style

# style
cg                   # 共轭梯度法；对于绝大多数问题，被认为是效果最好的；默认设置
sd                   # 最速下降法；一般来说，没有 cg 算法收敛快
quickmin
spin

# 示例
min_style         cg
```

---

### min_modify

- 设置能量最小化算法的参数；不同的设置参数会影响收敛速率和能量最小化过程中需要计算力的次数

```bash
# 语法
min_modify keyword values ...

# keyword
dmax                 # 最小化过程中控制最大移动距离
line
norm


# 示例
min_modify        dmax 0.2
```


---

### minimize

- 能量最小化

```bash
# 语法
minimize etol ftol maxiter maxeval

etol                 # 能量收敛条件（无单位）
ftol                 # 力收敛条件（力的单位）
maxiter              # 能量最小化的最大迭代次数
maxeval              # 计算力或能量的最大次数

# 示例
minimize          1.0e-4 1.0e-6 100 1000
```

- 能量最小化结束后，程序会打印一段统计摘要信息，介绍满足了何种收敛判据，以及能量、受力、最终的线性搜索和迭代次数等

```bash
Minimization stats:
  Stopping criterion = max iterations
  Energy initial, next-to-last, final =
       -0.626828169302     -2.82642039062     -2.82643549739
```


---

### set

- 设置原子类型

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
set               type 1 type/fraction 2 0.5 12393
set               type 1 type/ratio 2 0.5 12393
set               type 1 type/subset 2 100 1239

# 按 group 替换
region            top block INF INF INF INF 20 INF units box
group             top region top
set               group top type/fraction 2 1 23985

# 按 region 替换
region            mid block INF INF 18 32 INF INF units box
group             mid region mid
set               region mid type/fraction 2 0.3 23985
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
string                  # 字符串变量

# region functions
count(group)            # 统计 region 中 group 的原子数
fcm(group,dim)          # 计算 region 中 group 的总受力分量

# region functions
count(group,region)     # 统计 region 中 group 的原子数
fcm(group,dim,region)   # 计算 region 中 group 的总受力分量


# 示例
variable          x index run1 run2 run3
variable          iter equal 40
variable          n loop ${iter}
```

### dump

- [数据转储 - LAMMPS 中文站](https://lammpscnv2.vercel.app/zh/hello/novice/dump.html#dump%E8%BE%93%E5%87%BA)

- 设置输出原子构型信息
    - LAMMPS 预定义的一些关键字（如 id、x、fx 等）所代表的参量
    - 由 compute、fix 或 variable 三个命令所得到的参量值，具体可通过 `c_ID`、`f_ID` 或 `v_name` 关键字引用（必须是 per-atom 量，与 thermo_style 命令相反）

- [LAMMPS学习系列（43） - dump输出坐标的几种格式](https://mp.weixin.qq.com/s/rEzHMkKAJk44hoKUcp_wtQ)

```bash
# 语法
dump ID group-ID style N file args

ID                   # 为 dump 命令分配的 ID
group-ID             # 被 dump 的原子所属 group ID
style                # custom、one 等
N                    # 每 N 步输出一次构型
file                 # dump 文件名
args                 # style 参数

# custom 参数：原子属性列表
mass                 # 相对原子质量
id                   # 原子 ID
type                 # 原子类型
element              # 原子对应元素
x, y, z              # 笛卡尔坐标
xu, yu, zu           # 笛卡尔坐标（不做 PBC 处理）
xs, ys, zs           # 分数坐标
xsu, ysu, zsu        # 分数坐标（不做 PBC 处理）


# 示例
dump              1 all custom 500 dump.lammpstrj id type x y z

compute           1 all pe/atom
# 会报错
thermo_style      custom step temp pe etotal c_1
# 不会报错
dump              1 all custom 500 dump.lammpstrj id type x y z c_1
```


---

### dump_modify

- 修改 dump 命令的预定义参数

- dump 通常输出的结果是无序的，可通过 `dump_modify sort` 修正

- 由于是并行计算，系统中的粒子被分配给各个核心，因此取回时会发现有些原子略微超出了盒子边界。这通常来说不要紧，如果非常在意，可通过 `dump_modify strict` 修正

- 由于是每多少步进行一次，默认第一步是不进行输出的，只会输出 minimize 的最后一步和后面的周期。可通过 `dump_modify first` 修正

```bash
# 语法
dump_modify dump-ID keyword values ...

# keyword
sort
append

# sort 值
off                  # 乱序输出以提高性能；默认
id                   # 通过原子 ID 对输出进行排序
N                    # 通过第 N 列数据对输出进行升序排序
-N                   # 通过第 N 列数据对输出进行降序排序


# 示例
# 用于中断后重算时，将构型数据追加到之前的同名 dump 文件中
dump_modify       1 append yes
```


---

### undump

- 关闭先前定义的 dump，使其不再处于活动状态。这将关闭与 dump 关联的文件。

```bash
undump            1
```


---

### fix

- 给原子施加约束；`fix` 是在时间步进或最小化期间应用于系统的任何操作；可能是在时间积分的过程中更新原子的位置和速度，或是控制温度，或是给原子施加约束力，或是强制某种边界条件，或计算过程诊断，等等

- fix 的 style 有很多，且大多是单独的命令

- fix 引用（compute references）：`f_ID`

```bash
# 语法
fix ID group-ID style args

ID                   # 为 fix 命令分配 ID

fix ave/time
fix ave/correlate

fix temp/rescale

# 示例
fix               1 all nvt temp 300 300 100.0

# 对原子进行操作
```


---

### fix setforce

```bash
fix ID group-ID setforce fx fy fz keyword value ...

fx fy fz             # 力分量值；可以是变量
NULL                 # 变量，不改变（不额外设置）该方向的受力

# 示例
# 用于表面能、GSFE 计算
fix               1 all setforce 0.0 0.0 NULL
```


---

### fix nve

- 执行普通 (plain) 时间积分，以在每个时间步更新组中原子的位置和速度。这创建了与微正则系综（NVE）一致的系统轨迹，前提是存在（完全）周期性边界条件，并且没有系统的其他 “操纵”（例如，修改力或速度的固定）

- 时间积分采用 Verlet 算法

```bash
fix ID group-ID nve

# ID, group-ID与fix命令中定义相同
```


---

### fix nvt/npt/nph

- [LAMMPS中的系综（NPT/NVT）命令](https://zhuanlan.zhihu.com/p/109410109)（只是对官网的翻译）

- 这些命令用来对 Nose-Hoover 型的 non-Hamiltonian 运动方程进行时间积分。该运动方程用以从正则系综（NVT）、等温等压系综（NPT）、等焓系综（NPH）采样生成原子的位置和速度，从而对所定义的 group 内的原子在每一个时间步进行位置和速度的更新

- Nose-Hoover 控温 Tdamp（温度阻尼系数） 建议值 100\*dt、控压 Pdamp（压强阻尼系数） 建议值 1000\*dt（metal 单位制下，timestep 取 0.001，即 1 fs 时，对应的 Tdamp=0.1、Pdamp=1.0）

- 温度、压强不是保持不变，而是会有振荡，振幅与 Tdamp、Pdamp 有关

- 使用 npt 时必须保证在至少一个方向上控压，且这个方向的边界条件必须是 p

- `iso`

```bash
# 语法
fix ID group-ID style_name keyword value ...

# style_name
nvt
npt
nph

# keyword
drag                 # 热浴/压浴的 drag 因子；没必要加（以前算力不足时的做法）

# keyword value
# temp
Tstart Tstop Tdamp
# iso/aniso/tri
Pstart Pstop Pdamp


# 示例
fix               1 all nvt temp 300.0 300.0 100.0
```


---

### fix box/relax

- 在能量最小化过程中对模拟盒子施加外部压力或应力张量。这样就可以在最小化迭代过程中改变模拟盒子的大小和形状，使最终构型既是原子势能的能量最小值，又使系统压力张量接近指定的外部张量。从概念上讲，指定正压 -- 挤压模拟盒子，负压通常允许模拟盒子膨胀

- 正交盒子有 3 个自由度（x、y、z），三斜/非正交盒子有 6 个自由度（x、y、z、xy、yz、xz）

-  `iso` 表示根据静水压（压强张量对角分量的平均值）控制三个盒子矢量的长度，且按同一比例缩放（x、y、z 三个方向同时耦合控压）

- `aniso` 表示根据静水压控制三个盒子矢量的长度，但允许独立变化（x、y、z 三个方向各自独立控压，不进行耦合）

- `tri` 表示根据静水压控制所有盒子自由度，且允许独立变化

- `vmax` 用于限制能量最小化一次迭代中盒子体积的变化分数。若在最小化过程中压力没有稳定下来，可能是因为体积波动太大

- 默认值：vmax=0.0001

```bash
# 语法
fix ID group-ID box/relax keyword value ...

# iso Ptarget 等效于
x Ptarget y Ptarget z Ptarget couple xyz
# aniso Ptarget 等效于
x Ptarget y Ptarget z Ptarget couple none
# tri Ptarget 等效于
x Ptarget y Ptarget z Ptarget xy 0.0 yz 0.0 xz 0.0 couple none


# BCC、FCC
fix               1 all box/relax iso 0.0 vmax 0.01
# 正交晶系
fix               1 all box/relax aniso 0.0 vmax 0.01
```


---

### fix deform

```bash
# 语法
fix ID group-ID deform N parameter style args ... keyword value ...


N                    # 每 N 个时间步长进行盒子变形

# 参数
x y z xy xz yz

# style
final
delta
scale
erate                # 工程应变率
trate                # 真实应变率

remap x              # 重新映射原子坐标至变形中的盒子；即原子坐标随盒子尺寸改变


# 示例
variable          srate0 equal 1.0e10            # 实际应变速率 10^10 /s
variable          srate equal "v_srate0/1.0e12"  # 单位转换 s -> ps 0.01 /ps
fix	              1 all deform 1 x erate ${srate} units box remap x
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

### delete_atoms

- 删除原子

- 删除原子后，原子 ID 不连续，使用 `compress yes` 可对 ID 序号进行压缩，即重新排序，产生连续的原子 ID。

- 默认设置：compress=yes, bond=no, mol=no

```bash
# 语法
delete_atoms style args keyword value ...

# style
group                # 删除 group 内的原子
region               # 删除 region 内的原子
overlap              # 删除重叠原子
random               # 随机删除原子

# overlap 参数
cutoff group1-ID group2-ID

# keyword，值均为 no/yes
compress
bond
mol


# 示例
delete_atoms      group 1
delete_atoms      region 2
delete_atoms      overlap 0.3 g1 g2
```


---

### displace_atoms

- 移动原子位置、旋转

```bash
# 语法
displace_atoms group-ID style args keyword value ...

# style
move                 # 移动原子位置
rmap
random               # 移动的位移随机
rotate


# 示例

```


---

### change_box

- 改变盒子的体积/形状/边界条件

```bash
# 语法
change_box group-ID parameter args ... keyword args ...

# parameter
x y z xy yz xz       # 6 个分量
boundary             # 改变边界条件
ortho                # 使盒子正交
triclinic            # 使盒子三斜
set                  # 保存当前的盒子的状态
remap                # 重新映射原子坐标

# x y z xy yz xz 参数值
final                # 绝对值
delta                # 相对值
scale                # 缩放
volume               # 保持体积不变


# 示例
# 使 x=0 移至盒子中心
variable          hx equal "(xhi - xlo)/2"
change_box        all x final -${hx} ${hx} remap units box
# z 方向添加 5Å 的真空层
change_box        all z delta 0 5
# x 扩 1.1 倍，z 缩 1.1 倍
change_box        all x scale 1.1 z volume
# x 扩 1.1 倍，y、z 缩 √1.1 倍
change_box        all x scale 1.1 y volume z volume
# x、y 扩 1.1 倍，z 缩 1.21 倍
change_box        all x scale 1.1 z volume y scale 1.1 z volume
```


---

### box

- large 表示允许非正交盒子的倾斜系数可以是任意数（tilt factors），默认值为 small

```bash
box               tilt large
```


---

### replicate

- 扩胞

```bash
replicate         1 2 3
```


---

### atom_modify

```bash
map
sort
```


---

### read_data

- 读取 LAMMPS data 构型格式文件（可读取 gzip 格式）

```bash
read_data         data.lmp
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

- 将构型保存成 LAMMPS data 格式文件

- 使用 LAMMPS 内置命令构建模型后，需设置原子类型对应的相对原子质量（或势函数），再使用 `write_data`，否则会报错

```bash
write_data        data.lmp
```


---

### read_restart、restart、write_restart

- 用于重启计算（二进制文件）

- 体系大，驰豫时间也对应长，在体系驰豫后保存 restart 文件，可直接读取用于后续的模拟过程，无需再进行驰豫，可提高效率

- 在能量最小化或驰豫阶段，一般只需在驰豫结束保存一个 restart 文件即可

- LAMMPS 源码 tools 目录下的 restart2data 工具，可将二进制 restart 文件转换成 LAMMPS data 构型格式文件，以便 `read_data` 读入

- restart 文件存储、不会存储的信息：

```bash
read_restart      restart.equil

# 周期性；每隔 10000 步保存一次，restart.equil.* 文件
restart           10000 restart.equil
# 一次性
write_restart     restart.equil
```

### fix print

- 每 N 步输出文本内容（用于调试）

- 默认选项：无文件输出，screen=yes，输出文件中的标题行 title string（# 号是自带的）`# Fix print output for fix-ID`

```bash
# 语法
fix ID group-ID print N string keyword value ...

N                    # 每 N 步输出

# keyword
file                 # 写入内容到文件；文件名不能为变量？
append               # 追加内容到文件
screen               # 是否输出到屏幕；yes/no


# 示例
fix               1 all print 100 "${strain} ${stress}" file strain_stress.dat screen no
```


---

### fix_modify

```bash

```


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

- 2024 年引入的

- [LAMMPS 蒙特卡洛 MC 模拟案例](https://mp.weixin.qq.com/s/79qR5g0m9FlpgE-JAO7J-Q)

- LAMMPS 示例代码路径 `examples/mc/in.sgcmc.eam`

```bash
# 语法
fix ID group-ID sgcmc every_nsteps swap_fraction temperature deltamu ...

every_nsteps         # 每隔 every_nsteps MD 步执行一次 MC 循环
swap_fraction        # MC 循环中原子交换比例（1.0 表示所有原子都进行 trial moves）
temperature          # MC 温度（Metropolis criterion中的 T；通常和 MD 温度相同）
deltamu              # 化学势差



```


---

### fix phonon

- [Fetching Title#3ues](https://docs.lammps.org/fix_phonon.html)

- 基于涨落 - 耗散理论（luctuation-dissipation theory）计算动力学矩阵

- 该 fix 命令假设体系为具有周期性点阵的晶体。体系的温度不应超过熔点，以保持体系为固态

```bash
# 语法
fix ID group-ID phonon N Noutput Nwait map_file prefix keyword values ...

N                    # 每隔 N 时间步测量一次格林函数
deltamu              # 化学势差
Noutput              # 每隔 Nouput 测量输出一次动力学矩阵
Nwait                # 在测量前等待 Nwait 时间步
map_file             # map 文件或 GAMMA
prefix               # 输出文件的前缀
```


---

### jump

- 关闭当前输入脚本文件，打开命令中文件名所指定的文件，并从那个文件开始读入 LAMMPS 命令；与命令 `include` 不同的是，LAMMPS 不会再返回到之前的输入文件了

- `SELF` 含义：重新打开当前 in 文件并再次读取

```bash
# 语法
jump file label

file                 # 要跳转到的 in 文件名
label                # 可选；要跳转到的 in 文件中的设置的标签；从标签的位置开始向下执行


# 示例
jump              newfile
jump              in.run2 runloop
jump              SELF runloop
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
next              x
next              a t x myTemp
```


---

### if

- 在输入文件中提供 if-then-else 功能

```bash
# 语法
if boolean then t1 t2 ... elif boolean f1 f2 ... else e1 e2 ...


# 示例；中间不能有空行，否则会报错
if                "${pot_type} == TaNbVMoW_mtp" then &
"pair_style        mlip TaNbVMoW_mtp.ini" &
"pair_coeff        * *" &
elif              "${pot_type} == eam" &
"pair_style        eam/alloy" &
"pair_coeff        * * Nb.eam.alloy Nb" &
else              "print 'No Match'"
```


---

### print

- 打印文本字符串到屏幕和日志文件

```bash
# 语法
print string keyword value

# keyword
file                 # 写入文件
append               # 追加内容到文件
screen               # yes/no
universe             # yes/no

# 示例
variable          outputfn string "file.dat"
# 格式化输出；只能格式化 thermo 关键字的变量
print             "$(v_N) $(v_pe:%15.6f)" file ${outputfn}
```


---

### shell

- 执行 Shell 命令

```bash
# 语法
shell command args

command              # cd mkdir mv rm rmdir 等 Shell 命令


# 示例
shell      ./script.sh     # 执行 Bash 脚本
shell      mkdir folder    # 创建目录
```


---

### compute

- 为 group 原子定义一种计算

- style 中含有 “atom”，为单原子量；含有 “local”，为局域量；不包含前两者，为全局量

- compute 引用（compute references）：`c_ID`

- 计算出的量是瞬时值，也就是说它们只是原子在当前时间步或迭代步的信息。当然，compute 命令也可以在内部保存体系在之前一个状态的某些信息

- 定义 compute 命令的时候并不会执行计算。真正的计算过程是被其他 LAMMPS 命令激活的，比如某些 fix 命令需要计算温度的时候，或这需要产生热力学信息的时候，或者需要 dump 输出到文件中的时候

```bash
# 语法
compute ID group-ID style args

ID                   # 为 compute 命令分配 ID

# style
ke                   # 总动能
ke/atom              # 平均原子动能
pe                   # 总势能
pe/atom              # 平均原子势能
pressure
rdf                  # 计算 rdf
msd                  # 计算 MSD
temp
voronoi/atom


reduce sum
reduce ave



# 示例
compute           1 all temp
compute           1 all pe/atom
# 计算每个原子在 x y z方向上所受到的力
compute           1 all porperty/atom fx fy fz

# 将 W.xyz 导入 OVITO，Add Modification -- Color coding，在 input property 选项中选择 c_1 可得到以平均原子势能为 colorbar 的构型
compute           1 all pe/atom
dump              1 all custom 100 W.xyz id type x y z c_1
```

- 一些单独的 compute 命令

```bash
compute pressure            # 整体压强
compute stress/atoms        # 局部压强

compute chunk/atom
compute msd/chunk

compute cna/atom

compute vacf
```


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

### neb

WIP...

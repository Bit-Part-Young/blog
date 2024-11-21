---
title: 分子动力学原理
top: false
cover:
toc: true
mathjax: true
summary: 分子动力学原理
description: 分子动力学原理
tags:
  - 分子动力学
categories:
  - 科研工具
date: 2023-09-27 19:00:00
abbrlink: 207179
password:
---

# 分子动力学原理

## 多尺度介绍

多尺度课程分布：
- 新生开学第一周不上
- 课程介绍 1 周
- 国庆放假 1 周
- MD：4 次课
- DFT：4 次课
- PF：5 次课？

---

模拟和建模的区别

多尺度方法：

- 多层次：
- 同时进行/并行：物理机制上无法将其分开，强耦合；可以分成不同的区域
- 时间多尺度


---

## 介绍

molecular dynamics 叫分子运动学更合适


>[Notes on MD hands-on session of MSE6701H-CHN - CodiMD](https://notes.sjtu.edu.cn/s/ULArhqGqt)

C++/Python 实现 MD（待测试）
[GitHub - GiovanniBussi/simplemd: A simple Lennard-Jones molecular dynamics software](https://github.com/GiovanniBussi/simplemd)

参考资料：

>[GitHub - stanfordbshan/CompMatBook: Computational Materials Science(Book)](https://github.com/stanfordbshan/CompMatBook/)

>[单斌](https://bohrium.dp.tech/user/stanfordbshan)

>[GitHub - brucefan1983/Molecular-Dynamics-Simulation: Sample codes for my book on molecular dynamics simulation](https://github.com/brucefan1983/Molecular-Dynamics-Simulation)

[MD 笔记 - zhaobo9337 - 知乎](https://www.zhihu.com/people/zhaobo9337/posts)

[论文 - Introduction to molecular dynamics simulations](https://pubs.aip.org/aapt/ajp/article/88/5/401/1056833/Introduction-to-molecular-dynamics-simulations)


MD 教程（含广义层错能计算）
>[GitHub - shuozhixu/LAMMPSatUCSB](https://github.com/shuozhixu/LAMMPSatUCSB)


含高熵合金模型生成及弹性常数计算相关脚本（从 LAMMPS 官方例子修改得到）
>[GitHub - jianhuizhai/LAMMPS: This folder contains the examples of LAMMPS and some useful programming codes or results.](https://github.com/jianhuizhai/LAMMPS)


velocity verlet 算法（含两原子及多原子）
>[Verlet integration - Wikipedia](http://en.wikipedia.org/wiki/Verlet_integration#Velocity_Verlet)

>[GitHub - antoineblosse/velocityVerlet: Research Lab - Professor Paesani](https://github.com/antoineblosse/velocityVerlet)（一个简单简谐振子的 velocity verlet 算法实现）

>[md.py](https://github.com/glennklockwood/md-intro/blob/master/md.py)（氩原子的 MD 实现：LJ 势 + velocity verlet + 能量、力演化）


含 Al、石墨烯的拉伸测试
>[GitHub - nuwan-d/LAMMPS\_tutorials\_for\_short\_courses: Required LAMMPS and MATLAB files for several molecular dynamics simulations.](https://github.com/nuwan-d/LAMMPS_tutorials_for_short_courses)


>[LAMMPS tutorials - EVOCD](https://icme.hpc.msstate.edu/mediawiki/index.php/LAMMPS_tutorials.html)

---


```text
螺旋上升：解耦


纳米线：用圆柱框住晶体，圆柱外的原子删除
```


---

## 基本原理

- 牛顿第二定律

- 用时间平均（达到平衡）代替系综平均（两者等价）

系综涉及统计物理相关内容，计算复杂（相空间等知识点）

补充（ChatGPT4 生成）

- **遍历性假设**（Ergodic Hypothesis）：在分子动力学中，遍历性假设是一个核心概念，它表明系统在足够长的时间内，其通过时间演化能遍历其所有可能的微观状态。换句话说，系统的任何一个微观状态都能够在其时间演化的轨迹中出现。
- **时间平均与系综平均的等价性**：在理想条件下，如果一个物理系统满足遍历性，那么对系统的某个物理量进行长时间的时间平均，得到的结果应该与通过统计系综中大量相同系统的平均（即系综平均）相同。这意味着单个系统的长时间行为可以代表整个系综的平均行为。


---

## 基本步骤

- 初始条件/化

- 演化（核心）

- 结果后处理


---

### 初始化

- 初始化原子构型


- 初始化速度/温度

速度满足麦克斯韦玻尔兹曼分布（可用平均分布代替）

速度修正，保证体系总动量为零


- 边界条件

- 控制参数


---

### 力计算

力：相互作用能 U（势能） 对原子坐标的偏导数

---

### 积分算法

推进算法也称作积分算法

---

- verlet 算法

$$r(t+\Delta t)=2r(t)-r(t-\Delta t)+a\Delta t^2+O(\Delta t^4)$$

$$v(t)=\frac{r(t+\Delta t)-r(t-\Delta t)}{2\Delta t}+O(\Delta t^2)$$

根据当前及上一时刻位置确定下一时刻的坐标位置及速度

优点：位置确定的精度高 $O(\Delta t^4)$；

缺点：确定当前速度需要下一刻的位置，速度确定的精度低，$O(\Delta t^2)$

Verlet 不是一个自启动的算法，所以第一步的时候，我们需要根据初始的速度，反推前一步的位置。只有同时有当前步和前一步的位置信息，Verlet 算法才能够更新迭代获得下一步的位置信息

代码示例：[一维谐振子的Verlet算法.ipynb](https://github.com/stanfordbshan/CompMatBook/blob/main/Chapter06/%E4%B8%80%E7%BB%B4%E8%B0%90%E6%8C%AF%E5%AD%90%E7%9A%84Verlet%E7%AE%97%E6%B3%95.ipynb)

---

- velocity verlet 算法

原理：首先根据当前位置和速度计算出下一时刻的位置，然后再根据新的位置计算出下一时刻的加速度，最后再用新的加速度和旧的加速度的平均值来更新速度。

$$x(t + \Delta t) = x(t) + v(t) \Delta t + 0.5 * a(t) * {\Delta t}^2$$

$$a(t + \Delta t) = f(x(t+\Delta t))$$

$$ v(t + \Delta t) = v(t) + 0.5 *(a(t) + a(t + \Delta t)) * \Delta t$$

实际计算：推进半步（减少变量存储 4 个变量，位置 1 速度 1 加速度 2；减少为 3 个变量）

$$step 1: v(t + \Delta t/2) = v(t) + 0.5 * a(t) * \Delta t$$

$$step 2:x(t + \Delta t) = x(t) + v(t + \Delta t/2) * \Delta t$$

$$step 3: a(t + \Delta t) = f(x(t+\Delta t))$$

$$step 4: v(t + \Delta t) = v(t + \Delta t/2) + 0.5 * a(t + \Delta t) * \Delta t$$

---


- leap frog 算法

- 参考：
    - [蛙跳积分法 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-hans/%E8%9B%99%E8%B7%B3%E7%A7%AF%E5%88%86%E6%B3%95)
    - [Leapfrog integration - Wikipedia](https://en.wikipedia.org/wiki/Leapfrog_integration)


原理：在相同的时间步，位置和速度的更新是分开的

$$x(t + \Delta t) = x(t) + v(t+\Delta t/2)*\Delta t$$

$$v(t + \Delta t/2) = v(t-\Delta t/2) + a * \Delta t$$

---

### 时间步长

步长太小：耗时

步长太大：可能无法描述正确的运动轨迹

合适的步长：能够正确描述运动轨迹（最快的运动 原子振动）；

原子振动量级：THz（$10^{12}$ 量级），时间 $10^{-13}$ 量级

原子振动周期的 50~100 分之一；$10^{-15}$ 量级（fs 飞秒量级）

----

### 边界条件

simulation box/cell/domain：模拟盒子/胞

边界原子如何处理

---

- 自由边界条件：分子、团簇、纳米颗粒

- 固定边界条件：压缩模型、表面模型中下表面一两个原子层进行固定

- 周期性边界条件
    - 可以消除自由表面的影响；模拟无穷大的体系
    - **自己的原子之间引入了人为的相互作用**；限制了声子波长；

实现：



- 最小影像准则：（计算胞不能任意小）

$$
L > 2*R_{cutoff}
$$

计算位错相关性质，体系至少含几十万个原子才算比较准确


---

### MD 能做/不能做

- 能做的：

不能做的：涉及到电子（视原子为 particle）

时间尺度：ns；长度尺度：nm


---

## 势函数

### 势函数

- 势函数查找网站
    - [OpenKIM · Knowledgebase of Interatomic Models · Interatomic Potentials and Force Fields](https://openkim.org/)
    - [Interatomic Potentials Repository](https://www.ctcms.nist.gov/potentials/)

- 总能、势能（总能 - 自能）

- 势函数（物理领域）、力场（化学领域）

- 材料中的键（键合特征）：金属、陶瓷、高分子、稀有气体

- Lennard-Jones 势（6-12 势；一个人名）
    - 正项（12，数学意义）排斥，负项（6，有物理依据）吸引
    - 势能为 0；平衡距离
    - 描述惰性气体较适用（物理相互作用）
    - 截断问题：引入截断会导致相互作用力的不连续
        - Truncation 截断（LAMMPS：lj/cut）
        - Shift 平移（LAMMPS：pair modify shift yes）
        - Tail 多项式拟合（有两个截断距离；LAMMPS：pair modify tail yes）
    - Mixing rules 混合法则（LAMMPS：pair modify mix ...）：
        - 几何平均
        - 算术平均（更常用）
        - 六阶近似

- 其他势函数
    - Mie
    - Buckingham：吸引项与 LJ 类似；原子间距离很小时，会迅速吸引（缺点）；[Buckingham potential - Wikipedia](https://en.wikipedia.org/wiki/Buckingham_potential)
    - Born-Mayer-Huggins
    - [莫尔斯势 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E8%8E%AB%E5%B0%94%E6%96%AF%E5%8A%BF)
    - [Welcome to potentials’s documentation! — potentials 0.1 documentation](https://interatomic-potentials.readthedocs.io/en/latest/index.html)

- 离子体系的势函数
    - 对势 + 库伦相互作用（+ 三体角度项）
    - 极化问题：引入 core-shell 模型

- 中心力场（Central force potential）
    - 相互作用只与距离有关
    - 更倾向于简单构型，如 BCC FCC
    - 满足柯西关系（$C_{12}=C_{44}$；某些体系会不满足）

- 金属体系势函数
    - 嵌入原子势 EAM：
        - 二体单独考虑，其余 n 体考虑成一项（嵌入能）
        - 截断到第 3、4 近邻足够
        - 含共价键的体系和 HCP 结构，描述不够准确
    - MEAM：Modified EAM；电子密度贡献拆成两部分，引入了三体项之间的相互作用

- 高分子势函数
    - 势函数组成如下
        - 键长
        - 键角（球谐函数 + 非球谐函数）
        - 二面角（前三个：成键相互作用）
        - 前三项可用简谐形式近似（键不会断掉，无法描述化学反应，非反应力场）
        - 物理相互作用
        - 库伦项 + ...
    - Morse 势可描述有限距离下的键断

- 反应力场 Reactive Force Field
    - 键序 Bond Order（键长越短，键序越高）
    - 校正
    - 计算量很大

- 势函数拟合
    - 最小化：计算 cost function
    - 需要考虑相转变能量差计算性质

- ML 势函数


---

### 力的计算

- 力演化 - 对势：需要原子之间的距离

- Demo 程序的计算复杂度 $O(N^2)$

- 近邻列表 Neighbor list：将计算复杂度减小为 $O(N)$
    - 第一次 $O(N^2)$，后面 $O(N)$
    - 原子移动距离小于 $r_{skin}$，不更新；大于，更新（小，更新频率会频繁；更新的计算复杂度 $O(N^2)$）

- 力的计算 - 角度项

- 长程相互作用（库伦相互作用）
    - 直接计算库仑相互作用时遇到的问题，即直接求和收敛缓慢且计算成本高
    - 算法：
        - Ewald sum method：借助傅里叶变换
        - PP/PM 方法（Particle-Particle/Particle-Mesh）
        - Random Batch Ewald（交大团队开发）

- 经验势函数总结

- 势函数选择：Bonding，Transferability，Accuracy，Efficiency


---

## 分子静力学

### 案例 1：表面能计算

$$
\gamma = \frac{G_{slab} - G_{bulk}}{A_{surface}} \approx \frac{E_{slab} - E_{bulk}}{A_{surface}}
$$

总体步骤：
- 计算 bulk 的总能量（获取平衡常数及该平衡常数下的构型的 energy/ atom）
- 计算 slab 的总能量
    - 切表面
    - 弛豫表面
    - 计算弛豫表面的总能量
- 计算表面能


>熵的组成：构型熵、振动熵（声子谱计算可得到）、
>
>势函数中约定了单位

---

#### 总能计算

- bulk 体系平衡总能 LAMMPS 计算脚本

```bash
# LAMMPS input script for total energy calculation
units metal
boundary p p p
atom_style atomic

lattice fcc 3.615
region box block 0 10 0 10 0 10
create_box  1 box
create_atoms  1 box

# Potential
pair_style eam
pair_coeff * * Cu_u6.eam
neighbor 0.2 bin
neigh_modify delay 5

# Time step
timestep  0.001

# Variables to output
variable vpa equal "vol/ atoms"
variable epa equal "pe/ atoms"

# MD
fix 1 all nve
run 0

# Output the energy
print "${a} \${vpa} \${epa}" append ev.dat
```

>`fix` - 对体系做各种改变

>`run 0` - 并非跑零步，只计算能量



---

#### 切表面

```bash

```


---

### 能量最小化

势能曲面

鞍点：在某个路径下，能量对坐标的二阶导小于零，其他路径均大于 0


---


局域能量最小化


Hessian 矩阵通常很难求


相关算法

- 基于一阶导
    - 最速下降法
    - 共轭梯度法


- 基于一阶和二阶导
    - BFGS


```bash
min_style sd
min_style cg
min_style htfn
min_style quickmin
min_style fire
```


---


全局能量最小化

- 模拟退火
- 遗传算法
- 粒子群算法


---


过渡态寻找

示例：表面模型中吸附原子的扩散



跃迁概率

- NEB（LAMMPS 和 VASP 中有）
- Dimer
- ART-n



mpirun lmp -in in.file -sf opt -sc none (-sf opt -sc none 表示导入优化的包)





-----

### 案例 2：熔点计算

固液相变点

熔化的相变是一级相变（状态函数的一阶导不连续）

熔化是晶核形成

缺陷较容易形核

过热现象

LAMMPS 升降温速率：10^11K/s

DSC 速率：10K/min

升温、降温速率过快

降温：均质形核，得到的构型最后可能有晶界，可能形成多晶



- 加热 - 冷却法

分子动力学：升温（过热）与降温（过冷）得到的突变温度点不会重合（原因：分子动力学模拟的升/降温速率比实验的升/降温速率快很多）


不是很好的原因：
模拟的构型是 perfect
模拟的升温、降温速率过快



---



界面迁移速度为零时可能为熔点




---


- 固液共存法
  - 构建固液界面
    - 切换到 NVE 系综（孤立体系），不控温
    - 切换到 NPH
    - 使用 2 种 thermostat


中间区域高温，两边低温，低温高温热传导速率不一样


---

### 系综

NVE 系综：少见





NVT 系综

温度的波动需满足的一定的规律

温度的方差

能量的方差




NPT 系综：



---

## 控温

thermostat（热浴/恒温器）

也可以通过控制原子受力

控温离不开控制速度

$$
E_K = \frac{3}{2}Nk_BT=\frac{1}{2}\sum m_i v^2_i
$$

- Velocity scaling（对速度标定）
    - isokinetics 算法：速度重置，较野蛮；实际体系的温度演化不符合热力学统计规律，不是很好的控温方法
    - Berendsen 算法：比 isokinetics 好很多，能给出部分合理的热力学统计温度
- Stochastic thermostat（引入一些随机过程）
    - Andersen 算法
    - Langevin 算法：LAMMPS 中有
- Extended Langrangian（扩展拉格朗日）
    - Nose-Hoover 算法
    - Nose-Hoover chain 算法






计算当前温度，标定

$$
\lambda = \sqrt{\frac{T_{target}}{T(t)}}
$$

速度重置

$$
v^{'}_i = \lambda v_i
$$

温度演化不满足正则系综下的要求，不合理

有时候有用，初始模拟时，构建的体系通常远离平衡状态，通过这种方式，可以使体系快速达到想要的状态，基于该状态再进行实际的模拟




Berendsen 算法

$$
\lambda = \sqrt{1+\frac{\Delta t}{\tau}\left[ \frac{T_{target}}{T(t)} -1 \right]}
$$

$\Delta t$ 为时间步长，引入 coupling constant $\tau$，使温度缓慢达到目标温度，使体系变化不那么剧烈，相对好一些，但也无法证明其能给出正确的正则分布








Andersen 算法

每步每个原子进行速度重置

能给出正则系综下的温度要求；会破坏原子轨迹的连续性；可能导致能量动量不守恒；用的也不是很广泛



Langevin 算法

粘滞力 + 随机力
>只有粘滞力，会导致最终静止

对原子的受力进行修改

$$
f_i = -E - \frac{m}{\tau}v_i+w_i
$$

E 为势函数给出的力，v 为粘滞力，w 为随机力（使原子不会停止下来）






Nose-Hoover 算法

$$
f_i = -E - m \gamma v_i
$$

粘滞力系数 $\gamma$

---

## 控压

控制压强通过控制体系的体积；体积通过控制速度

压强计算：Virial theorem

压强变化率 $\tau_P$



$\alpha$

$\alpha$ 和 $\tau_P$ 的关系

$$
\alpha = -\frac{\beta \left[ P_{target}-P(t)\right]}{3\tau_P}
$$

$\beta$ 为体模量



>https://docs.lammps.org/fix_nh.html

>https://docs.lammps.org/fix_press_berendsen.html


---

## 性质分析

### 性能参数评估

直接获取的物理量


- N V E_k E_p M \rho
- c_i
- U H
- T P

T 的误差与 T/\sqrt{N}成正比

静水压力 P = 1/3 \sum P ii




---

计算推导的物理量

- 弹性常数

>

- 等压热容 Cp

有限差分法：需要选取适中的值；结果更稳定




H 的方差：误差可能会大一些


- 等温压缩系数（体模量 B 的倒数）


- 热膨胀系数

V、H 的协方差

- 扩散系数

浓度梯度

均方位移 MSD = 2Dt



LAMMPS compute MSD


时间短，观察到的是原子的振动


- 剪切粘度

P 的自相关函数

NPT（更稳定）/NVT

上下薄层，找出上下层原子速度最大且方向相反的原子，对其速度进行交换

\tau = 粘度 · 速度/h

剪切率：v/h






- 热导
晶格热导，没有电子热导

J 热流

平衡 MD

非平衡 MD


交换动能


- 声子

力常数矩阵（0K 下）




速度自关联函数

Fluctuation dissipation

>[fix phonon command — LAMMPS documentation](https://docs.lammps.org/fix_phonon.html)


---

### 结构分析

pair correlation function


partial pair correlation function

实际算法：以每个原子为中心计算，最后求平均



宏观

局域

缺陷

性能参数和结构表征

热力学参数

结构参数

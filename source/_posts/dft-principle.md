---
title: DFT 原理
top: false
cover: false
toc: true
mathjax: true
summary: DFT 原理
tags:
  - 计算模拟
  - DFT
categories:
  - 科研基础
date: 2023-09-27 19:00:00
abbrlink: "50289"
password:
---

# DFT 原理

参考资料：

《计算材料学》华中科技大学 配套资源
>[materialssimulation.com/book](http://www.materialssimulation.com/book)


>[GitHub - stanfordbshan/CompMatBook: Computational Materials Science(Book)](https://github.com/stanfordbshan/CompMatBook/)

>[单斌](https://bohrium.dp.tech/user/stanfordbshan)



DFT 原理介绍
>[GitHub - czjiangjun/DFT\_Manuscript](https://github.com/czjiangjun/DFT_Manuscript)






DS-PAW：国产的 DFT 计算程序
>https://doi.org/10.1016/j.apsusc.2023.158083



PASP 程序：结合 VASP，主要处理磁性体系
>https://doi.org/10.1063/5.0043703

>http://www.cps.fudan.edu.cn/XHJ/CN/show.aspx?infolb=70&infoid=275&flag=9



---




基态
- 内聚能
- 平衡点阵常数（密度）
- 弹性模量和弹性常数（弹性能）
- 声子谱 力常数（能量对位移的一阶导数）
- 磁性有序（构造不同的磁性结构、磁性与晶体结构和体积等有关）
- 热稳定性
- 相变（主要是自由能）
- 空位/缺陷形成
- 扩散
- 化学反应
- 原子受力


激发态
- 比热（sp）
- 光发射
- 光吸收
- 带隙
- 传输性质

---

薛定谔方程简写成 SE


哈密顿量 能量算符

能量组成：
动能：电子、原子核动能
势能：电子之间、原子核之间、电子 - 原子核之间（+ 外部施加的势场）





与时间无关（稳态）


孤立 H 原子的 SE 能够精确求解

自由粒子（能量项只有动能）
一维无限深势阱




波恩海默/绝热近似

原子质量 10-27 量级
电子质量 10-31 量级

核心思想是把核的运动和电子的运动分开处理：处理电子运动时，认为核是固定不动的；处理核运动时，认为快速运动的电子建立一个平均化了的负电荷分布，核在电子的负电荷平均场中运动。





难点：电子之间的相互作用


考虑


veff

单电子近似与平均场近似

在平均场近似中，需要求解单电子本征方程才能得到体系的解，但要求解单电子方程又必须知道各个轨道的电荷分布

实际操作：该过程称为自洽场 (SCF) 方法



Hartree 近似 忽略了泡利不相容原理

有效势为两项

Hartree 近似，引入泡利不相容原理，将波函数写成行列式（SD Slater 行列式）


问题：平均场近似（自洽场）仍忽略了电子之间的关联（电子间的瞬时相关作用）


电子关联能：指精确的基态能量与 HF 能量之差：



泛函：把函数映射到一个数上

变分 和最小化相关




Hohenberg-Kohn 定理
vr 与 nr 是一一对应关系（反证法）

$$
E[n] = F[n] + V[n] = T[n] + U[n] + V[n]
$$

$U[n]$ 的主要部分为 $U_H[n]$ （Hartree 势能泛函）

$T[n]$ 的主要部分为 $T_S[n]$ （单电子动能泛函；单电子近似得到）

电子动能、势能泛函分解

$$
U[n] = U_H[n] + U_X[n]
$$

$$
T[n] = T_S[n] + T_C[n]
$$

$$
E_{XC}[n] = T_C[n] + U_X[n]
$$

$$
E[n] = T_S[n] + U_H[n] + E_{XC}[n] + V[n]
$$

T[n] U[n] 与体系无关（电子的动能、电子的势能）

V[n] 与体系有关，体系给定，则其可知（原子核对电子的势场）


有效势为三项



v(r) 用赝势近似



变分法得到单电子方程

$$
[-\frac{\hbar^2}{2m}\nabla^2 + v_{ext}(\vec r)+v_H(\vec r)+v_{XC}(\vec r)]\psi(r) = \varepsilon_{i}\psi_{i}(r)
$$

交换关联能的作用：抵消非物理的 Hartree 项


Jacob 天梯

局域密度近似（LDA）：第一级阶梯


广义梯度近似（GGA）：加入密度梯度作为泛函变量 第二级阶梯

常用 GGA 泛函是 PBE


meta-GGA 第三级阶梯

杂化密度泛函



>PPT 中的第 18 页的 fi 是占据数


---

## 晶体的电子结构

密度泛函理论没有引入近似


$\delta$ 函数

积分为 1


傅里叶变换

离散傅里叶变换


傅里叶级数


点阵和周期性 $\delta$ 函数类似



晶格的空间密度分布函数：周期性 $\delta$ 函数


电子密度分布函数 n(r) 、势能 v(r 也具有周期性
相关能量算符也具有周期性
波函数不具有周期性

| k+G | 的物理含义：与电子的动能相关，不能无限大；非常大时，其系数 c 会非常小

可以 k 限制在第一布里渊区 [-N1/2, N1/2]

k 点数：N=N1\*N2\*N3 晶体超胞
（k 是倒空间的某一个点，理论上有无数多个，可以将其限制在第一布里渊区内）

将薛定谔方程转换成本征值（求解）问题

将问题限制在原胞内

k 相互独立（可以进行并行处理）

对于每个 k，最多可以得到 M 个本征值
（可以不用求所有的本征值，求解其最小的一部分 k 即可）

k 的本征值给出能带结构


$e^{ikr}$ 为平面波形式


波恩 冯卡门 边界条件

Bloch 定理

倒空间原点

$$

\text{Schrödinger Equation} \rightarrow \text{Eigen problem}


$$

$$\sum_{m} \left[ \frac{\hbar^2 | \mathbf{k} + \mathbf{G}_m |^2}{2m_e} \delta_{m,m'} + V_{m-m'} \right] c_{i,m} = \varepsilon_i c_{i,m'}
$$

---

## DFT 第一性原理计算

### k 点采样

基态的电子密度应该与所有的 k 有关
每个 k 点对应一个电子密度
对 k 进行积分（布里渊区积分），只考虑占据态（fi 占据数）；仍是无数个 k 点

转换成采样求和的方式

均匀取样（isotropic sampling) 含义：模拟的超晶胞的各个方向长度是一样的（正方）

$$\frac{b_{1}}{N_{1}}=\frac{b_{2}}{N_{2}}$$

MP 方法（把 gamma 点避开）

$$
\vec{k} = \sum_{i=1}^{3} \frac{n_i}{N_i} \vec{b}_i
$$

shift MP 方法


gamma 点的计算误差较大，应尽量避开；有些情况无法避开

k 点在 FBZ 中的对称性（减小计算量，对计算的 k 在求和公式中增加权重）

不可约布里渊区


$\hat{S}$ 旋转操作


对于六方结构，MP 方法的 k 点取样与其对称性不是太符合，还是以 gamma 为中心



k 点取样规则：
- 每个方向上的 k 点密度应尽量保持一致
- k 点越密，结果越精确
- 对于原子或分子，无需 k 点取样，直接计算其 gamma 点
- 需要做收敛性测试



---

### 占据数

金属：导带没有填满


引入分数占据数 smearing 方法

$\sigma$ 展宽

---

### 截断能

---

### 赝势

把不成键的电子（内层电子）与原子核合并起来

---

## PBC 条件

计算耗时 N3


真空层厚度：一般至少 10 埃

---

DFT 只能预测基态电子密度和基态总能

总能
力
晶格常数
键长
振动频率
声子谱
静态介电相应

激发态能量（价带的是激发态能量；导带的是激发态）
能带（原理上就无法准确计算；GW 方法；泛函改进）
能带结构
波函数（计算的是辅助波函数）
费米面
超导
激子
电子输运

---

精度


内聚能精度较低

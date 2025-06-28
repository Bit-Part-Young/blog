---
title: 金属常见晶体结构的间隙原子位点
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: 金属常见晶体结构的间隙原子位点
description: 金属常见晶体结构的间隙原子位点
tags:
  - 材料科学
  - 点缺陷
categories:
  - 科研工具
date: 2024-11-05 15:56:34
abbrlink: 535416
password:
---

# 金属常见晶体结构的间隙原子位点

**注：以下 3 张示意图均来自教材书籍：余永宁《金属学原理》**

---

## BCC 结构

- BCC 结构间隙位置示意图（扁八面体间隙、非正四面体间隙）

![BCC-intestitial-sites-1.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307152048455.png)

- latgen 中关于 BCC 间隙原子位置的选项（6 个八面体间隙 + 12 个四面体间隙）

```bash
# 八面体间隙（扁八面体）
There are 6 octahedral interstitial sites within lattice BCC(001):
1) [0.5 0 0]
2) [0 0.5 0]
3) [0.5 0.5 0]
4) [0 0 0.5]
5) [0 0.5 0.5]
6) [0.5 0 0.5]

# 四面体间隙
There are 12 tetrahedral interstitial sites within lattice BCC(001):
7) [0.25 0.5 0]
8) [0.75 0.5 0]
9) [0.5 0.25 0]
10) [0.5 0.75 0]
11) [0.5 0 0.25]
12) [0 0.5 0.25]
13) [0 0.25 0.5]
14) [0 0.75 0.5]
15) [0.25 0 0.5]
16) [0.75 0 0.5]
17) [0 0.5 0.75]
18) [0.5 0 0.75]
```



---

## FCC 结构

- FCC 结构间隙位置示意图

![FCC-intestitial-sites-1.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307152048016.png)

- latgen 中关于 FCC 间隙原子位置的选项（4 个八面体间隙 + 8 个四面体间隙）

```bash
# 八面体间隙（晶胞各个棱的中点）
There are 4 octahedral interstitial sites within lattice FCC(001):
1) [0.5 0.5 0.5]
2) [0.5 0 0]
3) [0 0.5 0]
4) [0 0 0.5]

# 四面体间隙（体对角线离顶点的 1/4 处）
There are 8 tetrahedral interstitial sites within lattice FCC(001):
5) [0.25 0.25 0.25]
6) [0.25 0.25 0.75]
7) [0.25 0.75 0.25]
8) [0.75 0.25 0.25]
9) [0.75 0.75 0.75]
10) [0.75 0.75 0.25]
11) [0.75 0.25 0.75]
12) [0.25 0.75 0.75]
```



---

## HCP 结构

- 间隙原子位置基于如下的 HCP 结构基矢及单胞原子位置：

```bash
# latgen 中的 HCP 构建选项 3: U along x, 120 degree 得到如上坐标形式
# atomsk 默认生成的中心原子坐标为 0.333 0.667 0.5
1.0
   3.2340000000000000    0.0000000000000000    0.0000000000000000
  -1.6170000000000000    2.8007261558388792    0.0000000000000000
   0.0000000000000000    0.0000000000000000    5.1680000000000152
Zr
2
direct
   0.0000000000000000    0.0000000000000000    0.0000000000000000 Zr
   0.6666666666666700    0.3333333333333300    0.5000000000000000 Zr
```

- HCP 结构间隙位置示意图
![HCP-intestitial-sites-1.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307152049962.png)

- latgen 中关于 HCP 间隙原子位置的选项（2 个八面体间隙 + 4 个四面体间隙）

```bash
There are 2 octahedral interstitial sites within lattice HCP(001):
  1) [0.333333 0.666667 0.25]
  2) [0.333333 0.666667 0.75]

There are 4 tetrahedral interstitial sites within lattice HCP(001):
  3) [0.666667 0.333333 0.125]
  4) [0 0 0.375]
  5) [0 0 0.625]
  6) [0.666667 0.333333 0.875]
```



---

## 超胞中的第一近邻间隙位点

- 注意事项：
    - 以 2\*2\*2 超胞为例
    - 原子位点序号为 pymatgen 中的生成的含所有四面体或八面体间隙超胞的构型原子位点序号
    - 中心原子 (0.5, 0.5, 0.5) 的序号为 7

---

- Python 脚本

```Python
"""获取 HCP 间隙掺杂体系四面体间隙的第一近邻原子位点"""

import numpy as np
from pymatgen.core.structure import Structure

# 含所有四面体或八面体间隙的单胞构型文件
structure_fn = "XXX"
structure = Structure.from_file(structure_fn)
supercell = structure * 2

print(supercell[7].frac_coords)
distance_list = []
for i in range(len(supercell)):
    # 序号为 7 的原子位于超胞中心位点 (0.5, 0.5, 0.5)
    if i != 7:
        distance = supercell.get_distance(7, i)
        distance_list.append(distance)


array = np.array(distance_list).round(3)

min_indices = np.where(array == np.min(array))[0]

for min_index in min_indices:
    index = min_index + 1
    print(
        index,
        supercell[index].frac_coords,
        supercell.get_distance(7, index).round(3),
    )
```

- BCC 中心原子的第一近邻四面体间隙位点及其距离

```bash
# 第一近邻有 8 个，组成八边形
21 [0.625 0.25  0.5  ] 1.818
23 [0.625 0.75  0.5  ] 1.818
25 [0.375 0.25  0.5  ] 1.818
27 [0.375 0.75  0.5  ] 1.818
35 [0.25  0.625 0.5  ] 1.818
39 [0.75  0.625 0.5  ] 1.818
41 [0.25  0.375 0.5  ] 1.818
45 [0.75  0.375 0.5  ] 1.818
```

- BCC 中心原子的第一近邻八面体间隙位点及其距离

```bash
# 第一近邻有 6 个，组成双四棱锥
19 [0.25 0.5  0.5 ] 1.626
23 [0.75 0.5  0.5 ] 1.626
29 [0.5  0.25 0.5 ] 1.626
31 [0.5  0.75 0.5 ] 1.626
46 [0.5  0.5  0.25] 1.626
47 [0.5  0.5  0.75] 1.626
```

- HCP POSCAR 格式如下（x y 坐标调换时，下面的间隙坐标也需进行相应的调换）

```bash
# HCP Ti relaxed
   1.00000000000000
     2.9370745813452541    0.0000000000000000    0.0000000000000000
    -1.4685372906726271    2.5435812012202854    0.0000000000000000
     0.0000000000000000    0.0000000000000000    4.6457462370147713
   Ti
     2
Direct
  0.0000000000000000  0.0000000000000000  0.0000000000000000
  0.3333333300000021  0.6666666699999979  0.5000000000000000
```

- HCP 中心原子的第一近邻四面体间隙位点及其距离

```bash
39 [0.5    0.5    0.6875] 1.742
46 [0.5    0.5    0.3125] 1.742
```

- HCP 中心原子的第一近邻八面体间隙位点及其距离

```bash
17 [0.33333333 0.16666666 0.625     ] 2.055
19 [0.33333333 0.66666666 0.625     ] 2.055
23 [0.83333333 0.66666666 0.625     ] 2.055
24 [0.33333333 0.16666666 0.375     ] 2.055
26 [0.33333333 0.66666666 0.375     ] 2.055
30 [0.83333333 0.66666666 0.375     ] 2.055
```



---

## 其他

- 部分结构与 FCC 间隙的关系：[8.2: Close-packing and Interstitial Sites - Chemistry LibreTexts](https://chem.libretexts.org/Bookshelves/Inorganic_Chemistry/Book%3A_Introduction_to_Inorganic_Chemistry_(Wikibook)/08%3A_Ionic_and_Covalent_Solids_-_Structures/8.02%3A_Close-packing_and_Interstitial_Sites)
    - 萤石 CaF2：可看作 F 元素占据了 FCC 全部的四面体间隙位点
    - 岩盐结构 NaCl：可看作 Na/Cl 元素占据了 FCC 全部的八面体间隙位点
    - Li3B: 可看作 Li 元素占据了 FCC 全部的四面体和八面体间隙位点
    - 闪锌矿 ZnS：可看作 S 元素占据了一半的四面体间隙位点（2 个上 +2 个下）

![Structures-FCC-interstitial-sites](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images/202411091538417.png)

- 纤锌矿型（wurtzite）是一种六方晶系，又称六方硫化锌，以纤锌矿为例，S 原子作六方密堆积，Zn 原子填充在半数的四面体空隙中（z 方向坐标值 u 是个变量，不同体系可能会有不同；ASE 可直接构建）

- 三种结构的间隙位点示意图参考：[Interstitial Sites: Size, Types, Applications, And Calculations – Materials Science & Engineering](https://msestudent.com/interstitial-sites-size-types-applications-and-calculations/)

![BCC-intestitial-sites-2.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407052014588.png)

![FCC-intestitial-sites-2.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407052014611.png)

![HCP-intestitial-sites-2.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202407052014348.png)

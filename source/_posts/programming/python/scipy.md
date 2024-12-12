---
title: SciPy 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: SciPy 使用
description: SciPy 使用
tags:
  - SciPy
categories:
  - 编程
  - Python
date: 2024-09-17 16:50:00
abbrlink: 501607
password:
---

# SciPy 使用

## 介绍

参考资料

- [python微分求解 - 我是谁](https://yuhldr.github.io/posts/13877.html)



---

## 使用

```python
# 样条插值
from scipy.interpolate import interp1d

# 三次样条插值：在每个数据点上都是光滑的，且在二阶导数上连续
# cubic 三次；quadratic 二次
interp1d(x, y, kind="cubic")


# 物理常数
from scipy.constants import physical_constants

physical_constants          # 查看所有的物理常数

# 光速
value, unit, uncertainty = physical_constants["XXX"]
"speed of light in vacuum"  # 光速
"Planck constant":          # 普朗克常数
"electron mass"             # 电子质量
"proton mass"               # 质子质量
"Avogadro constant"         # 阿伏伽德罗常数


# 平滑 smoothing 处理
from scipy.ndimage import gaussian_filter1d

rdf=gaussian_filter1d(rdf, sigma=...)
sigma       # 高斯滤波的展宽；值不能太大，否则会偏离原始数据


# 特殊函数
from scipy import special


# 最小二乘拟合
from scipy.optimize import leastsq

leastsq(func, x0, args=())
# 参数
func            # 残差函数，理论值和观测值的差；调用形式应为 func(p, *args)， p 是模型参数的数组
x0              # 参数的初始猜测值，数组形式
args            # 传递给 func 的额外参数

# 返回值 (x, ier)
x               # 拟合参数的最佳值

ier             # 终止标志，1-5
1               # 函数的两次迭代之间的相对误差小于 ftol
2               # 两次迭代之间的相对参数变化小于 xtol
3               # 以上两个条件同时满足
4               # 方向余弦的平方和的值（即参数向量的变化量）小于 gtol
5               # 函数调用次数超过 maxfev 设定的最大值
```

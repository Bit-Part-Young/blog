---
title: gnuplot 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: gnuplot 使用
description: gnuplot 使用
tags:
categories:
date: 2024-11-13 19:54:28
abbrlink: 195428
password:
---

# gnuplot 使用

- gnuplot 读取数据文件时，会自动忽略中含 `#` 的行；有 print 命令

- 常用命令

```bash
gnuplot     # 进入交互式绘图
gnuplot script.gnu  # 脚本运行；脚本后缀名不限

u           # using 简写；指定如何从输入数据中读取和使用数据列
w           # with 简写；指定绘图样式

# 绘图样式
p           # points 简写；点绘图
l           # lines 简写；线绘图
lp          # linespoints 简写；点线绘图
pt N        # 点的样式；N 为编号
lt N        # 线的样式
lw value    # linewidth 简写；线的宽度；value 为数值
lc          # linecolor 简写；指定颜色；rgb "red"

# set 命令；可控制图表的布局、样式、标签、轴属性、刻度、图例
title       # 标题
xrange      # x 轴范围
yrange      # y 轴范围
xlabel      # x 轴标签
ylabel      # x 轴标签
output      # 输出文件
grid        # 网格
terminal    # 输出格式
xtics       # x 轴刻度
ytics       # x 轴刻度
key         # 图例
style       # 绘图样式
logscale    # 对数刻度坐标轴
multiplot   # 多/子图；按顺序写绘制子图的命令

# 绘图示例
plot 'data.txt' u 1:2 w lp

# 正弦函数
set xrange [-10:10]
plot sin(x) w lp pt 7
```

- 图例设置

```bash
set key ...

on        # 开启图例
off       # 开启图例
box       # 显示边框
nobox     # 不显示边框

top, bottom, left, right  # 图例放置位置；可组合 top left
at x,y                    # 图例放置在具体坐标
inside, outside           # 绘图区域内/外部
```

- 输出格式

```bash
set terminal ...

png pdf jpeg              # 图片格式
size 800 800              # 图片尺寸
enhanced font 'Arial,12'  # 字体及大小
```

- [表面态颜色-gnuplot颜色设置](https://mp.weixin.qq.com/s/mIv6nqGjsPJCLP5so7qQ8w)

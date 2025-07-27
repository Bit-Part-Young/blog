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

## 介绍

- [gnuplot 使用](https://mp.weixin.qq.com/s/eGcxXSEWm3f06qg3_qpYHw)

- gnuplot 读取数据文件时，**会自动忽略中注释、非数值行**；有 print 命令

- gnuplot 读取数据文件是，默认分隔符为空位或制表符，`set datafile separator ","` 使分隔符为逗号

- gnuplot 字体设置不是很灵活

- [gnuplot 科技绘图的调色板 - Jerkwin](https://jerkwin.github.io/2018/08/20/%E7%A7%91%E6%8A%80%E7%BB%98%E5%9B%BE%E7%9A%84%E8%B0%83%E8%89%B2%E6%9D%BF/)（有很多不错的预设颜色，推荐）

- gnuplot 中线和点的编号及对应样式：[Gnuplot line types - stack overflow](https://stackoverflow.com/questions/19412382/gnuplot-line-types)

- [表面态颜色-gnuplot颜色设置](https://mp.weixin.qq.com/s/mIv6nqGjsPJCLP5so7qQ8w)

- [gnuplot 绘图 demo](http://www.gnuplot.info/demo/index.html)


---

## 使用

### 运行

```bash
gnuplot                   # 交互式绘图
gnuplot script.gnu        # 脚本运行；脚本后缀名不限
```


---

### 命令简写

- gnuplot 中的命令支持简写

- [gnuplot的关键词与缩写 - Jerkwin](https://jerkwin.github.io/2025/04/09/gnuplot%E7%9A%84%E5%85%B3%E9%94%AE%E8%AF%8D%E4%B8%8E%E7%BC%A9%E5%86%99/)

```bash
ter                       # terminal
out                       # output

u                         # using
w                         # with

p                         # points
l                         # lines
lp                        # linespoints
ps                        # pointsize
lw                        # linewidth
lc                        # linecolor

xr                        # xrange

bor                       # border

rep                       # replot
```


---

### plot 命令

```bash
# 示例
plot "data.txt" u 1:2 w lp

# 参数
u                         # 指定数据列；如 u 1:2 含义为第 1 列为 x，第 2 列为 y
w                         # 指定绘图样式
every ::0::10             # 使用前 10 行数据

# 绘图样式
p                         # 点绘图
l                         # 线绘图
lp                        # 点线绘图
impulses

pt N                      # 点的样式；N 为编号
lt N                      # 线的样式；N 为编号
ps value                  # 点的大小
lw value                  # 线的宽度；value 为数值
lc                        # 指定颜色；rgb "red"

xerr                      # x 误差棒
yerr                      # y 误差棒
xyerrorbars               # xy 误差棒 
filledcurve
```

- plot 命令示例

```bash
# 正弦函数；不依赖外部数据文件
set xrange [-10:10]
plot sin(x) w lp pt 7


# 使用部分行数据绘制多个曲线
plot "thermo.out" every ::0::199 u 1:3 w p pt 7 ps 0.2 lc rgb "red" title "heat", \
     "thermo.out" every ::200::300 u 1:3 w p pt 7 ps 0.2 lc rgb "blue" title "cooling" \


# 使用偶数行数据进行绘制
plot "<(awk 'NR % 2 == 1' data.txt)" ...


# 使用循环绘制多个曲线
legend_titles = "x y z"
plot for [i=2:4] "mvac.out" u 1:i with l lw 7-i title word(legend_titles, i-1)


# 自定义 x 数据
set xrange [1:5067]
plot 'data.txt' u 0:4 w l


# 使用变量，且对列数据进行操作
l0 = 132.622
plot 'thermo.out' u (($10 - l0)/l0):(-($4)) w lp
```


---

### set 命令

- 可控制图表的布局、样式、标签、轴属性、刻度、图例

```bash
terminal                  # 输出格式
output                    # 输出文件名
title                     # 标题
xrange                    # x 轴范围
yrange                    # y 轴范围
xlabel                    # x 轴标签
ylabel                    # x 轴标签
xtics                     # x 轴刻度
ytics                     # x 轴刻度
mxtics n                  # 在主刻度之间增加 n 个次刻度
mytics n                  # 同上
key                       # 图例
log x                     # x 轴使用 log 坐标
style                     # 绘图样式
logscale                  # 对数刻度坐标轴
multiplot                 # 多/子图；按顺序写绘制子图的命令
grid                      # 网格


# 其他
set border lw 2.0         # 设置坐标轴线宽


# 添加垂直线
# 指定 y 的范围
set arrow 1 nohead from 0.1,0 to 0.1,1
# 自适应当前绘图的 y 轴范围
# dashtype 1 实线（默认）；2：短虚线；3 点线；4 长短虚线
set arrow 1 nohead from 0.5, graph 0 to 0.5, graph 1 dashtype 4 lw 3


# 设置 x 轴刻度标签
set xtics ("{/Symbol G}" 0, "X" 0.1)
```


---

### 图例

```bash
set key ...

on                        # 开启图例
off                       # 关闭图例；或者 unset key
box                       # 显示边框
nobox                     # 不显示边框

top/bottom/left/right     # 图例放置位置；可组合 top left
at x,y                    # 图例放置在具体坐标
inside, outside           # 绘图区域内/外部
font ...                  # 图例字符大小

set key samplen 3         # 设置图例 label 长度
```


---

### 输出格式

```bash
set terminal ...          # gnuplot 进入交互，输入 set terminal，查看支持的图片格式

png pdf jpeg              # 图片格式
size 800 800              # 图片尺寸；没有 dpi 设置参数
enhanced font 'Arial,12'  # 字体及大小
```


---

### 较美观的 gnuplot 设置

```bash
# config.gnu

set terminal pngcairo size 1000,800 enhanced font "Times New Roman,25"

# 设置调色板
setpal="if(pal eq 'cls'){set colorsequence classic};if(pal ne 'def' && pal ne 'cls'){do for[i=1:words(value(pal))]{set style line i lw 4 lc rgb word(value(pal),i)}}"

fav="#1F77B4 #FF7400 #00A13B #D62728 #984EA3 #A65628 #EE0F84 #7F7F7F #BCBD22 #17BECF"
pal='fav'; @setpal

set border lw 5.0

set xtics nomirror
set ytics nomirror

# unset key

# 设置全局线宽（还可设置 点的大小）
set for [i=1:7] style line i lw 5
# 6.0 版本该命令弃用（不报错，会有 warning）
set style increment user


# 使用示例
# set loadpath "~/scripts/cms-scripts/plots"
# load "config.gnu"

# set output "test.png"

# plot for [i=1:7] sin(x)+i*0.1 w l
```


---

### fit 参数拟合

```bash
# EOS 拟合
set fit errorvariables

EOS(x) = B0*x/Bp * ( (V0/x)**(Bp)/(Bp-1.) + 1.) - B0*V0/(Bp-1.) + E0

B0 = 1.; Bp = 4.; E0 = $E0; V0 = $V0
fit EOS(x) "${evf}" u (\$1):(\$2) via B0, Bp, V0, E0
```

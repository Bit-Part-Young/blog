---
title: Matplotlib 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Matplotlib 使用
description: Matplotlib 使用
tags:
  - Matplotlib
categories:
  - 编程
  - Python
date: 2023-10-25 10:30:00
abbrlink: 404245
password:
---

# Matplotlib 使用

## 介绍

WIP...

---

### 参考资料

- [官方 cheatsheet](https://matplotlib.org/cheatsheets/)
- Matplotlib Tutorial：[GitHub - rougier/matplotlib-tutorial: Matplotlib tutorial for beginner](https://github.com/rougier/matplotlib-tutorial)
- 精美科研绘图示例：[Veusz 2D Examples](https://veusz.github.io/examples/)
- 在 Matplolib 中使用 LaTeX：[Use latex with matplotlib on HPCs where you can't sudo! · GitHub](https://gist.github.com/chiang-yuan/62fbcaae06bf77f793a8f9b5aed1ba70)


matplotlib mplstyle 写法

```python
from matplotlib.axes import Axes

ax: Axes

fig = plt.figure()
ax = fig.subplots()

# 查看下两者区别
ax = plt.subplot()

fig, ax = plt.subplots()

ax = fig.add_subplot()  # 返回 Axes object

# 填充
ax.fill_between()
```


matplotlib 图中的所有元素

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404091019401.png)



```python
# 新字体使用时，rebuild font cache list，防止没有检测到
import matplotlib.font_manager

matplotlib.font_manager._rebuild()
```



```python
# 使用 TEX 引擎
plt.rcParams["text.usetex"] = True
```

```python
plt.rcParams["mathtext.fontset"]
```

数学字体（默认为 `dejavusans`）：[Writing mathematical expressions — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/users/explain/text/mathtext.html)

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404091028106.png)


---

>[matplotlib.style — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/api/style_api.html)

>[Style sheets reference — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

```python
plt.style.available

plt.style.use()
```



---

## 使用

### 基本

- 函数式绘图（隐式）：调用 `matplotlib.pyplot` 中的函数来创建图形，如 `plot()` 等；绘制子图较麻烦

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label="$y=\sin(x)$")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.show()

# plt.savefig("sin.png")
```

---

- 对象式绘图（显式）：通过显式创建 Figure 和 Axes 对象来创建绘图区域，然后在其上调用相应的方法绘制各种图形元素；绘制子图方便

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y, label="$y=\sin(x)$")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()

# fig.savefig("sin.png")
```

---

- 常用绘图形式

```python
# 点线图
ax.plot(x, y, ...)


# 散点图
ax.scatter(x, y, s, c, cmap, ...)

s               # marker size；float 或 array-like
c               # marker colors；array-like 或 color list；该参数可结合 colorbar 使用
cmap            # colormap


# 直方图
ax.hist(x, bins, histtype, edgecolor, ...)

bins            # 将 x 范围等分成 bins 份
edgecolor       # 边缘颜色


# 水平线
ax.axhline()  


# 二维直方图
ax.hist2d()
```


---

### 子图绘制

- 方式 1

```python
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 6))
```

- 方式 2

```python
fig, axs = plt.subplots(nrows=1, ncols=2)

# 调整子图之间的间距
fig.subplots_adjust(hspace=0.0, wspace=0.0)

# axs = axs.flatten()
# axs 数组扁平化，利于 for 循环
for i, ax in enumerate(axs.flat):
	...

    # 第二列的 y 轴坐标刻度不显示
     if i % 2 == 1:
         ax.yaxis.set_tick_params(labelleft=False)

# 设置整个子图的 x y 轴标签；y x 参数调整标签与坐标轴的距离
fig.supxlabel("x", y=0.05)
fig.supylabel("y", x=0.01)

# 添加整个子图的图例 在图外面
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, bbox_to_anchor=(1.1, 0.1))
```

>[matplotlib.figure — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.supxlabel)


---

### 双 Y 轴

```python
ax1.plot(...)

ax2 = ax.twinx()
ax2.plot(...)

# 解决双 Y 轴图列重叠问题
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2)
```

---

- 误差棒图

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 2, 4, 2]
yerr = [[0.5, 1, 0.5, 1, 0.5], [1, 2, 1, 2, 1]]  # 下、上误差；需为正值
yerr = [0.5, 1, 0.5, 1, 0.5]  # 上下误差一样

fig, ax = plt.subplots()

ax.errorbar(x, y, yerr=yerr, fmt="o", linewidth=1, capsize=6)

ax.set(xlabel="X", ylabel="Y", title="Error Bar Example")

plt.show()
```

---

### colorbar 绘制

- [GitHub - 1313e/CMasher: Scientific colormaps for making accessible, informative and 'cmashing' plots](https://github.com/1313e/CMasher)

- colormap：从蓝到红渐变：`coolwarm`、`jet`、`bwr`

```python
# 将 colorbar 放在图片右侧
scatter_ax = ax.scatter(x, y, c=colors, cmap="bwr")
cbar = fig.colorbar(
    scatter_ax,
    ax=ax,  # 第二个参数名为 ax
)
cbar.set_label("colorbar label")


# 将 colorbar 水平放置并嵌在图中右下角
fig, ax = plt.subplots(figsize=(8, 8))
scatter_ax = ax.scatter(x, y, c=colors, cmap="bwr")
# colorbar 位置；[x, y, width, height] 比例
cbar_ax = ax.inset_axes([0.3, 0.05, 0.5, 0.05])
# colorbar 水平放置
fig.colorbar(
    scatter_ax,
    cax=cbar_ax,  # 第二个参数名为 cax
    orientation="horizontal",
)
```

---

### 3d 绘图

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10, 8))

ax.scatter(x, y, z, c="b", marker="o", label="3d plot")

ax.set(xlabel="X", ylabel="Y", zlabel="Z")
ax.legend()

plt.show()
```

---

- 较美观的点线图：[sci作图 - 计算材料学](https://ywwang0.github.io/2020/10/07/sci%E4%BD%9C%E5%9B%BE/)

```python
ax.plot(
    x,
    y,
    "^",
    ls="solid",
    lw=1,
    markeredgecolor="black",
    markersize=8,
    label="...",
)
```

---

### 设置

- `ax.set()` ：设置轴属性，可接受多种参数；[matplotlib.axes.Axes.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html)

```python
xlim/ylim                    # x、y 轴范围
xlabel/ylabel                # x、y 轴标签
title                        # 图标题
xticks/yticks                # x、y 轴刻度
xticklabels/yticklabels      # x、y 轴刻度标签
xscale/yscale                # x、y 轴比例
facecolor                    # 轴背景颜色

ax.set_xlabel("x")
ax.set_ylabel("y")
# or
ax.set(xlabel="x", ylabel="y")
```

---

#### 图例

`ax.legend()`

```python
# label 不在图例上显示
ax.plot(x, y, label="_nolegend_")

# 图例
ax.legend(ncols, loc, bbox_to_anchor, ...)

ncols               # 图例排布列数
loc                 # 图例位置
frameonalpha        # 图例边框背景透明度
bbox_to_anchor      # 2-tuple floats，(x, y)；x≥1.0 时，图例在外面
```

有将两个图例 label 放在一行的示例：[Legend Demo — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

---

#### 字体

- Times New Roman 字体问题：Linux 默认没有该字体，可将该字体拷贝到 `~/.fonts` 或 `~/.local/share/fonts`

- 临时使用中文字体：[Matplotlib学习笔记.md](https://github.com/LiuQixuan/PythonLearningNote/blob/master/Matplotlib%20%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md)

```python
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

zh_font = FontProperties(fname="./SimHei.ttf")

plt.xlabel("x 轴", fontproperties = zh_font)
plt.ylabel("y 轴", fontproperties = zh_font)

plt.legend(props={"family": "SimHei"})
```


---

- matplotlib joint 绘制（上、右两侧分别是 x, y 的直方图）
	- [scientific-visualization-book/code/layout/standard-layout-2.py at master · rougier/scientific-visualization-book · GitHub](https://github.com/rougier/scientific-visualization-book/blob/master/code/layout/standard-layout-2.py)
	- [seaborn.JointGrid — seaborn 0.13.2 documentation](https://seaborn.pydata.org/generated/seaborn.JointGrid.html)
	- [seaborn.jointplot — seaborn 0.13.2 documentation](https://seaborn.pydata.org/generated/seaborn.jointplot.html)
	- [Scatter plot with histograms — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html)


- 热图 heatmap / 关联图绘制：`plt.matshow()`，`seaborn.heatmap()`
- 饼状关联图绘制（Origin 可以绘制）：[biokit/notebooks/viz/corrplot.ipynb at master · biokit/biokit · GitHub](https://github.com/biokit/biokit/blob/master/notebooks/viz/corrplot.ipynb)
- 手绘风格（无必要）：需安装 xkcd-script font（但还是会提示找不到相关字体）；[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html#sphx-glr-gallery-showcase-xkcd-py)


---

- 其他

```python
# x 轴 label 变成字符串
ax.set_xticks()

# 设置 x 轴的次刻度 minor tick
ax.set_xticks(range(0, 10, 1), minor=True)

# f-string 对于在图中添加需要 LaTeX 格式的 text 效果不是很好，改用 str.replace()
ax.text(3.0, 1.5, r"RMSE=cha$\,·\,10^{-5}$ Pa$\,·\,$s".replace("cha", str(score_rmse)))


# 将 Y 轴的刻度及 label 放到右边
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")

# 设置 x/y 轴主、次刻度间隔
from matplotlib.ticker import MultipleLocator

ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))

# 让 figure 呈正方形
ax.set_aspect("equal", adjustable="box")

# 正常显示负号
plt.rcParams["axes.unicode_minus"] = False

ax.texts  # 获取文本
ax.texts[0].set_fontsize()
```

---

#### 配置文件路径

- [matplotlibrc](https://matplotlib.org/stable/users/explain/customizing.html#the-matplotlibrc-file)：matplotlib 库的配置文件（`matplotlib/mpl-data/matplotlibrc`）
- 字体路径：`matplotlib/mpl-data/mpl-data/fonts/ttf`
- 缓存路径：`~/.cache/matplotlib`

```python
import matplotlib

# matplotlib/mpl-data/matplotlibrc
matplotlib.matplotlib_fname()

# matplotlib/mpl-data/
# 字体所在路径：mpl-data/fonts/ttf
matplotlib.get_data_path()

# matplotlib 缓存路径 ~/.cache/matplotlib
matplotlib.get_cachedir()
```

---

#### 配色

[scripts/scripts/python/color.py at master · yh-phys/scripts · GitHub](https://github.com/yh-phys/scripts/blob/master/scripts/python/color.py)

[审稿人也会爱的配色\~科研配色收藏第9期 - 知乎](https://zhuanlan.zhihu.com/p/698897001)

```python
"#4F4FFE"
"#CE3D32"
```

```python
import matplotlib.pyplot as plt

plt.rcParams["axes.prop_cycle"].by_key()["color"]

# 默认颜色循环
prop_cycle_list = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202404091017405.png)



---

#### rcParams

matplotlib [rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams)

```python
# 方式 1
import matplotlib.pyplot as plt

plt.rcParams.keys()

# 方式 2
import matplotlib

matplotlib.rc_params()
```


```python
# rcParams 所有参数
KeysView(RcParams({'_internal.classic_mode': False,
          'agg.path.chunksize': 0,
          'animation.bitrate': -1,
          'animation.codec': 'h264',
          'animation.convert_args': ['-layers', 'OptimizePlus'],
          'animation.convert_path': 'convert',
          'animation.embed_limit': 20.0,
          'animation.ffmpeg_args': [],
          'animation.ffmpeg_path': 'ffmpeg',
          'animation.frame_format': 'png',
          'animation.html': 'none',
          'animation.writer': 'ffmpeg',
          'axes.autolimit_mode': 'data',
          'axes.axisbelow': 'line',
          'axes.edgecolor': 'black',
          'axes.facecolor': 'white',
          'axes.formatter.limits': [-5, 6],
          'axes.formatter.min_exponent': 0,
          'axes.formatter.offset_threshold': 4,
          'axes.formatter.use_locale': False,
          'axes.formatter.use_mathtext': False,
          'axes.formatter.useoffset': True,
          'axes.grid': False,
          'axes.grid.axis': 'both',
          'axes.grid.which': 'major',
          'axes.labelcolor': 'black',
          'axes.labelpad': 4.0,
          'axes.labelsize': 'medium',
          'axes.labelweight': 'normal',
          'axes.linewidth': 0.8,
          'axes.prop_cycle': cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']),
          'axes.spines.bottom': True,
          'axes.spines.left': True,
          'axes.spines.right': True,
          'axes.spines.top': True,
          'axes.titlecolor': 'auto',
          'axes.titlelocation': 'center',
          'axes.titlepad': 6.0,
          'axes.titlesize': 'large',
          'axes.titleweight': 'normal',
          'axes.titley': None,
          'axes.unicode_minus': True,
          'axes.xmargin': 0.05,
          'axes.ymargin': 0.05,
          'axes.zmargin': 0.05,
          'axes3d.grid': True,
          'axes3d.xaxis.panecolor': (0.95, 0.95, 0.95, 0.5),
          'axes3d.yaxis.panecolor': (0.9, 0.9, 0.9, 0.5),
          'axes3d.zaxis.panecolor': (0.925, 0.925, 0.925, 0.5),
          'backend': 'agg',
          'backend_fallback': True,
          'boxplot.bootstrap': None,
          'boxplot.boxprops.color': 'black',
          'boxplot.boxprops.linestyle': '-',
          'boxplot.boxprops.linewidth': 1.0,
          'boxplot.capprops.color': 'black',
          'boxplot.capprops.linestyle': '-',
          'boxplot.capprops.linewidth': 1.0,
          'boxplot.flierprops.color': 'black',
          'boxplot.flierprops.linestyle': 'none',
          'boxplot.flierprops.linewidth': 1.0,
          'boxplot.flierprops.marker': 'o',
          'boxplot.flierprops.markeredgecolor': 'black',
          'boxplot.flierprops.markeredgewidth': 1.0,
          'boxplot.flierprops.markerfacecolor': 'none',
          'boxplot.flierprops.markersize': 6.0,
          'boxplot.meanline': False,
          'boxplot.meanprops.color': 'C2',
          'boxplot.meanprops.linestyle': '--',
          'boxplot.meanprops.linewidth': 1.0,
          'boxplot.meanprops.marker': '^',
          'boxplot.meanprops.markeredgecolor': 'C2',
          'boxplot.meanprops.markerfacecolor': 'C2',
          'boxplot.meanprops.markersize': 6.0,
          'boxplot.medianprops.color': 'C1',
          'boxplot.medianprops.linestyle': '-',
          'boxplot.medianprops.linewidth': 1.0,
          'boxplot.notch': False,
          'boxplot.patchartist': False,
          'boxplot.showbox': True,
          'boxplot.showcaps': True,
          'boxplot.showfliers': True,
          'boxplot.showmeans': False,
          'boxplot.vertical': True,
          'boxplot.whiskerprops.color': 'black',
          'boxplot.whiskerprops.linestyle': '-',
          'boxplot.whiskerprops.linewidth': 1.0,
          'boxplot.whiskers': 1.5,
          'contour.algorithm': 'mpl2014',
          'contour.corner_mask': True,
          'contour.linewidth': None,
          'contour.negative_linestyle': 'dashed',
          'date.autoformatter.day': '%Y-%m-%d',
          'date.autoformatter.hour': '%m-%d %H',
          'date.autoformatter.microsecond': '%M:%S.%f',
          'date.autoformatter.minute': '%d %H:%M',
          'date.autoformatter.month': '%Y-%m',
          'date.autoformatter.second': '%H:%M:%S',
          'date.autoformatter.year': '%Y',
          'date.converter': 'auto',
          'date.epoch': '1970-01-01T00:00:00',
          'date.interval_multiples': True,
          'docstring.hardcopy': False,
          'errorbar.capsize': 0.0,
          'figure.autolayout': False,
          'figure.constrained_layout.h_pad': 0.04167,
          'figure.constrained_layout.hspace': 0.02,
          'figure.constrained_layout.use': False,
          'figure.constrained_layout.w_pad': 0.04167,
          'figure.constrained_layout.wspace': 0.02,
          'figure.dpi': 100.0,
          'figure.edgecolor': 'white',
          'figure.facecolor': 'white',
          'figure.figsize': [6.4, 4.8],
          'figure.frameon': True,
          'figure.hooks': [],
          'figure.labelsize': 'large',
          'figure.labelweight': 'normal',
          'figure.max_open_warning': 20,
          'figure.raise_window': True,
          'figure.subplot.bottom': 0.11,
          'figure.subplot.hspace': 0.2,
          'figure.subplot.left': 0.125,
          'figure.subplot.right': 0.9,
          'figure.subplot.top': 0.88,
          'figure.subplot.wspace': 0.2,
          'figure.titlesize': 'large',
          'figure.titleweight': 'normal',
          'font.cursive': ['Apple Chancery',
                           'Textile',
                           'Zapf Chancery',
                           'Sand',
                           'Script MT',
                           'Felipa',
                           'Comic Neue',
                           'Comic Sans MS',
                           'cursive'],
          'font.family': ['sans-serif'],
          'font.fantasy': ['Chicago',
                           'Charcoal',
                           'Impact',
                           'Western',
                           'Humor Sans',
                           'xkcd',
                           'fantasy'],
          'font.monospace': ['DejaVu Sans Mono',
                             'Bitstream Vera Sans Mono',
                             'Computer Modern Typewriter',
                             'Andale Mono',
                             'Nimbus Mono L',
                             'Courier New',
                             'Courier',
                             'Fixed',
                             'Terminal',
                             'monospace'],
          'font.sans-serif': ['DejaVu Sans',
                              'Bitstream Vera Sans',
                              'Computer Modern Sans Serif',
                              'Lucida Grande',
                              'Verdana',
                              'Geneva',
                              'Lucid',
                              'Arial',
                              'Helvetica',
                              'Avant Garde',
                              'sans-serif'],
          'font.serif': ['DejaVu Serif',
                         'Bitstream Vera Serif',
                         'Computer Modern Roman',
                         'New Century Schoolbook',
                         'Century Schoolbook L',
                         'Utopia',
                         'ITC Bookman',
                         'Bookman',
                         'Nimbus Roman No9 L',
                         'Times New Roman',
                         'Times',
                         'Palatino',
                         'Charter',
                         'serif'],
          'font.size': 10.0,
          'font.stretch': 'normal',
          'font.style': 'normal',
          'font.variant': 'normal',
          'font.weight': 'normal',
          'grid.alpha': 1.0,
          'grid.color': '#b0b0b0',
          'grid.linestyle': '-',
          'grid.linewidth': 0.8,
          'hatch.color': 'black',
          'hatch.linewidth': 1.0,
          'hist.bins': 10,
          'image.aspect': 'equal',
          'image.cmap': 'viridis',
          'image.composite_image': True,
          'image.interpolation': 'antialiased',
          'image.lut': 256,
          'image.origin': 'upper',
          'image.resample': True,
          'interactive': False,
          'keymap.back': ['left', 'c', 'backspace', 'MouseButton.BACK'],
          'keymap.copy': ['ctrl+c', 'cmd+c'],
          'keymap.forward': ['right', 'v', 'MouseButton.FORWARD'],
          'keymap.fullscreen': ['f', 'ctrl+f'],
          'keymap.grid': ['g'],
          'keymap.grid_minor': ['G'],
          'keymap.help': ['f1'],
          'keymap.home': ['h', 'r', 'home'],
          'keymap.pan': ['p'],
          'keymap.quit': ['ctrl+w', 'cmd+w', 'q'],
          'keymap.quit_all': [],
          'keymap.save': ['s', 'ctrl+s'],
          'keymap.xscale': ['k', 'L'],
          'keymap.yscale': ['l'],
          'keymap.zoom': ['o'],
          'legend.borderaxespad': 0.5,
          'legend.borderpad': 0.4,
          'legend.columnspacing': 2.0,
          'legend.edgecolor': '0.8',
          'legend.facecolor': 'inherit',
          'legend.fancybox': True,
          'legend.fontsize': 'medium',
          'legend.framealpha': 0.8,
          'legend.frameon': True,
          'legend.handleheight': 0.7,
          'legend.handlelength': 2.0,
          'legend.handletextpad': 0.8,
          'legend.labelcolor': 'None',
          'legend.labelspacing': 0.5,
          'legend.loc': 'best',
          'legend.markerscale': 1.0,
          'legend.numpoints': 1,
          'legend.scatterpoints': 1,
          'legend.shadow': False,
          'legend.title_fontsize': None,
          'lines.antialiased': True,
          'lines.color': 'C0',
          'lines.dash_capstyle': <CapStyle.butt: 'butt'>,
          'lines.dash_joinstyle': <JoinStyle.round: 'round'>,
          'lines.dashdot_pattern': [6.4, 1.6, 1.0, 1.6],
          'lines.dashed_pattern': [3.7, 1.6],
          'lines.dotted_pattern': [1.0, 1.65],
          'lines.linestyle': '-',
          'lines.linewidth': 1.5,
          'lines.marker': 'None',
          'lines.markeredgecolor': 'auto',
          'lines.markeredgewidth': 1.0,
          'lines.markerfacecolor': 'auto',
          'lines.markersize': 6.0,
          'lines.scale_dashes': True,
          'lines.solid_capstyle': <CapStyle.projecting: 'projecting'>,
          'lines.solid_joinstyle': <JoinStyle.round: 'round'>,
          'markers.fillstyle': 'full',
          'mathtext.bf': 'sans:bold',
          'mathtext.cal': 'cursive',
          'mathtext.default': 'it',
          'mathtext.fallback': 'cm',
          'mathtext.fontset': 'dejavusans',
          'mathtext.it': 'sans:italic',
          'mathtext.rm': 'sans',
          'mathtext.sf': 'sans',
          'mathtext.tt': 'monospace',
          'patch.antialiased': True,
          'patch.edgecolor': 'black',
          'patch.facecolor': 'C0',
          'patch.force_edgecolor': False,
          'patch.linewidth': 1.0,
          'path.effects': [],
          'path.simplify': True,
          'path.simplify_threshold': 0.111111111111,
          'path.sketch': None,
          'path.snap': True,
          'pcolor.shading': 'auto',
          'pcolormesh.snap': True,
          'pdf.compression': 6,
          'pdf.fonttype': 3,
          'pdf.inheritcolor': False,
          'pdf.use14corefonts': False,
          'pgf.preamble': '',
          'pgf.rcfonts': True,
          'pgf.texsystem': 'xelatex',
          'polaraxes.grid': True,
          'ps.distiller.res': 6000,
          'ps.fonttype': 3,
          'ps.papersize': 'letter',
          'ps.useafm': False,
          'ps.usedistiller': None,
          'savefig.bbox': None,
          'savefig.directory': '~',
          'savefig.dpi': 'figure',
          'savefig.edgecolor': 'auto',
          'savefig.facecolor': 'auto',
          'savefig.format': 'png',
          'savefig.orientation': 'portrait',
          'savefig.pad_inches': 0.1,
          'savefig.transparent': False,
          'scatter.edgecolors': 'face',
          'scatter.marker': 'o',
          'svg.fonttype': 'path',
          'svg.hashsalt': None,
          'svg.image_inline': True,
          'text.antialiased': True,
          'text.color': 'black',
          'text.hinting': 'force_autohint',
          'text.hinting_factor': 8,
          'text.kerning_factor': 0,
          'text.latex.preamble': '',
          'text.parse_math': True,
          'text.usetex': False,
          'timezone': 'UTC',
          'tk.window_focus': False,
          'toolbar': 'toolbar2',
          'webagg.address': '127.0.0.1',
          'webagg.open_in_browser': True,
          'webagg.port': 8988,
          'webagg.port_retries': 50,
          'xaxis.labellocation': 'center',
          'xtick.alignment': 'center',
          'xtick.bottom': True,
          'xtick.color': 'black',
          'xtick.direction': 'out',
          'xtick.labelbottom': True,
          'xtick.labelcolor': 'inherit',
          'xtick.labelsize': 'medium',
          'xtick.labeltop': False,
          'xtick.major.bottom': True,
          'xtick.major.pad': 3.5,
          'xtick.major.size': 3.5,
          'xtick.major.top': True,
          'xtick.major.width': 0.8,
          'xtick.minor.bottom': True,
          'xtick.minor.pad': 3.4,
          'xtick.minor.size': 2.0,
          'xtick.minor.top': True,
          'xtick.minor.visible': False,
          'xtick.minor.width': 0.6,
          'xtick.top': False,
          'yaxis.labellocation': 'center',
          'ytick.alignment': 'center_baseline',
          'ytick.color': 'black',
          'ytick.direction': 'out',
          'ytick.labelcolor': 'inherit',
          'ytick.labelleft': True,
          'ytick.labelright': False,
          'ytick.labelsize': 'medium',
          'ytick.left': True,
          'ytick.major.left': True,
          'ytick.major.pad': 3.5,
          'ytick.major.right': True,
          'ytick.major.size': 3.5,
          'ytick.major.width': 0.8,
          'ytick.minor.left': True,
          'ytick.minor.pad': 3.4,
          'ytick.minor.right': True,
          'ytick.minor.size': 2.0,
          'ytick.minor.visible': False,
          'ytick.minor.width': 0.6,
          'ytick.right': False}))
```


---

### 其他

- hatch：填充样式

- 双 Y 轴 + brokenaxes 绘制（matplotlib 及 brokenaxes 实现效果一般，建议还是用 Origin）：[python - Matplotlib with brokenaxes package second Y-Axis - Stack Overflow](https://stackoverflow.com/questions/60026605/matplotlib-with-brokenaxes-package-second-y-axis)

- 在 Jupyter Notebook 中使用 `%matplotlib inline`，从 matplotlib 3.2 版本开始，这个命令在大多数情况下已不再是必需的，因为 Jupyter 和 IPython 的默认行为已经是将图形内嵌显示

- 给每张子图表 (a) (b) 序号标签（最后其实还是用 ax.text() 实现；效果一般）：[Labelling subplots — Matplotlib 3.8.4 documentation](https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html)

- 箱线图又称为盒须图，是显示一组数据分散情况的统计图，因形状如箱子而得名。 它主要用于反映原始数据分布的特征，还可以进行多组数据分布特征的比较。

```python
ax.boxplot(x, showmeans=...)
# x 为二维数组时，每一列都会产生一个统计图形
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202404271553335.png)

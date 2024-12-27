---
title: Pandas 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Pandas 使用
description: Pandas 使用
tags:
  - Pandas
categories:
  - 编程
  - Python
date: 2023-10-25 11:30:00
abbrlink: 302151
password:
---

# Pandas 使用

## 介绍

参考资料：

- [Python-notes/pandas-notes.md at master · RuihaoQiu/Python-notes · GitHub](https://github.com/RuihaoQiu/Python-notes/blob/master/pandas-notes.md)
- [深入浅出pandas-1 - Python-100-Days](https://github.com/jackfrued/Python-100-Days/blob/master/Day66-80/72.%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BApandas-1.md)
- [GitHub - ajcr/100-pandas-puzzles: 100 data puzzles for pandas, ranging from short and simple to super tricky (60% complete)](https://github.com/ajcr/100-pandas-puzzles)
- [GitHub - jvns/pandas-cookbook: Recipes for using Python's pandas library](https://github.com/jvns/pandas-cookbook)



---

## 使用

### 工具

- 不是太好用：[GitHub - lux-org/lux: Automatically visualize your pandas dataframe via a single print! 📊 💡](https://github.com/lux-org/lux)

- [GitHub - Kanaries/pygwalker: PyGWalker: Turn your pandas dataframe into an interactive UI for visual analysis](https://github.com/Kanaries/pygwalker/)


---

### 创建 DataFrame / Series

```python
import pandas as pd

pd.__version__   # 查看 pandas 版本

# 二维数据结构
df = pd.DataFrame(...)

# 一维数据结构
ser = pd.Series(...)

# value 为标量的 dict 数据，变换成 DataFrame 方式
data = {"a": 1, "b": 2, "c": 3}

df = pd.DataFrame([data])
df = pd.DataFrame(data, index=[0])
df = pd.DataFrame(data, index=[0, 1, 2])
# 将 多个 dict 数据存储成 list，再变换成 DataFrame（效率较高）
df = pd.DataFrame([data, data])

print(df)
```


---

### 快速查看数据信息

```python
# DataFrame 方法
info()
describe()
head()
tail()
count()
astype()             # 设置数据类型


# DataFrame 属性
dtypes               # 数据类型
shape                # m 行 n 列
size                 # 
index                # 行索引
columns              # 列名
values               # 数值
ndim                 # 维度

# Series 属性
is_unique
name


df.corr()               # Pearson 相关系数矩阵
```


---

### 索引

```python
# Series 索引
ser[1]             # 整数索引
ser.iloc[1]
ser["a"]           # 标签索引
ser.loc["a"]


df.loc[]           # 基于标签索引；闭区间
df.iloc[]          # 基于整数位置索引；半开区间

# 选择单列
df["col1"]
df.col1
df.loc[:, "col1"]
df.iloc[:, 0]

# 选择多列
df[["col1", "col2"]]
df.loc[:, ["col1", "col2"]]
df.iloc[:, [2:5]]

# 选择行
df.loc[1:3]        # 行标签索引默认是整数 0 - N-1，此时写法和 iloc 类似
df.loc[["a", "b"]]
df.iloc[1:3]

# 选择行和列
df.loc[1:3, ["col1", "col2"]]
df.loc[["a", "b", "c"], ["col1", "col2"]]
df.iloc[1:3, 2:4]
```


---

### 筛选

```python
# 类别数据
df[df["col1"] == "class1"]
df[~df["col1"] == "class1"]
df[df["col1"].isin(["class1", "class2"])]

# 数值数据
df[df["col1"] > 0]
# 多个条件，每个条件需用 () 包起来
df[(df["col1"] > 0) & (df["col1"] < 1.0)]
```


---

### 统计

```python
df.sum()
df.max()
df.min()
df.mean()
```


---

### IO

- 保存成 csv 文件时，在文件头添加注释（无内置函数）：[python - Write comments in CSV file with pandas - Stack Overflow](https://stackoverflow.com/questions/29233496/write-comments-in-csv-file-with-pandas)

```python
pd.read_csv()       # 从 csv 文件读取数据
# 参数
sep                 # 分隔符，默认是","；多个空格，可以使用 "\s+"
comment             # 忽略注释行；如 "#" 开头的
header              # 表头；可以为 None；默认用第一行的内容作为表头
skiprows            # 跳过 N 行
index_col           # 用作行索引（标签）的列
usecols             # 需要加载的列，可以使用序号或者列名


# 可自动识别分隔符（逗号、单个空格、制表符，制表符+空格），速度会慢一些
# 两个空格不行
df = pd.read_csv(csv_fn, sep=None, engine="python")


pd.read_excel()     # 从 Excel 文件读取数据
# 参数
sheet_name          # 指定数据表的名称
# header skiprows 等参数同上
# 无 sep 参数


df.to_csv()         # 保存成 csv 文件
# 参数
index               # 是否写入行索引
float_format        # 浮点数的格式化字符串


# 将数据（列表格式）写入 JSON 文件
df = pd.DataFrame({
    "A": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    "B": ["x", "y", "z"]
})

# 保存为 JSON 文件
df.to_json("output.json", orient="records", lines=True)

# 读取 JSON 文件
pd.read_json("output.json", orient="records", lines=True)

# 保存的 JSON 数据格式
{"A":[1,2,3],"B":"x"}
{"A":[4,5,6],"B":"y"}
{"A":[7,8,9],"B":"z"}
```


---

### 数据分组

groupby：对数据进行分组处理

```python
df.groupby("col1").mean()
df.groupby("col1").max()
df.groupby("col1").min()
```


---

### map()、apply() 函数

lambda 匿名函数：主要用在 `map()`、`apply()` 函数中

`map()`：主要用于对 Series 中的每个元素应用一个函数或映射关系，常用于数据替换；映射中缺少与 Series 中的值相对应的键，则结果中相应的元素会被设置为 NaN
`apply()`：可用于 DataFrame 和 Series

pandas apply 用法：[（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg - 费弗里 - 博客园](https://www.cnblogs.com/feffery/p/11468762.html)

```python
# 两者等价
df[df["col1"] > 0]
df[df["col1"].apply(lambda x: x > 0)]
```


---

### 其他

- 按照特定的列顺序进行排列

```python
df["col1"] = pd.Categorical(
    df["col1"],
    categories=lst1,
    ordered=True,
)
df["col2"] = pd.Categorical(
    df["col2"],
    categories=lst2,
    ordered=True,
)

df.sort_values(
    by=["col1", "col2"],
    ignore_index=True,
    inplace=True,
)
```

---

- 参数 `inplace=True`：可使操作直接在 df 上执行，而非返回新的 DataFrame 对象

- 参数 `ignore_index=True`：忽略索引

- 参数 `axis=0` 表示为行，`axis=1` 表示为列

```python
df.reset_index(drop=True, inplace=True)  # 重置行索引
pd.concat([df1, df2], axis=...)          # 行/列 拼接
df.sort_values(by=...)                   # 按照 列/行 排序
df.values.reshape(-1)                    # 将数据转化成一维
df.round()                               # 四舍五入；当 df 既有数值和字符串数据时，也可以使用
```


```python
df.diff()       # 同列相邻元素差值

df.unique()
df.nunique()

df.nlargest()   # 查看排前 N 的数据
df.nsmallest()  # 查看排后 N 的数据

# df 数据合并
pd.merge(df1, df2, how='outer')
```


```python
df.drop()   # 去掉行/列数据

# 统计该列出现的不同值及对应数目
df.value_counts(sort=False)

# 绘图
df.plot(kind="bar")

df.duplicated()
df.drop_duplicates(, keep=..., inplace=...)
keep                # first last

# 缺失值处理
isnull()
isna()
dropna()
fillna(value=0)
```

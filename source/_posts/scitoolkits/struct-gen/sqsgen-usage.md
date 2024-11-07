---
title: sqsgen 安装与使用
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: sqsgen 安装与使用
description: sqsgen 安装与使用
tags:
  - sqsgen
categories:
  - 科研工具
  - 结构建模
date: 2023-06-06 15:30:30
abbrlink: 531256
password:
---

# sqsgen 安装与使用

## 介绍

- sqsgen：SQS（special quasi-random structure, 特殊准随机结构）生成程序
    - 目标函数为 WC 参数（warren-cowley parameter）
    - 生成速度相比 ATAT 及 ICET 相关模块要快，功能也更多
    - 10000 个原子以内的构型的 sqs 生成速度在 2min 以内
    - 可事先估计生成 sqs 结构所耗费时间
    - 浓度用具体的原子数目表示，比百分比形式更方便
    - 有 OpenMP 和 OpenMPa + MPI 两种版本



---

## 安装

- 安装：[How to install sqsgen? — sqsgenerator 0.3 documentation](https://sqsgenerator.readthedocs.io/en/latest/installation_guide.html)

---

### conda 安装

只有 OpenMP 版本

```bash
conda create -n sqsgen python=3.11

conda install -c conda-forge sqsgenerator

# 安装构型文件导出格式所需的 package
pip install -U pymatgen ase
```


---

### 编译

- 有 OpenMP+MPI 两种版本

- 创建 sqsgen 的 Python 虚拟环境，安装必要的 package，并下载源码

```bash
conda create -n sqsgen_mpi -c conda-forge boost boost-cpp cmake gxx_linux-64 libgomp numpy pip python=3

git clone https://github.com/dgehringer/sqsgenerator.git
```

- OpenMP 版本

```bash
conda activate sqsgen_mpi
cd sqsgenerator

SQS_Boost_INCLUDE_DIR="${CONDA_PREFIX}/include" \
SQS_Boost_LIBRARY_DIR_RELEASE="${CONDA_PREFIX}/lib" \
CMAKE_CXX_COMPILER="g++" \
CMAKE_CXX_FLAGS="-DNDEBUG -O2 -mtune=native -march=native" \
pip install .
```

- OpenMP+MPI 版本

```bash
conda activate sqsgen_mpi
cd sqsgenerator

SQS_MPI_HOME="${HOME}/src/openmpi" \
SQS_USE_MPI=ON \
SQS_Boost_INCLUDE_DIR="${CONDA_PREFIX}/include" \
SQS_Boost_LIBRARY_DIR_RELEASE="${CONDA_PREFIX}/lib" \
CMAKE_CXX_COMPILER="g++" \
CMAKE_CXX_FLAGS="-DNDEBUG -O2 -mtune=native -march=native" \
pip install .
```

- 注意事项：
    - 与官方的编译教程相比，主要的区别为 `CMAKE_CXX_COMPILER` 选择所在 Linux 系统的默认加载的 g++，非 conda 版本的 g++（后者编译时在自己的机器上出错）
    - 编译安装出错后，重新安装时，建议删除 sqsgenerator 目录下的新增文件 `sqsgenerator/core/include/version.hpp`。
    - Python 版本可适当降低，如 3.9
    - 使用 mpirun 多核运行 sqsgen 时，不要使用 `-c gz` 参数，会出现 `FileExistsError: [Errno 17] File exists: 'XXX.tar.gz'` 的报错。最终的 `*.result.yaml` 文件会覆盖成一个文件 (本应 N)。并行计算，一次生成 N 个结构（同一时间）；N 个结构之间是不同的


---

### 源代码修改

- 当要构建的 sqs 构型原子数很多时（1000 及以上），默认导出的构型文件名前缀太长（类似哈希码），会导致在 Linux 系统中无法写入保存成文件

```python
# sqsgenerator/io.py 第 358 行左右

    # modified by ysl
    # for rank, structure in structures.items():
        # filename = f'{rank}.{format}'
    for i, (rank, structure) in enumerate(structures.items(), 1):
        filename = f'{i}.{format}'
```



---

## 使用

### 程序输入文件

- sqs.yaml（sqsgen 程序输入文件）示例

```yaml
# 文件内容为构建 Ti2AlNb B2 相超胞（Ti 占据一个格点，Al 和 Nb 随机占据另一个格点）
structure:
  file: b2.vasp
  supercell: [4, 4, 4]
iterations: 1e7
shell_weights:
  1: 1.0
  2: 1.0
which: Al
composition:
  Al: 32
  Nb: 32
```

- yaml 文件内容相关参数

```bash
structure         # 初始结构，VASP POSCAR 格式或使用 file、supercell 参数
iterations        # MC 迭代次数
shell_weights     # 计算目标函数 WC 参数考虑的第 N 近邻原子距离的权重；对于 BCC，考虑到第二近邻即可
which             # 选中具体的原子位点进行 mcsqs
composition       # 浓度；生成空位时，元素用数字 0 代替
```


---

### 常用命令

- 命令行使用：[CLI reference — sqsgenerator 0.3 documentation](https://sqsgenerator.readthedocs.io/en/latest/cli_interface.html)

```bash
# sqs 生成耗费时间估计
sqsgen compute estimated-time sqs.yaml

# 查看帮助
sqsgen run iteration --help

# sqs 生成；lammps-data 可改成 vasp 等
sqsgen run iteration sqs.yaml -di parameters -di objective -nm -e -f lammps-data -c gz -w ase

# 参数
--dump-include, -di    # 导出输出的一些 dump 信息，包括 parameters, objective, timings；选择前两个即可
--no-minimal, -nm      # 不只考虑最小目标函数下的构型（默认生成 10 个不同的构型）
--export, -e           # 将输出结构导出
--format, -f           # sqs 构型文件格式
--compress, -c         # 将构型文件打包压缩
--writer, -w           # 输出构型文件格式的后端（pymatgen 和 ase；后者支持的格式比前者多）
```



---

## 示例

- 参考：多亚点阵 sqsgen 生成示例：[Advanced topics — sqsgenerator 0.3 documentation](https://sqsgenerator.readthedocs.io/en/latest/advanced_topics.html)

---

### 示例 1

- rocksalt 结构 TiN 生成 (Ti0.25Al0.25)(B0.25N0.25) 的 sqs

- 多亚点阵结构，Ti 和 Al 随机占据一个格点，B 和 N 随机占据另一个格点

- ti-al-b-n.yaml
    - `composition` 写法：上面的元素是占据格点的元素，下面的元素是被占据的元素

- 注意事项：
    - 对于多亚点阵结构，一种元素不能同时占据两种位点，否则会报错
    - 要建的 sqs 构型较大且删除的原子较多时，速度会变慢许多，可先替换原子再用 pymatgen 删除

```yaml
structure:
  supercell: [2, 2, 2]
  file: ti-n.vasp
iterations: 5e5
shell_weights:
  2: 1.0
composition:
  B:
    N: 16
  N:
    N: 16
  Ti:
    Ti: 16
  Al:
    Ti: 16
```


---

### 示例 2

- FCC Al 生成 0.5% 自间隙浓度的 sqs；自间隙类型：八面体间隙

- al-is-oct-all.vasp（初始构型文件；单胞中所有八面体间隙位点）

```plain
# FCC Al
    1.00000000000000
    4.05000000000000      0.00000000000000      0.00000000000000
    0.00000000000000      4.05000000000000      0.00000000000000
    0.00000000000000      0.00000000000000      4.05000000000000
    Al C
     4 4
direct
    0.00000000000000      0.00000000000000      0.00000000000000  Al
    0.50000000000000      0.50000000000000      0.00000000000000  Al
    0.00000000000000      0.50000000000000      0.50000000000000  Al
    0.50000000000000      0.00000000000000      0.50000000000000  Al
    0.50000000000000      0.50000000000000      0.50000000000000  C
    0.50000000000000      0.00000000000000      0.00000000000000  C
    0.00000000000000      0.50000000000000      0.00000000000000  C
    0.00000000000000      0.00000000000000      0.50000000000000  C
```

- Al-is.yaml（输入文件）

```yaml
structure:
  file: al-is-oct-all.vasp
  supercell: [10, 10, 10]
iterations: 1e6
shell_weights:
  1: 1.0
  2: 0.5
which: C
composition:
  Al: 20
  0: 3980
```

- parse-yaml.py（检查生成的 10 个 sqs 构型中自间隙原子坐标相同的个数）

```python
import yaml
import pandas as pd
import numpy as np
from glob import glob


def main():
    # read YAML file
    with open(glob("*.result.yaml")[0], "r") as file:
        data = yaml.safe_load(file)

    configurations_data = data["configurations"]
    is_index_list = []
    for index, configuration_id in enumerate(configurations_data.keys(), 1):
        configuration_list = configurations_data[configuration_id]["configuration"]
        pd_data = pd.DataFrame(configuration_list)
        is_index = (pd_data[pd_data.iloc[:, 0] != "0"].index).to_list()

        is_index_list.append(is_index)

    print("configuration 1-10 interstitial index list:")
    print(np.array(is_index_list))
    print("\n")

    print("same interstitial index between two configuration:")
    same_count_list = []
    for j in range(0, 9):
        for k in range(j + 1, 10):
            common_elements = set(is_index_list[j]) & set(is_index_list[k])
            count = len(common_elements)
            same_count_list.append(count)
            print(
                f"configuration {j+1}, {k+1}, the number of same vacancy index is: {count}."
            )

    count_series = pd.Series(same_count_list)
    print(f"\nTotal interstitial num is {len(is_index_list[0])};")
    print(count_series.describe())


if __name__ == "__main__":
    main()
```



---

## 相关问题

- 当需构建的 sqs 构型很大时（原子数 10000+），sqsgen 程序所需的内存也很大，超算的计算节点由于有内存配比限制，终端命令行运行时会被 kill

```bash
batch-fe.sh: line 29: 2976792 Killed                  sqsgen run iteration ${yaml_name} -di parameters -di objective --no-minimal -e -f lammps-data -c gz -w ase
slurmstepd: error: *** JOB 25428400 ON node022 CANCELLED AT 2023-05-30T19:46:40 ***
slurmstepd: error: Detected 1 oom-kill event(s) in StepId=25428400.batch. Some of your processes may have been killed by the cgroup out-of-memory handler.
```

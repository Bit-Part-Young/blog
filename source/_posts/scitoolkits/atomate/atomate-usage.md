---
title: atomate 使用
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: atomate 使用
description: atomate 使用
tags:
  - 高通量
  - atomate
categories:
  - 科研工具
  - atomate
date: 2023-06-18 18:30:30
abbrlink: 120740
password:
sticky: "98"
---

# atomate 使用

## 介绍

- 官网：[atomate (Materials Science Workflows) — atomate 1.0.3 documentation](https://atomate.org/)

- 高通量计算（主要 VASP）工具；主要在队列系统（如 Slurm、PBS 等）上运行；自动生成、保存任务运行过程中的所有记录（输入文件、输出文件、数据提取、错误信息等）

- 数据存储于数据库（MongoDB）中，易于获取、查询、分析

- 提供了许多性质计算（静态、弛豫、弹性常数、能带、EOS、体模量、NEB）的标准 workflow，只需提供晶体结构（POSCAR），即可进行高通量计算；标准的 workflow 可以进行自定义修改

- 可自定义设计新的性质计算 workflow

- **少量计算还是手动计算速度更快**


firetask 细节会在提交后生成的 `*submit*` 文本文件中查看

custodian 默认的纠错次数上限为 5

atomate workflow 的自定义设计代码主要由 FireWorks 包控制

输入参数形成的输入文件代码主要由 pymatgen 包控制

输出文件中的数据提取、绘图及其他高级分析主要由 pymatgen 包控制

Workflow，Firework（Firework 的列表可称做 fireworks），Firetask（一个 Firework 由若干个基本的 Firetask 组成）



---

## 使用

### lpad

- 管理 launchpad

```bash
# lpad 参数
-i            # ID
-s            # 状态；有 READY/WAITING/COMPLETED/FIZZLED/RUNNING
              # DEFUSED 该 firework 不运行
-m            # max
-t            # 以表格形式列出 workflow 中 firework 的状态
-d            # all 会显示 firework 之间的关联
              # count 统计数目
              # ids 统计 id
              # more 输出中的 _exception 字段会显示 custodian 的相关 warning 或报错

# 查看 fireworks 报告
lpad report

# 重新计算 fireworks
lpad rerun_fws -i 3
lpad rerun_fws -s FIZZLED

# 查看 fireworks
lpad get_fws
lpad get_fws -i 3
lpad get_fws -s FIZZLED
lpad get_fws -s FIZZLED -m 5
lpad get_fws -s FIZZLED -d more

# 查看 workflow （所属 fireworks 及其计算目录）
lpad get_wflows
lpad get_wflows -i 1
# -t 参数需安装 prettytable
lpad get_wflows -s FIZZLED -t -m 5
lpad get_wflows -s FIZZLED -d more

# 查看 fireworks 的计算目录
lpad get_launchdir fw_id

defuse_wflows               # cancel (de-fuse)
reignite_wflows             # reignite (un-cancel)
archive_wflows              # 存档（soft-remove）
delete_wflows               # 永远删除

# 以下两个命令不推荐使用
# 重设lpad，所有 lpad 中的 fireworks 都会被删除
lpad reset

# 初始化，一般不用？
lpad init
```

---

### qlaunch

- 将 workflow 提交到超算队列
    - 过程：先创建 `block_date/launcher_date` workflow 目录（`qlaunch rapidfire` 命令；`qlaunch singleshot` 无此步骤），之后生成 `FW_submit.script` Slurm 提交脚本，再在此目录下创建 `launcher_date` firework 计算目录

- `qlaunch rapidfire` 若出现以下提示时，不会再提交作业

```bash
No jobs exist in the LaunchPad for submission to queue
# 或
No READY jobs detected
```

```bash
qlaunch (-r) rapidfire            # 一次提交多个任务
qlaunch rapidfire --nlaunches 5   # 指定提交任务数
qlaunch singleshot                # 一次提交一个任务

# 参数
-q
```


---

### rlaunch

- 直接在计算平台本地上运行计算

```bash
rlaunch singleshot     # 会将当前目录下的所有文件分别单独压缩成 gz 格式
rlaunch rapidfire      # 会生成 launcher_date workflow 目录
```

- 高通量正确计算完成时，custodian.json 文件无纠错


---

### 使用 tips

- 用 Python 脚本生成 workflows 的 fireworks 后，需要用 qlaunch 相关命令将 fireworks 提交到队列系统中，对于只有一个 firework 的 workflows（如弛豫和静态计算），若共生成了**N 个 fireworks**，`qlaunch rapidfire --nlaunches N` 即可（体系较小时，N 可缩减成 N/2 等）

- 对于有多个 fireworks（如 M 个）的 workflows（如弹性常数计算），可以先提前了解这些多个 fireworks 之间的逻辑关系，若共有**N 个 workflows**，可先 `qlaunch rapidfire --nlaunches N`，N 个中有部分 fireworks（如 X 个）计算完成后，可适当再 `qlaunch rapidfire --nlaunches X*(M-1)`，进行该 workflow 其余部分 fireworks 的计算，一定程度上可以控制计算成本（虽然可能需要时不时查看 fireworks 的计算完成情况）

- **不建议直接 `qlaunch rapidfire`**（只要作业未结束，生成其他的 workflow，会自动到队列中等待，计算目录容易混淆）

- atomate 无法在只将 workflow 产生后就能看到输入文件，需让其实际运行才能看到；做法：核数设为 1；运行后待输入文件产生，将 Jobid 删除，检查输入文件参数



---

## 案例

### 静态计算

- Python 代码示例

```python
from atomate.common.powerups import add_namefile, add_tags
from atomate.vasp.workflows.presets.core import wf_static
from fireworks.core.launchpad import LaunchPad
from pymatgen.core.structure import Structure

structure = Structure.from_file("POSCAR")

wf = wf_static(structure)

wf = add_namefile(wf)
wf = add_tags(wf, {"task_name": "atomate static workflow test"})

lpad = LaunchPad.auto_load()
lpad.add_wf(wf)

print("The static test workflow is added.")
```


---

### 弛豫计算

- Python 代码示例

```python
from atomate.common.powerups import add_namefile, add_tags
from atomate.vasp.workflows.presets.core import wf_structure_optimization
from fireworks.core.launchpad import LaunchPad
from pymatgen.core.structure import Structure

structure = Structure.from_file("POSCAR")

wf = wf_structure_optimization(structure)

wf = add_namefile(wf)
wf = add_tags(wf, {"task_name": "atomate relaxation workflow test"})

lpad = LaunchPad.auto_load()
lpad.add_wf(wf)

print("The relaxation test workflow is added.")
```


---

### 弹性常数计算

- Python 代码示例

```python
from atomate.common.powerups import add_namefile, add_tags
from atomate.vasp.workflows.presets.core import wf_elastic_constant
from fireworks.core.launchpad import LaunchPad
from pymatgen.core.structure import Structure

structure = Structure.from_file("POSCAR")

wf = wf_elastic_constant(structure=structure)

wf = add_namefile(wf)
wf = add_tags(wf, {"task_name": "atomate elastic constant workflow test"})

lpad = LaunchPad.auto_load()
lpad.add_wf(wf)

print("The elastic constant test workflow is added.")
```

- atomate 中计算弹性常数使用的是应力 - 应变法；先结构优化，再施加变形并 ISIF=2 弛豫 （用到的是 StaticSetOne.yaml 文件中的参数），最后拟合弹性常数并计算弹性性质

- 弹性常数计算 workflow 的 `fw.name`

```bash
Ni-elastic structure optimization--78
Ni-elastic deformation 0--77
...
Ni-elastic deformation 5--72
Analyze Elastic Data--71
```

- 运行弹性常数计算 workflow 时，若部分变形的 firework 计算结束，部分 fizzled，它会先根据已计算的变形 firework 的数据进行弹性常数拟合，因此**需检查该 workflow 中的所有 firework 是否都计算完成并检验结果是否合理**

- atomate 计算弹性常数得到的弹性张量中 POSCAR-format (raw) 与 IEEE-format (ieee_format) 之间的区别：
    - [Elastic Constants - Materials Project Documentation](https://docs.materialsproject.org/methodology/materials-methodology/elasticity)
    - 有时相同，有时不同（存在旋转关系），可使用 `pymatgen.core.tensors.Tensor` 类的 `get_ieee_rotation()` 方法进行转换
    - 建议采用 POSCAR-format

```python
# 弹性常数计算 workflow 程序实现涉及的文件路径
# wf_elastic_constant()
atomate/vasp/workflows/presets/core.py

# get_wf_elastic_constant()
atomate/vasp/workflows/base/elastic.py

# ElasticTensorToDb 类；含弹性常数拟合细节
# 自定义弹性数据保存到 db 中的 collection 的名称：修改 "elasticity" 即可，即 db.db["elasticity"]
atomate/vasp/firetasks/parse_outputs.py
```

- 弹性常数计算 workflow 默认参数设置

```python
# 计算 2 阶弹性常数（默认）
# 第一步弛豫
{"ENCUT": 700, "EDIFF": 1e-6, "LAECHG": False, "LREAL": False}
# ISIF = 2 弛豫部分
{"ISIF": 2, "IBRION": 2, "NSW": 99, "ISTART": 1}


# 计算 3 阶弹性常数
Kpoints.automatic_density(structure, 40000, force_gamma=True)
stencils = np.linspace(-0.075, 0.075, 7)


# wf_elastic_constant_minimal() 设置
stencil = np.arange(0.01, 0.01 * order, step=0.01)


# wf_elastic() 会调用 get_wf_elastic_constant()
# get_wf_elastic_constant() 源代码
# Convert to conventional if specified
if conventional:
    structure = SpacegroupAnalyzer(structure).get_conventional_standard_structure()

uis_elastic = {"IBRION": 2, "NSW": 99, "ISIF": 2, "ISTART": 1}
vis = vasp_input_set or MPStaticSet(structure, user_incar_settings=uis_elastic)
strains = []
if strain_states is None:
    strain_states = get_default_strain_states(order)
if stencils is None:
    # 应变范围为 -10% ~ 10%，间隔 5%
    stencils = [np.linspace(-0.01, 0.01, 5 + (order - 2) * 2)] * len(strain_states)
if np.array(stencils).ndim == 1:
    stencils = [stencils] * len(strain_states)
for state, stencil in zip(strain_states, stencils):
    strains.extend([Strain.from_voigt(s * np.array(state)) for s in stencil])
```



---

## MongoDB Compass 使用

### 数据库连接

- 连接数据库：New connection - Advanced Connection Options
    - General: Connection String Scheme 选择 mongodb；填写 Host
    - Authentication: Authentication Method 选择 Username/Password；填写 Username、Password 和 Database，Authentication Mechanism 选择 Default

- 修改连接的 connection 名称："New Connection" 有编辑选项

- [x] MONGOSH 使用（暂无必要）

- [手把手教你注册MongoDB Atlas](https://mp.weixin.qq.com/s/jF5o7YNHw88uI7rjTxFkIw)


---

### 使用

- MongoDB 中存储的每条数据称为 document，具体数据值通过字段查询（即 dict 中的 key 和 value）

- 在 MongoDB Compass 软件中通过字段筛选 document，字段间通过 `.` 连接，示例

```json
{"tags.structure_id": "ICET-Training-No-00754"}
```

- atomate 连接 MongoDB，数据获取与筛选

```python
import os
from atomate.vasp.database import VaspCalcDb

# 方式 1
db_json_path = ...
# 方式 2 将 db.json 放入 ~/.{bash,zsh}rc 文件中
db_json_path = os.getenv("DB_JSON_PATH")
atomate_db = VaspCalcDb.from_db_file(db_json_path)

# 弹性数据分析 colletion
elasticity_collection = atomate_db.db["elasticity"]
# 吉布斯计算任务 collection
gibbs_collection = atomate_db.db["gibbs_tasks"]

# find() 可以使用 Projection Operators（以 $ 开头）
query = {"task_label": "volume relaxation"}
query = {"task_id": {"$gt": 18, "$lt": 44}}
query = {"tags.solute": {"$in": solute_list}}
query = {"completed_at": {"$regex": "2022-08-05 *"}}

# 0: 不提取数据；1: 提取数据
projection = {
    "_id": 0,
    "dir_name": 1,
    "task_id": 1,
    "completed_at": 1,
    "state": 1,
    "task_label": 1,
    "formula_reduced_abc": 1,
    "run_stats": 1,
    "input": 1,
    "output": 1,
    "tags": 1,
}

# 统计满足筛选条件的 documents 数目
# 方式 1
count = atomate_db.collection.count_documents(query)
# 方式 2
count = atomate_db.collection.aggregate([{"$match": query}, {"$count": "total"}])
# 方式 3 不行？
count = db.collection.find(query).count()

# 获取满足 query projection 条件的所有 documents
documents = atomate_db.collection.find(query, projection)
# 一条 document
document = atomate_db.collection.find_one(query, projection)
```

可用 Projection Operators：[Query and Projection Operators - MongoDB Manual v7.0](https://www.mongodb.com/docs/manual/reference/operator/query/#std-label-query-selectors)

find() manual：[db.collection.find() - MongoDB Manual v7.0](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/)

- `find()` 或 `find_one()` 返回的结果是 `pymongo.cursor` 对象，可以将其转化成 json 或 dataframe 的形式

参考链接：[https://www.geeksforgeeks.org/convert-pymongo-cursor-to-json/](https://www.geeksforgeeks.org/convert-pymongo-cursor-to-json/)；[https://www.geeksforgeeks.org/convert-pymongo-cursor-to-dataframe](https://www.geeksforgeeks.org/convert-pymongo-cursor-to-dataframe)

- 判断 `find()` 或 `find_one()` 返回的结果是否是空的

参考链接：[https://www.geeksforgeeks.org/how-to-check-if-the-pymongo-cursor-is-empty](https://www.geeksforgeeks.org/how-to-check-if-the-pymongo-cursor-is-empty/?ref=lbp)

统计 key 的个数：[https://stackoverflow.com/questions/12536592/mongodb-iterate-over-collection-by-key](https://stackoverflow.com/questions/12536592/mongodb-iterate-over-collection-by-key)

>[https://github.com/hackingmaterials/atomate/issues/445](https://github.com/hackingmaterials/atomate/issues/445)

---

- document 常用数据

```python
# 输入构型
input_structure_dict = document["input"]["structure"]
# 输出构型
output_structure_dict = document["output"]["structure"]
structure = Structure.from_dict(...)

# 能量
energy = document["output"]["energy"]
energy_pa = document["output"]["energy_per_atom"]

# 计算耗时
document["run_stats"]["overall"]["Elapsed time (sec)"]
document["run_stats"]["overall"]["Total CPU time used (sec)"]

# 每个 firework 计算目录路径；需通过简单的正则表达式处理
dir_name = document["dir_name"]
calc_path = (re.search("/dssg.*", dir_name)).group()

# add_tags 中添加的一些 tag
document["tags"]["XXX"]

# 原子数
natoms = document["nsites"]
# 元素数
nelements = document["nelements"]
# 构型体积
volume = document["output"]["structure"]["lattice"]["volume"]
# 平均原子体积
volume_pa = volume / natoms
```

---

- MongoDB 中的 atomate documet 数据无法直接全部写入到 json 文件中
    - 其 key 和 dict 涉及到 str 均使用单引号
    - json 文件不识别 bool 变量？

```json
'_id': ObjectId('62dbb72c531c489b7a006879')
```


---

### 常见 workflow 的 document keys

- 弛豫 wf

```json
dict_keys(
    [
        "_id",
        "dir_name",
        "analysis",
        "calcs_reversed",
        "chemsys",
        "completed_at",
        "composition_reduced",
        "composition_unit_cell",
        "custodian",
        "elements",
        "formula_anonymous",
        "formula_pretty",
        "formula_reduced_abc",
        "input",
        "last_updated",
        "nelements",
        "nsites",
        "orig_inputs",
        "output",
        "run_stats",
        "schema",
        "state",
        "tags",
        "task_id",
        "task_label",
        "transformations",
    ]
)
```

`calcs_reversed` key 下的 keys （需添加 `[0]`；含大部分同级下的 keys）

```json
dict_keys(
    [
        "vasp_version",
        "has_vasp_completed",
        "nsites",
        "elements",
        "nelements",
        "run_type",
        "input",
        "output",
        "formula_pretty",
        "composition_reduced",
        "composition_unit_cell",
        "formula_anonymous",
        "formula_reduced_abc",
        "dir_name",
        "completed_at",
        "task",
        "output_file_paths",
        "bader",
    ]
)
```

- 弹性常数计算 wf 会生成弹性性质分析 `elasticity` collection

```json
dict_keys(
    [
        "_id",
        "analysis",
        "initial_structure",
        "optimized_structure",
        "tags",
        "fitting_data",
        "elastic_tensor",
        "derived_properties",
        "formula_pretty",
        "fitting_method",
        "order",
    ]
)
```

- 吉布斯自由能计算 wf 会生成 `gibbs_tasks` collection

```python
dict_keys(
    [
        "_id",
        "metadata",
        "structure",
        "formula_pretty",
        "energies",
        "volumes",
        "pressure",
        "poisson",
        "mass",
        "natoms",
        "bulk_modulus",
        "gibbs_free_energy",
        "temperatures",
        "optimum_volumes",
        "debye_temperature",
        "gruneisen_parameter",
        "thermal_conductivity",
        "anharmonic_contribution",
        "success",
    ]
)
```


---

### 相关问题

- 新版 MongoDB Compass 可以修改一个页面下的 Document 条数（25-100）

- Master `db.json` 问题：Host 只能写数字的形式，SiYuan 可以写字符串的形式（在 MongoDB Compass 填写的 Host 也需对应的形式）

```bash
    raise ServerSelectionTimeoutError(
pymongo.errors.ServerSelectionTimeoutError:
```

- MongoDB 数据库连接失败（数据库服务未启动；XXX 指 Host）

```bash
# 报错情况 1
getaddrinfo ENOTFOUND XXX

# 报错情况 2
Connection failed: XXXX: [Errno 111] Connection refused, Timeout: 30s, Topology Description:
```

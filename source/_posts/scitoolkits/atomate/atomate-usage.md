---
title: atomate 安装与使用
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: atomate 安装与使用
description: atomate 安装与使用
tags:
  - 高通量
  - atomate
categories:
  - 科研工具
date: 2023-06-18 18:30:30
abbrlink: 120738
password:
sticky: "99"
---

# atomate 安装与使用

## 介绍

- 官网：[atomate (Materials Science Workflows) — atomate 1.0.3 documentation](https://atomate.org/)
- 高通量计算（主要 VASP）工具；主要在队列系统（Slurm、PBS 等）上运行；自动生成、保存作业运行过程中的所有记录（输入文件、输出文件、数据提取、错误信息等）；
- 数据保存到数据库（Mongodb）中，易于获取、查询、分析；
- 提供了许多性质计算（静态、弛豫、弹性常数、能带、EOS、体模量、NEB）的标准 workflow，只需提供晶体结构（POSCAR），即可进行高通量计算；标准的 workflow 可以进行自定义修改；
- 可以自定义设计新的性质计算 workflow。

firetask 细节会在提交后生成的 `*submit*` 文本文件中查看

custodian 默认的纠错次数上限为 5

atomate workflow 的自定义设计代码主要由 FireWorks 包控制

输入参数形成的输入文件代码主要由 pymatgen 包控制

输出文件中的数据提取、绘图及其他高级分析主要由 pymatgen 包控制


---

## 安装

- atomate 安装：[Installing atomate — atomate 1.0.3 documentation](https://atomate.org/installation.html)
- **必要条件**：VASP 计算软件与 Mongodb 数据库账号。
- [pymatgen](https://pymatgen.org/)：输入文件生成，输出文件的数据提取与分析
- [custodian](http://materialsproject.github.io/custodian/)：运行计算代码（VASP），执行错误检查与纠正
- [FireWorks](https://materialsproject.github.io/fireworks/)：设计、管理、执行 workflow


---

### 安装流程

- 新建 conda 虚拟环境，如 atomate_env（名字任意），安装 atomate package（会自动安装另外的 pymatgen custodian 和 FireWorks 依赖 packages）
- pymatgen 和 custodian 包更新频率相比 atomate 和 FireWorks 要高很多
- 当一个 conda 环境使用了很久且修改过相关 package 或 module 的源代码，不建议单独升级某个 package，有可能会破坏 package 之间的依赖关系

```bash
pip install atomate

pip install -U pymatgen custodian

# custodian 2023.3.10 版本以上，运行 atomate 会出错
pip install -U custodian==2023.3.10
```

custodian 版本过高出现的报错
```bash
    from custodian.vasp.handlers import (
ImportError: cannot import name 'MaxForceErrorHandler' from 'custodian.vasp.handlers' (/home/yslarch/src/miniconda3/lib/python3.10/site-packages/custodian/vasp/handlers.py)
```


---

### 配置文件

- atomate 标准 config 配置文件参考：[standard\_config](https://github.com/hackingmaterials/atomate/tree/main/atomate/vasp/examples/standard_config)
- 配置文件内容中涉及到路径填写时，需填写绝对路径，不可使用相对路径或 `$HOME` 等环境变量（否则会报错，重要提醒！！！）
- atomate 配置文件目录结构（目录名可任意）

```text
atomate_env
├── config/
│   ├── db.json
│   ├── FW_config.yaml
│   ├── my_fworker.yaml
│   ├── my_launchpad.yaml
│   └── my_qadapter.yaml
└── logs/
```

---

- `db.json` 文件内容：连接 mongodb 数据库（注：除了 port 条目（entry）的 value 是整数；其他都是字符串，且条目及对应的 value 值都应用双引号）

```json
{
    "host": "<HOSTNAME>",
    "port": <PORT>,
    "database": "<DB_NAME>",
    "collection": "tasks",
    "admin_user": "<ADMIN_USERNAME>",
    "admin_password": "<ADMIN_PASSWORD>",
    "readonly_user": "<READ_ONLY_PASSWORD>",
    "readonly_password": "<READ_ONLY_PASSWORD>",
    "aliases": {}
}
```

---

- `my_fworker.yaml` 文件内容：

```yaml
name: <WORKER_NAME>
category: ''
query: '{}'
env:
    db_file: <INSTALL_DIR>/config/db.json
    vasp_cmd: <VASP_CMD>  # eg: mpirun vasp_std
    scratch_dir: null  # optional
```

---

- `my_launchpad.yaml` 文件内容：

```yaml
host: <HOSTNAME>
port: <PORT>
name: <DB_NAME>
username: <ADMIN_USERNAME>
password: <ADMIN_PASSWORD>
ssl_ca_file: null
logdir: null
strm_lvl: INFO
user_indices: []
wf_user_indices: []
```

---

- `my_qadapter.yaml` 文件内容：配置队列系统；当 fireworks 提交到队列系统时，会自动生成 slurm 或 PBS 提交脚本文件。

```yaml
host: <HOSTNAME>
port: <PORT>
name: <DB_NAME>
username: <ADMIN_USERNAME>
password: <ADMIN_PASSWORD>
_fw_name: CommonAdapter
_fw_q_type: SLURM
rocket_launch: rlaunch rapidfire
nodes: 1
ntasks: 1
ntasks_per_node: 1
walltime: 72:00:00
queue: CLUSTER
account: null
job_name: null
pre_rocket: null
post_rocket: null
logdir: <INSTALL_DIR>/logs
```

参数说明：
- `_fw_q_type` - 队列系统类型，如 SLURM PBS 等；
- `queue` - 队列名称；如 master 服务器中的 CLUSTER 队列；
- `walltime` - 作业最长运行时间；


注：若无法将 fireworks 提交到队列系统，rocket_launch 可进行以下修改：
```yaml
rocket_launch: rlaunch -c <INSTALL_DIR>/config rapidfire
```

---

- `FW_config.yaml` 文件内容：

```yaml
CONFIG_FILE_DIR: <INSTALL_DIR>/config

# 该参数对应设置应该是在 fireworks 包中的
# fireworks/scripts/qlaunch_run.py 约第 242 行
# 队列更新间隔
QUEUE_UPDATE_INTERVAL: 5
```

需将其路径添加到 PATH 中：
```bash
export FW_CONFIG_FILE=<atomate_config_dir>/config/FW_config.yaml
```

若 atomate 环境有多个，可进行如下设置（可使用 `$HOME` 等变量；切换 atomate 环境后，需 `source` 使其生效）：
```bash
conda_venv_name=$(conda info -e | grep \* | awk '{print $1}')
if [[ $conda_venv_name == atomate_env1 ]]; then
   export FW_CONFIG_FILE=<atomate_config_dir1>/config/FW_config.yaml
elif [[ $conda_venv_name == atomate_env2 ]]; then
   export FW_CONFIG_FILE=<atomate_config_dir2>/config/FW_config.yaml
fi
```


---

- 配置 pymatgen：VASP 赝势路径 + Material Project 网站 API

方式 1：新建 `~/.pmgrc.yaml` 或 `~/.config/.pmgrc.yaml` 文件，添加以下内容

```yaml
PMG_VASP_PSP_DIR: <psp_dir>
PMG_MAPI_KEY: <api_key>
```

方式 2：使用 pmg 命令来生成配置文件

```bash
pmg config --add PMG_VASP_PSP_DIR <psp_dir>
pmg config --add PMG_MAPI_KEY <api_key>
```

赝势目录结构：

```text
pseudopotentials
├── POT_GGA_PAW_PBE
│   ├── POTCAR.Ac.gz
│   ├── POTCAR.Ac_s.gz
│   ├── POTCAR.Ag.gz
│   └── ...
├── POT_GGA_PAW_PW91
│   ├── POTCAR.Ac.gz
│   ├── POTCAR.Ac_s.gz
│   ├── POTCAR.Ag.gz
│   └── ...
└── POT_LDA_PAW
    ├── POTCAR.Ac.gz
    ├── POTCAR.Ac_s.gz
    ├── POTCAR.Ag.gz
    └── ...
```

```bash
# pymatgen 寻找 POTCAR 的两种路径形式
# 形式 1 所有元素 POTCAR 在一个目录下
pseudopotentialsPOT_GGA_PAW_PBE/POTCAR.XXX
# 形式 2 元素 POTCAR 按元素分类在子目录下
pseudopotentialsPOT_GGA_PAW_PBE/XXX/POTCAR
```

注：若 `<psp_dir>` 赝势目录下没有 `POT_GGA_PAW_PBE` 名称目录，可设置软链接：

```bash
ln -s PBE_folder POT_GGA_PAW_PBE
```


---

### 相关问题

- 配置文件中的 db.json 路径没有设置正确

解决方法：db.json 的文件路径需设置为绝对路径

```bash
ValueError: Could not get next FW id! If you have not yet initialized the database, please do so by performing a database reset (e.g., lpad reset)
```

---

- 赝势路径或赝势目录结构没有设置正确

解决方法：参照上节中赝势路径和赝势目录结构设置

```bash
OSError: You do not have the right POTCAR with functional PBE and label Nb_pv in your VASP_PSP_DIR. Paths tried: ['/home/xxx/src/POT/PAW_PBE/POT_GGA_PAW_PBE/POTCAR.Nb_pv', '/home/xxx/src/POT/PAW_PBE/POT_GGA_PAW_PBE/Nb_pv/POTCAR']
```

---

- 没有创建 logs 目录

解决方法：创建 config 目录的同时创建 logs 目录

```bash
FileNotFoundError: [Errno 2] No such file or directory: 'path/atomate/logs/launchpad-debug.log'

During handling of the above exception, another exception occurred:

  File "conda_path/envs/atomate_nbsi/lib/python3.11/site-packages/fireworks/scripts/lpad_run.py", line 132, in get_lp
    f"FireWorks was not able to connect to MongoDB at {lp.host}:{lp.port}. Is the server running? "
                                                       ^^
UnboundLocalError: cannot access local variable 'lp' where it is not associated with a value
```

---

- 未添加 `FW_CONFIG_FILE` 环境变量

```bash
ValueError: Fireworks was not able to connect to MongoDB.
```

---

- 不生成 VASP 计算输入文件，只生成.err .out（空文件）和 FW_submit.script 文件，job 处于不断提交 - kill - 再提交的循环

解决方法：**这是自己遇到过的一个特殊情况**。自己安装过 `zsh`，且将 `zsh` 加入到 `~/.bash_profile` 中使登录服务器便切换到 zsh，最终导致上述问题出现（发现的原因是该问题出现后只有这个新变量因素）。将 `~/.bash_profile` 中与 `zsh` 相关的内容注释掉，问题可得到解决。



---

## 使用

### 相关命令行命令

- `lpad`：管理 launchpad

```bash
-i            # ID
-s            # state READY/WAITING/COMPLETED/FIZZLED/RUNNING
              # DEFUSED 该 firework 不运行
-m            # max
-t            # table
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

lpad defuse_wflows -s READY/WAITING  # defuse workflow

lpad delete_wflows  # delete workflow  两者区别是什么？

# 以下两个命令不推荐使用
# 重设lpad，所有 lpad 中的 fireworks 都会被删除
lpad reset

# 初始化，一般不用？
lpad init
```

---

- `qlaunch`：将 workflow 提交到队列到系统中

```bash
# 一次提交一个任务
qlaunch singleshot

# 一次提交多个任务
qlaunch (-r) rapidfire
# 指定提交任务数
qlaunch rapidfire --nlaunches 5
```

- `rlaunch`：直接在计算平台上运行

```bash
rlaunch rapidfire
```

若出现以下提示时，不会再提交作业

```bash
No jobs exist in the LaunchPad for submission to queue
# 或
No READY jobs detected
```


高通量正确计算完成时，custodian.json 文件无纠错


---

### 使用 tips

- 用 python 脚本生成 workflows 的 fireworks 后，需要用 qlaunch 相关命令将 fireworks 提交到队列系统中，对于只有一个 firework 的 workflows（如弛豫和静态计算），若共生成了**N 个 fireworks**，`qlaunch rapidfire --nlaunches N` 即可（体系较小时，N 可缩减成 N/2 等）；
- 对于有多个 fireworks（如 M 个）的 workflows（如弹性常数计算），可以先提前了解这些多个 fireworks 之间的逻辑关系，若共有**N 个 workflows**，可先 `qlaunch rapidfire --nlaunches N`，N 个中有部分 fireworks（如 X 个）计算完成后，可适当再 `qlaunch rapidfire --nlaunches X*(M-1)`，进行该 workflow 其余部分 fireworks 的计算，一定程度上可以控制计算成本（虽然可能需要时不时查看 fireworks 的计算完成情况）。
- **不建议直接 `qlaunch rapidfire`**。



---

## 案例

### 测试

WIP...


---

### 弛豫计算

WIP...


---

### 静态计算

WIP...


---

### 弹性常数计算

弹性常数计算时，部分 fw 成功，部分 fizzled，它会先根据成功的那部分数据进行拟合得到弹性数据，因此需检查所有 fw 是否都成功计算完成并检验结果是否合理；修改相关错误，重新提交 fizzled fw 后（之前错误生成的输入文件会进行更新），分析那步 fw 会处于 WAITING 状态，以进行更新


自定义弹性常数计算 wf 保存到 db 中的 collection 的名字：

```python
# atomate/vasp/firetasks/parse_outputs.py 中的 ElasticTensorToDb 类（修改 "elasticity" 即可）
db.db["elasticity"] 

# 或 atomate/vasp/workflows/base/elastic.py 中的 get_wf_elastic_constant() 有涉及
```


---

弹性常数计算 workflow 的 `fw.name`

```python
Ni-elastic structure optimization--78
Ni-elastic deformation 0--77
...
Ni-elastic deformation 5--72
Analyze Elastic Data--71
```



---

## MongoDB Compass 使用

### 数据库连接

- 连接数据库：New connection - Advanced Connection Options
    - General: Connection String Scheme 选择 mongodb；填写 Host
    - Authentication: Authentication Method 选择 Username/Password；填写 Username、Password 和 Database，Authentication Mechanism 选择 Default

- 修改连接的 connection 名称：“New Connection” 有编辑选项

- [ ] MONGOSH 使用


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

可用 Projection Operators ：[Query and Projection Operators - MongoDB Manual v7.0](https://www.mongodb.com/docs/manual/reference/operator/query/#std-label-query-selectors)

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

---

- MongoDB 数据库连接失败（数据库服务未启动；XXX 指 Host）

```bash
getaddrinfo ENOTFOUND XXX
```

```bash
Connection failed: XXXX: [Errno 111] Connection refused, Timeout: 30s, Topology Description: 
```

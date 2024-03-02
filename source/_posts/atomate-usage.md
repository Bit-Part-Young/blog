---
title: atomate 安装与使用
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: atomate 安装与使用
tags:
  - 高通量
  - atomate
categories:
  - 科研工具
date: 2023-06-18 18:30:30
abbrlink: 12073
password: 
sticky: "99"
---

# atomate 安装与使用

## 介绍

>[atomate (Materials Science Workflows) — atomate 1.0.3 documentation](https://atomate.org/)

- 高通量计算（主要 VASP）工具；主要在队列系统（超算平台 Slurm PBS）上运行；自动生成、保存作业运行过程中的所有记录（输入文件、输出文件、数据提取、错误信息等）；
- 数据保存到数据库（mongodb）中，易于获取、查询、分析；
- 提供了许多性质计算（弛豫、静态、弹性常数、能带、EOS、体模量、NEB）的标准 workflow，只需提供晶体结构（POSCAR），即可进行高通量计算；标准的 workflow 可以进行自定义修改；
- 可以自定义设计新的性质计算 workflow。



---

## 安装

>[Installing atomate — atomate 1.0.3 documentation](https://atomate.org/installation.html)

- pymatgen：输入文件生成，输出文件的数据提取与分析
- custodian：运行模拟代码（VASP），执行错误检查与纠正
- FireWorks：设计、管理、执行 workflow

>[Home | pymatgen](https://pymatgen.org/)

>[Home | custodian](http://materialsproject.github.io/custodian/)

>[FireWorks 2.0.3 documentation](https://materialsproject.github.io/fireworks/)



---

### 必要条件

VASP 计算软件与 mongodb 数据库账号。


---

### 安装流程

新建 conda 虚拟环境，如 atomate_env（名字任意），安装 atomate package（会自动安装另外的 pymatgen custodian 和 FireWorks 依赖 packages）

```bash
pip install atomate

# pymatgen和custodian包更新频率相比atomate和FireWorks要高很多
pip install -U pymatgen custodian

# custodian 2023.3.10版本以上，运行atomate会出错
pip install -U custodian==2023.3.10
```


custodian 版本过高出现的报错
```bash
/home/yslarch/src/miniconda3/lib/python3.10/site-packages/atomate/vasp/drones.py:46: FutureWarning: which is deprecated; use which in shutil instead.
shutil.which has been available since Python 3.3. This will be removed in v2023.
  BADER_EXE_EXISTS = which("bader") or which("bader.exe")
Traceback (most recent call last):
  File "/home/yslarch/scripts/atomate-test/examples/1-relaxation/opt_swf.py", line 8, in <module>
    from atomate.vasp.workflows.presets.core import wf_structure_optimization
  File "/home/yslarch/src/miniconda3/lib/python3.10/site-packages/atomate/vasp/workflows/__init__.py", line 1, in <module>
    from .presets.core import (
  File "/home/yslarch/src/miniconda3/lib/python3.10/site-packages/atomate/vasp/workflows/presets/core.py", line 14, in <module>
    from atomate.vasp.powerups import (
  File "/home/yslarch/src/miniconda3/lib/python3.10/site-packages/atomate/vasp/powerups.py", line 21, in <module>
    from atomate.vasp.firetasks.glue_tasks import CheckBandgap, CheckStability
  File "/home/yslarch/src/miniconda3/lib/python3.10/site-packages/atomate/vasp/firetasks/__init__.py", line 30, in <module>
    from .run_calc import (
  File "/home/yslarch/src/miniconda3/lib/python3.10/site-packages/atomate/vasp/firetasks/run_calc.py", line 11, in <module>
    from custodian.vasp.handlers import (
ImportError: cannot import name 'MaxForceErrorHandler' from 'custodian.vasp.handlers' (/home/yslarch/src/miniconda3/lib/python3.10/site-packages/custodian/vasp/handlers.py)
```

>当一个 conda 环境使用了很久且修改过相关 package 或 module 的源代码，不建议单独升级某个 package，有可能会破坏 package 之间的依赖关系


---

### 配置文件

atomate 标准 config 配置文件：[standard\_config](https://github.com/hackingmaterials/atomate/tree/main/atomate/vasp/examples/standard_config)


atomate 配置文件目录结构（目录名任意）
```javascript
atomate_env
├── config
│   ├── db.json
│   ├── FW_config.yaml
│   ├── my_fworker.yaml
│   ├── my_launchpad.yaml
│   └── my_qadapter.yaml
└── logs

```

>注：以下配置文件内容中涉及到路径填写时，需填写绝对路径，不可使用相对路径或 `$HOME` 等环境变量。（重要提醒！！！）

---

- `db.json`：连接 mongodb 数据库

注：除了 port 条目（entry）的 value 是整数；其他都是字符串，且条目及对应的 value 值都应用双引号。

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


**注：若无法将 fireworks 提交到队列系统，rocket_launch 可进行以下修改：**
```yaml
rocket_launch: rlaunch -c <INSTALL_DIR>/config rapidfire
```

---

- `FW_config.yaml` 文件内容：

```yaml
CONFIG_FILE_DIR: <INSTALL_DIR>/config
```

**需将 `FW_config.yaml` 所在的路径添加到环境变量中：**
```shell
export FW_CONFIG_FILE=<atomte_config_dir>/config/FW_config.yaml
```


如果 atomate 环境有多个（atomate_env_1, atomate_env_2, …），可以进行如下设置（可以使用 `$HOME` 等变量）：
```shell
conda_venv_name=$(conda info -e | grep \* | awk '{print $1}')
if [[ $conda_venv_name == atomate_env1 ]]; then
   export FW_CONFIG_FILE=<atomte_config_dir1>/config/FW_config.yaml
elif [[ $conda_venv_name == atomate_env2 ]]; then
   export FW_CONFIG_FILE=<atomte_config_dir2>/config/FW_config.yaml
fi
```

**注：切换 atomate 环境后，需进行 `source ~/.bashrc` 或 `~/.zshrc`。**

---

- 配置 pymatgen：使其找到赝势路径及调用 material project 网站的 API

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

---

方式 1：新建 `~/.pmgrc.yaml` 或 `~/.config/.pmgrc.yaml` 文件，手动添加以下内容
```yaml
PMG_VASP_PSP_DIR: <psp_dir>
PMG_MAPI_KEY: <api_key>
```

---

方式 2：使用 pmg 命令来生成配置文件。
```bash
pmg config --add PMG_VASP_PSP_DIR <psp_dir>
pmg config --add PMG_MAPI_KEY <api_key>
```

**注：若<<psp_dir>>赝势根目录下没有 `POT_GGA_PAW_PBE` 名称的 PBE 赝势目录，可设置软链接：**
```bash
ln -s PBE_folder POT_GGA_PAW_PBE
```


---

### 安装结束后可能会遇到的问题

- 相关 yaml 配置文件中的 db.json 路径没有设置正确

```bash
ValueError: Could not get next FW id! If you have not yet initialized the database, please do so by performing a database reset (e.g., lpad reset)
```

**解决方法**：db.json 的文件路径需设置为绝对路径。

---

- 赝势路径或赝势目录结构没有设置正确

```bash

OSError: You do not have the right POTCAR with functional PBE and label Nb_pv in your VASP_PSP_DIR. Paths tried: ['/home/xxx/src/POT/PAW_PBE/POT_GGA_PAW_PBE/POTCAR.Nb_pv', '/home/xxx/src/POT/PAW_PBE/POT_GGA_PAW_PBE/Nb_pv/POTCAR']

```

**解决方法**：参照上节中赝势路径和赝势目录结构设置。

---

- 没有创建 logs 目录

```bash
FileNotFoundError: [Errno 2] No such file or directory: '/dssg/home/acct-mseklt/mseklt/yangsl/atomate_nbsi/logs/launchpad-debug.log'

During handling of the above exception, another exception occurred:

  File "/dssg/home/acct-mseklt/mseklt/.conda/envs/atomate_nbsi/lib/python3.11/site-packages/fireworks/scripts/lpad_run.py", line 132, in get_lp
    f"FireWorks was not able to connect to MongoDB at {lp.host}:{lp.port}. Is the server running? "
                                                       ^^
UnboundLocalError: cannot access local variable 'lp' where it is not associated with a value
```

**解决方法**：创建 config 目录的同时创建 logs 目录。

---

- 不生成 VASP 计算输入文件，只生成.err .out（空文件）和 FW_submit.script 文件，job 处于不断提交 -kill- 再提交的循环

**解决方法**：**这是自己遇到过的一个特殊情况**。自己安装过 `zsh`，且将 `zsh` 加入到 `~/.bash_profile` 中使登录服务器便切换到 zsh，最终导致上述问题出现（发现的原因是该问题出现后只有这个新变量因素）。将 `~/.bash_profile` 中与 `zsh` 相关的内容注释掉，问题可得到解决。



---

## 使用

### 相关命令行命令

- `lpad`：管理 launchpad

```bash
# 查看lpad帮助
lpad -h

# 查看fireworks的报告
lpad report

# 对某个fireworks重新计算
lpad rerun_fws -i 3
lpad rerun_fws -s FIZZLED



# 查看firework 
lpad get_fws -h
lpad get_fws
lpad get_fws -i 3
lpad get_fws -s FIZZLED
lpad get_fws -s FIZZLED -m 5
lpad get_fws -s FIZZLED -d more

# 查看workflow及其所有的fireworks
lpad get_wflows -h
lpad get_wflows
lpad get_wflows -i 1
# 使用-t参数需要安装prettytable package， pip install prettytable 
lpad get_wflows -s FIZZLED -t -m 5
lpad get_wflows -s FIZZLED -d more

# 以下的两个命令不推荐使用
# 重设lpad，所有lpad中的fireworks都会被删除
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
# 指定提交任务的数量
qlaunch rapidfire --nlaunches 5
```


---

### 使用 tips

- 用 python 脚本生成 workflows 的 fireworks 后，需要用 qlaunch 相关命令将 fireworks 提交到队列系统中，对于只有一个 firework 的 workflows（如弛豫和静态计算），若共生成了**N 个 fireworks**，`qlaunch rapidfire --nlaunches N` 即可（体系较小时，N 可缩减成 N/2 等）；
- 对于有多个 fireworks（如 M 个）的 workflows（如弹性常数计算），可以先提前了解这些多个 fireworks 之间的逻辑关系，若共有**N 个 workflows**，可先 `qlaunch rapidfire --nlaunches N`，N 个中有部分 fireworks（如 X 个）计算完成后，可适当再 `qlaunch rapidfire --nlaunches X*(M-1)`，进行该 workflow 其余部分 fireworks 的计算，一定程度上可以控制计算成本（虽然可能需要时不时查看 fireworks 的计算完成情况）。
- **不建议直接 `qlaunch rapidfire`**。



---

## 案例

### 测试

WIP…


---

### 弛豫计算

WIP…


---

### 静态计算

WIP…


---

### 弹性常数计算

WIP…



---

## MongoDB Compass 使用

### 连接数据库

- New connection - Advanced Connection Options - General: Connection String Scheme: mongodb: 填写 Host - Authentication: Authentication Method: Username/Password: 填写 Username、Password 和 Database，Authentication Mechanism 选择 Default


MONGOSH 使用

---


mongodb 中的 atomate documet 数据无法直接全部写入到 json 文件中
- 其 key 和 dict 涉及到 str 均使用单引号；
- json 文件不识别 bool 变量？


```json
'_id': ObjectId('62dbb72c531c489b7a006879')
```


mongodb 中的结构用以下方法获取较合适（将结构 dict 转成单独的 json 文件）
```python
struct = Structure.from_dict()
```



`gibbs_tasks` collection 中的 document 的 keys
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

弛豫 collection 中的 document 的 keys
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

>“calcs_reversed” key 对应的值（还需添加 `[0]`）含大部分同级下的 keys 的值信息

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


弹性性质分析 elasticity collection 中的 document 的 keys
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



```json
{
  // 课题组服务器只能填写纯数字的 host port 形式
  // MongoDB Compass 的登录相关信息也只能填该形式
  "host": "202.121.180.16",
  "port": 27017,
  // 学校超算可以填字符串的 host port 形式
  "host": "proxy.pi.sjtu.edu.cn",
  "port": 37017,
}
```


master db.json 问题：host 只能写数字的形式，siyuan 可以写字符串的形式
```bash
  File "/home/yangsl/src/miniconda3/envs/atomate_env/lib/python3.11/site-packages/pymongo/topology.py", line 269, in _select_servers_loop
    raise ServerSelectionTimeoutError(
pymongo.errors.ServerSelectionTimeoutError: proxy.pi.sjtu.edu.cn:37017: [Errno -2] Name or service not known, Timeout: 30s, Topology Description: <TopologyDescription id: 653cc2a8f1b06ed5cd32f2d0, topology_type: Unknown, servers: [<ServerDescription ('proxy.pi.sjtu.edu.cn', 37017) server_type: Unknown, rtt: None, error=AutoReconnect('proxy.pi.sjtu.edu.cn:37017: [Errno -2] Name or service not known')>]>
```


MongoDB 数据库连接失败（数据库服务未启动）

```bash
getaddrinfo ENOTFOUND
```

```bash
Connection failed: 202.121.180.16:27017: [Errno 111] Connection refused, Timeout: 30s, Topology Description: <TopologyDescription id: 659a430b861c320565200565, topology_type: Unknown, servers: [<ServerDescription ('202.121.180.16', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('202.121.180.16:27017: [Errno 111] Connection refused')>]>
```

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401091527481.png)

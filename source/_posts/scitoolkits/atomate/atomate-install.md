---
title: atomate 安装
top: true
pin: true
cover:
toc: true
mathjax: true
math: true
summary: atomate 安装
description: atomate 安装
tags:
  - 高通量
  - atomate
categories:
  - 科研工具
  - atomate
date: 2023-06-18 18:30:30
abbrlink: 120738
password:
sticky: "99"
---

# atomate 安装

## 安装

- atomate 安装：[Installing atomate — atomate 1.0.3 documentation](https://atomate.org/installation.html)
- **必要条件**：VASP 计算软件与 MongoDB 数据库账号
- [pymatgen](https://pymatgen.org/)：输入文件生成，输出文件的数据提取与分析
- [custodian](http://materialsproject.github.io/custodian/)：运行计算代码（VASP），执行错误检查与纠正
- [FireWorks](https://materialsproject.github.io/fireworks/)：设计、管理、执行 workflow


---

### 安装流程

- 使用 conda 创建 Python 虚拟环境，如 atomate_env（名字任意），安装 atomate 包（会自动安装 pymatgen custodian 和 FireWorks 依赖 packages）

- pymatgen 和 custodian 包更新频率相比 atomate 和 FireWorks 要高很多

- 当一个 Python 虚拟环境使用了很久且修改过相关包中的模块源代码，不建议单独升级某个包，有可能会破坏包之间的依赖关系

```bash
pip install atomate

pip install -U pymatgen custodian

```


---

### 配置文件

- atomate 标准 config 配置文件参考：[standard\_config](https://github.com/hackingmaterials/atomate/tree/main/atomate/vasp/examples/standard_config)

- 配置文件内容中涉及到路径填写时，需填写绝对路径，不可使用相对路径或 `$HOME` 等环境变量（**否则会报错，重要提醒！！！**）

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

- `db.json` 文件内容：连接 MongoDB 数据库（注：除了 port 条目（entry）的 value 是整数；其他都是字符串，且条目及对应的 value 值都应用双引号）

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

- `my_qadapter.yaml` 文件内容：配置队列系统；当作业提交到队列系统时，会自动生成 Slurm 或 PBS 提交脚本文件

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

```bash
_fw_q_type      # 调度系统类型，如 SLURM PBS 等
queue           # 队列名称；如 Master 服务器中的 CLUSTER 队列
walltime        # 作业最长运行时间
```

注：若无法提交到队列系统，rocket_launch 可进行以下修改：

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

若 atomate 环境有多个，可进行如下设置（可使用 `$HOME` 等变量；切换 atomate 环境后，`source` 使其生效）：

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
psp_dir/POT_GGA_PAW_PBE/POTCAR.XXX
# 形式 2 元素 POTCAR 按元素分类在子目录下
psp_dir/POT_GGA_PAW_PBE/XXX/POTCAR
```

注：若 `<psp_dir>` 赝势目录下没有 `POT_GGA_PAW_PBE` 名称目录，可设置软链接：

```bash
ln -s PBE_folder POT_GGA_PAW_PBE
```



---

## 相关问题

- custodian 版本过高出现的报错（custodian 2023.3.10 版本以上，运行 atomate 会出错；**现已解决**）

```bash
    from custodian.vasp.handlers import (
ImportError: cannot import name 'MaxForceErrorHandler' from 'custodian.vasp.handlers' (/home/yslarch/src/miniconda3/lib/python3.10/site-packages/custodian/vasp/handlers.py)
```

- 配置文件中的 db.json 路径没有设置正确：**db.json 的文件路径需设置为绝对路径**

```bash
ValueError: Could not get next FW id! If you have not yet initialized the database, please do so by performing a database reset (e.g., lpad reset)
```

- 赝势路径或赝势目录结构没有设置正确：**参照上节中赝势路径和赝势目录结构设置**

```bash
OSError: You do not have the right POTCAR with functional PBE and label Nb_pv in your VASP_PSP_DIR. Paths tried: ['/home/xxx/src/POT/PAW_PBE/POT_GGA_PAW_PBE/POTCAR.Nb_pv', '/home/xxx/src/POT/PAW_PBE/POT_GGA_PAW_PBE/Nb_pv/POTCAR']
```

- 没有创建 logs 目录：创建 config 目录的同时创建 logs 目录

```bash
FileNotFoundError: [Errno 2] No such file or directory: 'path/atomate/logs/launchpad-debug.log'

During handling of the above exception, another exception occurred:

  File "conda_path/envs/atomate_nbsi/lib/python3.11/site-packages/fireworks/scripts/lpad_run.py", line 132, in get_lp
    f"FireWorks was not able to connect to MongoDB at {lp.host}:{lp.port}. Is the server running? "
                                                       ^^
UnboundLocalError: cannot access local variable 'lp' where it is not associated with a value
```

- 未添加 `FW_CONFIG_FILE` 环境变量

```bash
ValueError: Fireworks was not able to connect to MongoDB.
```

- 不生成 VASP 计算输入文件，只生成.err .out（空文件）和 FW_submit.script 文件，job 处于不断提交 - kill - 再提交的循环
    - 解决方法：**这是自己遇到过的一个特殊情况**。自己安装过 `zsh`，且将 `zsh` 加入到 `~/.bash_profile` 中使登录服务器便切换到 zsh，最终导致上述问题出现（发现的原因是该问题出现后只有这个新变量因素）。将 `~/.bash_profile` 中与 `zsh` 相关的内容注释掉，问题可得到解决

---
title: 最新 atomate 安装
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: 最新 atomate 安装
description: 最新 atomate 安装
tags:
  - 高通量
  - atomate
categories:
  - 科研工具
date: 2024-11-12 17:37:45
abbrlink: 543717
password:
sticky: "99"
---

# 最新 atomate 安装

截至 2024.11.12，最新的 atomate 及其依赖包版本分别为

```bash
# 包          # 版本          # 日期
atomate       1.1.0          2023.08.26
pymatgen      2024.10.29     2024.10.29
custodian     v2024.10.16    2024.10.16
firework      2.0.3          2021.03.12
```



---

## 相关问题

- 使用 lpad 命令时，出现如下报错：
    - 参考：[AttributeError: "safe\_load()" has been removed · Issue #531 · materialsproject/fireworks · GitHub](https://github.com/materialsproject/fireworks/issues/531)
    - firework 的最新 Release 版本为 2021 年的，很老；GitHub 中的 fireworks 源码有对该问题进行解决，下载源码之后 `python setup.py install` 重新安装该包；或降版本 `ruamel.yaml <0.18.0`

```bash
  File "/path/env/lib/python3.11/site-packages/ruamel/yaml/main.py", line 1039, in error_deprecation
    raise AttributeError(s, name=None)
AttributeError:
"safe_load()" has been removed, use

  yaml = YAML(typ='safe', pure=True)
  yaml.load(...)

instead of file "path/env/lib/python3.11/site-packages/fireworks/utilities/fw_serializers.py", line 256

            dct = yaml.safe_load(f_str)
```

- 使用 Python 代码生成 workflow，并添加到 lpad 中，出现 `cannot encode object: True, of type: <class 'numpy.bool'>` 报错：
    - 参考：[bson.errors.InvalidDocument: cannot encode object: True, of type: \<class 'numpy.bool\_'\> · Issue #522 · materialsproject/fireworks · GitHub](https://github.com/materialsproject/fireworks/issues/522)

```python
# 生成 wf(workflow) 后，检查 metadata dict 中的值类型
for key, val in wf.metadata.items():
    print(f"{key}: {type(val)}")

# output:
"""
structure: <class 'dict'>
nsites: <class 'int'>
elements: <class 'list'>
nelements: <class 'int'>
formula: <class 'str'>
formula_pretty: <class 'str'>
formula_reduced_abc: <class 'str'>
formula_anonymous: <class 'str'>
chemsys: <class 'str'>
is_ordered: <class 'bool'>
is_valid: <class 'numpy.bool_'>
"""

# 若存在 <class 'numpy.bool'>，将其转换成 bool 类型
# 如 key 为 "is_valid"
wf.metadata[key] = bool(wf.metadata[key])
```

- `my_qadapter.yaml` 中的 `walltime` 参数会转换成秒的整数，不符合 Slurm 脚本规范
    - 可注释该参数

```bash
# my_qadapter.yaml 中
walltime: 24:00:00

# Slurm 脚本中；不符合规范
#SBATCH --time=86400
```

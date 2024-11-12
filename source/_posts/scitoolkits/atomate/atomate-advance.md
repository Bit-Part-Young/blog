---
title: atomate 进阶使用
top: true
cover:
toc: true
mathjax: true
summary: atomate 进阶使用
description: atomate 进阶使用
tags:
  - atomate
  - 高通量
categories:
  - 科研工具
date: 2023-07-27 10:42:30
abbrlink: 420310
password:
---

# atomate 进阶使用

ml-atomate：[GitHub - takahashi-akira-36m/ml\_atomate: Machine learning-assisted Atomate code for autonomous computational materials screening.](https://github.com/takahashi-akira-36m/ml_atomate)


以下两段代码来自 MP Workshop 2021 05_automated_dft lesson（写成 atomate basic 示例代码）

```python
from atomate.vasp.workflows.presets.core import wf_structure_optimization, wf_bandstructure

# 生成 workflow object
so_wf = wf_structure_optimization(structure=si)
print(so_wf)
print(so_wf.as_dict())
# Workflow object: (fw_ids: odict_keys([-1]) , name: Si)

bs_wf = wf_bandstructure(structure=si)
print(bs_wf)
# Workflow object: (fw_ids: odict_keys([-2, -3, -4, -5]) , name: Si)
```


```python
from fireworks.core.launchpad import LaunchPad

lpad = LaunchPad.auto_load()
lpad.add_wf(wf)

# 查看 firework id 对应的 workflow status
lpad.get_wf_summary_dict(fw_id=1)

lpad.get_wf_ids()
lpad.get_fw_dict_by_id()
lpad.defuse_wf()

# 示例
{
    "state": "READY",
    "name": "Si",
    "created_on": datetime.datetime(2021, 7, 29, 19, 34, 11, 524000),
    "updated_on": datetime.datetime(2021, 7, 29, 19, 34, 11, 524000),
    "states": OrderedDict([("Si-structure optimization--1", "READY")]),
    "launch_dirs": OrderedDict([("Si-structure optimization--1", [])]),
}
```


```python
# OptimizeFW firework 中的 firetasks
<class 'atomate.vasp.firetasks.write_inputs.WriteVaspFromIOSet'>
<class 'atomate.vasp.firetasks.run_calc.RunVaspCustodian'>
<class 'atomate.common.firetasks.glue_tasks.PassCalcLocs'>
<class 'atomate.vasp.firetasks.parse_outputs.VaspToDb'>
```


---

## 使用

- 预定义 workflow yaml 的文件路径：`atomate/vasp/workflows/base/library`

- 预定义 firework 路径：`atomate/vasp/fireworks/core.py`

- atomate 源代码目录树（忽略 feff lammps qchem 目录）

```text
atomate
├── common
│   ├── firetasks
│   ├── __init__.py
│   └── powerups.py
├── __init__.py
├── utils
│   ├── database.py
│   ├── fileio.py
│   ├── __init__.py
│   ├── testing.py
│   └── utils.py
└── vasp
    ├── analysis
    ├── builders
    ├── config.py
    ├── database.py
    ├── drones.py
    ├── firetasks
    ├── fireworks
    ├── __init__.py
    ├── powerups.py
    ├── submission_filter.py
    ├── vasp_config.py
    ├── vasp_powerups.py
    └── workflows
```


---

### 通过 yaml 文件自定义、导入 workflow

- 参考：[https://atomate.org/workflow_yaml_reference.html](https://atomate.org/workflow_yaml_reference.html)

- yaml 文件示例 1：

```yaml
# MP 能带计算的工作流 yaml 文件

fireworks:
- fw: atomate.vasp.fireworks.core.OptimizeFW
- fw: atomate.vasp.fireworks.core.StaticFW
  params:
    parents: 0
- fw: atomate.vasp.fireworks.core.NonSCFUniformFW
  params:
    parents: 1
- fw: atomate.vasp.fireworks.core.NonSCFLineFW
  params:
    parents: 1
common_params:
  db_file: db.json
  $vasp_cmd: $HOME/opt/vasp
name: bandstructure
metadata:
  tag: testing_workflow
```

- yaml 文件示例 2：

```yaml
%%file opti.yaml  
fireworks:
# Relaxation for
- fw: atomate.vasp.fireworks.core.OptimizeFW
  override_default_vasp_params: # 覆写 INCAR 参数
    user_incar_settings:
        ISPIN: 2
```

- 相关模块及函数：

```python
from atomate.utils.utils import ...

get_wf_from_spec_dict()     # 通过 yaml 文件导入 workflow
get_meta_from_structure()   # 
get_fws_and_tasks           # 获取给定 workflow 的 fw_ids 和 task_ids


from monty.serialization import loadfn

loadfn()                  # 导入 yaml 文件
```


---

### 其他

- [ ] 理解 Fireworks & Custodian 中一些类和函数的作用

- [ ] 了解 atomate 中的 `env_chk()` 函数作用

- INCAR 等输入文件与对应的.org 文件内容无区别（绝大部分）

- atomate fw 计算时长达到规定的 walltime 时限，该 fw 会视为 COMPLETED，还是 RUNNING（视为 RUNNING）

- 在同一目录下第二次 运行 `qlaunch rapidfire` 提交任务，会在已有的 block 目录下生成计算任务的子目录

- 一些参数含义

```python
# atomate/vasp/workflows/presets/core.py
# pymatgen/io/vasp/sets.py
user_incar_settings    # uis
vasp_input_set         # vis
```

---

- 层错能计算：[https://github.com/willtu/gsfe_workflow](https://github.com/willtu/gsfe_workflow)

```python
from atomate.vasp.workflows.base.neb import get_wf_neb_from_endpoints
```

---

- 查看 VASP 计算数据存储在 MongoDB 中的 document 的所有 keys

```python
from atomate.vasp.drones import VaspDrone

VaspDrone.schema
```

---

- custodian 中已定义的 error 信息

```python
error_msgs = {
        'algo_tet': ['ALGO=A and IALGO=5X tend to fail'], 
        'amin': ['One of the lattice vectors is very long (>50 A), but AMIN'], 
        'bravais': ['Inconsistent Bravais lattice'], 
        'brions': ['BRIONS problems: POTIM should be increased'], 
        'brmix': ['BRMIX: very serious problems'], 
        'coef': ['while reading plane', 'while reading WAVECAR'], 
        'dentet': ['DENTET'], 
        'dfpt_ncore': ['PEAD routines do not work for NCORE', 'remove the tag NPAR from the INCAR file'], 
        'edddav': ['Error EDDDAV: Call to ZHEGV failed'], 
        'eddrmm': ['WARNING in EDDRMM: call to ZHEGV failed'], 
        'elf_kpar': ['ELF: KPAR>1 not implemented'], 
        'elf_ncl': ['WARNING: ELF not implemented for non collinear case'], 
        'grad_not_orth': ['EDWAV: internal error, the gradient is not orthogonal'], 
        'hnform': ['HNFORM: k-point generating'], 
        'incorrect_shift': ['Could not get correct shifts'], 
        'inv_rot_mat': ['rotation matrix was not found (increase SYMPREC)'], 
        'nbands_not_sufficient': ['number of bands is not sufficient'], 
        'nicht_konv': ['ERROR: SBESSELITER : nicht konvergent'], 
        'point_group': ['group operation missing'], 
        'posmap': ['POSMAP'], 'pricel': ['internal error in subroutine PRICEL'], 
        'pssyevx': ['ERROR in subspace rotation PSSYEVX'], 
        'read_error': ['Error reading item', 'Error code was IERR= 5'], 
        'real_optlay': ['REAL_OPTLAY: internal error', 'REAL_OPT: internal ERROR'], 
        'rhosyg': ['RHOSYG'], 'rot_matrix': ['Found some non-integer element in rotation matrix', 'SGRCON'], 
        'rspher': ['ERROR RSPHER'], 'set_core_wf': ['internal error in SET_CORE_WF'], 
        'subspacematrix': ['WARNING: Sub-Space-Matrix is not hermitian in DAV'], 
        'symprec_noise': ['determination of the symmetry of your systems shows a strong'], 
        'tet': ['Tetrahedron method fails', 'tetrahedron method fails', 'Fatal error detecting k-mesh', 'Fatal error: unable to match k-point', 'Routine TETIRR needs special values', 'Tetrahedron method fails (number of k-points < 4)', 'BZINTS'], 
        'tetirr': ['Routine TETIRR needs special values'], 
        'too_few_bands': ['TOO FEW BANDS'], 
        'triple_product': ['ERROR: the triple product of the basis vectors'], 
        'zbrent': ['ZBRENT: fatal internal in', 'ZBRENT: fatal error in bracketing'], 
        'zheev': ['ERROR EDDIAG: Call to routine ZHEEV failed!'], 
        'zpotrf': ['LAPACK: Routine ZPOTRF failed', 'Routine ZPOTRF ZTRTRI']
}
```

---

- lpad 命令行中的内容

```python
#!/XXX/envs/atomate_env/bin/python3.11
# -*- coding: utf-8 -*-
import re
import sys
from fireworks.scripts.lpad_run import lpad
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(lpad())
```

- qlaunch 命令行中的内容

```python
#!/XXX/envs/atomate_env/bin/python3.11
# -*- coding: utf-8 -*-
import re
import sys
from fireworks.scripts.qlaunch_run import qlaunch
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(qlaunch())
```



---

## 相关问题

- 部分 workflow 有 VASP 计算过程，但无法将计算数据保存到 MongoDB 中（个人理解）

```bash
custodian.custodian.ReturnCodeError: Job return code is 174. Terminating…
```

解决方法：[Check returncode to raise CustodianError() leading some trouble · Issue #41 · materialsproject/custodian · GitHub](https://github.com/materialsproject/custodian/issues/41)

源代码修改：将 `custodian/custodian.py` 中 `Custodian` 类的 `terminate_on_nonzero_returncode` 参数值改成 `False`。

```python
class Custodian:
    ...
    def __init__(
        self,
        ...
        # modified by ysl
        # terminate_on_nonzero_returncode=True,
        terminate_on_nonzero_returncode=False,
    ):
```

---

- 涉及到含元素 Si 的 atomate 计算（atomate 1.1.0 版本），会出现如下报错（2023.10.12）

```bash
Traceback (most recent call last):
  File "/dssg/home/acct-mseklt/mseklt/yangsl/scripts/atomate-test/examples/atomate_test_NbSi.py", line 11, in <module>
    lpad.add_wf(wf)
    return _op_msg_uncompressed(flags, command, identifier, docs, opts)
bson.errors.InvalidDocument: cannot encode object: True, of type: <class 'numpy.bool_'>
```

atomate 版本为 1.1.0，但在 mongodb 的数据库中 documentation 中的 schema.version 版本仍显示是 1.0.3

---

修改 workflow 的 db_file 路径需要修改 firework 中的相关定义



---

## 常用模块

### atomate.utilities.visualize

可视化 workflow

```python
from fireworks.utilities.visualize import plot_wf
from atomate.vasp.workflows.presets.core import wf_bandstructure
from pymatgen.core.structure import Structure

structure = Structure.from_file("POSCAR")
wf = wf_bandstructure(structure)

plot_wf(wf)
```

示例：能带计算 workflow 中的 fireworks

![wf_bandstructure.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307151935728.png)


---

### atomate.common.powerups

>[Tags are not passed to individual fireworks in QChem workflow · Issue #576 · hackingmaterials/atomate · GitHub](https://github.com/hackingmaterials/atomate/issues/576)

- `add_namefile()` 函数：每个 firework 计算目录会写入 `FW–<fw.name>-<fw.fw_id>` 格式的空文件，以更好地查看当前目录是什么具体的计算任务内容，如在 `block*` 目录下执行命令：`ls -l launch*/FW–*`

- `add_tags()` 函数：给 workflow 的所有 fireworks 添加 tag，会在 MongoDB 中的 document 中添加 tags，以便筛选；以更好地识别计算数据是哪个具体的 research project

```python
from atomate.common.powerups import ...


add_namefile()
add_tags()
```


---

### atomate.vasp.fireworks

atomate 中预设的 VASP firework
```python
from atomate.vasp.fireworks.core import ...

StaticFW
OptimizeFW
```


---

### atomate.vasp.workflows.presets

- `atomate/vasp/workflows/presets`: preset（预设）workflows，通常只需提供构型
- `atomate/vasp/workflows/base`: raw workflows，需要更多参数设置

用于 elastic tensor 的标准预设 workflow 使用了许多超出确定弹性张量所需的计算，这样可以得到一个高质量的张量，其中一些数值噪声会在重复计算中被消除。也可以生成 minimal 的 workflow，它既不使用更昂贵的 DFT 参数，也不进行扩展计算。使用该 workflow 生成的张量通常不太精确，但对于具有大量对称性的简单半导体通常足够使用。（摘自 workshop 2019）

- [ ] 参数 `c` 的含义是什么，如何写

```python
from atomate.vasp.workflows.presets.core import ...

# 从 atomate/vasp/workflows/base/library/ 目录下的 yaml 文件中生成 workflow
# 调用的是 atomate.utils.utils 中的 get_wf_from_spec_dict
get_wf(structure, wf_filename)

# 能带计算相关
wf_bandstructure(structure, c=None)
wf_bandstructure_no_opt(structure, c=None)
wf_bandstructure_hse(structure, c=None)
wf_bandstructure_plus_hse(structure, gap_only=True, c=None)
wf_bandstructure_plus_boltztrap(structure, c=None)

# 静态计算
wf_static(structure, c=None)

# 结构弛豫
wf_structure_optimization(structure, c=None)

# 介电常数相关
wf_dielectric_constant(structure, c=None)
wf_dielectric_constant_no_opt(structure, c=None)

# 压电常数
wf_piezoelectric_constant(structure, c=None)

# 弹性常数计算相关
wf_elastic_constant(structure, c=None, order=2, sym_reduce=False)
wf_elastic_constant_minimal(structure, c=None, order=2, sym_reduce=True)

# ...
wf_nmr(structure, c=None)

# ...
wf_raman_spectra(structure, c=None)

# 吉布斯自由能计算
wf_gibbs_free_energy(structure, c=None)

# 体模量 B
wf_bulk_modulus(structure, c=None)

# 热膨胀系数
wf_thermal_expansion(structure, c=None)

# NEB 计算
wf_nudged_elastic_band(structures, parent, c=None)
```


---

### atomate.vasp.powerups

>[Customize KPOINTs without using user\_kpoints\_settings (dict) - Atomate - Materials Science Community Discourse](https://matsci.org/t/customize-kpoints-without-using-user-kpoints-settings-dict/35309)

- 修改 VASP workflow 计算中的输入参数设置

```python
from atomate.vasp.powerups import ...

# 具体 modify_incar_params 格式要求可查看
# atomate/vasp/firetasks/write_inputs.py 中的 ModifyIncar 类
add_modify_incar()

add_modify_kpoints()       # 查看 ModifyKpoints 类

add_modify_potcar()        # 查看 ModifyPotcar 类

clear_modify()
```

示例

```python
modified_wf = add_modify_incar(
    wf,
    modify_incar_params={
        "incar_update": {
            "EDIFFG": -0.05,
        },
    },
    fw_name_constraint="optimization",
)

modified_wf = add_modify_potcar(
    orig_wf,
    modify_potcar_params={
        "potcar_symbols": {
            "W": "W_sv",
        },
    },
    fw_name_constraint=None,
)

# Gamma 无法变成 Monkhorst？
kpoints_update_dict = {
    "comment": "Automatic kpoint scheme",
    "num_kpts": 0,
    "generation_style": "Monkhorst",
    "kpts": [[10, 10, 10]],
    "kpts_shift": [0.0, 0.0, 0.0],
    "kpts_weights": None,
    "coord_type": None,
    "labels": None,
    "tet_number": 0,
    "tet_weight": 0,
    "tet_connections": None,
}
```

---

- `use_fake_vasp()` 函数：不实际运行，模拟运行 workflow

```python
from fireworks import LaunchPad
from atomate.vasp.powerups import use_fake_vasp
from atomate.vasp.workflows import wf_bandstructure
from pymatgen.core.structure import Structure


struc = Structure.from_file("POSCAR")
wf = wf_bandstructure(struc)

# 是否要将目录中的文件分成inputs和outputs？workshop中的进行了分类
path = ...
ref_dirs = {
        "Si-structure optimization": f"{path}/Si_structure_opt",
        "Si-static": f"{path}/Si_static",
        "Si-nscf uniform": f"{path}/Si_nscf_line",
        "Si-nscf line": f"{path}/Si_nscf_uniform"
        }

wf = use_fake_vasp(
        wf, 
        ref_dirs,
        params_to_check=None,
        check_incar=True,
        check_kpoints=True,
        check_poscar=True,
        check_potcar=True,
        clear_inputs=True
      )

lp = LaunchPad.auto_load()
lp.add_wf(wf)

# 1为fw_id
lp.get_wf_summary_dict(1)
```

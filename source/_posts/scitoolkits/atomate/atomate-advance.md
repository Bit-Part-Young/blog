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
  - atomate
date: 2023-07-27 10:42:30
abbrlink: 420310
password:
---

# atomate 进阶使用

结合 VASP + phono3py 的 atomate 工作流：[GitHub - MatFrontier/ph3pywf](https://github.com/MatFrontier/ph3pywf)

ml-atomate：[GitHub - takahashi-akira-36m/ml\_atomate: Machine learning-assisted Atomate code for autonomous computational materials screening.](https://github.com/takahashi-akira-36m/ml_atomate)

[atomate. utils package](https://atomate.org/atomate.utils.html](https://atomate.org/atomate.utils.html))

[Customizing workflows — atomate 1.0.3 documentation](https://atomate.org/customizing_workflows.html)


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

- 参考：
    - [https://atomate.org/workflow_yaml_reference.html](https://atomate.org/workflow_yaml_reference.html)
    - [How to write a parameters to YAML file denpends on workflow - Atomate - Materials Science Community Discourse](https://matsci.org/t/how-to-write-a-parameters-to-yaml-file-denpends-on-workflow/37337)

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
# file opti.yaml
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
```


---

### 其他

- [ ] 理解 Fireworks & Custodian 中一些类和函数的作用

- [ ] 了解 atomate 中的 `env_chk()` 函数作用

- INCAR 等输入文件与对应的.org 文件内容无区别（绝大部分）

- atomate fw 计算时长达到规定的 walltime 时限，该 fw 会视为 COMPLETED，还是 RUNNING（视为 RUNNING）

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

- [Tags are not passed to individual fireworks in QChem workflow · Issue #576 · hackingmaterials/atomate · GitHub](https://github.com/hackingmaterials/atomate/issues/576)

- `add_namefile()` 函数：每个 firework 计算目录会写入 `FW–<fw.name>-<fw.fw_id>` 格式的空文件，以更好地查看当前目录是什么具体的计算任务内容，如在 `block*` 目录下执行命令：`ls -l launch*/FW–*`

- `add_tags()` 函数：给 workflow 的所有 fireworks 添加 tag，会在 MongoDB 中的 document 中添加 tags，以便筛选；以更好地识别计算数据是哪个具体的 research project

```python
from atomate.common.powerups import ...

# 相关函数
add_namefile()         # 给 firework 添加 name
add_tags()             # 给 namefile 添加 tag
```

![Untitled 10.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202411130850488.png)

![Untitled 11.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202411130852831.png)



---

### atomate.vasp.fireworks

- atomate 中预设的 VASP firework

- `double_relaxation_run` 的含义为 `Returns a list of two jobs corresponding to an AFLOW style double relaxation run`

```python
from atomate.vasp.fireworks.core import ...

StaticFW                 # 静态计算
OptimizeFW               # 结构优化
ScanOptimizeFW           # 使用 SCAN metaGGA functional 结构优化
TransmuterFW             # 弹性常数计算变形阶段用到


# OptimizeFW 类参数
job_type                 # 默认值为 "double_relaxation_run"，可选值 "normal"、"full_opt_run"、"neb"；其他 FW 无该参数
```


---

### atomate.vasp.workflows.presets

- `atomate/vasp/workflows/presets`: preset（预设）workflows，通常只需提供构型

- `atomate/vasp/workflows/base`: raw workflows，需要更多参数设置

- `wf_elastic_constant()` 和 `wf_elastic_constant_minimal()` 之间的区别：用于 elastic tensor 的标准预设 workflow 使用了许多超出确定弹性张量所需的计算，这样可以得到一个高质量的张量，其中一些数值噪声会在重复计算中被消除。也可以生成 minimal 的 workflow，它既不使用更昂贵的 DFT 参数，也不进行扩展计算。使用该 workflow 生成的张量通常不太精确，但对于具有大量对称性的简单半导体通常足够使用。（摘自 workshop 2019）

- 参数 `c` （Config dict，作为 `atomate.vasp.powerups` 模块中的 `add_common_powerups()` 函数参数）

```python
# add_common_powerups() 支持以下 4 个 key
"ADD_NAMEFILE"
"SCRATCH_DIR"
"ADD_MODIFY_INCAR"
"GAMMA_VASP_CMD"

"USER_INCAR_SETTINGS"    # 不在下面的路径中

# atomate.vasp.workflows.presets.core 中定义的 wf 函数常用到的 Config dict
"VASP_CMD"
"ADD_WF_METADATA"
"DB_FILE"

# 这些 Config dict 默认值所在的文件路径
atomate/vasp/config.py
```

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

- K 点默认参数设置

```python
reciprocal_density: 64     # 弛豫
reciprocal_density: 100    # 静态 
grid_density: 7000         # 弹性常数计算；第一步弛豫、ISIF = 2 弛豫部分
```


---

### atomate.vasp.powerups

- 参考：[Customize KPOINTs without using user\_kpoints\_settings (dict) - Atomate - Materials Science Community Discourse](https://matsci.org/t/customize-kpoints-without-using-user-kpoints-settings-dict/35309)

- 修改 workflow 中的 VASP 计算输入参数设置

```python
from atomate.vasp.powerups import ...

# 具体 modify_incar_params 格式要求可查看
# atomate/vasp/firetasks/write_inputs.py 中的 ModifyIncar 类
add_modify_incar()

add_modify_kpoints()       # 查看 ModifyKpoints 类

add_modify_potcar()        # 查看 ModifyPotcar 类

clear_modify()

use_fake_vasp()           # 不实际进行运算，主要起演示 atomate 计算流程作用

use_no_vasp()


# 示例
wf = add_modify_incar(
    wf,
    modify_incar_params={
        "incar_update": {
            "EDIFFG": -0.05,
        },
    },
    fw_name_constraint="optimization",    # 施加约束，使其只对特定的 firework 起作用
)

wf = add_modify_potcar(
    wf,
    modify_potcar_params={
        "potcar_symbols": {
            "W": "W_sv",
        },
    },
    fw_name_constraint=None,
)

wf = add_modify_kpoints(
    wf,
    modify_kpoints_params={
        "kpoints_update": {
            "kpts": [[10, 10, 10]],
        },
    },
)
```

---

- `use_fake_vasp()` 函数：不实际运行，模拟运行 workflow

```python
from fireworks import LaunchPad
from atomate.vasp.powerups import use_fake_vasp
from atomate.vasp.workflows import wf_bandstructure
from pymatgen.core.structure import Structure

structure = Structure.from_file("POSCAR")
wf = wf_bandstructure(structure)

# 是否要将目录中的文件分成 inputs 和 outputs？workshop 中的进行了分类
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

# 1 为 fw_id
lp.get_wf_summary_dict(1)
```

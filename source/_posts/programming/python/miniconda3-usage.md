---
title: Miniconda3 安装与使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Miniconda3 安装与使用
description: Miniconda3 安装与使用
tags:
  - Miniconda3
categories:
  - 编程
  - Python
date: 2023-06-06 15:30:30
abbrlink: 437116
password:
---

# Miniconda3 安装与使用

- Miniconda3： Python 环境管理工具，轻量级 Anaconda 发行版；与完整的 Anaconda 发行版相比，Miniconda 只包含了最基本的组件，体积小，推荐在课题组服务器中安装与使用。

- 参考资料
	- [Conda备忘清单 & conda cheatsheet & Quick Reference](https://wangchujiang.com/reference/docs/conda.html)



---

## 安装与卸载

### 安装

```bash
# Linux
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh

# macOS
brew install miniconda
# or
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh

bash Miniconda3-latest-Linux-x86_64.sh
```

- 按 `Enter` 键、输入 `yes`；自定义设置 Miniconda3 安装路径，如：`~/src/miniconda3`。快结束安装时，会提示 `Do you wish the installer to initialize Miniconda3` 是否 `conda initialize`，输入 `yes`，其会在 `~/.bashrc` 或 `~/.zshrc` 添加以下内容，以后每次登录可直接使用 `conda`。

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/ysl/src/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/ysl/src/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/ysl/src/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/ysl/src/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

```

- 安装完成后，登录会默认激活 base 环境，可通过以下命令取消（建议取消）。

```bash
conda config --set auto_activate_base false
```

- 超算平台可直接 `module load miniconda`，运行 `conda init bash` 会在 `~/.bashrc` 中添加 `conda initialize` 内容。


---

### 换源

- conda 换源
	- conda 默认使用官方源（conda-forge）进行 package 安装和更新，但经常下载速度较慢。可以通过更换国内镜像源（如 [清华镜像源](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)）加速下载。
	- 有些 package 及其最新版本只能通过官方源安装（如 compilers），因此有时需留意某些 package 的安装要求。

---

备份 `~/.condarc`，在 `~/.condarc` 中添加以下内容：
```shell
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

conda 设置相关命令：
```bash
# 查看 conda 相关设置
conda config --show
conda config --show-sources
conda clean -i  # 清除索引缓存

# 获取指定配置
conda config --set key value
conda config --add key value  # 添加
conda config --remove key value  # 移除
conda config --add channels <CHANNELNAME>  # 添加 conda 源
conda config --remove channels <CHANNELNAME>  # 移除
```


---

- pip 换源：[pypi 清华镜像源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```bash 
# 临时使用
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

# 设为默认
python -m pip install -U pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```


---

### 卸载

- `rm -rf miniconda3`，将 `~/.bashrc` 或 `~/.zshrc` 中的 `conda initialize` 语句删除或注释，`source` 或重新登录使其生效。



---

## 使用

### conda 环境变量

写 shell 或 Python 相关脚本时可能会用到以下 conda 环境变量：

| 环境变量 | 说明 |
|:------------:|:------------:|
| `CONDA_DEFAULT_ENV` | 当前激活的虚拟环境的名称 |
| `CONDA_PREFIX` | 当前激活的虚拟环境的路径 |
| `CONDA_EXE` | conda 可执行文件路径 |
| `CONDA_PYTHON_EXE` | 当前激活的虚拟环境的 Python 可执行文件路径 |
| `CONDA_PROMPT_MODIFIER` | 在命令行提示符中显示的当前环境的信息。包含环境名称、环境类型等（如会输出 `(base)` 信息） |
| `CONDA_SHLVL` | 当前激活的 Conda 环境的嵌套深度。如果没有激活的环境，则为 0 |

---

### Miniconda3 目录结构

```text
miniconda3
├── bin/
├── compiler_compat/
├── condabin/
├── conda-meta/
├── envs/
├── etc/
├── include/
├── lib/
├── LICENSE.txt
├── licensing/
├── man/
├── sbin/
├── share/
├── shell/
├── ssl/
├── x86_64-conda_cos7-linux-gnu/
└── x86_64-conda-linux-gnu/
```

部分目录含义：

| 目录名称 | 说明 |
|:---------------:|:------:|
| `bin/` | 存储可执行文件 |
| `envs/` | 存储各个虚拟环境 |
| `pkgs/` | 存储下载的 package，以便在安装和更新时使用 |
| `condabin/` | 中的辅助脚本和可执行文件用于配置和管理 miniconda3 |
| `etc/` | 含配置文件，允许自定义和配置 miniconda3 的行为，`etc/profile.d/conda.sh` |
| `shell/` | 用于配置 Shell 提示符，提供有关当前环境和激活的环境的信息 |

---

`base` 之外的虚拟环境 packages 路径：
```shell
miniconda3/envs/<conda_env>/lib/pythonX.X/site-packages
# or
~/.conda/envs/<conda_env>/lib/pythonX.X/site-packages
```


---

### 常用 conda 命令

- 虚拟环境相关

```bash
# 创建虚拟环境
# 方式 1
conda create -n <ENVNAME> python=3.X
# 方式 2
conda env create -f conda-env.yml

# 查看已安装的虚拟环境
conda env list
conda info -e

# 激活环境
conda activate <ENVNAME>

# 退出环境
conda deactivate

# 删除虚拟环境
conda remove -n <ENVNAME> --all

# 重命名虚拟环境名称
conda rename -n <ENVNAME> <NEWENVNAME>

# 从已有环境克隆新环境
conda create --clone <ENVNAME> -n <NEW_ENVNAME>
```

- packages 相关

```bash
# 安装 package
conda install <package>

# 列出已安装 package
conda list

# 查看具体 package 信息
conda list <package>

# 更新 package
conda update <package>

# 搜索可用 package
conda search numpy
```

- 删除 pkgs 目录中的缓存的 packages（**清理空间常用**）
	- 安装 packages 时的缓存路径:`~/.conda/pkgs/`

```bash
conda clean -a

conda clean -p
# --dry-run 模拟运行，不实际删除
conda clean -p --dry-run
```


---

### 常用 pip 命令

- 安装 package

```bash
# PyPI 安装
pip install <package>
# 更新 package
pip install -U <package>

# 本地安装
pip install git+url
pip install .
pip install -r requirements.txt
# editable mode
pip install -e .
python setup.py install
python pip install ".[test]"

# 示例
git clone https://github.com/CederGroupHub/sparse-lm
cd sparselm
pip install .
```

- 常用 packages：多个 packages 一行命令安装可能出现报错，建议单个安装

```bash
pip install pymatgen ase pyxtal scikit-learn ipython ipykernel tldr
```

- 列出已安装 packages

```bash
pip freeze
```

- 查看具体 package 信息：该 `pip` 命令比 `conda list <package>` 命令更详细，可以查看 package 的版本、安装路径、依赖关系等信息

```bash
pip show <package>

# 示例
Name: scikit-learn
Version: 1.3.0
Summary: A set of python modules for machine learning and data mining
Home-page: http://scikit-learn.org
Author:
Author-email:
License: new BSD
Location: /home/yslarch/src/miniconda3/lib/python3.10/site-packages
Requires: joblib, numpy, scipy, threadpoolctl
Required-by:
```


---

### 用 venv 创建虚拟环境

- 使用 `venv` 创建轻量级 “虚拟环境”
- VSCode 的 Python 插件无法直接识别由 `venv` 生成的虚拟环境，需手动输入解释器路径

```bash
python -m venv venv  # 创建
source venv/bin/activate  # 激活
deactivate  # 退出
```


---

### uv

- [uv](https://github.com/astral-sh/uv)：快速安装 Python package

- 安装

```bash
# Linux macOS 安装/更新
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- 使用

```bash
uv venv                    # 创建虚拟环境 .venv/
source .venv/bin/activate  # 激活
deactivate                 # 取消

uv pip install <package>   # 安装 package；与 pip 基本一致
```



---

## 相关问题

### 虚拟环境使用

- 当有多种不同的程序，（如 atomate、sqsgen、scikit-learn 等），建议根据自身需求各自创建其虚拟环境使其互相隔离，而不是都装在 conda 的默认 base 环境，不要嫌切换环境麻烦，不同程序之间 package 之间的依赖不同，装在一起很容易出问题。

- base 环境可以装一些自己常用的 package（如个人常使用 pymatgen、ase 等）

- 给离线安装的 conda 环境（其环境名是路径）添加环境名

```bash
conda activate ~/src/deepmd-kit

# 添加符号链接
ln -s path/to/project path/to/miniconda3/envs/<env_name>

conda activate <env_name>
```

- Linux conda 当前用户创建的虚拟环境名消失，只有 root 的：`~/.zshrc` 中的 `conda init` 代码中的相关路径变成了 root 的，将其改回当前用户的路径

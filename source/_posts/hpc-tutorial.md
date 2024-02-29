---
title: 服务器、超算使用教程
top: true
pin: true
cover: false
toc: true
mathjax: true
math: true
summary: 服务器、超算使用教程
tags:
  - HPC
  - 服务器
categories:
  - 科研工具
date: 2023-06-04 18:30:30
abbrlink: 13796
password:
---

# 服务器、超算使用教程

## 服务器、超算介绍

### master

- linux 系统版本：Ubuntu 22.04；
- 无 root 权限；无法使用 apt、apt-get、dpkg、snap 命令安装软件程序；
- Slurm 任务调度系统；
- CPU：共 64 核；2 块 RTX 3090 GPU，显存 24G；调用 GPU 时只能一整块调用，显存自动分配；cpu 信息查看：`cat /proc/cpuinfo`。
- intel 套件：intel-oneapi 2022.1.0 版本；
- 总内存 512G；内存信息查看：`free -h` 或 `cat /proc/meminfo`；
- 较大体积的数据（master 本地或超算上的）可以放到 `${HOME}/storage` 中

---

master 上已安装的程序/软件（`cat /opt/bin/README` 查看）

```text
# Code                 Function
ave....................Get the averages of data columns in a file
bave...................Get the block averages of data columns in a file
binave.................Get the bin averages of data columns in a file
crysinfo...............Get the crystalline symmetry info for an xyz file
cumsum.................Get the cummulative sum of data columns in a file
d2p....................Dump2phonon, get dynamical matrix from a lammps trajectory file
dos2th.................Get thermal info from phonon DOSes.
dumpana................Analyze the lammps dump file
find-min-pos...........Find the location (line #) of a minimum value within a column data
find-val-pos...........Find the location of a given value within a column data
get-col-num............Get the column number of a word in the first line of the file.
getpot.................Get vasp potential for desired elements.
gsub...................Submit GPU jobs.
hist...................Get the histogram of a data file.
histjoin...............To join multiple files from hist.
latgen.................To generate the position file for selected crystals.
lmp....................LAMMPS
mathfun................To perform simple math calculations.
ovito..................To visualize atomic configurations.
phana..................To analyze binary file from fix-phonon.
posconv................To convert formats of pos files
run....................To find the locations of running jobs.
spave..................To get the spatial average from data columns in a file
submit.................To submit CPU jobs.
v6.gam.................vasp.6.3.0.gam
v6.ncl.................vasp.6.3.0.ncl
v6.std.................vasp.6.3.0.std
vacf...................To measure phonon DOS based on velocity-velocity autocorrelation function method
vasp...................vasp.5.4.4.std
vasp.5.gam.............vasp.5.4.4.gam
vasp.5.std.............vasp.5.4.4.std
vasp.6.gpu.............vasp.6.3.0.std.gpu (OpenACC)
vasp.6.gpu.gam.........vasp.6.3.0.gam.gpu
vasp_gam...............vasp.5.4.4.gam
vaspkit................Toolkit for vasp calculations.
vasp_std...............vasp.5.4.4.std
viscal.................To calculate shear viscosity based on Green-Kubo method
vmd....................To visualize md trajectories
```

>`/home/share` 目录，不同用户可将临时共享文件放此，所有用户可删除文件，但文件夹需其所有者才能删除，因此建议将文件夹进行打包压缩再放到 share 目录中。


---

### manager

- linux 系统版本：Ubuntu 16.04；
- 无 root 权限；无法使用 apt、apt-get、dpkg、snap 命令安装软件程序；
- PBS 任务调度系统；
- intel 套件：2015 版本（应该）；
- CPU：共 12 个节点（node1~11+manager；部分节点已坏），共 100 核。


---

### 超算

- linux 系统版本：Centos 7.7.1908(pi) 8.3.2011(思源一号)；
- 无 root 权限；无法使用 yum 命令安装软件程序；
- Slurm 任务调度系统；
- Pi、ARM、思源一号提交的任务在任一平台都可以看到；
- Pi 和 ARM 用的是相同的用户目录；
- Pi 的一些基础程序的版本比思源一号旧许多。
- 超算中的核有内存配比限制

>sylogin1 占用率高，比其他登录节点（2-5）卡，是超算断开连接，vim 使用卡顿的可能原因之一。思源的登录节点为随机分配，应尽量避免登录到 sylogin1。

---

VASP 赝势文件位置

```bash
# manager
/opt/.vasp_pot

# master
/work/backup/.vasp_pot/

# 以下不具有参考性，以自己的超算用户目录为准
# 思源一号 mseklt 用户目录
$HOME/.sjtu_mgi/.vasp.pot

# Pi mseklt 用户目录
$HOME/opt/VASP/VASP_PSP
```

>Pi 上的 VASP 赝势与思源和 manager 上的有些不同，相比之下，前面的不全。



---

## 服务器、超算登录

### SSH 登录

>[通过 SSH 登录集群 - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/login/sshlogin.html)

manager
```bash
ssh username@202.120.55.11 -p 312
```

master
```bash
ssh username@202.120.55.11 -p 313
```

思源一号
```bash
ssh username@sylogin.hpc.sjtu.edu.cn
```

Pi（cpu 队列）
```bash
ssh username@pilogin.hpc.sjtu.edu.cn
```

Pi（centos 队列）
```bash
ssh username@oldlogin.hpc.sjtu.edu.cn
```

ARM
```bash
ssh username@armlogin.hpc.sjtu.edu.cn
```

注：超算平台的 SSH 端口均为默认值 22；因此 `-p 22` 可省略。


---

### 终端 SSH 免密登录

- 无需输入用户名和密码即可登录，还可以作为服务器的别名来简化使用。免密登录需建立从远程主机（集群的登录节点）到本地主机的 SSH 信任关系。建立信任关系后，双方将通过 SSH 密钥对进行身份验证。

- 在本地主机上生成的 SSH 密钥对，输入以下命令，**持续 Enter 即可**；将在 `~/.ssh`（或 `C:\User\username\.ssh`） 路径下生成密钥对文件 `id_rsa` 和 `id_rsa.pub`；将 `id_rsa.pub` 的内容（注意字符之间只有一个空格，复制后需注意）添加到远程主机的 `~/.ssh/authorized_keys` 文件中。

```bash
ssh-keygen -t rsa
```

- 密钥对生成方式有 ssh-keygen 和 putty（ppk 格式，WinSCP 软件密钥验证需该格式），其中后者可通过 Mobaxterm 软件中 tool 工具中的 MobaKeyGen 来生成（在空白处乱按加快生成速度；将生成的公钥保存成 file.pub，私钥保存成 file.ppk）。

- 设置服务器别名：在 `~/.ssh/config`（或 `C:\User\username\.ssh\config`）设置：

```bash
Host alias
    HostName 
    User 
    Port 
    IdentityFile 
```

具体示例：

```bash
Host Manager
    HostName 202.120.55.11
    User username
    Port 312
    IdentityFile ~/.ssh/id_rsa

Host Master
    HostName 202.120.55.11
    User username
    Port 313
    IdentityFile ~/.ssh/id_rsa

Host Pi
    HostName pilogin.hpc.sjtu.edu.cn
    User username
    Port 22
    IdentityFile ~/.ssh/id_rsa

Host SiYuan
    HostName sylogin.hpc.sjtu.edu.cn
    User username
    Port 22
    IdentityFile ~/.ssh/id_rsa
```

之后，只需输入以下内容即可登录：

```bash
ssh Manager

ssh Pi

ssh SiYuan
```


---

### 客户端免密登录

- 常用软件：MobaXterm、Tabby（学校有定制版） 等。

- 免密登录方式：将 id_rsa 私钥文件所在路径添加到 Use private key 选项中（Bookmark settings 选项可以将默认的 Session name 改成自己想要的别名）。

![MobaXterm 免密登录](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/test-2023-06-04-17-43-41.png)


---

### VSCode 免密登录

- 安装 **Remote Development** 扩展，如上面的 `~/.ssh/config` 内容已设置好，会自动识别设置好的主机名（**config 文件所在路径可自定义**）。

- vscode 远程连接 manager（机子较老，10 余年历史） ，有时会导致其负载过高而崩溃，不建议长时间连接；vscode 远程连接 master（2023 年 5 月配置）暂无相关问题。

- 在超算上使用 python 插件中的 pylance 语言服务器，会时不时出现 pylance 崩溃的问题（以及使用 jupyter notebook，pi 在这方面比思源更稳定一些），因为超算的登录节点资源有限，建议将 pylance 换成 jedi（功能不及 pylance），会稍微稳定些；建议不在超算平台上使用 jupyter notebook。master 暂无相关问题。



---

## 任务准备、提交、检查

### Slurm 任务调度系统

>[Slurm 作业调度系统 - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/job/slurm.html)

- 常用命令：
	- `sbatch` - 作业提交
	- `squeue` - 查看排队作业状态
	- `scancel` - 删除作业
	- `scontrol` - 查看作业参数
	- `sinfo` - 查看集群状态

- 节点状态：
	- `drain` - 节点故障
	- `alloc` - 节点在用
	- `idle` - 节点可用
	- `down` - 节点下线
	- `mix` - 节点部分占用，但仍有剩余资源

- 作业状态：
	- `R`- 正在运行
	- `PD` - 正在排队
	- `CG` - 即将完成
	- `CD` - 已完成


- 作业提交

```bash
sbatch job.slurm
```

- 查看作业参数

```bash
scontrol show job

scontrol show job JOB_ID
```

参数包括：
```bash
UserId|WorkDir|JobState|JobId|JobName|NumNodes|NumCPUs|StdErr|StdOut|Command|RunTime
```


查看特定队列特定状态的节点
```bash
sinfo --partition=64c512g -N | grep 'drain'
```



---

### PBS 任务调度系统

manager 为此作业调度系统。

常用命令：`qsub` - 提交作业；`qdel` - 取消作业


VASP 任务提交命令
```bash
submit -nc -n 8 vasp

submit -n 8 vasp
```


LAMMPS 任务提交命令
```bash
submit -nc -n 8 lmp -in in.file

submit -n 8 lmp -in in.file
```

- `submit` 命令是孔老师写的一个 PBS 任务提交脚本。
- `-nc` 参数的含义是不将文件复制到计算节点中；**推荐用带 `-nc` 参数的命令**。
- 上述命令会自动生成对应的 `PBS.batch` 脚本；**当提交的任务出错时，并进行修改后，可以使用 `qsub PBS.batch` 命令提交任务。**


---

**manager 中与 PBS 相关的一些 alias 设置**

q 相关命令均由 qstat 延伸：
```bash
alias q='qstat -u yangsl'
alias qq='pestat'
alias qa='qstat -a'
alias qn='qstat -u yangsl|wc -l|awk '\\''{if ($1>0) print "Number of jobs by yangsl: " $1-5; else print "Number of jobs by yangsl: 0"}'\\'';qstat -a|wc -l|awk '\\''{print "Number of jobs by all: " $1-5}'\\'''
```

查看方法：
```bash
alias | grep ^q
```

- `q` - 查看自己任务的状态；
- `qstat` - 查看所有任务的状态；
- `qa` - 查看所有任务的状态（比 qstat 显示的信息更多一些）；
- `qq` - 查看计算节点的状态（`excl` - 正在运行；`free` - 空闲；`down` - 出现故障）；
- `run` - 查看自己任务的结果输出路径和信息；
- `qn` - 查看自己提交任务的数量和 manager 目前已提交的任务总数；
- `ssh node02` - 连接计算节点；任务到了截止时间后程序会终止，只会输出 `error` 和 `out` 文件，可以通过 `ssh node` 节点到计算该任务的节点中去，在 `scratch` 文件夹中可以找到该任务计算的结果；
- 计算时间：
    - `Elap Time` 为**实际时间**（小时: 分）；`Req'd Time` 为**截止计算时间**（240 小时）；
    - `Time Use` 为**实际时间 * 节点数。**


---

### 超算队列介绍

>[快速上手 - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/quickstart/index.html)

- 超算队列内存情况

```text
arm128c256g    每核2G内存    arm
64c512g        每核8G内存    siyuan
cpu            每核4G内存    pi
small          每核4G内存    pi
dgx2           每核6G内存    pi
**huge           每核35G内存   pi
192c6t         每核31G内存   pi**
cpu，small和dgx2队列作业运行时间最长7天，huge和192c6t最长2天。作业延长需发邮件申请，附上用户名和作业ID，延长后的作业最长运行时间不超过14天。
```

---

- 队列资源选择

```text
资源如何选择？
交我算HPC+AI平台采用 CentOS 的操作系统，配以 Slurm 作业调度系统，所有计算节点资源和存储资源，均可统一调用。

若是大规模的 CPU 作业，可选择 CPU 队列或思源一号64c512g队列，支持万核规模的并行；

若是小规模测试，可选 small 队列或思源一号64c512g队列；

GPU 作业请至 dgx2 队列或思源一号a100队列；

**大内存作业可选择 huge 或 192c6t 两种队列**。
```

---

- **192c6t 和 huge 大内存队列，核数有一定要求，且排队时间较长**

192c6t 队列
```bash
sbatch: error: The cpu demand is lower than 48. Please submit to huge or cpu partition.
sbatch: error: Batch job submission failed: Unspecified error
```

huge 队列
```bash
sbatch: error: The cpu demand is lower than 6. Please submit to small partition.
sbatch: error: Batch job submission failed: Unspecified error
```

---

- 超算收费情况（2023.05.30）

```text
交我算平台集群总费用为CPU，GPU和存储费用之和。费率标准如下：

CPU 价格：0.04元/核/小时（Pi 2.0集群 cpu/small/huge/192c6t/debug 队列）

                   0.05 元/核/小时（思源一号集群 64c512g 队列）

                   0.01元/核小时（arm128c256g队列）
GPU 价格：2 元/卡/小时（dgx2队列 V100 GPU）

                   2.5 元/卡/小时（思源一号 a100队列 A100 GPU）

免费存储 3 TB，超出部分 200 元/TB/年（存储按天扣费）

每个新账户赠送价值 300 元的积分，供免费试用
```

---

- 超算软件模块使用

>[软件模块使用方法 - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/app/module.html)

```bash
module avail/av         # 查看超算预部署软件模块
module av [MODULE]      # 查看具体模块
module load [MODULE]    # 加载相应软件模块
module list             # 列出已加载模块
module purge            # 清除所有已加载软件模块
module show [MODULE]    # 列出该模块的信息，如路径、环境变量等
```

**查看 module load 相关软件模块的 lib 和 include 路径方法：**

`module load boost` 相关版本后，使用 `module show boost` 命令可以查到 `boost` 的 `lib` 库位置，然后使用命令 `grep -rn "libboost_python" /path/to/lib/*` 检索相应的库文件

---

- 超算代理相关设置

>[数据共享与传输 - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/transport/index.html)

思源一号克隆 Github repo（或 wget 下载远程文件） 速度慢或无法进行；pi 则正常。

解决方案：在计算节点上运行（有时也还是不稳定）或使用 [Github 增强 - 高速下载](https://greasyfork.org/zh-CN/scripts/412245-github-%E5%A2%9E%E5%BC%BA-%E9%AB%98%E9%80%9F%E4%B8%8B%E8%BD%BD) 油猴插件，选择合适的 URL 进行克隆。

计算节点是通过 proxy 节点代理进行网络访问的，因此一些软件需要特定的代理设置。需要找到软件的配置文件，修改软件的代理设置。

查看代理：
```bash
echo $http_proxy $https_proxy $no_proxy
```

git、wget、curl 等软件支持通用变量，代理参数设置为：
```bash
# 思源一号计算节点通用代理设置
https_proxy=http://proxy2.pi.sjtu.edu.cn:3128
http_proxy=http://proxy2.pi.sjtu.edu.cn:3128
no_proxy=puppet,proxy,172.16.0.133,pi.sjtu.edu.cn

 # π2.0计算节点通用代理设置
http_proxy=http://proxy.pi.sjtu.edu.cn:3004/
https_proxy=http://proxy.pi.sjtu.edu.cn:3004/
no_proxy=puppet
```

Python、MATLAB、Rstudio、fasterq-dump 等软件需要查询软件官网确定配置参数：
```bash
### fasterq-dump文件，配置文件路径 ~/.ncbi/user-settings.mkfg

# 思源一号节点代理设置
/tools/prefetch/download_to_cache = "true"
/http/proxy/enabled = "true"
/http/proxy/path = "http:/proxy2.pi.sjtu.edu.cn:3128"

# π2.0节点代理设置
/tools/prefetch/download_to_cache = "true"
/http/proxy/enabled = "true"
/http/proxy/path = "http://proxy.pi.sjtu.edu.cn:3004"

### Python需要在代码里面指定代理设置，不同Python包代理参数可能不同

# 思源一号节点代理设置
proxies = {
    'http': 'http://proxy2.pi.sjtu.edu.cn:3128',
    'https': 'http://proxy2.pi.sjtu.edu.cn:3128',
}
# π2.0节点代理设置
proxies = {
    'http': 'http://proxy.pi.sjtu.edu.cn:3004',
    'https': 'http://proxy.pi.sjtu.edu.cn:3004',
}

### MATLAB

# 思源一号节点代理设置
proxy2.pi.sjtu.edu.cn:3128

# π2.0节点代理设置
proxy.hpc.sjtu.edu.cn:3004
```

---

注意：

- **队列一般不设置独占节点（不能加 `#SBATCH --exclusive`）**
- **超算平台无法安装 OVITO**，可视化平台有 OVITO，按小时收费
- 登录密码输错 5 词，需等待一段时候才能再次登录


---

### 任务提交示例

>以下任务提交脚本代码使用的思源一号中的 64c512g 队列；超算中有许多不同版本的程序，可根据自身需求 `module load` 相应版本的程序


SBATCH 相关参数
```bash
#SBATCH --job-name=vasp_job
#SBATCH --account=wen
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --ntasks-per-node=1
#SBATCH --mem=50GB
#SBATCH -o %j.out
#SBATCH -e %j.err

#SBATCH --exclusive
```


---

#### VASP

module load 超算中的 VASP
```bash
#!/bin/bash

#SBATCH -J vasp
#SBATCH -p 64c512g
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge

module load vasp/5.4.4-intel-2021.4.0

ulimit -s unlimited

mpirun vasp_std
```

---

本地编译的 VASP 版本
```bash
#!/bin/bash

#SBATCH -J vasp
#SBATCH -p 64c512g
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge

module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

ulimit -s unlimited

export OMP_NUM_THREADS=1
export I_MPI_ADJUST_REDUCE=3

mpirun $HOME/bin/vasp_std
```


**注：相关命令含义**
```bash
ulimit -s unlimited

export OMP_NUM_THREADS=1 
export I_MPI_ADJUST_REDUCE=3
```

- `ulimit -s unlimited` - 设置进程的堆栈大小限制。通过指定 `unlimited`，表示将堆栈大小限制设置为无限制。堆栈是用于存储函数调用和局部变量的内存区域，增加堆栈大小限制可以允许进程使用更多的堆栈空间。这对于需要递归调用或者使用大量局部变量的程序可能是必需的。
- `export OMP_NUM_THREADS=1` - 设置 `OMP_NUM_THREADS` 环境变量，并将其值设为 1。`OMP_NUM_THREADS` 是 OpenMP 库使用的一个环境变量，用于指定并行计算时使用的线程数。在这里，将线程数设置为 1 表示只使用一个线程进行并行计算。这可以用于限制并行化的程度，特别是当希望使用单线程执行时。
- `export I_MPI_ADJUST_REDUCE=3` - 设置 `I_MPI_ADJUST_REDUCE` 环境变量，并将其值设为 3。`I_MPI_ADJUST_REDUCE` 是 Intel MPI 库使用的一个环境变量，用于调整 MPI 库中用于并行归约操作（reduce operation）的算法。将该变量设置为 3 表示使用性能优化的归约算法。这可以提高 MPI 程序中归约操作的效率。

---

#### LAMMPS

```bash
#!/bin/bash

#SBATCH --job-name=lmp
#SBATCH --partition=64c512g
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --output=%j.out
#SBATCH --error=%j.err

module purge

module load lammps/20220324-intel-2021.4.0-omp

mpirun lmp -i in.test
```

---

超算 Pi 新 CPU 队列 LAMMPS 任务提交脚本示例
```bash
#!/bin/bash

#SBATCH -J lmp_pi
#SBATCH -p cpu
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge
module load lammps/20230802-oneapi-2021.4.0

mpirun lmp -in in.test
```


---

#### Python

```bash
#!/bin/bash

#SBATCH -J python
#SBATCH -p 64c512g
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge

conda activate <ENV_NAME>
# source path/activate <ENV_NAME>

python test.py
```


---

#### Shell

```bash
#!/bin/bash

#SBATCH -J bash
#SBATCH -p 64c512g
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -o %j.out
#SBATCH -e %j.err

module purge

bash test.sh
```


---

### 任务状态检查

任务提交后，会出现 `jobid.err` 和 `jobid.out` 文件：

- `err` 文件为空（大小为 0），表示提交的任务未出错；
- `err` 文件不为空（大小不为 0），表示提交的任务出错；需查看 `err` 文件中的出错提示，进行修改。


---

### 相关问题

- [x] `mpirun` 和 `srun` 的区别是什么？intel 编译套件？

>[srun和mpirun的区别](http://bbs.keinsci.com/thread-23497-1-1.html)

- srun 是 slurm 作业调度系统的一个命令，mpirun 是 mpi（实现形式有 openmpi，mpich，intel mpi 等）的一个命令，两者在效率方面是无法直接比较的。
- 当你用 slurm 作业调度系统的时候，你可以通过 srun 提交作业，提交的作业如果是 mpi 并行的，那么它会去调用相应的 mpirun 来运行作业，这两个就是这样一个关系
- mpirun 用来并行任务



---

## 数据传输

>[数据共享与传输 - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/transport/index.html)

超算中进行数据传输一般在 data 节点上进行。超算传输节点：

- Pi
```bash
data.hpc.sjtu.edu.cn
```

- 思源一号
```bash
sydata.hpc.sjtu.edu.cn
```


---

### 命令行

主要使用 scp 和 rsync 两个命令：

- scp（Secure Copy）是一种安全的文件传输协议，它使用 SSH（Secure Shell）协议来加密和传输文件。SCP 允许你将文件从一个系统复制到另一个系统，也可以在本地系统和远程系统之间传输文件。它提供了对远程系统的安全访问，并使用类似于 cp（复制）命令的语法来指定源文件和目标位置。
- rsync 可以通过检测源和目标文件之间的差异，仅传输发生更改的部分，从而在网络带宽和传输时间上提供更好的性能。

---

- scp: `scp -r src_path dest_path`
```bash
# 将manager的数据上传到master上
scp -r 1.manager yangsl@master:/home/yangsl/test

# 将master的数据下载到manager上
scp -r yangsl@master:/home/yangsl/test/1.master .

scp -r mseklt@sylogin.hpc.sjtu.edu.cn:/dssg/home/acct-mseklt/mseklt/yangsl/tests/1.sy .
scp -r 1.manager mseklt@sylogin.hpc.sjtu.edu.cn:/dssg/home/acct-mseklt/mseklt/yangsl/tests
```

- rsync: `rsync -avu src_path dest_path`
```bash
# 将manager的数据上传到master上
rsync -avu 1.manager yangsl@master:/home/yangsl/test

# 将master的数据下载到manager上
rsync -avu yangsl@master:/home/yangsl/test/1.master .

rsync -avu mseklt@sylogin.hpc.sjtu.edu.cn:/dssg/home/acct-mseklt/mseklt/yangsl/tests/1.sy .
rsync -avu 1.manager mseklt@sylogin.hpc.sjtu.edu.cn:/dssg/home/acct-mseklt/mseklt/yangsl/tests
```

**注：rsync 的部分参数介绍：**
- `a, --archive` - 归档模式。保持文件属性和目录结构，并递归地复制子目录。这是最常用的 rsync 选项，相当于 `rlptgoD`。
- `r, --recursive` - 递归地复制目录和子目录。
- `l, --links` - 处理符号链接。保持符号链接的属性。
- `p, --perms` - 保持文件权限。
- `t, --times` - 保持文件时间戳。
- `g, --group` - 保持文件所属组。
- `o, --owner` - 保持文件所有者。
- `D, --devices` - 保持设备文件（块设备和字符设备）。
- `v, --verbose` - 显示详细输出。在传输过程中显示文件列表。
- `z, --compress` - 使用压缩传输。在网络带宽有限时，可以加快传输速度。
- `h, --human-readable` - 以人类可读的格式显示输出。文件大小以 KB、MB、GB 等表示。
- `n, --dry-run` - 执行模拟运行，不实际进行文件传输或同步。可以用于检查操作的效果。
- `-delete` - 删除目标文件夹中与源文件夹不匹配的文件。这将确保目标文件夹与源文件夹完全同步。
- `-exclude` - 排除指定的文件或目录，不进行传输或同步。可以使用通配符模式进行匹配。
- `-include` - 只包括指定的文件或目录，排除其他文件或目录。可以使用通配符模式进行匹配。
- `e, --rsh=COMMAND` - 指定用于远程 shell 的命令。默认为使用 ssh。
- `-u，--update` - 仅传输源文件中更新或修改过的文件。使用 `-u` 选项可以减少传输的数据量，节省带宽和传输时间。


---

### 客户端

主要使用 WinSCP；免密登录方式如下：

![WinSCP 免密登录](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/test-2023-06-04-17-42-44.png)


---

### manager 与超算间的数据传输

upload 与 download 脚本

上传与下载：
- manager 与 Pi：`upload -s P` 或将 `P` 改成 `H` 或 `h`
- manager 与思源一号：将 `P` 改成 `s`
- `which upload` 或 `which download`，**查看其可执行文件位置与源码内容**

```bash
upload -s P manager/path pi/path
upload -s s manager/path siyuan/path

download -s P pi/path manager/path
download -s s siyuan/path manager/path
```



---

## 程序编译/安装

**注：在超算上编译程序，由于登录节点资源有限，需在计算节点上进行，需申请临时计算节点（一个核即可）**。

```bash
# 思源一号
srun -p 64c512g -n 1 --pty /bin/bash

# Pi
srun -p small -n 1 --pty /bin/bash
```


---

### posconv、NumNei

- posconv：构型文件格式转换（POSCAR xyz pos lammpstrj 等）
- NumNei：计算 BCC、FCC 和金刚石结构的第 N 近邻原子距离
 - 编译
	- 编译器选择：gfortran 或 ifort（gfortran 已足够；ifort 性能可能更好些）
	- gfortran：课题组服务器及超算中含 gfortran（如超算中的 `gcc/11.2.0`）
	- ifort：课题组服务器及超算中含 ifort（如超算中的 `intel-oneapi-compilers/2021.4.0`）

```bash
                                        POSCONVERT
                                   2023-06-16  17:15:45

          Program to convert atomic configuration files

          =======================  Input Configuration   =======================
          Please select input configuration format:
               1. VASP POSCAR;
               2. PWSCF POSITION CARD;
               3. xyz file;
               4. groF and/or MSS format;
               5. BGF (ReaxFF);
               6. ReaxFF save file;
               7. MS Car file;
               8. LAMMPS full;
               9. LAMMPS dump atom;
              10. Siesta STRUCT_IN;
              11. Abinit/BigDFT xyz;
              12. MS RES file;
              13. ARTn;
               0. Exit.
          Your choice [3]:
```


---

### latgen

- 构型生成程序，包括 BCC、FCC、HCP、diamond、含点缺陷、置换固溶体、表面等构型。
- 编译依赖 voro++

---

- voro++ 编译

```bash
wget https://math.lbl.gov/voro++/download/dir/voro++-0.4.6.tar.gz

tar -xzvf voro++-0.4.6.tar.gz

cd voro++-0.4.6.tar.gz

# 修改 config.mk 的 PREFIX 选项
PREFIX=${HOME}/src/voro++

make && make install
```

---

编译器可选择 icc；修改 latgen 中的 Makefile 文件内容（`INC`：voro++ 的头文件路径； `LIB`：库路径）

```bash
VoroINC = -I${HOME}/src/voro++/include/voro++
VoroLIB = -L${HOME}/src/voro++/lib -lvoro++
```


---

### dumpana

- LAMMPS dump 文件后处理程序。可以计算：CSRO；RDF、PDF、g(r) （径向分布函数）；扩散系数等
- dumpana、latgen、posconv 和 vaspkit 等程序都可以通过 `latgen < inp.script` 命令，使其不用每次交互输入参数，节约时间（**重要！！！**）。
- 编译依赖 voro++ 和 gsl（C 数值计算库）

```bash
Code to analyse the atom style dump files of lammps. Functions available:
--------------------------------------------------------------------------------
  1. Voronoi diagram analysis;         |  11. Output selected frames;
  2. Chemical Short Range Order;       |  12. Average over frames;
  3. Honeycutt-Andersen bond index;    |  13. Pair correlation function;
  4. Common Neighbor/Centro-symmetry;  |  14. Static structure factor;
  5. Prepare for FEFF9;                |  15. Bond length/angles;
  6. Voronoi cluster connectivity;     |  16. Spatial distribution of atoms;
  7. Output selected atoms/clusters;   |  17. Radial distribution of atoms;
  8. Output bgf format with property;  |  18. RMSD between frames;
  9. Local order parameter Ql, qlql;   |  19. Bhatia-Thornton structure factor;
 10. Configurational entropy of mixing;|  20. MSD for selected atoms;
---------------------------------------+----------------------------------------
 21. Heredity of atomic clusters;      |  31. Count # selected atoms vs time;
 22. Pair correlation for atomic prop; |  32. Unwrap PBC bonded atoms;
--------------------------------------------------------------------------------

Usage:
    dumpana [options] [file [file2]]
```

---

- gsl 编译

```bash
wget https://mirror.ibcp.fr/pub/gnu/gsl/gsl-latest.tar.gz

./configure --prefix=${HOME}/src/gsl

make && make install

# 将 gsl 的 lib 路径添加到 LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$HOME/src/gsl/lib:${LD_LIBRARY_PATH}
```

---

- master 平台编译

修改 Makefile 文件内容（voro++、gsl 的 `INC` 和 `LIB`），编译

```bash
VoroINC = -I${HOME}/src/voro++/include/voro++
VoroLIB = -L${HOME}/src/voro++/lib -lvoro++

GslINC  = -I${HOME}/src/gsl/include
GslLIB  = -L${HOME}/src/gsl/lib -lgsl -lgslcblas

# master 上有 voro++、gsl；可不用修改
VoroINC = -I/opt/libs/voro/include/voro++
VoroLIB = -L/opt/libs/voro/lib -lvoro++

GslINC  = -I/opt/libs/gsl/include
GslLIB  = -L/opt/libs/gsl/lib -lgsl -lgslcblas
```

---

- 思源一号平台编译

```bash
git clone https://github.com/lingtikong/dumpana.git

module purge
module load gsl/2.7.1-intel-2021.4.0
module load intel-oneapi-compilers/2021.4.0

# 编译器选择 icc
# 修改 Makefile 文件的 voro++ 内容，gsl 可不用修改

make
```

若使用时报错，设置 gsl 相关的动态链接库文件的软链接

```bash
ln -s /dssg/opt/icelake/linux-centos8-icelake/intel-2021.4.0/gsl-2.7.1-363bjoc7gmwz4mpn2csc7paszwv5h2wk/lib/libgsl.so.27 ~/lib/
ln -s /dssg/opt/icelake/linux-centos8-icelake/intel-2021.4.0/gsl-2.7.1-363bjoc7gmwz4mpn2csc7paszwv5h2wk/lib/libgslcblas.so.0 ~/lib/
```


---

### Atomsk

- 结构建模程序；同 latgen 相比，可生成孪晶、晶界、位错等更多复杂构型
- 下载：[Atomsk - Download](https://atomsk.univ-lille.fr/dl.php)；安装：[Atomsk - Install - Pierre Hirel](https://atomsk.univ-lille.fr/doc/en/install.html)

---

**编译**

- 可执行版本（最简单方式）：

```bash
wget https://atomsk.univ-lille.fr/code/atomsk_b0.13.1_Linux-amd64.tar.gz

tar -xzvf atomsk_b0.13.1_Linux-amd64.tar.gz

cd atomsk_b0.13.1_Linux-amd64

ln -s atomsk ~/bin
```

---

- 源码编译：

依赖 blas 和 lapack 库（manager/master/超算上没有这两个库，需自己编译；编译 lapack 需要先编译 blas；**intel 套件有相关库**）

编译 blas 和 lapack 步骤以及压缩包：
>[apt - How to build and link BLAS and LAPACK libraries by hand for use on cluster? - Ask Ubuntu](https://askubuntu.com/questions/1270161/how-to-build-and-link-blas-and-lapack-libraries-by-hand-for-use-on-cluster)

>[LAPACK build and test guide - GNU Project](https://gcc.gnu.org/gcc-3.0/lapack-guide.html)

>[BLAS (Basic Linear Algebra Subprograms)](https://netlib.org/blas/)


创建 `~/lib`，并将其添加到 `LD_LIBRARY_PATH`；将 `*.a` 静态库文件设置软链接（或复制）到此

```bash
export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH
```

- 编译 blas

```bash
tar -xzvf blas-3.8.0.tgz

cd BLAS-3.8.0/

make

mv blas_LINUX.a libblas.a

cp *.a ~/lib
```

---

- 编译 lapack

```bash
tar -xzvf lapack-3.9.0.tar.gz

cd lapack-3.9.0/

cp make.inc.example make.inc

# 这步花费时间会比较长
make

cp *.a ~/lib
```

---

下载 Atomsk 源文件，进入 `src`，修改 Makefile 文件

```bash
LAPACK=-L$HOME/lib/ -llapack -lblas
INSTPATH=$HOME/src
CONFPATH=${INSTPATH}/etc
```

编译：

```bash
make atomsk

# 应该会出错，但没关系，这步非必需
make install
```


编译成功：

```text

    \o/ Compilation was successful!

    <i> To install Atomsk system-wide, you may now run:
          sudo make install
```


---

- master 编译 ifort 版本

```bash
git clone https://github.com/pierrehirel/atomsk.git

cd atomsk/src

make -f Makefile.ifort atomsk
```


---

- 思源一号超算编译 ifort 版本

```bash
git clone https://github.com/pierrehirel/atomsk.git

cd atomsk/src

module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

make -f Makefile.ifort atomsk
```

设置 `libiomp5.so` 文件的软链接或者使用前 `module load intel-oneapi-compilers/2021.4.0`

```bash
ln -s /dssg/opt/icelake/linux-centos8-icelake/gcc-8.5.0/intel-oneapi-compilers-2021.4.0-rszhbg2vjwqqeddqqdryjwxromenbfmr/compiler/2021.4.0/linux/compiler/lib/intel64_lin/libiomp5.so ~/lib/libiomp5.so
```


---

### VASP5.4.4

参考：[Installing VASP.5.X.X - Vaspwiki](https://www.vasp.at/wiki/index.php/Installing_VASP.5.X.X)、[VASP - 上海交大超算平台用户手册 Documentation](https://docs.hpc.sjtu.edu.cn/app/engineeringscience/vasp.html)、[VASP - CodiMD](https://notes.sjtu.edu.cn/s/daoG4JIYX#)


VASP5.4.4 源代码目录结构：

```text
vasp.X.X.X (root directory)
                            |
         ---------------------------------------
        |              |          |             |
       arch           bin       build          src
                                                |
                                         ---------------
                                        |       |       |
                                       lib    parser   CUDA
```

目录含义：

- `arch`：针对不同架构的 Makefile 模板，如 `makefile.include.linux_intel`
- `bin`：编译后的可执行程序文件目录
- `build`：编译时自动复制 src 目录内源码后执行编译的目录
- `src`：源码目录
- `lib`：库目录，对应以前的 vasp.lib 目录
- `CUDA`：GPU CUDA 代码目录

---

安装步骤：

>VASP5.4.4 安装包：manager: `/opt`，master: `/opt/software`；将其复制到自己的用户目录下打包压缩，上传至超算平台）

```bash
# 申请计算节点

# 导入 oneapi 套件
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0

# 删除 bulid 和 bin 目录中的内容
make veryclean
rm bin/*

cp arch/makefile.include.linux_intel makefile.include

# 编译；耗时 20-30 分钟
make  # make all
```

- 三种版本可分开进行编译：`make std`，`make gam`，`make ncl`
- `bin` 目录若出现 `vasp_std`, `vasp_gam`, `vasp_ncl` 三种版本的可执行文件，则表示编译成功；
- 将 `vasp_std` 设置软链接


---

### VASP6.3.0 + HDF5

思源一号超算平台编译

>[Installing VASP.6.X.X - VASP Wiki](https://www.vasp.at/wiki/index.php/Installing_VASP.6.X.X)

VASP6.3.0 源代码目录结构：

```text
                  vasp.x.x.x (root directory)
                               |
         ------------------------------------------------
        |        |        |         |          |         |
       arch     bin     build      src     testsuite   tools
                                    |
                              -------------
                             |      |      |       
                            lib   parser  fftlib
```

---

安装步骤：

>master 的 vasp.6.3.0 目录在 `/opt/software` 下；将其复制到自己的目录下打包，上传至超算平台）

```bash
# 申请计算节点

# 导入 oneapi 套件；hdf5
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mpi/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load hdf5/1.12.2-intel-2021.4.0

# 查看 hdf5/1.12.2-intel-2021.4.0 的安装路径
module show hdf5/1.12.2-intel-2021.4.0

cp arch/makefile.include.intel makefile.include
# 删除 MKLROOT    ?= 后的内容
# 将 HDF5_ROOT  ?= 后的内容替换为 hdf5 的安装路径

make
```

---

可能会出现以下报错：

```bash
error while loading shared libraries: libhdf5_fortran.so.102: cannot open shared object file: No such file or directory
```

原因：缺少 `libhdf5_fortran.so.102` 动态链接库，其实 module load 的 `hdf5/1.12.2-intel-2021.4.0` 有该动态链接库，不过版本更新一些，为 `libhdf5_fortran.so.200`

解决方法：

- 将 `libhdf5_fortran.so.200` 软链接为 `libhdf5_fortran.so.102`

```bash
mkdir ~/lib

ln -s /dssg/opt/icelake/linux-centos8-icelake/intel-2021.4.0/hdf5-1.12.2-nxwmp3tddhreojgbib25ldc7wusvzf3m/lib/libhdf5_fortran.so.200 ~/lib/libhdf5_fortran.so.102
```

- 将 `~/lib` 写入到 `LD_LIBRARY_PATH`

```bash
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:$HOME/lib
```


---

### LAMMPS

使用 cmake 编译

```bash
wget https://download.lammps.org/tars/lammps-2Aug2023.tar.gz
tar -xzvf lammps-2Aug2023.tar.gz
cd lammps-2Aug2023

# 导入 oneapi 套件
module purge
module load intel-oneapi-compilers/2021.4.0
module load intel-oneapi-mkl/2021.4.0
module load intel-oneapi-mpi/2021.4.0

# 编译配置
mkdir build-oneapi && cd build-oneapi
cmake -C ../cmake/presets/oneapi.cmake ../cmake

# 编译
make
```


---

### vaspkit

- VASP 预、后处理工具；[Overview — VASPKIT 1.5 documentation](https://vaspkit.com/)
- 预处理：不同计算任务的输入文件生成与检验；结构对称性分析等
- 后处理：力学性质；能带；态密度；费米面分析等
- 安装：在 [vaspkit - Binaries](https://sourceforge.net/projects/vaspkit/files/Binaries/) 中下载 vaspkit 最新版本，解压，设置环境变量（`cp how_to_set_environment_variables ~/.vaspkit`）；设置 `PBE_PATH`、`VASPKIT_UTILITIES_PATH` 和 `PYTHON_BIN`（可选）参数；对可执行文件设置软链接


---

### VTST + VASP

>[VASP 5.4.1+VTST编译安装](http://hmli.ustc.edu.cn/doc/app/vasp.5.4.1-vtst.htm)

>[Installation — Transition State Tools for VASP](http://theory.cm.utexas.edu/vtsttools/installation.html)

VTST+VASP：嵌入过渡态理论版本的 VASP；计算过渡态

- VTST 部分

下载 vtstcode-197.tgz 和 vtstscripts.tgz：
```bash
wget <http://theory.cm.utexas.edu/code/vtstcode-197.tgz>
wget <http://theory.cm.utexas.edu/code/vtstscripts.tgz>
```

修改 VASP src 目录下的 main.F 文件：
```bash
CALL CHAIN_FORCE(T_INFO%NIONS,DYN%POSION,TOTEN,TIFOR, &
     LATT_CUR%A,LATT_CUR%B,IO%IU6)
```

替换成：
```bash
# 添加了"TSIF,"
CALL CHAIN_FORCE(T_INFO%NIONS,DYN%POSION,TOTEN,TIFOR, &
     TSIF,LATT_CUR%A,LATT_CUR%B,IO%IU6)
```

备份 src 目录下的 chain.F 文件；复制 vtstcode-197/vtstcode5 目录下的所有文件到 src 目录中：
```bash
cp src/chain.F src/chain.F-org
cp vtstcode-197/vtstcode5/* src/
```

修改 src/.objects 文件，在 chain.o 前添加如下内容：
```bash
bfgs.o dynmat.o instanton.o lbfgs.o sd.o cg.o dimer.o bbm.o \\
fire.o lanczos.o neb.o qm.o opt.o \\
```

- VASP 部分：同前面部分


---

### phonopy

- 计算声子谱；官网：[Welcome to phonopy — Phonopy v.2.20.0](https://phonopy.github.io/phonopy/)


安装
```bash
conda install -c conda-forge phonopy
```


---

### sqsgen

- 安装：[How to install sqsgen? — sqsgenerator 0.2 documentation](https://sqsgenerator.readthedocs.io/en/latest/installation_guide.html)
- 命令行使用：[CLI reference — sqsgenerator 0.2 documentation](https://sqsgenerator.readthedocs.io/en/latest/cli_interface.html)
- 多亚点阵 sqsgen 生成示例：[Advanced topics — sqsgenerator 0.2 documentation](https://sqsgenerator.readthedocs.io/en/latest/advanced_topics.html)

---

sqs 生成程序

- 目标函数为 WC 参数；
- 生成速度相比 ATAT 及 ICET 相关模块要快，功能也更多；
- 10000 个原子构型的 sqs 生成速度在 2min 以内；
- 可事先估计生成 sqs 结构所耗费时间；可计算 WC 参数等；
- 浓度用具体的原子数目表示，比百分比形式更方便
- 有 OpenMP 和 OpenMP+MPI 两种版本

---

conda 版本（OpenMP 版本）

```bash
conda create --name sqsgen python=3

conda install -c conda-forge sqsgenerator

# 导出构型文件需要以下 package
pip install pymatgen ase
```

---

编译版本（OpenMP+MPI）

```bash
conda create --name sqsgen -c conda-forge boost boost-cpp cmake gxx_linux-64 libgomp numpy pip python=3

git clone https://github.com/dgehringer/sqsgenerator.git
```

- OpenMP 版本

```bash
conda activate sqsgen
cd sqsgenerator

SQS_Boost_INCLUDE_DIR="${CONDA_PREFIX}/include" \\                                
SQS_Boost_LIBRARY_DIR_RELEASE="${CONDA_PREFIX}/lib" \\
CMAKE_CXX_COMPILER="g++" \\
CMAKE_CXX_FLAGS="-DNDEBUG -O2 -mtune=native -march=native" \\
pip install .
```

- OpenMP+MPI 版本

```bash
conda activate sqsgen
cd sqsgenerator

SQS_MPI_HOME="${HOME}/yangsl/src/openmpi" \\
SQS_USE_MPI=ON \\
SQS_Boost_INCLUDE_DIR="${CONDA_PREFIX}/include" \\
SQS_Boost_LIBRARY_DIR_RELEASE="${CONDA_PREFIX}/lib" \\
CMAKE_CXX_COMPILER="g++" \\
CMAKE_CXX_FLAGS="-DNDEBUG -O2 -mtune=native -march=native" \\
pip install .
```


---

### texlive

- 思源一号中的 texlive 版本为 2018；pi 为 2013；manager 为 2015；master 未安装；无法安装 package
- 可自定义安装路径

```bash
# 自定义安装路径 添加环境变量
export TEXLIVE_INSTALL_PREFIX=$HOME/src/texlive
export TEXLIVE_INSTALL_TEXDIR=$HOME/src/texlive/2023

# 安装
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz --no-check-certificate
tar -xzvf nstall-tl-unx.tar.gz
cd install-tl-*
perl ./install-tl --scheme=full  # 或 medium small
# perl ./install-tl --scheme=full --no-interaction # 不进行交互

# 安装完成后，再添加环境变量
export MANPATH=$HOME/src/texlive/2023/texmf-dist/doc/man
export INFOPATH=$HOME/src/texlive/2023/texmf-dist/doc/info
export PATH=$HOME/src/texlive/2023/bin/x86_64-linux:$PATH
```

>texlive 不同版本需要安装的 packages 数目：medium 约 1395 项；full 约 4543 项。


---

### ATAT

WIP…


---

### 源代码编译

>[linux源码编译安装软件原理 - 人生的哲理 - 博客园](https://www.cnblogs.com/renshengdezheli/p/13954234.html)

编译前，需理解 Makefile 文件中的命令含义！

```bash
# 自定义安装路径
./configure --prefix=

# 编译
make

# 安装
make install
```



---

## 交我算常见问题总结

以下是使用 “ 交我算 ” 过程中可能遇到的常见问题总结：

---

**充值/费率**

1. 计费系统 (HPC 账号和密码登陆)：[https://account.hpc.sjtu.edu.cn](https://account.hpc.sjtu.edu.cn)

2. 充值方法：[https://net.sjtu.edu.cn/info/1244/2392.htm](https://net.sjtu.edu.cn/info/1244/2392.htm)

3. 费率问题：请用交大邮箱发送至 hpc@stju.edu.cn 咨询

---

**致谢模版**

1. “ 交我算 ” 用户在发布科研成果或论文时，应标注 “ 本论文的计算结果得到了上海交通大学交我算平台的支持和帮助 “（The computations in this paper were run on the π 2.0 (or Siyuan Mark-I) cluster supported by the Center for High Performance Computing at Shanghai Jiao Tong University）. 论文发表后，欢迎将见刊论文通过邮件发送到 hpc@sjtu.edu.cn。

---

**登录问题**

1. 连不上集群： [https://docs.hpc.sjtu.edu.cn/faq/index.html#id6](https://docs.hpc.sjtu.edu.cn/faq/index.html#id6)

2. 登录常掉线：[https://docs.hpc.sjtu.edu.cn/login/index.html#id10](https://docs.hpc.sjtu.edu.cn/login/index.html#id10)

3. HPC studio 登录问题：[https://docs.hpc.sjtu.edu.cn/studio/faq.html#hpc-studio-proxy-error](https://docs.hpc.sjtu.edu.cn/studio/faq.html#hpc-studio-proxy-error)

4. Jupyter、Rstudio 连接提示需要输入密码：[https://docs.hpc.sjtu.edu.cn/studio/faq.html#jupyterrstudio](https://docs.hpc.sjtu.edu.cn/studio/faq.html#jupyterrstudio)

---

**排队问题**

1. status 监控系统：[https://status.hpc.sjtu.edu.cn](https://status.hpc.sjtu.edu.cn)，该系统包含各队列上线节点数、排队数、作业数等信息

2. π集群排队问题：思源一号可用 CPU/GPU 资源更多，欢迎使用思源一号。

3. 通过 squeue 查看作业，NODELIST(REASON) 为 resources/priority 表示正常排队，AssocGrpNodeLimit 表示欠费。

---

**作业问题**

1. 报错作业咨询，请将用户名、作业 ID、路径、作业脚本名邮件发至 [hpc@sjtu.edu.cn](mailto:hpc@sjtu.edu.cn)。

2. NodeFail：计算节点故障导致作业运行失败，重新提交作业即可，失败作业的机时系统会自动返还。

3. 运行程序时提示缺少 xxx.so 文件或者显示任务被 kill：如果是在登录节点出现该报错，请申请计算节点再做尝试。

---

**软件安装问题**

1. 如何在集群上安装软件：[https://docs.hpc.sjtu.edu.cn/faq/index.html#id16](https://docs.hpc.sjtu.edu.cn/faq/index.html#id16)

2. 商业软件问题：[https://docs.hpc.sjtu.edu.cn/faq/index.html#id17](https://docs.hpc.sjtu.edu.cn/faq/index.html#id17)

---

**数据传输问题**

1. $\pi$ 集群传输至思源一号：[https://docs.hpc.sjtu.edu.cn/transport/index.html#id4](https://docs.hpc.sjtu.edu.cn/transport/index.html#id4)

---

**常用链接**

- HPC 网站：[https://hpc.sjtu.edu.cn](https://hpc.sjtu.edu.cn)
- 用户文档：[https://docs.hpc.sjtu.edu.cn](https://docs.hpc.sjtu.edu.cn)
- 超算用户简明手册：[https://docs.hpc.sjtu.edu.cn/\_static/hpcbriefmanual.pdf](https://docs.hpc.sjtu.edu.cn/_static/hpcbriefmanual.pdf)
- 集群实时利用率：[https://account.hpc.sjtu.edu.cn/top](https://account.hpc.sjtu.edu.cn/top)
- 公众号/视频号：交我算

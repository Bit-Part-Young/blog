---
title: Docker 安装与使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Docker 安装与使用
description: Docker 安装与使用
tags:
  - Docker
categories:
  - Linux
date: 2023-09-18 17:00:00
abbrlink: 908171
password:
---

# Docker 安装与使用

## 介绍

- 镜像（image）与容器（container）的关系：类似对象与类的关系

- Docker Registry：一个 Docker Registry 中可以包含多个仓库（Repository）；每个仓库可以包含多个标签（Tag）；每个标签对应一个镜像

- 参考资料
    - [Docker Hub](https://hub.docker.com/)
    - [docker是什么？和kubernetes(k8s)是什么关系？\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1aA4m1w7Ew)
    - [【入门篇】Docker网络模式Linux - Bridge, Host, None\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Aj411r71b)



---

## 安装与卸载

### Windows

- 默认安装到 `C:\Program Files\Docker`，管理员打开 CMD，输入以下命使其安装到 D 盘：
    - **安装到非 C 盘，Docker Desktop 后面的设置修改会报错，建议还是默认安装**

```cmd
mklink /J "C:\Program Files\Docker" "D:\"
```

- 设置：
    - Resources -- `Disk image location`，将存储目录、修改为 D 盘
    - 换源：`Docker Engine` -- 添加 `registry-mirrors` 参数（下面的源可能失效）

```json
{
  "registry-mirrors": [
      "https://registry.docker-cn.com",
      "http://hub-mirror.c.163.com",
      "https://docker.mirrors.ustc.edu.cn"
  ]
}
```

- Docker Desktop 的两个数据目录默认盘在 C 盘，更改数据存储位置：
    - [How can I change the location of docker images when using Docker Desktop on WSL2 with Windows 10 Home? - Stack Overflow](https://stackoverflow.com/questions/62441307/how-can-i-change-the-location-of-docker-images-when-using-docker-desktop-on-wsl2)
    - [修改windows10中docker20默认位置 - 我是谁](https://yuhldr.github.io/posts/52201.html)


---

### macOS

- 安装：OrbStack（非常推荐）、Docker Desktop

- 卸载：[Uninstall Docker Desktop - Docker Docs](https://docs.docker.com/desktop/uninstall/)

- 配置文件：`~/.docker/config.json`
    - 设置代理

```json
{
    "proxies": {
        "default": {
            "httpProxy": "http://127.0.0.1:7890",
            "httpsProxy": "http://127.0.0.1:7890",
            "noProxy": "localhost,127.0.0.1,.daocloud.io"
        }
    },
}
```



---

## 使用

### 工具

- 容器管理平台：[GitHub - portainer/portainer: Making Docker and Kubernetes management easy.](https://github.com/portainer/portainer)

- [GitHub - veggiemonk/awesome-docker: :whale: A curated list of Docker resources and projects](https://github.com/veggiemonk/awesome-docker)

- 替代 Docker Desktop：[GitHub - iongion/container-desktop: Podman desktop companion](https://github.com/iongion/container-desktop)

- VSCode Docker 插件：可以查看镜像、容器和 Registry

- Docker 操作 TUI 版本（类似 lazigit）：[GitHub - jesseduffield/lazydocker: The lazier way to manage everything docker](https://github.com/jesseduffield/lazydocker)

- 自动更新 Docker 容器：[GitHub - containrrr/watchtower: A process for automating Docker container base image updates.](https://github.com/containrrr/watchtower)

- 查看容器资源占用情况：[GitHub - bcicen/ctop: Top-like interface for container metrics](https://github.com/bcicen/ctop)

- Docker 代理：
    - [Docker Proxy](https://docker.1panel.live/)（已失效）

- 镜像：目前 Docker Hub 的很多国内镜像均失效
    - 汇总：[国内的 Docker Hub 镜像加速器，由国内教育机构与各大云服务商提供的镜像加速服务 - Dockerized 实践 https://github.com/y0ngb1n/dockerized · GitHub](https://gist.github.com/y0ngb1n/7e8f16af3242c7815e7ca2f0833d3ea6)

    - 目前还有效（有些镜像不在白名单）：[GitHub - DaoCloud/public-image-mirror: 很多镜像都在国外。比如 gcr 。国内下载很慢，需要加速。致力于提供连接全世界的稳定可靠安全的容器镜像服务。](https://github.com/DaoCloud/public-image-mirror)

    - [DockerHub容器镜像库 - 应用容器化](https://dockerhub.icu/)

```bash
# 使用方法 添加前缀
              docker.io/library/busybox  # 原
m.daocloud.io/docker.io/library/busybox  # 添加镜像
          dockerhub.icu/library/busybox  # 添加镜像
```

- 镜像转存：
    - [2024自建Docker镜像代理加速，3分钟部署完毕\_哔哩哔哩\_bilibili](https://b23.tv/phYsDHn)

    - [Docker镜像停服? 我编写了一个镜像转存工具，解决国内无法使用docker的问题，解决docker镜像无法拉取问题，修复docker pull失败\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Zn4y19743)

    - [GitHub - tech-shrimp/docker\_image\_pusher: 使用Github Action将国外的Docker镜像转存到阿里云私有仓库，供国内服务器使用，免费易用](https://github.com/tech-shrimp/docker_image_pusher)

    - [GitHub - cmliu/CF-Workers-docker.io: 这个项目是一个基于 Cloudflare Workers 的 Docker 镜像代理工具。它能够中转对 Docker 官方镜像仓库的请求，解决一些访问限制和加速访问的问题。](https://github.com/cmliu/CF-Workers-docker.io)

    - [GitHub - dqzboy/Docker-Proxy: 🔥 🔥 🔥 自建Docker镜像加速服务，基于官方Docker Registry 一键部署Docker、K8s、Quay、Ghcr、Mcr、Nvcr等镜像加速\\管理服务。支持免服务器部署到Render\\Koyeb](https://github.com/dqzboy/Docker-Proxy)


---

### Docker 命令

- `docker` 命令

```bash
docker --help

# 通用命令：
  run         # 从一个镜像中创建并启动一个容器
  exec        # 在容器中执行一条命令
  ps          # 列出容器
  build       # 根据 Dockerfile 构建一个镜像
  pull        # 从 registry 拉取一个镜像
  push        # 推送一个镜像到 registry
  images      # 列出镜像
  login       # 登录到 registry
  logout      # 从 registry 退出
  search      # 在 Docker Hub 中搜索镜像
  info        # 查看 Docker 信息

# 管理命令:
  container   # 管理容器
  image       # 管理镜像
  network     # 管理网络

# 命令：
  attach      # 介入到一个正在运行的容器
  commit      # 根据容器的更改创建一个新的镜像
  cp          # 在本地文件系统与容器中复制文件/文件夹
  create      # 创建一个新容器
  kill        # 杀死一个或多个正在运行的容器
  logs        # 取得容器的日志
  rename      # 重命名一个容器
  restart     # 重新启动一个或多个容器
  rm          # 删除一个或多个容器
  rmi         # 删除一个或多个镜像
  start       # 启动一个或多个已经停止运行的容器
  stats       # 显示一个容器的实时资源占用
  stop        # 停止一个或多个正在运行的容器
  top         # 显示一个容器内的所有进程
```

- `docker run` 命令

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG…]

# 参数
-d --detach   # 后台运行
-it           # 交互式终端（两个参数）
--name        # 指定容器名称
-p --publish  # 将主机端口映射到容器内部的端口。如 -p 8080:80
-v --volume   # 挂载主机文件系统上的目录或文件到容器内部。如 -v /host/path:/container/path
--network     # 指定容器连接的网络。可以使用默认的 bridge 网络，也可以连接到自定义网络
-e --env      # 设置环境变量，将其传递给容器
--rm          # 在容器停止时自动删除容器
--link        # 连接容器到另一个容器，可以通过其他容器的别名来访问
--restart     # 容器重启策略，always、on-failure、unless-stopped 等

# 示例
docker run -it \
    --name texlive \
    -v $HOME/scripts:/workdir/scripts \
    texlive/texlive /bin/bash
```

- 其他命令

```bash
docker container prune  # 删除已停止的容器
docker image prune      # 删除未使用的镜像
docker ps -a            # 查看所有容器（包括已停止的）
```

- 注意事项：
    - `docker run` 时不指定容器名称，会自动分配名称，如 `silly_hawking`，用于临时容器或不需关心容器名称的情况下使用。
    - `docker run` 和 `docker create` 之间的区别：前者是创建容器并运行，后者是只创建容器。
    - `docker pull library/hello-world` 中的 `library/hello-world` 是镜像在仓库的位置，其中 `library` 是镜像所在的组，`hello-world` 是镜像名称；用 `<repository>:<tag>` 格式指定镜像版本，默认以 `latest` 作为默认标签
    - 不同的容器 Registry：

```bash
docker.io/XXX/XXX  # Docker Hub Registry
ghcr.io/XXX/XXX    # GitHub Container Registry
quay.io/XXX/XXX    # Quay.io RedHat Container Registry
```


---

### 制作镜像

- [docker-learning/02、创建一个自己的 Docker Image.md at master · qq20004604/docker-learning · GitHub](https://github.com/qq20004604/docker-learning/blob/master/02%E3%80%81%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E8%87%AA%E5%B7%B1%E7%9A%84%20Docker%20Image.md)

- Docker 忽略文件：`.dockerignore` 写在里面的文件或目录不会被打包到 image 中

- 优秀软件和服务的 Dockerfile 文件（一般）：[GitHub - stilleshan/dockerfiles](https://github.com/stilleshan/dockerfiles)



---

### Docker Compose

[【docker入门2】实战\~如何组织一个多容器项目docker-compose\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Wt411w72h)

- Docker 的多容器控制（容器编排），用于 Docker 自动化；将多个 Docker 容器的操作命令，简化成一条命令，自动完成配置中的容器启动

```bash
docker-compose.yml      # 配置文件
.env                    # 环境变量文件

# docker compose 可写成 docker-compose
docker compose up -d    # 启动 Docker 服务
docker compose pull     # 拉取最新的 Docker 镜像
docker compose stop     # 停止服务
docker compose down     # 停止服务并删除容器
docker compose build    # 根据配置文件构建 Docker 镜像
docker compose ps       # 列出正在运行的服务
docker compose logs     # 日志
```


---

## 相关问题

- [ ] Docker 容器中的数据如何同步（用 rsync，没找到其他好的方法）

- Linux 版的 Docker Desktop 登录比 Windows 和 Mac 端要麻烦一些

- 可通过 Docker 部署的应用（图源：水源社区）

![](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/mac-images/docker.jpeg)

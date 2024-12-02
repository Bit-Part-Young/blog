---
title: GitHub 图床搭建
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: GitHub 图床搭建
description: GitHub 图床搭建
tags:
  - 图床
categories:
  - Win 软件
date: 2022-08-29 00:08:57
abbrlink: 787729
password:
---

# GitHub 图床搭建

## 介绍

- 搭建图床，便于 Markdown 文档、博客文档中的图片同步



---

## 搭建方式

### GitHub + PicGo

- 参考：[使用Github+picGo搭建图床，保姆级教程来了 - 知乎](https://zhuanlan.zhihu.com/p/489236769)

- 搭建步骤：
    - 在 GitHub 上创建存储上传图片的仓库（**该仓库状态需是公开的**），并生成 token，用于 PicGo 访问 GitHub
    - 下载 PicGo 软件，配置 GitHub 图床：设定仓库名、分支名、Token、存储路径、自定义域名

```bash
# 自定义域名可以是 CDN 加速形式的 URL
https://cdn.jsdelivr.net/gh/username/repo
```

- PicGo 其他设置：
    - 禁用 `Ctrl + P` 快捷键
    - 自定义链接格式 `$fileName-$date$extName`（无效果？）
    - 打开 “时间戳重命名”



---

## 应用

- Obsidian：安装 Image Auto Upload Plugin 插件，进行相关设置

- Typora：偏好设置 -- 图片 -- 上传服务，建议选择 PicGo app（而非 PicGo-Core，相关设置更简单一些）；选择 PicGo 路径；验证图片上传选项

- VSCode：安装 PicGo 插件；填写 GitHub 图床设置

```json
{
    // VSCode PicGo 设置
    "picgo.customUploadName": "${fileName}-${date}${extName}",
    "picgo.picBed.current": "github",
    "picgo.picBed.uploader": "github",
    "picgo.picBed.github.repo": "",
    "picgo.picBed.github.branch": "master",
    "picgo.picBed.github.token": "",
    "picgo.picBed.github.path": "",
    "picgo.picBed.github.customUrl": "",
}
```

```bash
# VSCode 相关快捷键
Ctrl + Alt + U      # 从剪贴板上传图像
Ctrl + Alt + E      # 从资源管理器上传图像
Ctrl + Alt + O      # 从输入框上传图像
```



---

## 其他

- GitHub + Cloudflare 搭建图床
    - 方式 1：使用 Cloudflare 中的 Worker；[Github+Cloudflare搭建图床 - Cactus's Blog](https://cactusli.net/tutorial/%E7%BD%91%E7%BB%9C%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/Github_Cloudflare%E6%90%AD%E5%BB%BA%E5%9B%BE%E5%BA%8A.html)
    - 方式 2：使用 Cloudflare 中的 R2 存储桶

```bash
# 填入 PicGo/PicList 中的 GitHub 自定义域名格式
https://<your_domain>/<GitHub_repo>/<repo_branch>
```

- [使用cloudflare+jsdmirror加速github图床访问 - 渊澄](https://ycyc.win/posts/54996)（国内 IP 重定向至 jsdmirror 成功，国外 IP 重定向至 jsDelivr 失败）



---

## 相关问题

- GitHub Token 过期：`StatusCodeError: 401`；更新 Token；[PicGo+GitHub图床配置&常见错误 - Eighty Percent](http://b.aksy.space/study-notes/514.html)

- [SM.MS](https://sm.ms/) 网址失效（另一个常用的图床）；备用网址：[smms.app](https://smms.app)；[Bug SM.MS域名被墙，Picgo无法上传 · Issue #963 · Molunerfinn/PicGo · GitHub](https://github.com/Molunerfinn/PicGo/issues/963)

- [GitHub - 1357310795/SMMS\_Downloader: 下载/备份您在sm.ms图床上传的图片](https://github.com/1357310795/SMMS_Downloader)

- PicGo 平替：[GitHub - XPoet/picx: 🏞️ PicX 是一款基于 GitHub API 开发的图床工具，提供图片上传托管、生成图片链接和常用图片工具箱服务。](https://github.com/XPoet/picx)

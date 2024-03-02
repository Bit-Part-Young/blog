---
title: Github 图床搭建
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Github 图床搭建
description: Github 图床搭建
tags:
  - 图床
categories:
  - 图床
date: 2022-08-29 00:08:57
abbrlink: 7877
password:
---

# Github 图床搭建

## 介绍

搭建图床，便于 markdown 文档、博客文档中的图片同步。



---

## 搭建方式

### Github + PicGo

>[使用Github+picGo搭建图床，保姆级教程来了 - 知乎](https://zhuanlan.zhihu.com/p/489236769)

- 在 Github 上创建存储上传图片的 repo（**该 repo 状态需是公开状态**），并生成 token，用于 PicGo 访问 Github；下载 PicGo 软件，配置 Github 图床：设定仓库名、分支名、Token、存储路径、自定义域名（可以是 CDN 加速形式的 URL；`https://cdn.jsdelivr.net/gh/username/repo`）
- PicGo 其他设置：快捷键（禁用 `Ctrl + P`）；自定义链接格式 `$fileName-$date$extName`（无效果？）；打开“时间戳重命名”



---

## 应用

- Obsidian：安装 Image Auto Upload Plugin 插件，进行相关设置
- Typora：偏好设置 - 图片 - 上传服务，建议选择 PicGo app（而非 PicGo-Core，相关设置更简单一些）；选择 PicGo 路径；验证图片上传选项
- VSCode：安装 PicGo 插件；填写 Github 图床设置；快捷键：
	- `Ctrl + Alt + U` - 从剪贴板上传图像
	- `Ctrl + Alt + E` - 从资源管理器上传图像
	- `Ctrl + Alt + O` - 从输入框上传图像


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


---

## 相关问题

- Github Token 过期：`StatusCodeError: 401`；更新 Token；[PicGo+GitHub图床配置&常见错误 - Eighty Percent](http://b.aksy.space/study-notes/514.html)
- [SM.MS](https://sm.ms/) 网址失效（另一个常用的图床）；备用网址：[smms.app](https://smms.app)；[Bug SM.MS域名被墙，Picgo无法上传 · Issue #963 · Molunerfinn/PicGo · GitHub](https://github.com/Molunerfinn/PicGo/issues/963)

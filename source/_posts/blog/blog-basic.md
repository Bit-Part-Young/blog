---
title: 博客搭建基础
top: false
cover: 
toc: true
mathjax: true
summary: 博客搭建基础
description: 博客搭建基础
tags:
  - Nodejs
categories:
  - 博客
date: 2024-07-11 09:00:00
abbrlink: 110724
password:
---

# 博客搭建基础

## 博客/文档框架类型

>均为静态网页

>大部分框架都需要用到 Node.js（Hugo、Jekyll 除外）

- Jekyll
- Hexo
- Vuepress
- Hugo
- Docusaurus（主要文档）
- MkDocs（主要文档）
- Sphinx（主要文档）
- Wordpress
- Typecho
- …


---

## 域名

域名选择：

- 阿里云：[域名服务价格\_域名注册价格\_域名续费价格\_转入价格 - 阿里云](https://www.alibabacloud.com/zh/domain/pricing)
- 华为云：[价格计算器\_pricing -华为云](https://www.huaweicloud.com/pricing.html#/domains)
- 腾讯云：[域名价格 - 域名注册 - 腾讯云\_域名购买\_交易选购\_转入续费\_DNSPod](https://buy.cloud.tencent.com/domain/price)
- `.top` 域名价格较便宜（20+），`.xyz` 较贵（70+）

---

域名绑定：

- [如何搭建自己的个人网站（上） - Zhang Yi](http://codewithzhangyi.com/2018/04/19/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99%EF%BC%88%E4%B8%8A%EF%BC%89/)
- [如何搭建自己的个人网站（下） - Zhang Yi](http://codewithzhangyi.com/2018/04/20/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99%EF%BC%88%E4%B8%8B%EF%BC%89/)
- 在 username.github.io 仓库的 settings - General - Custom domain 中填入自己的域名，等待几天，看 Enforce HTTPS 选项是否可以勾选

![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307211853528.png)



---

## Node.js

- Node.js： A JavaScript runtime built on Chrome's V8 JavaScript engine 是一个不依赖浏览器的 JavaScript 运行环境，大部分前端项目比如 Vue、React 和后端项目比如 Express、Koa 均依赖于 Node.js 生态系统；
- Node.js 版本分支：`nodejs`（稳定版本，包括最新的功能和改进） 和 `nodejs-lts`（长期支持版本，LTS）


---

### 安装

```bash
curl -sS https://webi.sh/node | sh

source ~/.config/envman/PATH.env
```


---

### npm 相关命令

```bash
# 项目初始化，引导创建 package.json 文件
npm init

# 项目快速初始化（默认设置，跳过交互式设置）
npm init -y

# 安装依赖
npm install  # npm i
npm install <package>
# 将 package 保存到 package.json 中；默认会保存
npm install <package> --save  # npm i <package> -S
npm install <package>@1.0.0
# 全局安装
npm install -g <package>

# 安装 pnpm 和 yarn 包管理器
npm install -g pnpm yarn

# 卸载
npm uninstall

# 搜索
npm search

# 列出当前项目的所有依赖项
npm list

# 检查项目中的依赖项是否有更新的版本可用
npm outdated

# 检查项目的依赖项是否存在安全漏洞，并提供修复建议
npm audit
npm audit fix --force
npm audit fix

# 删除不在 package.json 文件中的依赖项
npm prune

# 运行在 package.json 文件中定义的脚本命令
npm run

# 验证 npm 缓存，并删除旧的缓存内容
npm cache verify

# 强制删除 npm 缓存
npm cache clean --force

npm config get registry
yarn config get registry

# 设置镜像源
npm config set registry http://registry.npmmirror.com
```

---

>[nvm,npm与nrm](https://fe32.top/articles/9r95s1wt/#nvm-%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)

- nvm：Node Version Manager， Node.js 版本管理器
- n：Node.js 版本管理器
- npm：Node Package Manager，Node.js 包管理器；npm 缓存路径：`~/.npm
- nrm：NPM registry manager，npm 源管理器
- npx：随 npm 一起安装的工具，用于执行 npm 包中的命令，而无需全局安装这些包。适用于一次性或少见使用的命令。
- 项目本地安装的包的命令路径：`./node_modules/.bin/command-name`

```bash
# 执行指定命令
npx <command>

# 查找将要运行的命令的路径
npx which <command>

# 检查系统设置，以查找可能影响 npx 运行的问题，并提供解决方案
npx doctor

# 执行指定的命令字符串
npx -c <command-string>
npx -c "node -v && npm -v"

npx taze      # 查看 package.json 中的依赖是否是最新
npx taze -w   # 更新并写入 package.json
```


---

## 其他

[搭建 CDN | Argvchs の小窝](https://argvchs.github.io/2023/01/05/build-cdn/)

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
  - Cloudflare
categories:
  - 博客
date: 2024-07-11 09:00:00
abbrlink: 110724
password:
---

# 博客搭建基础

## 网络基础知识

- [lec6：网络/网站基础知识概述 - 2023秋冬实用技能拾遗](https://slides.tonycrane.cc/PracticalSkillsTutorial/2023-fall-ckc/lec6/)

- CDN：内容分发网络，其原理大概是将服务内容分发至全网加速节点，让用户从就近的服务器节点上获取内容，从而提高网站的访问速度。

- 回环地址（Lookback address）：用于主机的自身通信，不会发送到网络上

```bash
127.0.0.1  # IPv4
::1        # IPv6
localhost  # 主机名
```

- 查看是否有 IPv6 地址：
    - [IPv6 测试](https://test-ipv6.com/)
    - [ipv6 test](https://ipv6-test.com/)



---

## 博客/文档框架类型

>大多为静态网页

>大部分框架都需要用到 Node.js（Hugo、Jekyll 除外）

- Jekyll
- Hexo
- Vuepress
- Vitepress
- Hugo
- Docusaurus（主要文档）
- MkDocs（主要文档）
- Sphinx（主要文档）
- WordPress
- Typecho
- ...


---

## 域名

域名选择：

- 阿里云：[域名服务价格\_域名注册价格\_域名续费价格\_转入价格 - 阿里云](https://www.alibabacloud.com/zh/domain/pricing)
- 华为云：[价格计算器\_pricing -华为云](https://www.huaweicloud.com/pricing.html#/domains)
- 腾讯云：[域名价格 - 域名注册 - 腾讯云\_域名购买\_交易选购\_转入续费\_DNSPod](https://buy.cloud.tencent.com/domain/price)
- Cloudflare 域名价格：[Cloudflare Domain Pricing](https://cfdomainpricing.com/)
- `.top` 域名价格较便宜（￥20+/年），`.xyz` 较贵（￥70+/年）

- [ ] 是否考虑转移到便宜的域名


---

域名绑定：

- [如何搭建自己的个人网站（上） - Zhang Yi](http://codewithzhangyi.com/2018/04/19/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99%EF%BC%88%E4%B8%8A%EF%BC%89/)
- [如何搭建自己的个人网站（下） - Zhang Yi](http://codewithzhangyi.com/2018/04/20/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99%EF%BC%88%E4%B8%8B%EF%BC%89/)
- 在 username.github.io 仓库的 settings - General - Custom domain 中填入自己的域名，等待几天，看 Enforce HTTPS 选项是否可以勾选

![Untitled](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202307211853528.png)



---

## 使用 Cloudflare 作为 DNS 服务器

- 注册/登录 Cloudflare 账号

- 添加域名到 Cloudflare
    - 点击 Dashboard 中的 “Add Site”，输入你的域名

- 选择计划：选择 “Free Plan”，确认

- Cloudflare 检查现有 DNS 记录
    - Cloudflare 会自动扫描你的域名的现有 DNS 记录并尝试导入它们。
    - 核对导入的记录，确保重要记录如 MX, CNAME, A 记录等都正确无误。

- 更新域名服务器
    - Cloudflare 会提供一对新的 DNS 服务器地址
    - 登录到你的域名注册商，导航至 DNS 管理页面，将现有的 DNS 服务器地址更换为 Cloudflare 提供的地址，保存更改

- 等待 DNS 更改生效：DNS 更改可能需要一些时间（1 小时到 48 小时，通常小于 1 小时，10 分钟以内）来全球生效

- 调整 Cloudflare SSL/TLS mode 为 `Full(strict)



---

## Cloudflare 代理访问 vercel.app 网站

>[使用 VitePress “重写” 网道（WangDoc）TypeScript 教程 · Issue #4837 · ruanyf/weekly · GitHub](https://github.com/ruanyf/weekly/issues/4837)

在国内并不能无痛访问 vercel.app 网站；Free 计划只能 connect 5 个 Git Repository（可创建的 project 数目多于 5 个，但也有数量限制）

注册/登录 Cloudflare 账号，然后：

- 准备一个域名，该域名需要使用 Cloudflare 提供的 DNS
- Vercel 项目（假如为 xxx） - 设置 - 域名配置，新增域名
    - 若已有域名如 seekanotherland.xyz，可以新增的域名为 xxx.seekanotherland.xyz
    - 可以将该域名重定向到 xxx.vercel.app，也可以不重定向（建议不重定向）

- 按照 Vercel 的要求，为域名添加 CNAME 记录
    - 在 Cloudflare 面板中的 DNS 中添加记录，cname.vercel-dns.com 对应的 IPV4 地址为 76.76.21.21



---

## 部署

>不同部署方式对比：[静态博客部署方式](https://blog.17lai.site/posts/5311b619/#%E5%90%84%E7%A7%8D%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F)

>[部署到 Vercel 或 Netlify](https://argvchs.github.io/2022/04/17/hexo-blog-4/)

>[Gitee Pages 介绍](https://help.gitee.com/services/gitee-pages/intro)

- GitHub Pages 部署：略

- Vercel 部署：
    - GitHub - Settings - Integrations - Applicaitons - 配置 Vercel，Repository access，在 Only select repositories 选择 repo（多于 5 个时，在 vercel 中只能显示 5 个）
    - GitHub 登录 [Vercel](https://vercel.com/login) - 首页 - New project - Import Git Repository - Deploy
    - 点击 Goto Dashboard 来到项目主页，选择顶部的 Settings，在 Project Name 中更改网站名称

- Netlify 部署：
    - GitHub 登录 [Netlify](https://app.netlify.com/)- 首页 - Add new site 中的 Import an existing project，点击 GitHub，与 GitHub 关联，选择仓库 Deploy - 项目主页，选择 Site settings，点击 Change site name 更改网站名称
    - 域名设置：[稳定性超过GitHub的美国netlify静态主机\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1wG411J7XX/)
    - [【CI/CD】Github Actions部署网站到Netlify\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1PG4y1r7DR)

- Cloudfale Pages 部署：
    - [Cloudflare Pages 自动化部署 Github 项目指南 | Indie Hacker Tools](https://indiehackertools.net/blog/cloudflare-pages-guide-automating-deployment-of-github-projects)
    - [Hi , Cloudflare Pages :: 木木木木木](https://immmmm.com/hi-cloudflare/)

- Vercel 部署时忽略 GitHub Actions 生成的 gh-pages 分支：[Vercel deploy忽略指定分支 | Oragekk's Blog](https://oragekk.me/tutorial/CI_CD/vercel-deploy.html)；选择 preject - Settings - Git - Ignored Build Step，选择 Only build production

- Cloudflare Pages 部署时忽略 GitHub Actions 生成的 gh-pages 分支：选择 preject - 设置 - 构建与部署，禁用预览分支的自动部署

- 个人部署设置：
    - Hexo、Jekyll、Docusaurus、Vuepress 和 Vitepress 框架等其他前端代码由 Vercel 部署
    - MkDocs 和 Hugo 框架由 Cloudflare Pages 部署

- Vercel 部署 Vuepress 框架失败：将 Vuepress 框架选择成 Other；[vercel部署失败，提示Error: ENOENT: no such file or directory, stat '/vercel/path0/src' · Issue #11647 · DIYgod/RSSHub · GitHub](https://github.com/DIYgod/RSSHub/issues/11647)



---

## 其他

- TCP/UDP 协议：均在传输层（待完善）

- [NGINX 配置 - 配置高性能、安全、稳定的NGINX服务器的最简单方法](https://www.digitalocean.com/community/tools/nginx?global.app.lang=zhCN)

- [Cloudflare浑身都是宝，普通用户能白嫖多少服务？盘点cloudflare的免费功能](https://mp.weixin.qq.com/s/ComwejsgG3f8W_AVJccwGQ)

- [使用 GitHub Actions 通过 acme.sh 自动申请 SSL 证书](https://github.com/danbao/auto-ssl)

- [GitHub - BitAUR/Puff: 开源、快速、便捷、基于Go的域名监控程序。](https://github.com/bitaur/puff)

- 优选 IP：[CloudflareSpeedTest](https://github.com/XIU2/CloudflareSpeedTest)

- 反向代理：
    - nginx：[【nginx入门】nginx反向代理与负载均衡教程\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Bx411Z7Do/)
    - [GitHub - Mc-Zen/zero: Advanced scientific number formatting for Typst.](https://github.com/Mc-Zen/zero)

- 自动获得公网 IPv4 或 IPv6 地址，并解析到对应的域名服务：[GitHub - jeessy2/ddns-go](https://github.com/jeessy2/ddns-go)
    - [外网访问家庭内网的两大最优方案，零基础教程 远程控制家庭电脑 ，公网访问家庭局域网\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV15T421X7aa)

- [GitHub - zanjie1999/cloudflare-api-v4-ddns: cloudflare 一键 ddns 脚本 (大陆可用)](https://github.com/zanjie1999/cloudflare-api-v4-ddns)

- 查询 DNS 在全球各地的解析结果：[GitHub - ccbikai/DNS.Surf: Querying DNS Resolution Results in Different Regions Worldwide.](https://github.com/ccbikai/DNS.Surf)

- [搭建 CDN - Argvchs の小窝](https://argvchs.github.io/2023/01/05/build-cdn/)

- 提供 DNS 查询的 API：[DNS.fish - Command-line DNS Record Lookup Tool](https://dns.fish/)

- Cloudflare R2 需要先添加订阅（免费额度：10GB/月），建议使用 PayPal 方式，可以使用银联银行卡；添加 Bucket，之后可以添加文件或文件夹；管理 API Token

- [ ] 如何进行 ICP 备案

- [ ] 如何白嫖域名（限制较多，不建议）：[2024最新免费域名教程，可托管CF，零失败率，解决所有坑点。\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1by411B7Ko/)

- [ ] 如何租服务器

- [ ] Cloudflare 代理域名 DNS 后，经常出现如下错误，如何解决（有时正常）

```bash
SSL handshake failed Error code 525
```

- [ ] 如何取消 Cloudflare 代理域名 DNS



---

## Node.js

- Node.js： A JavaScript runtime built on Chrome's V8 JavaScript engine 是一个不依赖浏览器的 JavaScript 运行环境，大部分前端项目比如 Vue、React 和后端项目比如 Express、Koa 均依赖于 Node.js 生态系统；
- Node.js 版本分支：`nodejs`（稳定版本，包括最新的功能和改进） 和 `nodejs-lts`（长期支持版本，LTS）
- [GitHub - sindresorhus/awesome-nodejs: Delightful Node.js packages and resources](https://github.com/sindresorhus/awesome-nodejs)


---

### 安装

- 方式 1：官网安装：[Download Node.js](https://nodejs.org/en/download/package-manager)

- 方式 2：

```bash
curl -sS https://webi.sh/node | sh

source ~/.config/envman/PATH.env
```


---

### npm 相关命令

```bash
# 项目初始化
npm init         # 引导创建 package.json 文件

# 项目快速初始化
npm init -y      # 默认设置，跳过交互式设置

# 安装依赖
npm install                    # 等同于 npm i
npm install <package>          # 安装特定 package
# 写入 package.json 中；默认会
npm install <package> --save   # npm i <package> -S
npm install <package>@version  # 安装特定 package 及版本
npm install -g <package>       # 全局安装
npm install -g pnpm yarn       # 安装 pnpm 和 yarn 包管理器

npm uninstall                  # 卸载
npm search                     # 搜索
npm list                       # 列出当前项目的所有依赖
npm outdated                   # 检查项目中的依赖是否有更新
npm outdated -g                # 全局
npm update -g                  # 跟新全局的包
npm outdated -g --depth=0      # 同上

npm audit                      # 检查项目依赖是否存在安全漏洞，并提供修复建议
npm audit fix
npm audit fix --force

npm prune                      # 删除不在 package.json 文件中的依赖项
npm run                        # 运行在 package.json 文件中定义的脚本命令
npm cache verify               # 验证 npm 缓存，并删除旧的缓存内容
npm cache clean --force        # 强制删除 npm 缓存

npm config get registry        # 查看源；npm 可改成 yarn
npm config set registry        # 设置镜像源

npm config set registry https://registry.npmmirror.com
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
npx <command>        # 执行指定命令
npx which <command>  # 查找将要运行的命令的路径
npx doctor  # 检查系统设置，查找影响 npx 运行的问题，并提供解决方案
npx -c <command-string>  # 执行指定的命令字符串

npx taze      # 查看 package.json 中的依赖是否是最新
npx taze -w   # 更新并写入 package.json
```

---

Corepack 是 Node.js 的一个实验性功能，通过自动管理和调用 JavaScript 包管理器的特定版本，如 yarn 和 pnpm（可以使用 yarn 的开发版本 4.3.1，稳定版本为 1.22.xx）

```bash
corepack enable   # 开启
corepack disable  # 取消
```

npm 配置文件：`.npmrc`

```bash
auto-install-peers=true

# 设置镜像源
registry=https://registry.npmmirror.com
```

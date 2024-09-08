---
title: Vuepress、Vitepress 框架
top: false
cover: 
toc: true
mathjax: true
summary: Vuepress、Vitepress 框架
description: Vuepress、Vitepress 框架
tags:
  - Vuepress
  - Vitepress
categories:
  - 博客
date: 2023-10-21 09:00:00
abbrlink: 102123
password:
---

# Vuepress、Vitepress 框架

## 介绍

- 较为简洁的文档 & 博客框架
- Vitepress 框架内容主要针对 Vuepress 1.x 版本（2.x 测试效果不太好）
- Vitepress 框架与其非常像（项目文件结构及配置；Vitepress 搭建比 Vuepress 简单；故不重复介绍）

- Vitepress 框架官网：[VitePress - 由 Vite 和 Vue 驱动的静态站点生成器](https://vitepress.dev/zh/)

- Vuepress 框架主题：
	- [reco 1.x 版本](http://v1.vuepress-reco.recoluan.com/)
	- [reco 2.x 版本](https://github.com/vuepress-reco/vuepress-theme-reco)（功能偏冗余）
	- [vuepress-theme-hope](https://github.com/vuepress-theme-hope/vuepress-theme-hope)

- 参考资料：
	- [GitHub - vuepress/awesome-vuepress: 🎉 A curated list of awesome things related to VuePress](https://github.com/vuepress/awesome-vuepress)



---

## 使用

### 快速搭建

- Vuepress 框架快速搭建

```bash
mkdir vuepress-demo && cd $_

yarn init  # 初始化项目

# 添加 scripts

# 安装 reco 主题
# 可以不安装主题，其余设置均一样
yarn add vuepress-theme-reco --dev

mkdir docs
echo '# Hello VuePress' > docs/README.md

# yarn 可替换成 pnpm、npm run
yarn docs:dev    # 本地预览
yarn docs:build  # 构建

# 若 build 时报错
# 通常是由于 Node.js 版本与 crypto 模块的兼容性问题引起的
# 方式 1 添加环境变量
export NODE_OPTIONS=--openssl-legacy-provider
# 方式 2  修改 package.json 中的 build 参数值
"docs:build": "NODE_OPTIONS=--openssl-legacy-provider vuepress build docs"
```

- 在 `package.json` 中添加 `scripts` 参数

```json
{
  "scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  }
}
```

- Vitepress 框架快速搭建

```bash
mkdir vitepress-demo && cd $_

# npm 可替换成 yarn、pnpm
npm add -D vitepress

npx vitepress init    # 初始化 

npm run docs:dev      # 本地预览
npm run docs:build    # 构建
npm run docs:preview  # 构建后预览
```

---

- 目录结构

```text
├── docs/
│   ├── .vuepress/      # .vitepress/
│   │   ├── config.js   # 配置文件 config.mjs
│   └── README.md
├── package.json
```


---

### 部署

- GitHub Actions 示例（Vitepress 框架部署时只需将 `.vuepress` 修改为 `.vitepress`）

```yaml
name: Vuepress Depoly

on:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  docs:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: latest
          cache: yarn

      - name: Install dependencies
        run: yarn
      - name: Build VuePress site
        run: yarn docs:build

      - name: Deploy to GitHub Pages
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: gh-pages
          build_dir: docs/.vuepress/dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```


---

### 配置

- [默认主题配置 - VuePress](https://v1.vuepress.vuejs.org/zh/theme/default-theme-config.html)

- 参考配置：[awesome-fenix/.vuepress/config.js at master · fenixsoft/awesome-fenix · GitHub](https://github.com/fenixsoft/awesome-fenix/blob/master/.vuepress/config.js)

- `docs/.vuepress/config.js` 文件常用参数设置
	- md 文档中的 title front matter 会与正文的一级标题均会渲染，导致重复，其他框架不会有该情况

```js
module.exports = {
  title: 'xxx',  // 网站标题
  description: 'xxx',  // 网站描述
  base: '/repo-name/',  // 通常为 GitHub repo name

  // 主题配置
  themeConfig: {

    // 在页面下方添加最后更新时间
    lastUpdated: 'Last Updated',

    // 搜索
    search: true,
    searchMaxSuggestions: 10,

    // 导航栏
    navbar: [
      // 普通导航栏
      { text: '首页', link: '/' },
      { text: '指南', link: '/guide/' },
      // 下拉菜单导航栏
      {
        text: '更多',
        children: [
          { text: '项目', link: '/projects/' },
          { text: '关于', link: '/about/' },
        ],
      },
    ],

    // docs 侧边栏配置 含多级子目录示例
    sidebar:[
        {
            title: '科研工具',
            path: '/scitoolkits/',
            collapsable: false,
            children: [
                {title: 'LAMMPS 安装', path: 'scitoolkits/lammps-install'},
                {
                    title: 'atomate',
                    path: 'scitoolkits/atomate/',
                    collapsable: false,
                    children: [
                        {title: 'atomate 安装与使用', path: 'scitoolkits/atomate/atomate-usage'},
                    ]
                },
    ],
    ...
  }
}
```

- Vitepress 框架配置（配置文件：`docs/.vitepress/config.js`）：

```js
import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "xxx",
  description: "xx",
  base: '/repo-name/',

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config

    docFooter: {
      prev: '上一页',
      next: '下一页'
    },

    footer: {
      message: '基于 MIT 许可发布',
      copyright: `版权所有 © 2024-${new Date().getFullYear()}`
    },

    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'medium'
      }
    },

    // 导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '笔记', link: 'scitoolkits/lammps-install' }
    ],

    // docs 侧边栏配置 含多级子目录示例
    sidebar: [
      {
        text: '科研工具',
        collapsed: false,
        items: [
            {text: 'LAMMPS 安装', link: 'scitoolkits/lammps-install'},
            {   
                text: 'atomate',
                collapsed: false,
                items: [
                    {text: 'atomate 安装与使用', link: 'scitoolkits/atomate/atomate-usage'},
                ]
            },
    ],
    ...
  }
}
```

- Vitepress 与 Vuepress 框架中 sidebar 参数配置差异
	- text - title, collapsed - collapsable, items - children, link - path
	- 多级子目录下，Vitepress 框架下不能有 index.md 文件，而 Vuepress 框架允许有

- reco v1.x 版本配置参考：[Vuepress-theme-reco-v1.x 新手指北之Hello烤鸭 | latte and cat](https://blog.latteandcat.cn/blogs/frontend/2023/theme-reco-1.x.html)

- reco v1.x 版本常用参数设置：
	- 有分类、标签和时间轴功能，因此可不用设置 docs 子目录的导航栏
	- 会预设一些插件（如 一键从页面底部到顶部）
	- **md 文档的目录侧边栏可自动生成，docs 的侧边栏仍需手动生成，较繁琐**

```js
  // 移动端优化
  head: [
    ['meta', { name: 'viewport', content: 'width=device-width,initial-scale=1,user-scalable=no' }]
  ],

  themeConfig: {

   // md 文档目录侧边栏 右侧
    subSidebar: 'auto',
    sidebarDepth: 5,

    startYear: '2024',

    // 关闭 404 页面腾讯公益
    noFoundPageByTencent: false,

    type: 'blog',

    blogConfig: {
        category: {
          location: 2, // 在导航栏菜单中所占的位置，默认 2
          text: '分类' // 默认文案 “分类”
        },
        tag: {
          location: 3, // 在导航栏菜单中所占的位置，默认 3
          text: '标签' // 默认文案 “标签”
        }
    },

    nav: [
      // 添加时间轴和 GitHub 链接
      { text: '时间轴', link: '/timeline/', icon: 'reco-date' },
      { text: 'GitHub', link: 'https://github.com/username', icon: 'reco-github' }
    ],

  }
```


---

### 搜索功能

Vuepress 和 Vitepress 框架均支持使用 Algolia DocSearch 搜索文档站点

```js
// docs/.vuepress/config.js
module.exports = {
  themeConfig: {
    // ...
    algolia: {
      appId: 'XXX',
      apiKey: 'XXX',
      indexName: 'XXX'
    },
    // ...
  }
}
```

```js
// docs/.vitepress/config.js
export default defineConfig({
  themeConfig: {
    // ...
    search: {
      provider: 'algolia',
      options: {
        appId: '...',
        apiKey: '...',
        indexName: '...'
      }
    },
    // ...
  }
})
```

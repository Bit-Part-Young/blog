---
title: Hexo 框架
top: false
cover:
toc: true
mathjax: true
summary: Hexo 框架
description: Hexo 框架
tags:
  - Hexo
categories:
  - 博客
date: 2023-10-21 09:00:00
abbrlink: 403157
password:
---

# Hexo 框架

## 介绍

- 官网：[Hexo](https://hexo.io/)

- 主题：
	- [Hexo 框架主题集合](https://hexo.io/themes/)
	- [butterfly](https://github.com/jerryc127/hexo-theme-butterfly)
	- [matery](https://github.com/blinkfox/hexo-theme-matery)
	- [icarus](https://github.com/ppoffice/hexo-theme-icarus)
	- [volantis](https://github.com/volantis-x/hexo-theme-volantis/)
	- [fluid](https://github.com/fluid-dev/hexo-theme-fluid)
	- [stun](https://github.com/liuyib/hexo-theme-stun)
	- [maupassant](https://github.com/tufu9441/maupassant-hexo)（简洁风）
	- [keep](https://github.com/XPoet/hexo-theme-keep)
	- 下载 matery 主题后，需将其 `.git` 删除（否则 Github Actions 部署的内容为空白；matery 主题设置不是很灵活，不是很推荐；butterfly 不会，推荐该主题）
	- butterfly 主题的预设功能比 matery 更丰富

- 博客网站实例：
	- stun 主题：[OrangeX4's Blog](https://orangex4.cool/)
	- butterfly 主题：[Risc\_lt的杂货铺 - Code/Life Balence](https://risc-lt.github.io/)（交大学生博客）

- 参考资料：
	- [Hexo 入门](https://blog.17lai.site/posts/40300608/#Hexo%E5%85%A5%E9%97%A8%E7%AF%87)
	- [Hexo 压缩静态文件 - Argvchs の小窝](https://argvchs.github.io/2022/08/27/hexo-minify-static-files/)
	- [资源压缩部署加速网站访问](https://ninojay.top/hexoplugin/hexo-all-minifier/)（A4 主题）



---

## 使用

### 快速搭建

- 快速搭建（以 butterfly 主题为例）

```bash
# 安装 Hexo
npm install -g hexo-cli

# 项目初始化
hexo init hexo-demo & cd $_  # 方式 1
mkdir hexo-demo & cd $_ & hexo init  # 方式 2

# 安装依赖
npm i

# 安装主题
# 非 butterfly，建议将 theme 中的 .git 删除
git clone -b dev https://github.com/jerryc127/hexo-theme-butterfly.git themes/butterfly
# 拷贝主题配置文件到根目录；非 butterfly 不一定适用
cp /butterfly/_config.yml _config.butterfly.yml

# 安装主题依赖
npm i hexo-theme-butterfly --save

# 将 CNAME 文件放入 source 目录，以解析域名
```

---

- 目录结构

```bash
├── _config.yml   # 配置文件
├── package.json  # 应用信息
├── scaffolds/    # 模板文件夹
├── source/       # 源文件夹
|   └── _posts/   # post 文件夹；md 文档可直接放于此，或归类成子目录
└── themes/       # 主题文件夹
```

---

- 配置文件

```bash
# 配置文件
_config.yml              # 全局配置文件
themes/XXX/_config.yml   # 主题配置文件

# _config.yml 基本内容
title                    # 网站标题
subtitle                 # 副标题
description              # 网站描述
keywords                 # 网站关键词
author                   # 作者
language                 # 语言
timezone                 # 时区
url                      # 网址
theme                    # 主题；butterfly 等

# _config.theme.yml` 内容
# 自定义修改
```


---

### 常用命令

>[Hexo 命令](https://hexo.io/zh-cn/docs/commands)

```bash
# 构建
hexo g  # hexo generate; npm run build
hexo g --watch  # 监视文件变动
hexo g --debug  # debug

# 实时预览
hexo s  # hexo server; npm run server
hexo s -p 5000  # 更改端口

# 部署
hexo d  # hexo deploy; npm run deploy
hexo g -d  # 构建后部署

# 清除缓存文件 db.json 和静态文件 public/
hexo clean  # hexo cl
```


---

### 部署

 - 设置 `_config.yml` 中的 `deploy` 选项（需安装 hexo-deployer-git 插件）

```yaml
deploy:
  type: git
  # repo public private 都可以
  repository: git@github.com:username/repo.git
  branch: main
```

---

- Github Actions 示例

```yaml
name: Hexo deploy

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - name: Use latest Node.js
        uses: actions/setup-node@v4
        with:
          node-version: latest
      - name: Cache NPM dependencies
        uses: actions/cache@v4
        with:
          path: node_modules
          key: ${{ runner.OS }}-npm-cache
          restore-keys: |
            ${{ runner.OS }}-npm-cache
      - name: Install Dependencies
        run: npm install
      - name: Build
        run: npm run build
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```


---

### 插件

- 参考：[hexo 使用记录 - 鹤翔万里的笔记本](https://note.tonycrane.cc/cs/tools/hexo/)

- hexo-generator-index/archive/category/tag：初始化 Hexo 项目会自动安装；生成主页 / 归档 / 分类 / 标签文件夹

- hexo-abbrlink：生成短链接，而非 post 中的 md 文件名

```yml
# permalink: :year/:month/:day/:title/
permalink: posts/:abbrlink.html
permalink_defaults:
pretty_urls:
  trailing_index: true # Set to false to remove trailing 'index.html' from permalinks
  trailing_html: true # Set to false to remove trailing '.html' from permalinks
```

- hexo-blog-encrypt：文章加密，只需要在 md 的文件 Front Matter 加上：

```yml
password: ...
```

- hexo-generator-feed：生成 RSS 订阅 xml 文件

```yml
feed:
  enable: true
  type: atom
  path: atom.xml
  limit: 20
```

- hexo-generator-index-pin-top：文章置顶，只需要在 md 的文件 Front Matter 加上：

```yml
top: true
```

- hexo-generator-search/searchdb：本地搜索设置

- hexo-algoliasearch 或 hexo-algolia：Algolia 搜索；更美观（Hexo butterfy，Docusaurus 支持，MkDocs 将支持）

- [hexo-tag-publications](https://github.com/njzjz/hexo-tag-publications)：由 bib 文件生成论文统计与信息展示网页（可单个、全部论文）
	- 在页面添加论文概要图片，在 bib 文件中的论文对应条目下添加 `image` 参数



---

## 主题设置

- butterfly 主题文章置顶 front-matter 参数：`sticky`，数值越大，置顶优先级越大
- matery 主题文章置顶 front-matter 参数：`top`，数值为 `true` 或 `false`

---

### butterfly

参考：

- [Butterfly - A Simple and Card UI Design theme for Hexo](https://butterfly.js.org/)
- [基于 Hexo 从零开始搭建个人博客系列 - 唐志远](https://fe32.top/articles/hexo1600/)
- [标签: Hexo - Justlovesmile's BLOG](https://blog.justlovesmile.top/tags/Hexo/)
- [重构博客记录\~ - 鹊楠の小窝](http://blog.quenan.love/posts/ae5416c7/index.html)

---

- 菜单栏 menu（分类、标签、存档；友链、关于、音乐、视频、相册等暂无必要）
- 网站 logo、个人头像、social 相关信息
- 代码
- 目录
- banner 图片
- 文章封面（Front Matter 中 cover 参数值为空，表示随机封面）
- 评论系统（暂无必要）
- 搜索系统（Algolia）
- 页面加载效果
- post 元信息（分类、标签、时间、字数统计、需阅读时间等）
- 侧边栏（butterfly）
- Footer 页脚信息
- 内容复制时、文章底部版权相关信息（内容复制建议不加版权信息）
- 日期过期提醒（noticeOutdate；失效？）
- 图片懒加载
- 相册（暂无必要）
- 右下角功能按钮（深/浅色切换，直达页面顶部等功能）
- 音乐、视频页面（音乐可全局吸底）
- [x] 添加 RSS 订阅功能：[为Butterfly主题添加RSS订阅 - InsectMk的个人空间](https://insectmk.cn/posts/d1271256/)

---

自定义修改 Footer 页脚信息：`themes/butterfly/layout/includes/footer.pug`



---

### matery

参考：

- 官方：[matery主题基本设置](https://blog.17lai.site/posts/40300608/#Hexo%E5%9F%BA%E7%A1%80%E9%85%8D%E7%BD%AE%E7%AF%87)
- [Matery主题搭建与优化教程超详细解析 - 小弋の生活馆](https://lovelijunyi.gitee.io/posts/b8ec.html)
- [Hexo 标签 - Lu's blog](https://islu.cn/tags/Hexo/)
- [小弋の生活馆全样式预览 - 小弋の生活馆](https://lovelijunyi.gitee.io/posts/c898.html)

---

**已解决/实现**：

- [x] 首页设置的音乐播放功能；文章内部音乐播放设置功能；如何设置单独页面音乐播放
- [x] 单独视频页面效果如何制作（和单独相册页面类似，但简单一些；如何放入多个视频？）
- [x] 离开博客标签页，出现可爱字体
- [x] 屏蔽网页源码（单纯的屏蔽鼠标右键和键盘事件；慎重添加）

- [x] 设置评论系统
	- 采用 waline（**可以实现不登录即可提交评论，也可以登录提交评论**）[快速上手 - Waline](https://waline.js.org/guide/get-started/)
	- valine 无人维护更新
	- 使用 gitalk 遇到的一些问题：其他人登录评论系统会出现 “网络错误”；所需要的权限过多

- [x] `hexo d` 后，CNAME 文件会被删除 [hexo部署后，CNAME会被自动删除，怎么办？ - 知乎](https://www.zhihu.com/question/28814437)：将需要上传至 GitHub 的内容放在 source 目录，例如 CNAME、favicon.ico、images 等

- [x] PC 端访问人数和访问量消失；手机端无看板娘，访问人数和访问量正常 [基于Hexo的matery主题搭建博客常见问题篇6 | 夜法之书](https://blog.17lai.site/posts/84b4059a/#busuanzi%E4%B8%8D%E8%92%9C%E5%AD%90%E8%AE%A1%E6%95%B0%E6%98%BE%E7%A4%BA%E5%BC%82%E5%B8%B8%EF%BC%8C%E4%B8%80%E9%97%AA%E5%B0%B1%E6%B2%A1)

- [x] RSS 订阅功能 [你可以用 RSS 订阅我的博客了 - 彭宏豪的个人博客，个人电子产品使用心得](https://penghh.fun/2021/05/18/2021-5-18-blogupdate/)、[GitHub - anyant/rssant: 蚁阅 - 让 RSS 更好用，轻松订阅你喜欢的博客和资讯](https://github.com/anyant/rssant)

- [ ] 不显示文章的图片和 summary，文章内容只能跳转到原链接上看

- [x] 博客密码 [在线加密解密](https://tool.oschina.net/encrypt?type=2)、[请问大佬这个文章密码的具体配置写法是什么样的？ · Issue #362 · blinkfox/hexo-theme-matery · GitHub](https://github.com/blinkfox/hexo-theme-matery/issues/362)

- md 文章中的 password 键的值需填写 SHA256 加密后的值
- 博客文章输入的值为 SHA256 加密前的原值
- 有破解的方法

- [x] 背景颜色：修改前：`#4cbf30`, `#0f9d58`；现在的：`#d9ed92` `#99d98c`；修改后：`48cae4` `0096c7`

- [x] 博客插入音乐、B 站视频 [hexo博客插入b站视频 - Lyz](https://blog.liguapi.top/2022/03/07/page-1/)

```html
<!-- markdown 中插入 B 站视频语法格式 --> 
<div 
     style="position: relative; width: 100%; height: 0; padding-bottom: 75%;">
    <iframe 
            src="//player.bilibili.com/player.html?aid=984726281&bvid=BV1Nt4y1n7hv&cid=807808976&page=1"
            scrolling="no" 
            border="0" 
            frameborder="no" 
            framespacing="0" 
            allowfullscreen="true" 
            style="position: absolute; width: 100%;height: 100%; left: 0; top: 0;"> 
    </iframe>
</div>
```

- [x] 修改滚动条：在 `themes/Matery/source/css/matery.css` 添加代码
- [x] 添加 loading-page（加载动画）[Matery 添加加载动画 | 斯莫笔记](https://small-rose.github.io/posts/7496029d.html)
- [x] 添加导航页（里面的相关链接待修改；必要性不大）
- [x] 添加标签外挂（其他框架可能无法使用） [小弋の生活馆全样式预览 | 小弋の生活馆](https://lovelijunyi.gitee.io/posts/c898.html)

---

**待解决/实现**：

- [ ] 博客底部的文章链接出现 2 个 hexo-demo，暂无法解决
- [ ] CDN 加速
- [ ] 添加 GitHub badge（添加代码的位置需自己调整，尽量恰当）
- [ ] 添加思维导图渲染
- [ ] markdown 的复选框在 hexo 中无法正确渲染
- [ ] 让博客支持通知功能
- [ ] 豆瓣书单电影页面
- [ ] 自定义主题字体
- [ ] 相册的宽度和高度大小设置在 matery.css 文件中
- [ ] 测试 404 页面（404 页面未起作用）
- [ ] 换装、对话的看板娘（有些复杂；暂无必要）[GitHub - stevenjoezhang/live2d-widget: 把萌萌哒的看板娘抱回家 (ノ≧∇≦)ノ | Live2D widget for web platform](https://github.com/stevenjoezhang/live2d-widget)
- [ ] 为 Hexo 博客中的 Markdown 添加卡片式链接支持 [为 Hexo 博客中的 Markdown 添加卡片式链接支持 - OrangeX4's Blog](https://orangex4.cool/post/hexo-link-card/)
- [ ] “关于” 页面添加简历
	- [ ] [GitHub - godweiyang/hexo-theme-sungod: 一款定制化的Hexo博客主题](https://github.com/godweiyang/hexo-theme-sungod)
	- [ ] [韦阳的博客](https://godweiyang.com/)

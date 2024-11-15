---
title: 浏览器常用插件
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: 浏览器常用插件
description: 浏览器常用插件
tags:
  - Chrome
  - 油猴
  - 浏览器
categories:
  - Win 软件
date: 2023-05-05 18:30:30
abbrlink: 312685
password:
---

# 浏览器常用插件

## Chrome 插件

- Chrome 中的插件大多都可以在 Edge 和 Firefox 中找到
- 浏览器中的插件可以设置在隐私/无痕窗口中使用（Firefox 会自动提示，Chrome 和 Edge 需手动设置）
- Chrome 登录谷歌账号可同步安装过的插件（Tampermonkey 安装的油猴脚本无法同步）
- 隐藏浏览器书签栏：右键点击书签栏，取消勾选 “显示书签栏”


---

### Vimium

- 使用 Vim 快捷键浏览网页

- [ ] 暂无法在 Chrome 商店网页使用快捷键：[Make vimium work in Chrome WebStore and PDF viewer · Issue #3340 · philc/vimium · GitHub](https://github.com/philc/vimium/issues/3340)

- [ ] 使用 BewlyBewly 插件的 B 站首页网页无法使用上下移动的快捷键

```bash
# 快捷键
?            # 快捷键帮助
j / k        # 上下移动页面
t            # 新建标签页
r            # 刷新页面（同 F5）
x            # 关闭当前页面
gi           # 光标移动到输入框
X            # 恢复刚刚关闭的页面
H            # 回退
J / K        # 左右移动标签页；等同于 shift + j、shitf + k 
f            # 获取全页面的焦点，按照相应的位置输入字母打开新的链接
b            # 在当前页打开一个书签
o            # 相当于 Chorme 的地址栏，可以匹配历史记录、书签并在当前的窗口打开
yy           # 拷贝当前页面的 URL 到剪切板
```


---

### SwitchyOmega

- 自动切换对网页实现不同的代理（直连或代理），节省流量；配置好切换规则后，选择 "auto switch"

- [2024最新SwitchyOmega使用教程配置从入门到精通](https://switchyomega.org/)

```bash
# 规则列表网址
https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt

# 规则列表格式 选择 AutoProxy

# 个人使用切换规则
# 域名                    # 代理方式
*openai.com               # 代理
*bing.com                 # 代理
claude.ai                 # 代理
www.torrentleech.org      # 代理
www.em*ium.is             # 代理
pubs.acs.org              # 直接连接
pubs.aip.org              # 直接连接
www.sciencedirect.com     # 直接连接
```


---

### 其他插件

- 让 [网页版微信](https://wx.qq.com/) 可用：[GitHub - lqzhgood/wechat-need-web](https://github.com/lqzhgood/wechat-need-web?tab=readme-ov-file)

- AdBlock Plus：广告拦截；[GitHub - sbwml/halflife-list: ABP/ublock 广告过滤规则（每周一早上9点更新）](https://github.com/sbwml/halflife-list)

- Zotero Connector：保存网页中的文献到 Zotero 中

- OneTab：当标签页很多时，可以一键收起全部标签页，节省内存

- [沉浸式翻译](https://immersivetranslate.com/docs/) 网页翻译；百度翻译 API 申请：[百度翻译 | 沉浸式翻译](https://immersivetranslate.com/docs/services/baidu/)

- DeepL 翻译：网页翻译

- 沙拉查词：网页翻译

- Dark Reader：深色模式

- easyScholar：显示文献期刊排名；也可以下载 2021 年前的文献

- Copy As Plain Text：去除选中内容的所有格式，转换成普通文本

- Global Speed：全局网页视频速度控制

- [GitHub - 027xiguapi/code-box: 本插件可以用于CSDN/知乎/脚本之家/博客园等网站,实现无需登录一键复制代码;支持选中代码;或者代码右上角按钮的一键复制;解除关注博主即可阅读全文提示;去除登录弹窗;去除跳转APP弹窗.](https://github.com/027xiguapi/code-box)
    - 建议取消知乎的 “关闭登录弹窗”，否则无法打开收藏的弹窗

- 新标签页：[GitHub - XengShi/materialYouNewTab: A Simple New Tab ( browsers's home page ) inspired with Google's 'Material You' design](https://github.com/XengShi/materialYouNewTab)

- [GitHub - hanydd/BilibiliSponsorBlock: 一款跳过B站视频中恰饭片段的浏览器插件](https://github.com/hanydd/BilibiliSponsorBlock) （实用）

- 预览网页中的链接内容：[GitHub - XiCheng148/SmartPreview](https://github.com/XiCheng148/SmartPreview/)

- X media Downloader：推特视频下载

- 浏览推特内容平台时，模糊媒体资源：[GitHub - Dnevend/x-comfort-browse](https://github.com/dnevend/x-comfort-browse/)

- 屏蔽推特广告和纯视频内容，同时支持根据敏感词过滤；另外的两个功能是在时间线上显示用户的关注数和给用户加标签：[【工具自荐】免费的 Twitter/X 时间线优化工具 · Issue #5249 · ruanyf/weekly · GitHub](https://github.com/ruanyf/weekly/issues/5249)

- IDM Integration Module：IDM 下载集成模块；嗅探下载网页视频

- 隐藏浏览器插件（会把插件关掉）：[GitHub - cunzaizhuyi/up-mode-extension: This is a browser extension that protects the author's privacy by hiding pinned browser extensions.](https://github.com/cunzaizhuyi/up-mode-extension)

- LeechBlock：防止摸鱼时间过长

- Notion Boost：使网页版 Notion page 侧边栏生成目录



---

## 油猴脚本

- [x] 油猴脚本如何同步（通用 - 将新手改成初学者或高级；同步脚本，同步类型选择浏览器同步，WebDAV 不知为何同步失败）

- 需在 Chrome 中安装 Tampermonkey 插件（油猴脚本管理器）；[Greasy Fork - 安全、实用的用户脚本大全](https://greasyfork.org/zh-CN)

- [jAccount 验证码在线 ResNet 高速高精度毫秒级识别](https://greasyfork.org/zh-CN/scripts/432645)

- [上海交通大学 Canvas 平台课程视频播放器至尊版焕然一新插件](https://greasyfork.org/zh-CN/scripts/432918)

- [Github 增强 - 高速下载](https://greasyfork.org/zh-CN/scripts/412245)：加速 git clone

- GitHub 主页还原至原来的 feed：
    - [Github Old Feed](https://greasyfork.org/zh-CN/scripts/474728)（会无法显示 follow 的用户 fork 的 repo 动态）
    - [old-github-feed](https://github.com/Gerrit0/old-github-feed)

- [GitHub 的链接在新标签页打开](https://greasyfork.org/zh-CN/scripts/447005)

- [新标签页打开链接](https://greasyfork.org/zh-CN/scripts/429714)

- [沉浸式翻译](https://greasyfork.org/zh-CN/scripts/457196)

- [链接助手](https://greasyfork.org/zh-CN/scripts/422773)：文本转链接；百度网盘密码自动填写

- AC baidu 重定向：去广告，优化排列等。

- CSDN 广告过滤

- YAWF：微博过滤

- 知乎相关：
    - [知乎修改器🤜持续更新🤛努力实现功能最全的知乎配置插件](https://greasyfork.org/zh-CN/scripts/423404)
    - 知乎增强：移除登录弹窗、屏蔽首页视频、默认收起回答、快捷收起回答/评论（左键两侧）等。

```bash
# 个人 知乎增强油猴插件自定义屏蔽关键词
图片|照片|相册|笑话|搞笑|B站|女生|性别|电影|电视剧|视频|情感|游戏|微信|朋友圈
```

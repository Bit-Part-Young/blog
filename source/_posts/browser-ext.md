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
categories:
  - Win 软件
date: 2023-05-05 18:30:30
abbrlink: 31268
password:
---

# 浏览器常用插件

## Chrome 插件

浏览器中的插件可以设置在隐私窗口中使用（firefox 会自动提示，chrome 和 edge 需手动设置）


---

### Vimium

- 使用 Vim 快捷键浏览网页；[vimium的日常](https://coffee1993.github.io/2016/03/16/vimium%E7%9A%84%E6%97%A5%E5%B8%B8/)
- 快捷键
	- `?`：快捷键帮助
	- `j`、`k` : 上下移动
	- `J`、`K` (`shift + J`、`shitf + J`)： 上下移动标签页
	- `x` : 关闭当前页面
	- `X` : 恢复刚刚关闭的页面
	- `f` : 获取全页面的焦点，按照相应的位置输入字母打开新的链接
	- `b` : 在当前页打开一个书签
	- `o` : 相当于 Chorme 的地址栏，可以匹配历史记录、书签并在当前的窗口打开
	- `yy` : 拷贝当前页面的 URL 到剪切板（之后可以 Crtl+V 粘贴到其他地方）
	- `gi` : 光标移动到输入框，如果有多个可以按 Tab 键切换
	- `r` : 刷新页面（同 F5）


---

### SwitchyOmega

- 自动切换对网页实现不同的代理（直连或代理），节省流量。配置好切换规则后，选择 “auto switch”；[2023最新SwitchyOmega使用教程配置从入门到精通](https://switchyomega.org/)
- 规则列表网址：

```bash
https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt
```

- 个人使用切换规则：

| 域名                    | 代理方式 |
| ----------------------- | -------- |
| `*openai.com`           | 代理     |
| `*bing.com`             | 代理     |
| `claude.ai`             | 代理     |
| `www.torrentleech.org`  | 代理     |
| `www.em*ium.is`         | 代理     |
| `pubs.acs.org`          | 直接连接 |
| `pubs.aip.org`          | 直接连接 |
| `www.sciencedirect.com` | 直接连接 |

---

### 其他 Chrome 插件

- Adblock Plus：广告拦截；[GitHub - sbwml/halflife-list: ABP/ublock 广告过滤规则（每周一早上9点更新）](https://github.com/sbwml/halflife-list)
- Zotero Connector：保存网页中的文献到 Zotero 中。
- OneTab：当标签页很多时，可以一键收起全部标签页，节省内存。
- [沉浸式翻译](https://immersivetranslate.com/docs/) 网页翻译；百度翻译 API 申请：[百度翻译 | 沉浸式翻译](https://immersivetranslate.com/docs/services/baidu/)
- DeepL 翻译：网页翻译。
- 沙拉查词：网页翻译。
- easyScholar：显示文献期刊排名；也可以下载 2021 年前的文献。
- Copy As Plain Text：去除选中内容的所有格式，转换成普通文本。
- Global Speed：全局网页视频速度控制。
- Notion Boost：使网页版 Notion page 侧边栏生成目录。
- IDM Integration Module：IDM 下载集成模块；嗅探下载网页视频。
- Bing Unchained - Use new Bing in Chrome：实现在 Chrome 中使用 new Bing；已失效，可使用 [New Bing Anywhere (Bing Chat GPT-4)](https://chrome.google.com/webstore/detail/new-bing-anywhere-bing-ch/hceobhjokpdbogjkplmfjeomkeckkngi/related)
- WebChatGPT：使 ChatGPT 具备互联网访问功能（**不是很好用**）。



---

## 油猴插件

- 需在 Chrome 中安装 Tampermonkey 插件（油猴插件管理器）；[Greasy Fork - 安全、实用的用户脚本大全](https://greasyfork.org/zh-CN)
- [jAccount 验证码在线 ResNet 高速高精度毫秒级识别](https://greasyfork.org/zh-CN/scripts/432645-jaccount-%E9%AA%8C%E8%AF%81%E7%A0%81%E5%9C%A8%E7%BA%BF-resnet-%E9%AB%98%E9%80%9F%E9%AB%98%E7%B2%BE%E5%BA%A6%E6%AF%AB%E7%A7%92%E7%BA%A7%E8%AF%86%E5%88%AB)：自动填写验证码。
- 上海交通大学 Canvas 平台课程播放器插件：Canvas 平台视频播放器功能增强；[上海交通大学 Canvas 平台课程视频播放器至尊版焕然一新插件](https://greasyfork.org/zh-CN/scripts/432918-%E4%B8%8A%E6%B5%B7%E4%BA%A4%E9%80%9A%E5%A4%A7%E5%AD%A6-canvas-%E5%B9%B3%E5%8F%B0%E8%AF%BE%E7%A8%8B%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE%E5%99%A8%E8%87%B3%E5%B0%8A%E7%89%88%E7%84%95%E7%84%B6%E4%B8%80%E6%96%B0%E6%8F%92%E4%BB%B6)
- [Github 增强 - 高速下载](https://greasyfork.org/zh-CN/scripts/412245-github-%E5%A2%9E%E5%BC%BA-%E9%AB%98%E9%80%9F%E4%B8%8B%E8%BD%BD)：加速 git clone。

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401082135895.png)

- GitHub 主页还原至原来的 feed：[Github Old Feed](https://greasyfork.org/zh-CN/scripts/474728)、[old-github-feed](https://github.com/Gerrit0/old-github-feed)
- [沉浸式翻译](https://greasyfork.org/zh-CN/scripts/457196)
- [KeepChatGPT](https://greasyfork.org/zh-CN/scripts/462804-keepchatgpt)：使网页版 ChatGPT 更稳定。
- [链接助手](https://greasyfork.org/zh-CN/scripts/422773)：文本转链接；百度网盘密码自动填写
- AC baidu 重定向：去广告，优化排列等。
- CSDN 广告过滤
- 知乎增强：移除登录弹窗、屏蔽首页视频、默认收起回答、快捷收起回答/评论（左键两侧）等。

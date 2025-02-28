---
title: Zotero 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Zotero 使用
description: Zotero 使用
tags:
  - Zotero
categories:
  - Win 软件
date: 2023-07-21 15:45:30
abbrlink: 701251
password:
---

# Zotero 使用

## 介绍

- [GitHub - redleafnew/Zotero\_introduction: A Short Chinese Introduction to Zotero](https://github.com/redleafnew/Zotero_introduction)

- 文献管理软件，可通过浏览器插件保存网页中的文献，也可直接导入文献 PDF 文件

- 可实现文献、文献中的批注云同步

- 插件生态很好，个人感觉比 EndNote 好用很多



---

## 安装

- 官网下载

- Windows Portable 版本：[Zotero Portable (digital research organizer) - PortableApps.com](https://portableapps.com/apps/office/zotero-portable)



---

## 使用

- Zotero 文献存储路径修改（默认 C 盘）：编辑 -- 首选项 -- 高级 -- 文件和文件夹，数据存储位置

- 文献云同步：通过 WebDAV，主要有 InfiniCLOUD 和坚果云（推荐使用前者）
    - [如何在Zotero中设置webdav连接到坚果云？ - 坚果云帮助中心](https://help.jianguoyun.com/?p=3168)
    - [Zotero × Logseq - 有意栽花花满枝](https://blog.hjroyal.top/posts/tools/2023-04-zotero_logseq/)

```bash
toi.teracloud.jp/dav       # 可能会变
dav.jianguoyun.com/dav
```

- 将 Zotero 中导入的文献按添加时间进行排序：文献库界面右上方，附件（“链接” 图标），添加 “添加时间”；或者添加导入文献具体日期的文献库分类

- 内置 PDF 阅读器切换到双页浏览：查看 -- 奇数分布

- Zotero 快速复制引文：在 Zotero 选中任意一个文献，按 `command + shift + C/A`, 再转到想插入文献的地方，按 `command + V`, 粘贴完成（默认格式在首选项 -- 导出里面设置）

- Zotero 文献阅读颜色标签标准

```bash
# 下划线
蓝色               # 细节
黄色               # 结果
红色               # 结论
绿色               # 论文方法描述
```


---

### 插件推荐

- 注：主要针对 Zotero 7

- [Zotero 插件商店 - Zotero 中文社区](https://zotero-chinese.com/plugins/)（为插件都提供了多个下载源地址）
- Add-on Market for Zotero：直接在 Zotero 内安装插件（最优先推荐）
- Translate for Zotero：翻译插件（可设置百度翻译的 API key）
- Jasminum：中文插件（CNKI）
- [蒲公英](https://github.com/l0o0/tara)：Zotero 备份助手，用于备份和恢复 Zotero 常用设置，插件，转换器，CSL 引文格式（Mac 端工具栏上未显示插件）
- Better BibTex for Zotero：导出 BibTeX
- Green Frog：更新影响因子
- Ethereal Reference：解析参考文献（目前有问题）
- [GitHub - MuiseDestiny/zotero-figure: 一个基于 PDFFigure2 的 PDF 图表解析插件](https://github.com/MuiseDestiny/zotero-figure)
- Linter for Zotero：元数据格式化
- Zotero Tag
- Folder Import for Zotero
- Zotero IF Pro Max
- Zotero Citation Counts Manager
- Zotero Style：容易卡顿
- [GitHub - northword/zotero-itemtree-expand: Zotero 插件，令文库条目列表换行以便阅读全部标题。](https://github.com/northword/zotero-itemtree-expand)



---

## 相关问题

- [ ] Zotero，将网页文献通过其插件导入到软件中时，出现以下内容：使用 ScienceDirect 保存时发生错误。改为尝试用 Embedded Metadata 保存
    - [使用 ScienceDirect 保存时发生错误。改为尝试用 Embedded Metadata 保存。 - Zotero Forums](https://forums.zotero.org/discussion/118089/%E4%BD%BF%E7%94%A8-sciencedirect-%E4%BF%9D%E5%AD%98%E6%97%B6%E5%8F%91%E7%94%9F%E9%94%99%E8%AF%AF-%E6%94%B9%E4%B8%BA%E5%B0%9D%E8%AF%95%E7%94%A8-embedded-metadata-%E4%BF%9D%E5%AD%98)
    - Chrome 浏览器出现以上问题，Safari 正常；但在请求 PDF 时，会出现 “There was a problem providing the content you requested” 的错误

- Zotero 导入 Elsevier 网页文献现绝大部分都无法成功下载 PDF，需手动下载 PDF 再导入

- [ ] Zotero 如何导出一篇文献的参考格式

---
title: Notion 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Notion 使用
description: Notion 使用
tags:
  - Notion
categories:
  - Win 软件
date: 2024-11-07 12:18:30
abbrlink: 121830
password:
---

# Notion 使用

## 介绍

- 跨平台同步的笔记软件；也有网页版，但网页版的体验不如客户端，很卡

- 可查看每一个页面的内容更新情况（页面右上角的时钟图标）

- Notion 可用教育邮箱使用教育版

- 缺点
    - 不可以改变图片大小
    - task list 没有快捷键

---

- [Notion工具资源集合](https://notion2go.com/)
- Notion 开源替代品：[GitHub - docmost/docmost](https://github.com/docmost/docmost)
- 备份（不好用，且复杂）：[GitHub - LoneKingCode/notion-backup](https://github.com/LoneKingCode/notion-backup)
- 使用 Notion 的 Authorization：[Authorization](https://developers.notion.com/docs/authorization)


---

## 使用

### 快捷键

```bash
# + Space         # 一级标题；其他类推
" + Space         # 引用
> + Space         # toggle list
Ctrl + E          # 将文本转为内联代码
/color            # 更改文本颜色（可在开头或结尾输入；默认 /default）
Crtl + F          # 查找（当前页面）
Crtl + P          # 查找（所有页面）
Ctrl + Shift + E  # 公式
Ctrl + Shift + 8  # 代码块
/pdf              # 嵌入 pdf
```


---

### notion2md

- Notion 自带的导出 md 效果不是很好

- notion 转 md：[GitHub - echo724/notion2md](https://github.com/echo724/notion2md)

- 设置 Notion Integration，获取 API KEY，在 Notion 每个 page 下 add connection 设置的 Notion Integration

```bash
export NOTION_TOKEN='<token>'

notion2md --download --unzipped -n name -p folder -u [[]]
```


---

### md2notion

- md 转成 notion（在 Notion 的页面中生成子页面）：[GitHub - Cobertos/md2notion: A better Notion.so Markdown importer](https://github.com/Cobertos/md2notion)

- 安装出现 `Invalid input` 报错解决方法：[HTTPError - Invalid Input · Issue #40 · Cobertos/md2notion · GitHub](https://github.com/Cobertos/md2notion/issues/40)

```bash
pip install notion-cobertos-fork
```

- CLI 形式

```bash
python -m md2notion token_v2 [[test]] [[]]
```

- Python 脚本形式

```python
from notion.client import NotionClient
from notion.block import PageBlock
from md2notion.upload import upload

# Follow the instructions at https://github.com/jamalex/notion-py#quickstart to setup Notion.py
client = NotionClient(token_v2="")
page = [[test]]

with [[]]", "r", encoding="utf-8") as mdFile:
    newPage = page.children.add_new(PageBlock, title="TestMarkdown Upload")
    upload(mdFile, newPage) #Appends the converted contents of [[]] to newPage
```

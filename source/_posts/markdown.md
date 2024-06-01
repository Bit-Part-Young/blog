---
title: Markdown 使用
top: false
pin: false
cover:
toc: true
mathjax: true
math: true
summary: Markdown 使用
description: Markdown 使用
tags:
  - markdown
categories:
  - 排版语言
date: 2022-09-25 23:58:35
abbrlink: 46884
password:
---

# Markdown 使用

## 介绍

markdown cheatsheet

---

### 参考资料

lec3：Markdown 语法及应用
>[lec3.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec3.md)

>[GitHub - tchapi/markdown-cheatsheet: Markdown Cheatsheet for Github Readme.md](https://github.com/tchapi/markdown-cheatsheet)



[markdown在线编辑器 - Markdown Editor](https://markdown-editor.org/)


---

## 使用

标题

---

引言

---

无序列表

---

有序列表


---

分割线

---

代码块

---

图片插入

图片描述可以为空；图片位置可以是路径，也可以是 URL

```text
![图片描述](图片位置)

<img src="图片位置" alt="图片描述" 
    style="..."/>
```

---


插入链接


---

脚注

```text
这是脚注[^1]

[^1]: 脚注 1
```



---

## 字体

>[Markdown如何设置字体颜色加粗倾斜\_markdown 加粗\_大前小白的博客-CSDN博客](https://blog.csdn.net/weixin_45195200/article/details/105675238)

- markdown 编辑器本身不支持字体、字号、颜色的修改。但 markdown 支持 HTML 标签，可以使用内嵌 HTML 来实现这些功能。
- 可以在 `<font></font>` 标签中设置字体、大小、颜色；字号数值可设为 1~7，网页默认为 3。
- docusaurus 框架无法显示；hexo mkdocs 显示正常。


```markdown
<font face="微软雅黑" >微软雅黑</font>
<font face="华文彩云" >华文彩云</font>

<font size=2 >2号字</font>
<font size=5 >5号字</font>

<font color=#FF000 >红色</font> 
<font color=#008000 >绿色</font>
<font color=#FFFF00 >黄色</font>
```



---

## 表格

- `:` 位置表示 左、右、居中对齐方式
- hexo 框架只显示左对齐，mkdocs 框架正常

```markdown
| 标题 1 | 标题 2 | 标题 3 |
| :--- | ---: | :---: |
| 左 | 右 | 中 |
```

| 标题 1  | 标题 2  | 标题 3 |
| :--- | ---: | :---:|
| 左 | 右 | 中 |

---


excel 单元格， csv 内容转成 markdown 表格
>[Table to Markdown - MarkDown Convert](https://markdown-convert.com/en/tool/table)


---

## 内容折叠

```markdown
<details>
<summary>折叠内容</summary>
<p>这是一个折叠内容</p>
</details>

<details open>
<summary>expanded 折叠内容</summary>
<p>这是一个 expaned 折叠内容</p>
</details>
```

<details>
<summary>折叠内容</summary>
<p>**这是一个折叠内容**</p>
</details>

---

<details open>
<summary>expaned 折叠内容</summary>
<p>这是一个 expaned 折叠内容</p>
</details>


---

## 热键 hotkey

```text
<kbd>⌘F</kbd>
```

| Key     | Symbol | Key       | Symbol |
| ------- | ------ | --------- | ------ |
| Option  | ⌥      | Command   | ⌘      |
| Control | ⌃      | Caps Lock | ⇪      |
| Shift   | ⇧      | Tab       | ⇥      |
| Esc     | ⎋      | Power     | ⌽      |
| Return  | ↩      | Delete    | ⌫      |
| Up      | ↑      | Down      | ↓      |
| Left    | ←      | Right     | →      |

---

## 表情 emoji

emoji cheatsheet:
>[GitHub - ikatyang/emoji-cheat-sheet: A markdown version emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)
>[📙 Emojipedia — 😃 Home of Emoji Meanings 💁👌🎍😍](https://emojipedia.org/)

案例：
>[Release v2023.9.10 · materialsproject/pymatgen · GitHub](https://github.com/materialsproject/pymatgen/releases/tag/v2023.9.10)

|      ico      |    shortcode    |         ico         |       shortcode       |
|:-------------:|:---------------:|:-------------------:|:---------------------:|
|    :smile:    |    `:smile:`    |        :joy:        |        `:joy:`        |
|    :wink:     |    `:wink:`     |      :smiley:       |      `:smiley:`       |
| :sweat_drops: | `:sweat_drops:` |  :speech_balloon:   |  `:speech_balloon:`   |
|  :hospital:   |  `:hospital:`   | :hammer_and_wrench: | `:hammer_and_wrench:` |
| :bug:              |      `:bug:`           |                     |                       |

---

## 其他

- 多级任务

- [ ] An uncompleted task
	- [ ] A subtask

```text
- [ ] An uncompleted task
	- [ ] A subtask
```

---

 - `[]()` 格式
	- 图片：`![pic_name](pic_path)`
	- 链接：`[link_name](link)`
	- 目录用：`[section_name](#section)`；（Typora 软件可直接使用 `[TOC]` 生成目录；github 和 gitee 不识别 `[TOC]`，gitee 会自动在左侧生成目录，github 需写代码生成；当涉及到 `.` 时，可忽略，涉及到空格时，需用连字符连接，涉及到大写字母，需将其小写）


Markdown 文件里链接到内部内容时推荐使用相对链接
```markdown
[Link to a header](#awesome-section)
[Link to a file](docs/readme)

#### 示例
- [1. 《多尺度材料模拟与计算》实验报告 Markdown 模板](#1-多尺度材料模拟与计算实验报告-markdown-模板)
  - [1.1. 目录](#11-目录)
  - [1.2. 实验目的](#12-实验目的)
  - [1.3. 实验方法](#13-实验方法)
  - [1.4. 实验内容](#14-实验内容)
    - [1.4.1. 实验内容 1](#141-实验内容-1)
    - [1.4.2. 实验内容 2](#142-实验内容-2)
  - [1.5. 分析与讨论](#15-分析与讨论)
  - [1.6. 结论](#16-结论)
  - [1.7. 参考文献](#17-参考文献)
  - [1.8. 附录](#18-附录)
```

---

- `<br>`：HTML 标签，用于在 markdown 生成的 HTML 文档中插入换行



alert 语法

github

notes sjtu

---

Markdown 中带圆圈的数字编号，没有相应语法，直接复制粘贴即可：
```markdown
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩
```

markdown 自定义图片大小：[markdown中插入图片怎么定义图片的大小或比例？ - 知乎](https://www.zhihu.com/question/23378396)

markdown 图片并排

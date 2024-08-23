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
  - Markdown
categories:
  - 排版语言
date: 2022-09-25 23:58:35
abbrlink: 468849
password:
---

# Markdown 使用

## 介绍

- 一种轻量级文本**标记语言**（markup language，本质），是对 HTML 的一种简化
- 语法简单，易于学习，易于使用
- Markdown 只决定解析出的 HTML 是什么，不会决定任何视觉上的样式
- 规范：CommonMark 规范、GitHub GFM 规范、Pandoc 规范、Typora 规范等
- 扩展语法包括：表格、脚注、任务列表、公式、流程图等

- 参考资料：
	- Markdown 语法及应用：[lec3.md](https://github.com/TonyCrane/PracticalSkillsTutorial/blob/master/slides/src/lec3.md)
	- [GitHub - tchapi/markdown-cheatsheet: Markdown Cheatsheet for Github Readme.md](https://github.com/tchapi/markdown-cheatsheet)



---

## 工具

- [markdown在线编辑器 - Markdown Editor](https://markdown-editor.org/)
- 下载 md 文档中的 online 图片：[GitHub - YellowAndGreen/Md-ImgLocalize: Download and convert all online images to local images in markdown files.](https://github.com/YellowAndGreen/Md-ImgLocalize)
- Excel 单元格， CSV 内容转成 Markdown 表格：[Table to Markdown - MarkDown Convert](https://markdown-convert.com/en/tool/table)
- CSV 转 Markdown 表格（还可以转 LaTeX 表格等）：[Convert CSV to Markdown Table - Table Convert Online](https://tableconvert.com/csv-to-markdown)

- 检查 markdown 文件中的链接是否失效
	- [GitHub - gaurav-nelson/github-action-markdown-link-check: Check all links in markdown files if they are alive or dead. 🔗✔️](https://github.com/gaurav-nelson/github-action-markdown-link-check)
	- [GitHub - UmbrellaDocs/linkspector: Uncover broken links in your content.](https://github.com/UmbrellaDocs/linkspector)



---

## 语法

### 行内标记

- `*` 和 `_` 等效
- 下划线无 Markdown 语法，可以直接使用 HTML 的 `<u>` tag 来实现

```markdown
*斜体* _也是斜体_ \*这不是斜体\*
**粗体** __也是粗体__
***粗斜体*** ___也是粗斜体___
`行内代码`
~~删除线~~
<u>下划线</u>
```


---

### 标题

- 井号 `#` 开头，井号与标题间至少一个空格
- 只有 1～6 级标题
- 可以跨过某一级，但不推荐

```markdown
# 一级标题
## 二级标题
```


---

### 段落

- 直接编写文本即为普通段落
- 段落间通过空行来分割（有空行就有新的段落）
- 段落内换行：在行尾添加 `<br>`


---

### 引用

- `>` 加一个空格后接内容（空格可加可不加）；可以嵌套
- 内部可以嵌套使用 Markdown 语法（有些软件和博客框架无法正常渲染）
- 需要一个空行来退出环境

```markdown
> 引用
```


---

### 无序列表

- `- + *` 后接一个空格然后接内容
- 嵌套列表直接缩进一次即可

```markdown
- 无序列表 1
- 无序列表 2
```


---

### 有序列表

- 数字加点 后接空格 再接内容；也可以数字加 `)` 后接空格 再接内容
- 有序列表可以和无序列表互相嵌套

```markdown
1. 有序列表 1
2. 有序列表 2
```


---

### 分割线

- 使用 `* - _` 中任意一个字符重复至少三次
- 分割线上方不要有文字
- 分割线上下最好都加空行

```markdown
---
```


---

### 代码块

- 三个 \` 或 \~ 围起来构成代码块（\~ 或 \` 可以加语言名称）
	- 带有高亮支持的软件会对其进行高亮显示
	- 不加（或加 `text`）不进行高亮

~~~markdown
```c
#include <stdio.h>

int main() {
    printf("hello world\n");
    return 0;
}
~~~


---

### 图片插入

- 感叹号 - 方括号 - 圆括号组合
- 图片描述可以为空
- 图片位置可以是本地文件路径，也可以是 URL
- 默认无法调整图片大小，可借助 HTML 语法
- 图片不会嵌入 md 文件中，要交给别人 md 文件的话请附带上所有素材文件

```markdown
![图片描述](图片位置)

![](图片位置)
```


---

### 插入链接

- 方括号 - 圆括号组合
- 链接左右加 `<>` 自动链接

```markdown
[文字](链接)

<链接>
等价于 [链接](链接)
```

- 目录用：`[section name](#section)`
	- Typora 软件可直接使用 `[TOC]` 生成目录；GitHub 和 Gitee 不识别 `[TOC]`
	- Gitee 会自动在左侧生成目录，GitHub 需手动生成
	- 当涉及到 `.` 时，可忽略，涉及到空格时，需用 `-` 连字符连接，涉及到大写字母，需将其小写）

```markdown
- [一级标题](#一级标题)
  - [二级标题](#二级标题)
```


---

### 表格

- 每个单元格的内容用 `|` 分开
- 第二行一定要有，规定整列对齐方式；`|--|` 或 `|:--|` 左对齐，`|--:|` 右对齐，`|:--:|` 居中对齐，`-` 的个数随意
- Hexo 框架只显示左对齐，MkDocs 框架正常显示

```markdown
| 标题 1 | 标题 2 | 标题 3 |
| :--- | ---: | :---: |
| 左 | 右 | 中 |
```


---

### 任务列表

- 也称 checklist；`- [ ]` 插入未完成任务，`- [x]` 插入已完成任务
- GitHub、Obsidian 会自动加上 checkbox 支持修改

```markdown
- [ ] task 1 - TODO
- [x] task 2 - DONE
```


---

### 脚注

- 使用 `[^脚注名]` 插入脚注
- 在文中任意位置添加 `[^脚注名]: 脚注内容` 定义脚注内容
- 脚注名只是标记、匹配使用的，可以是任何字符串；最终的编号一般由在文中出现的顺序决定

```text
这是脚注[^1]

[^1]: 脚注 1
```


---

## 其他

- Markdown 自定义图片大小：[markdown中插入图片怎么定义图片的大小或比例？ - 知乎](https://www.zhihu.com/question/23378396)

- 内容折叠/展开

```markdown
<details>
<summary>折叠内容</summary>
<p>这是一个折叠内容</p>
</details>

<details open>
<summary>展开内容</summary>
<p>展开内容</p>
</details>
```

- 表情 emoji
	- Markdown emoji cheatsheet：[GitHub - ikatyang/emoji-cheat-sheet: A markdown version emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)
	- [📙 Emojipedia — 😃 Home of Emoji Meanings 💁👌🎍😍](https://emojipedia.org/)

- Markdown 中带圆圈的数字编号，没有相应语法，直接复制粘贴

```markdown
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩
```

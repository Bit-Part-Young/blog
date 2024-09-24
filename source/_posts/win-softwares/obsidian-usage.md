---
title: Obsidian 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Obsidian 使用
description: Obsidian 使用
tags:
  - Obsidian
categories:
  - Win 软件
date: 2023-07-26 15:00:00
abbrlink: 466176
password:
---

# Obsidian 使用

## 介绍

- 本地笔记管理软件
- [由此开始 - Obsidian 中文帮助 - Obsidian Publish](https://publish.obsidian.md/help-zh/)


---

### Notion 优缺点

#### 优点

- 不需要复杂设置，即可实现多端同步（PC、移动端）
- 有版本控制，可实时查看 page 修改情况
- 手机端与电脑端的使用体验一致

---

#### 缺点

- 不能用图链；导出成 md 文件时图片名字是一串 hash 码，不好识别；导出的 md 文档也带有 hash 码
- 表格和公式功能较鸡肋；表格中 LaTeX 公式不起作用
- 标题级数只能到 3 级（Obsidian 和 Typora 可到 6 级）
- 内容很长时，会变得很卡；网页版更卡
- 较花哨，很多功能其实用不太到


---

### Obsidian 优缺点

#### 优点

- 插件丰富
- 支持 Vim 及其配置文件设置，个人较中意
- 目录在右侧栏，相比 Notion 在最上面更有利于快速跳转
- 支持 Front Matter，更利于博客同步
- 支持分屏（快捷键自定义设置：上下分屏：`Alt+Shift+V`；左右分屏：`Alt+Shift+S`
- 有幻灯片演示功能（添加 `---` 横线；效果一般）

---

#### 缺点

- 导出的 pdf 文档没有书签
- 无法直接打开浏览单个 md 文档内容（仓库化管理）


---

## 使用

- 个人 Obsidian 软件配置模板：[obsidian-config: Obsidian configuration template.](https://gitee.com/yangsl306/obsidian-config)

- 字体设置：可分别设置界面字体、正文字体和代码字体

```bash
# 个人字体设置
Smiley Sans              # 界面字体；得意黑
LXGW WenKai              # 正文字体；霞鹜文楷
MesloLGM Nerd Font Mono  # 代码字体；Nerd Font

# 基本快捷键
Ctrl + L            # Task list
Ctrl + Shift + L    # 打开文件列表

# 自定义快捷键
Ctrl + Alt + O      # 打开 Vault 
Ctrl + Alt + H      # 插入水平线 
Ctrl + Alt + K      # 插入代码块 
Ctrl + Alt + S      # 切换实时阅览/源码模式 
```


---

### 数据同步实现

#### PC 端之间

- Obsidian + Git 插件 + Gitee/GitHub 仓库 + GitHub 图床（图片自动上传并转成图链），即可实现笔记云同步
- Obsidian 也可换成 Typora，但个人喜欢 Obsidian 中的 Vim 功能及丰富的插件


---

#### 手机 - PC 端之间

- Obsidian iPhone 端需用 iCloud 同步库
- [实测好用！Obsidian 免费同步Infini Cloud （WebDave） - 知乎](https://zhuanlan.zhihu.com/p/654370814)
- 手机端个人主要随时记录想法或看到的一些有用链接，仅这些内容需要同步，不需要太多的插件。可通过 Obsidian + Remotely Save（WebDAV 使用 Infini Cloud）插件实现
- Remotely Save 无版本回退功能，建议等两端同步好之后，再对文档进行修改，**否则有数据丢失的风险**


---

### 插件

- [Obsidian-插件推荐（20230630更新） - 知乎](https://zhuanlan.zhihu.com/p/353449575)

- Obsidian LaTeX 相关插件（建议在 VSCode 中书写 LaTeX 公式）：
	- [GitHub - RyotaUshio/obsidian-math-booster](https://github.com/RyotaUshio/obsidian-math-booster)
	- [GitHub - artisticat1/obsidian-latex-suite](https://github.com/artisticat1/obsidian-latex-suite)

- 整合 Obsidian 与 Zotero 的插件（可尝试）：[GitHub - PKM-er/obsidian-zotlit](https://github.com/PKM-er/obsidian-zotlit)

---

- 外观：
	- 推荐使用 Blut Topaz、Border、[AnuPpuccin](https://github.com/AnubisNekhet/AnuPpuccin) 主题（后两者会出现卡顿情况）
	- AnuPpuccin 使用 CSS：下载 `extended-colorschemes.css` 和 `custom-rainbow-colors.css` 文件，将其复制到 `vault/.obsidian/snippets` 中，进入 “设置 - 外观 - CSS 代码片段”，刷新，应用当前代码片段
	- Blut Topaz 主题效果图：

![vault-screenshot.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202312120853566.png)

---

- [Vimrc Support](https://github.com/esm7/obsidian-vimrc-support)：支持设置 `.vimrc` 配置文件（实用性很高；需在编辑器选项中打开 Vim 模式）
	- [08\_obsidian01.md](https://github.com/alexzhang1030/full-keyboard/blob/0cb16b4d9fbc2d8e589b38fad14308220d184d72/docs/08_obsidian01.md)
	- [obsidian-vimrc-support\_readme.md](https://github.com/PKM-er/Pkmer-Docs/blob/84e53b107bff5fe3f4f76f54d909275625acf17d/10-Obsidian/Obsidian%E7%A4%BE%E5%8C%BA%E6%8F%92%E4%BB%B6/Readme/obsidian-vimrc-support_readme.md?plain=1#L3)
	- [.obsidian.vimrc](https://github.com/conneroisu/conneroisu-obsidian-vimrc/blob/main/.obsidian.vimrc)
    - 个人 `.obsidian.vimrc` 设置：[.obsidian.vimrc · Falling Slowly/obsidian-config - Gitee.com](https://gitee.com/yangsl306/obsidian-config/blob/main/.obsidian.vimrc)
    - [ ] 状态栏 powerline 设置不起作用：[vimrc support里面提到可以定制状态栏成powerline风格，但是无效 - 疑问解答 - Obsidian 中文论坛](https://forum-zh.obsidian.md/t/topic/23660)
	- [ ] Obsidian Vim 插件无法使用重复替换操作的快捷键

- Obsidian Git：Git 插件以实现版本控制 + 云同步。相关设置：
    - 自动 commit 和 push（称为备份）时间间隔设置为 30min（在文件最后一次改变后的 30min，可避免在编辑文件时自动备份；也可以设置成最后一次 commit 后的 30min；二选一）
    - commit message 为 `vault backup: {{date}}`（默认）
    - Obsidian 启动时 pull
    - 忽略空白和新行（需先开启 Line author information 选项，可选）
    - Windows 与 Linux 中的文件权限两者不同，在 Windows 上使用 git 插件时，可在该 repo 中输入 `git config core.fileMode false` 命令以忽略文件权限变化

- Linter：md 文档自动格式化
	- 不会处理代码块中的内容格式
	- 中日韩文与数字和英文之间的空格：由单个空格分隔
	- 标题空行：标题前后均有一个空行
	- 移除末尾空格
	- 移除字符前后空格

```bash
，,!！?？;；:：)）”]》    # 移除字符后的空格
¿¡‘“([（《              # 移除字符前的空格
```

- Remotely Save：数据同步；支持 S3、Dropbox、WebDAV（常用，推荐 Infini Cloud）、Onedrive 远程服务。相关设置：
    - 填写服务器地址、用户和密码信息
    - 启动后自动运行一次：启动后第 1 秒运行一次
    - 同步配置文件夹：对于手机 - PC 端之间互相同步，开始可先开启，手机端同步到配置文件后，再将其关闭
    - Infini Cloud 服务器地址：`https://toi.teracloud.jp/dav/`

- Auto Link Title：自动获取 URL 标题（实用性很高）；快捷键 `Crtl + Shift + E`；无法实现文档中的全部链接标题的获取，只能单个

- Advanced Tables：Markdown 表格增强；按 Tab 键自动补全 Markdown 表格所需格式

- Editing Toolbar：在文档编辑栏上方添加类似 Office 的工具栏

- Remember cursor position：记住光标位置

- Vault Statistics：Vault 信息统计，包括文档数，文档中的字符和词数（出现在右下角）

- Image Auto Upload Plugin：借助 PicGo/PicList 实现图片自动上传并转成图链

- Obsidian Enhancing Export：将 Obsidian md 文档导出不同的文件格式（**通过 Pandoc 导出，需安装并配置；含中文的 md 导出成 pdf 格式一般都会报错，建议手动写命令，其他格式可以成功导出**）

- floating toc：目录浮动体；[GitHub - PKM-er/obsidian-floating-toc-plugin](https://github.com/cumany/obsidian-floating-toc-plugin)

- Admonitions：和 GitHub 中的 alert 语法一样

```text
> [!NOTE]
> [!TIP]
> [!IMPORTANT]
> [!WARNING]
> [!CAUTION]
```

效果：

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/images/202401081127325.png)


---

### 工具

- Notion Notes 转 Obsidian：[GitHub - connertennery/Notion-to-Obsidian-Converter: Converts exported Notion notes to work with Obsidian.](https://github.com/connertennery/Notion-to-Obsidian-Converter)

- Obsidian 模板制作（个人主要添加预定义的 Front Matter 键值对）



---

## 相关问题

- VSCode 复制代码到 Obsidian，每行会产生多余空格
	- [从visual studio code复制代码后 产生的unicode的空格问题 - 疑问解答 - Obsidian 中文论坛](https://forum-zh.obsidian.md/t/topic/9332)
	- 解决方法：使用 `Ctrl + Shift + V` 粘贴
	- 新版 VSCode，该问题已解决？

- [ ] Obsidian 光标在 N 级标题行时会被黏住

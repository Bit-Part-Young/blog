---
title: VSCode 常用插件
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: VSCode 常用插件
description: VSCode 常用插件
tags:
  - VSCode
categories:
  - Win 软件
date: 2022-08-26 18:52:37
abbrlink: 189254
password:
---

# VSCode 常用插件

## 介绍

- 代码编辑器，有丰富的插件

- VSCode 连接远程服务器，点击打开的文件，会立马跳转到相应的目录中，定位文件相比 MobaXterm 更便捷，便于下载文件到本地

```bash
# 命令行启动
code             # VSCode
code-insiders    # VSCode Insiders
```

- 配置文件 `settings.json`：**分用户和远程设置**；配置文件中有设置但没安装的插件其命令不会有高亮

- VSCode 配置同步：[VSCode官方的配置同步方案\_vscode同步\_蝉沐风的码场的博客-CSDN博客](https://blog.csdn.net/chanmufeng/article/details/123028133)

- [在VScode中，代码提示左边的图标各自代表什么含义？ - 知乎](https://www.zhihu.com/question/370258254/answer/1003317979)

- VSCode 中类、函数、方法、属性等的图标：[IntelliSense in Visual Studio Code](https://code.visualstudio.com/docs/editor/intellisense#_types-of-completions)

- VSCode 终端字体设置：[Change terminal font family to nerd font · Issue #81497 · microsoft/vscode · GitHub](https://github.com/microsoft/vscode/issues/81497)

```json
{
    // 终端字体
    "terminal.integrated.fontFamily": "MesloLGM Nerd Font",
    // 终端字体大小
    "terminal.integrated.fontSize": 14,
    // 编辑器字体大小
    "editor.fontSize": 14,
    // 窗口缩放大小
    "window.zoomLevel": 0.5,
}
```


---

### 快捷键

```bash
Ctrl + /                # 单行注释
Alt + Shift + A         # 多行注释
Ctrl + C                # 复制当前整行内容
Ctrl + X                # 剪切当前整行内容
Ctrl + Shift + K        # 删除一行
Crtl + J                # 工作区和终端间的切换
alt + shift + ↓         # 复制上一行代码到下一行
Ctrl + F4               # 关闭文件
Crtl + P / Crtl + Tab   # 文件跳转
Crtl + 点击图片          # 缩小图片
```



---

## 插件

### Vim

- 官网：[GitHub - VSCodeVim/Vim: :star: Vim for Visual Studio Code](https://github.com/VSCodeVim/Vim)

- 在 VSCode 中使用 Vim 快捷键；内置的一些 Vim 插件（常用）：airline、easymotion、surround

- Vim 设置

```json
    // Vim 配置
    "vim.leader": "<space>",
    "vim.surround": true,
    "vim.easymotion": true,
    "vim.handleKeys": {
        "<C-a>": false,
        "<C-f>": false
    },
    "vim.insertModeKeyBindings": [
        {
            "before": ["j", "j"],
            "after": ["<Esc>"]
        }
    ],
    "vim.normalModeKeyBindings": [
        {
            "before": ["j"],
            "after": ["g", "j"]
        },
        {
            "before": ["k"],
            "after": ["g", "k"]
        },
        {
            "before": ["K"],
            "after": ["5", "k"]
        },
        {
            "before": ["J"],
            "after": ["5", "j"]
        },
        {
            "before": ["L"],
            "after": ["$"]
        },
        {
            "before": ["H"],
            "after": ["^"]
        },
    ],
```

---

- easymotion 用法：

```bash
# 快捷键
<leader><leader> s <char>  # 查找字符
```

---

- surround 用法：
  - `"test"` with cursor inside quotes type `cs"'` to end up with `'test'`
  - `"test"` with cursor inside quotes type `ds"` to end up with `test`


---

### Python

- 集成插件；可识别 conda 创建的 Python 虚拟环境
- 其中的 Pylance 插件是 Python 的语言服务器（LSP），可实现自动补全，跳转到定义，自动解析类、函数等功能，非常好用
- isort 插件可对 import 的相关模块进行排序
- 转到某个类或函数的定义所在脚本时，代码编辑区上方会显示该类或函数的绝对路径，可点击该类或函数的名字，查看该类中所有的方法和属性（该函数平级的其他函数），点击跳转想要查看的方法/函数、属性即可，也可查看其他的类，会很简便

- 其他 Python 相关插件：
	- Black Formatter：代码格式化（其他：yapf、autopep8 和 ruff）
	- autoDocstring：自动为 Python 的函数和类写 docstring snippets
	- Jupyter：运行 Jupyter Notebook

- 问题：当 root 中已有 conda 时，当前用户下的 conda 虚拟环境名称无法被识别，可在设置中找到 `conda path` 选项，写入将当前用户下的 conda 路径

- Python 设置：脚本文件保存自动格式化

```json
{
    "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
        },
    },
    "isort.args":["--profile", "black"],
}
```


---

### 编程相关

- Remote Development：集成插件；可连接 WSL（自动识别）和远程服务器（若已设置别名，可自动识别）

- Github Copilot (Chat)：辅助编写代码，如代码自动补全，可在代码和侧边栏中开启对话。目前主要用它进行（Github Copilot Chat 目前只有 VSCode Insider 版本才有）

- WakaTime：统计编程项目 Codinig 数据

- TabOut：跳出括号（函数、列表、字典和字符串等）

- Rainbow CSV：高亮 CSV 和 TSV 文件

- Markdown All in One：
	- 语法高亮，自动补全，**可生成目录，添加/更新章节序号**
	- [VSCode插件生成编号、目录、文件目录树](https://github.com/lc-1203/k8s-practice/blob/main/06-Tools%26Tips/Markdown/VSCode%E6%8F%92%E4%BB%B6%E7%94%9F%E6%88%90%E7%BC%96%E5%8F%B7%E3%80%81%E7%9B%AE%E5%BD%95%E3%80%81%E6%96%87%E4%BB%B6%E7%9B%AE%E5%BD%95%E6%A0%91.md)
	- 暂无很好的 “中英文混排添加空格” 格式化的插件；使用 Obsidian 中的 Linter 插件，将 Markdown 内容复制到 Obsidian 中进行格式化

- Markdown PDF：将 markdown 文档导出成 pdf 文件，**需要本地或终端支持中文字符，不支持公式**

- Markdownlint：Markdown 语法风格格式化

```json
{
    // markdownlint 设置：md 文件保存自动格式化
    "[markdown]": {
        "editor.codeActionsOnSave": {
        "source.fixAll.markdownlint": "always"
        }
    }
}
```


---

### 前端相关

- Live Server：实时预览
- CSS Peak：
- Auto Rename Tag：自动重命名标签 tag


---

### 非编程相关

- PicGo：图床
- vscode-pdf：打开 pdf 文件（会与 LaTeX Workshop 插件冲突）
- Excel Viewer：查看 Excel 表格
- Material Icon Theme：文件、目录图标，美化用
- Front Matter CMS：管理 Front Matter
- [VScode 插件推荐-状态栏篇\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1HBsMejEJM/)


---

## code-server

>[Code Server 是什么？\_51CTO博客\_code server](https://blog.51cto.com/phyger/5156445)

>[GitHub - coder/code-server: VS Code in the browser](https://github.com/coder/code-server)

- 浏览器或远程使用 vscode 进行开发；服务器平台为 Linux 和 macOS，不支持 Windows；可脚本、二进制安装

- 将 `bind-addr` 改成 `0.0.0.0:8080`，可使用 `http://<ip>:8080` 的形式登录，在同一局域网下，不同电脑可以直接访问；不在同一局域网下，需使用内网穿透使其远程访问

- 无法显示图片、ipynb 文件；[Allow opening files, folders, and workspaces in existing code-server from CLI · Issue #164 · coder/code-server · GitHub](https://github.com/coder/code-server/issues/164)；**连接性不是很好**

```bash
# 指定 host 和 port
code-server --host host --port port 

# 打开文件
code-server <file>

# macOS
brew install code-server
brew services start code-server
# Now visit http://127.0.0.1:8080. Your password is in ~/.config/code-server/config.yaml
```



---

## 相关问题

- WSL1 无法安装插件：[Installing extensions to WSL VS Code Server gives \`EACCES: Permission Denied\` · Issue #90164 · microsoft/vscode · GitHub](https://github.com/microsoft/vscode/issues/90164)

- GitHub Copilot 无法连接服务器：[GitHub Copilot could not connect to server. Extension activation failed: "Timed out waiting for authentication provider to register" · community · Discussion #11324 · GitHub](https://github.com/orgs/community/discussions/11324)

```bash
GitHub Copilot could not connect to server. Extension activation failed: "Timed out waiting for authentication provider to register"
```

- 扩展远程主机在过去 5 分钟内意外终止了 3 次：[vscode 扩展主机意外终止怎么办，重装好几次了\_博问\_博客园](https://q.cnblogs.com/q/94411/)

- Pylance 语言服务器 crashed：[The Python Tools server crashed 5 times in the last 3 minutes. The server will not be restarted. · Issue #13679 · microsoft/vscode-python · GitHub](https://github.com/microsoft/vscode-python/issues/13679)

```bash
The Pylance server crashed 5 times in the last 3 minutes. The server will not be restarted. See the output for more information.
```

- Remote-ssh 远程连接服务器，使用 `plt.show()` 打不开画图窗口：
	- [python - Is there any way to show figures in VScode remote ssh (windows) - Stack Overflow](https://stackoverflow.com/questions/59063892/is-there-any-way-to-show-figures-in-vscode-remote-ssh-windows)
	- 解决方法：保存图片再打开查看；或者在互动窗口中运行代码

- vscode 加载图片错误：
	- [visual studio code - Error loading webview: Error: Could not register service workers: TypeError: Failed to register a ServiceWorker for scope - Stack Overflow](https://stackoverflow.com/questions/67698176/error-loading-webview-error-could-not-register-service-workers-typeerror-fai)
	- 解决方法：清除相关文件缓存：进入 `C:\Users\XX\AppData\Roaming\Code`，删除 `Cache`、`CachedData`、`CachedExtensions`、`CachedExtensionVSIXs`（目录如果存在）和 `Code Cache` 内容

```bash
加载 Web 视图时出错: Error: Could not register service workers: InvalidStateError: Failed to register a ServiceWorker: The document is in an invalid state.
```

- VSCode terminal profile 无法使用 zsh：[VSCode terminal task not using zsh profile · Issue #143061 · microsoft/vscode · GitHub](https://github.com/microsoft/vscode/issues/143061)

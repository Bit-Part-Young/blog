---
title: Jekyll 博客框架
top: false
toc: true
mathjax: true
summary: Jekyll 博客框架
description: Jekyll 博客框架
tags:
  - Jekyll
  - CV
categories:
  - 博客
abbrlink: 42765
date: 2023-11-25 09:00:00
cover:
password:
---

# Jekyll 博客框架

## 介绍

GitHub Pages 默认框架。



---

## 使用

### Jekyll 框架主题

- [GitHub - just-the-docs/just-the-docs: A modern, high customizable, responsive Jekyll theme for documentation with built-in search.](https://github.com/just-the-docs/just-the-docs)
- 简洁博客：[GitHub - cotes2020/jekyll-theme-chirpy: A minimal, responsive, and feature-rich Jekyll theme for technical writing.](https://github.com/cotes2020/jekyll-theme-chirpy)

---

#### chirpy 主题使用

- 文章置顶 front-matter 参数：`top`，数值为 `true` 或 `false`
- md 文档中的 URL 链接 title 中不能有 `|`，否则会渲染错误
- 渲染 checklist 时，会无法渲染 bullet list


---

### 安装 Ruby

#### Linux

```bash
sudo apt-get install ruby-full build-essential zlib1g-dev
```

将 gem(RubyGems packages) 安装目录更改为用户目录（root 用户会出问题）
```bash
rc_file=$HOME/.zshrc
echo '# Install Ruby Gems to ~/.gems' >> ${rc_file}
echo 'export GEM_HOME="$HOME/.gems"' >> ${rc_file}
echo 'export PATH="$HOME/.gems/bin:$PATH"' >> ${rc_file}
source ${rc_file}
```


---

#### macOS

macOS 默认已安装 Ruby，但并非最新版本
```bash
# 安装 rbenv 和 ruby-build
brew install rbenv ruby-build

# ~/.zshrc 添加
eval "$(rbenv init -)"

rbenv install 3.3.0  # 安装
rbenv global 3.3.0   # 设置全局版本
ruby -v              # 查看版本 

# 删除相关配置文件
rm -rf ~/.rbenv ~/.gem ~/.bundle
```

---

```bash
# 安装 jekyll 和 bundler；卸载 uninstall
gem install jekyll bundler

# 安装依赖
bundle install

# 本地预览
bundle exec jekyll server
```

---

`.gemrc` 内容：

- 镜像：[rubygems - 清华大学镜像](https://mirrors.tuna.tsinghua.edu.cn/help/rubygems/)

```yaml
:sources:
  - https://mirrors.tuna.tsinghua.edu.cn/rubygems/
```


---

### 部署

部署（不需要写 GitHub Actions yml 文件）：repo - Settings - Pages - Build and deployment - Branch

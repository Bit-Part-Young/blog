---
title: Hexo 框架 Butterfly 主题使用
top: false
cover: 
toc: true
mathjax: true
summary: Hexo 框架 Butterfly 主题使用
description: Hexo 框架 Butterfly 主题使用
tags:
  - Butterfly
  - Hexo
categories: 
  - 博客
date: 2022-08-04 16:20:00
abbrlink: 220845
password:
---

# Hexo 框架 Butterfly 主题使用

## 外挂标签

### Note

{% note 'fab fa-cc-visa' flat %}
你是刷 Visa 还是 UnionPay
{% endnote %}
{% note blue 'fas fa-bullhorn' flat %}
2021年快到了....
{% endnote %}
{% note pink 'fas fa-car-crash' flat %}
小心开车 安全至上
{% endnote %}
{% note red 'fas fa-fan' flat%}
这是三片呢？还是四片？
{% endnote %}
{% note orange 'fas fa-battery-half' flat %}
你是刷 Visa 还是 UnionPay
{% endnote %}
{% note purple 'far fa-hand-scissors' flat %}
剪刀石头布
{% endnote %}
{% note green 'fab fa-internet-explorer' flat %}
前端最讨厌的浏览器
{% endnote %}

### tag-inline

哪个英文字母最酷？ {% hideInline 因为西装裤(C装酷),查看答案,#FF7242,#fff %}

门里站着一个人? {% hideInline 闪 %}

---

查看答案
{% hideBlock 查看答案 %}
傻子，怎么可能有答案
{% endhideBlock %}

---

{% hideToggle Butterfly安装方法 %}
在你的博客根目录里

git clone -b master https://github.com/jerryc127/hexo-theme-butterfly.git themes/Butterfly

如果想要安装比较新的dev分支，可以

git clone -b dev https://github.com/jerryc127/hexo-theme-butterfly.git themes/Butterfly

{% endhideToggle %}


---
title: Rust 学习
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: Rust 学习
description: Rust 学习
tags:
  - Rust
categories:
  - 编程
date: 2024-02-01 09:00:00
abbrlink: 209024
password:
---

# Rust 学习

## 介绍

WIP...

Rust、Julia、Fortran 没有类的概念


---

### 参考资料

- [关于本书 - Rust语言圣经(Rust Course)](https://course.rs/)；[GitHub - sunface/rust-course](https://github.com/sunface/rust-course)
- [Rusty Book - Rusty Book(锈书)](https://rusty.course.rs/about.html)
- [Rust - 鹤翔万里的笔记本](https://note.tonycrane.cc/cs/pl/rust/)
- [GitHub - rust-lang-cn/book-cn: Rust 程序设计语言 中文版](https://github.com/rust-lang-cn/book-cn)
- [Rust 程序设计语言 - Rust 程序设计语言 中文版](https://rustwiki.org/zh-CN/book/)
- [Introduction - PyO3 user guide](https://pyo3.rs/)
- [GitHub - mainmatter/100-exercises-to-learn-rust: A self-paced course to learn Rust, one exercise at a time.](https://github.com/mainmatter/100-exercises-to-learn-rust)
- [GitHub - rust-lang/rustlings: :crab: Small exercises to get you used to reading and writing Rust code!](https://github.com/rust-lang/rustlings)
- [GitHub - guofei9987/rs\_lib: Rust调用C的例子（混合编程）](https://github.com/guofei9987/rs_lib)


---
库

- [GitHub - pola-rs/polars: Dataframes powered by a multithreaded, vectorized query engine, written in Rust](https://github.com/pola-rs/polars)

- 命令行参数解析：[GitHub - google/argh: Rust derive-based argument parsing optimized for code size](https://github.com/google/argh)


---

## 使用

### Rust 环境安装

```bash
# 方式 1
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh

# 方式 2
curl -sS https://webi.sh/rustlang | sh
```

加速安装：将 Rust 安装源设置国内源，在 `.bashrc` 或 `.zshrc` 中添加
```bash
export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
```

>[rustup | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/rustup/)

>[Rust Toolchain 反向代理使用帮助 — USTC Mirror Help  文档](https://mirrors.ustc.edu.cn/help/rust-static.html)


```bash
# 运行简单脚本
rustc *.rs
```


cargo 相关命令

```bash
cargo --list   # 查看所有安装的命令
# 安装 package （指 Rust binary）
cargo install <package>
# 若有新版本，覆盖旧版本
cargo install <package> --force
# --locked 确保安装时依赖项的版本与在 Cargo.lock 文件中的版本完全一致
cargo install --locked <package>
# 列出所有安装的 packages 及对应的版本
cargo install --list

cargo add <lib>

rustup update  # 更新 Rust 工具链
```

---

修改 Rust 的下载镜像为国内的镜像地址：创建或编辑 `$HOME/.cargo/config.toml`

```toml
[source.crates-io]
replace-with = 'mirror'

[source.mirror]
# 清华源
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
# 科大源
# registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"
# git 写法
# registry = "sparse+git://mirrors.ustc.edu.cn/crates.io-index/"
```

- [清华大学镜像 - crates.io-index.git](https://mirrors.tuna.tsinghua.edu.cn/help/crates.io-index.git/)、[Rust Crates 源使用帮助 — USTC Mirror Help  文档](https://mirrors.ustc.edu.cn/help/crates.io-index.html)
- cargo 1.68 版本开始支持稀疏索引：不再需要完整克隆 crates.io-index 仓库，可以加快获取包的速度。


---

项目：

```bash
# 创建项目
cargo new <project>

# 运行项目
cargo run

# 代码验证
cargo check
```

`cargo run` 相当于运行了编译 `cargo build` 和运行 `./target/debug/XXX` 两个步骤

默认是 `debug` 模式，代码编译速度快，运行速度慢；提高代码性能：添加 `--release` 编译

```bash
cargo run --release
cargo build --release
```



项目结构
```text
├── .git
├── .gitignore
├── Cargo.toml
└── src
    └── main.rs
```


`Cargo.toml`：项目数据描述文件

`Cargo.lock`：项目依赖详细清单

若项目是一个可运行的程序时，可上传 `Cargo.lock`；若是一个依赖库项目，建议将其添加到 `.gitignore` 中


`Cargo.toml` 设置

```toml
# package 配置
[package]
name = "world_hello"
version = "0.1.0"
edition = "2021"

# 项目依赖
[dependencies]
rand = "0.3"
hammer = { version = "0.5.0"}
color = { git = "https://github.com/bjz/color-rs" }
geometry = { path = "crates/geometry" }

```


项目依赖


---

### 工具

- Rust 相关 VSCode 插件：rust-analyzer

- [cargo-update](https://github.com/nabijaczleweli/cargo-update)：检查和更新 package 的 cargo 子命令

```bash
cargo install cargo-update  # 安装

cargo install-update -l     # 列出所有安装的 packages 
cargo install-update -a     # 检查并更新所有安装的 packages 
```

- cargo-cache：cargo 缓存管理工具

- rust-binstall

```bash
# 安装
curl -L --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.sh | bash

cargo binstall ripgrep
```

- 一次性更新所有软件包（跨平台）：[GitHub - topgrade-rs/topgrade: Upgrade all the things](https://github.com/topgrade-rs/topgrade)

```bash
brew install topgrade  # 安装
topgrade               # 使用
topgrade -n            # 不实际运行
```


---

## 语法

### 变量

```rust
let x = 5;
// 变量可变
let mut x = 5;
// 使用下划线开头忽略未使用的变量
let _x = 5;

// 常量
const
```

>若创建了一个变量却不在任何地方使用它，Rust 通常会给你一个警告，因为这可能会是个 BUG


---

### 基本类型

Rust 编译器可以根据变量的值和上下文中的使用方式来自动推导出变量的类型

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202402011629402.png)


![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202402011631440.png)


浮点类型：`f32` 和 `f64`，默认浮点类型是 `f64`

![image.png](https://cdn.jsdelivr.net/gh/Bit-Part-Young/BTY-imgs/lenovo-images/202402011634539.png)


NaN 类型

序列：`1..5`，生成从 1 到 4 的连续数字，不包含 5 ；`1..=5`，生成从 1 到 5 的连续数字，包含 5

```rust
for i in 1..=5 {
    println!("{}",i);
}
```


字符 `''`，字符串 `""`


单元类型：`()`

`main` 函数就返回单元类型

没有返回值的函数在 Rust 中有单独定义


```rust
// 类型注释
fn add(i: i32, j: i32) -> i32 {
   i + j
 }

```




语句：加分号 `;`，表达式：不加分号 `;`

Rust 是强类型语言，每个函数参数都需要标注类型，函数的位置可以随便放

---

- **垃圾回收机制 (GC)**，在程序运行时不断寻找不再使用的内存，典型代表：Java、Go
- **手动管理内存的分配和释放**, 在程序中，通过函数调用的方式来申请和释放内存，典型代表：C++
- **通过所有权来管理内存**，编译器在编译时会根据一系列规则进行检查


---




Rust 中的字符是 Unicode 类型，每个字符占据 4 个字节内存空间；在字符串中不一样，字符串是 UTF-8 编码，字符串中的字符所占的字节数是变化的 (1 - 4)，如中文在 UTF-8 中占用三个字节


`str` 类型是硬编码进可执行文件，也无法被修改，但是 `String` 则是一个可增长、可改变且具有所有权的 UTF-8 编码字符串。当 Rust 用户提到字符串时，往往指的就是 String 类型和 &str 字符串切片类型，这两个类型都是 UTF-8 编码

元组

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

用 `.` 获取元组中的值


---

结构体

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```


```rust
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };
  // 结构体更新
  let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };

```

- 初始化实例时，**每个字段**都需要进行初始化
- 初始化时的字段顺序**不需要**和结构体定义时的顺序一致

用 `.` 访问结构体实例内部的字段值


使用 `#[derive(Debug)]` 来打印结构体的信息

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
    println!("rect1 is {:#?}", rect1);
}
```

数组 `array`


```rust
if condition == true {
    // A...
} else {
    // B...
}
```


---

[【rust】Option\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV14t4y1u7TW)

模式匹配： `match` 和 `if let`

```rust
match target {
    模式1 => 表达式1,
    模式2 => {
        语句1;
        语句2;
        表达式2
    },
    _ => 表达式3
}
```


```rust
impl
```




代码注释

```rust
// 行注释

/* 
    块注释
*/ 
```

文档注释

```rust
/// 文档行注释

/**
文档块注释
*/
```


---


`!`：宏操作符

Rust 的集合类型不能直接进行循环，需要变成迭代器（可用 `.iter()` 方法），才能用于迭代循环

随机数：rand


---

### 参数解析

`clap` 库

```bash
cargo add clap --features derive
```

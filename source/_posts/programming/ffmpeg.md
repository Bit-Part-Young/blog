---
title: FFmpeg 使用
top: false
pin: false
cover: 
toc: true
mathjax: true
math: true
summary: FFmpeg 使用
description: FFmpeg 使用
tags:
  - FFmpeg
categories:
  - Linux
date: 2024-03-24 14:00:00
abbrlink: 243243
password:
---

# FFmpeg

参考资料：

- [FFmpeg 速查表](https://wangchujiang.com/reference/docs/ffmpeg.html)
- [FFmpeg 命令生成](https://alfg.dev/ffmpeg-commander/)
- [用FFmpeg来生成带背景和视频信息的缩略图（一） - Gu Gu Gu](https://bupt.dev/index.php/archives/67/)
- FFmpeg 的 GPL 和 LGPL 协议含义：[终于理解了什么是LGPL - findumars - 博客园](https://www.cnblogs.com/findumars/p/3556883.html)
- FFmpega + Python 实现给视频添加水印：[GitHub - HeiSir2014/ffmpeg-wiki](https://github.com/HeiSir2014/ffmpeg-wiki)



---

## 常用功能命令

### 视频相关

```bash
# 截取视频片段
# 时间格式：HH:MM:SS 或 秒数
ffmpeg -i input.* -ss START_TIME -to END_TIME -c copy output.*

# 分离视频流
ffmpeg -i input.mp4 -c:v copy -an output.mp4

# 分离音频流 aac m4a
ffmpeg -i input.mp4 -vn -y -acodec copy output.aac

# 水平裁剪视频两边空白
x=150; ffmpeg -i input.avi -filter:v "crop=out_w=in_w-2*${x}:out_h=in_h:x=${x}" output.avi

# 横向拼接两个视频
ffmpeg -i input1.avi -i input2.avi -filter_complex "[0:v][1:v]hstack=inputs=2[v]" -map "[v]" output.avi


# 多个视频文件合并

# 情况 1：使用 Concat 协议（适用于格式完全相同的视频）
# 创建一个文本文件：列出所有要合并的视频文件；文件路径前加 file
file 'file1.mkv'
file 'file2.mkv'
file 'file3.mkv'

ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mkv

# 情况 2：使用 Concat 滤镜（适用于需要重新编码的情况）
# 采用 libx264 视频编码器和 aac 音频编码器
ffmpeg -i "concat:input1.*|input2.*" -c:v libx264 -crf 23 -preset fast -c:a aac -b:a 192k output.mkv
```


---

### 图片相关

```bash
# 视频流转 gif
ffmpeg -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" -c:v gif -f gif output.gif

# 单张图片转 gif
ffmpeg -f image2 -i input.jpg output.gif

# 多张图片转 gif
# -r 1: 每秒 1 张的帧率
# %d: 表示一位数，按序号排列；2d 表示 01，02
ffmpeg -r 1 -f image2 -i input_%d.jpg  output.gif

# 单张图片 + 音频合并成视频
ffmpeg -r 0.1 -loop 1 -i input.png -i input.mp3 -c:v libx264 -tune stillimage -preset ultrafast -ss 00:00:00 -t 00:05:37 -c:a aac -b:a 320k -pix_fmt yuv420p -shortest output.mp4 -y

# 多张图片 + 音频合并成视频
# -pattern_type glob: 正则匹配
ffmpeg -r 0.1 -loop 1 -pattern_type glob -i 'input*.png' -i input.mp3 -c:v libx264 -tune stillimage -preset ultrafast -ss 00:00:00 -t 00:05:37 -c:a aac -b:a 320k -pix_fmt yuv420p -shortest output.mp4 -y

# 在图片中添加文字 使用 drawtext 过滤器实现
ffmpeg -i input.gif -vf "drawtext=text='Your Text Here':fontfile=/path/to/font.ttf:fontsize=24:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2" output.gif

```


---

### 音频相关

```bash
# 查看音乐文件元数据
ffprobe -v quiet -print_format json -show_format -show_streams input.flac

# 查看整轨 APE 音乐文件元数据（含歌曲总数和每首歌曲的开始时间）
ffprobe -show_entries format=nb_streams -show_entries stream=codec_type,start_time -print_format flat input.ape

# FLAC 转 MP3 保留元数据
ffmpeg -i input.flac -ab 320k -map_metadata 0 -id3v2_version 3 -acodec libmp3lame output.mp3

#  APE 转 FLAC
ffmpeg -i input.ape -c:a flac output.flac

# LPCM 无损压缩转 FLAC
```


---

### 其他

```bash
ffmpeg -hwaccels  # 列出硬件加速方法
ffmpeg -decoders  # 查看支持的所有解码器
ffmpeg -encoders  # 查看支持的所有编码器
```

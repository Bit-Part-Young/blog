import glob
import os

from PIL import Image


def figCompress(
    base_dir: str,
    target_dir: str,
    quality: int = 70,
    fig_suffix: str = "jpg",
):
    # 压缩但尽量保持高质量所有的.jpg图片
    for fig_file in glob.glob(f"{base_dir}/**/*.{fig_suffix}", recursive=True):
        try:
            # 构建目标文件路径
            relative_path = os.path.relpath(fig_file, base_dir)
            target_file_path = os.path.join(target_dir, relative_path)

            # 确保目标目录存在
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

            # 打开原始图片
            with Image.open(fig_file) as img:
                # 调整质量参数为85，可以根据需求调整
                img.save(target_file_path, quality=quality, optimize=True)
                # img.save(target_file_path, "JPEG", quality=quality, optimize=True)
                print(f"Compressed and saved to: {target_file_path}")
        except Exception as e:
            print(f"Error processing {fig_file}: {e}")


if __name__ == "__main__":
    # 设置原始和目标工作目录
    base_dir = "cover"
    target_dir = "cover-compressed"
    quality = 40

    figCompress(base_dir, target_dir, quality=quality, fig_suffix="jpg")
    figCompress(base_dir, target_dir, quality=quality, fig_suffix="png")

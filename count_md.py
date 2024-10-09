import os
from glob import glob


def count_md(directory: str) -> int:
    """统计 md 文件数目"""

    md_list = glob(
        os.path.join(directory, "**/*.md"),
        recursive=True,
    )

    filtered_md_list = [
        f
        for f in md_list
        if os.path.basename(f)
        not in [
            "index.md",
            "links.md",
            "changelog.md",
            "mkdocs-test.md",
            "README.md",
        ]
    ]

    # for f in filtered_md_list:
    #     print(f)

    return len(filtered_md_list)


directory_path = "source/_posts"
count = count_md(directory_path)
print(f"md files count: {count}.")

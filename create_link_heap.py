"""This script adds links to all of the finished markdown files in the obsidian repo into README.md, in a random order."""

import random
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as file:
    readme_text_to_keep = file.read().split("<br>")[0] + "<br>\n\n"

markdown_links: list[str] = []

folders_to_include: tuple[str, ...] = (
    "2 - Full Notes",
    "3 - Source Material",
    "4 - Maps of Content",
)

for path in Path("obsidian-vault").rglob("*.md"):
    if path.parts[1] in (folders_to_include):
        markdown_links.append(f"[{path.name}](./{path.as_posix().replace(" ", "%20")})")

random.shuffle(markdown_links)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_text_to_keep + ", ".join(markdown_links))

"""This script adds links to all of the finished markdown files in the obsidian repo into README.md, in a random order."""

import random
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as file:
    readme_text_to_keep = file.read().split("<br>")[0] + "<br>\n\n"

markdown_links: list[str] = []

for path in Path("obsidian-vault").rglob("*.md"):
    if "Rough Notes" not in str(path):
        markdown_links.append(f"[{path.name}](./{str(path).replace(" ", "%20")})")

random.shuffle(markdown_links)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_text_to_keep + ", ".join(markdown_links))

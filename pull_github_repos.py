"""Pulls all of my public github repos,
including their tags and README files,
and writes them into markdown files in 
my obsidian vault (in the /github_repos folder)
"""

import time
from typing import Final

import requests
from tqdm import tqdm

repos_data: list[dict] = []

GITHUB_USERNAME: Final[str] = "J-sephB-lt-n"
N_RESULTS_PER_PAGE: Final[int] = 50
page_num: int = 1

response = requests.get(
    url=f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
    params={
        "per_page": N_RESULTS_PER_PAGE,
        "page": page_num,
    },
)
for repo_info in tqdm(response.json()):
    # readme_metadata_response = requests.get(
    #     url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_info['name']}/readme"
    # )
    readme_contents_response = requests.get(
        url=f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{repo_info['name']}/main/README.md"
    )
    print(readme_contents_response.text)
    time.sleep(0.5)
    repos_data.append(
        {k: v for k, v in repo_info.items() if k in ("name", "description", "html_url")}
    )

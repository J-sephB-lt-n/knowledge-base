import requests

repos_metadata: list[dict] = []

url: str = "https://api.github.com/users/J-sephB-lt-n/repos?type=public"
while True:
    print(f"processing {url}")
    repos_data_response = requests.get(
        url=url,
        timeout=10,
    )
    repos_metadata += repos_data_response.json()
    if not repos_data_response.links.get("next"):
        break
    url = repos_data_response.links["next"]["url"]

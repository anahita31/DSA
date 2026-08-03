import os
import shutil
import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query getQuestion($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    difficulty
  }
}
"""

ROOT = os.path.dirname(os.path.abspath(__file__))


def get_difficulty(slug):
    try:
        response = requests.post(
            GRAPHQL_URL,
            json={
                "query": QUERY,
                "variables": {
                    "titleSlug": slug
                }
            },
            timeout=10,
        )

        data = response.json()

        return data["data"]["question"]["difficulty"]

    except Exception as e:
        print(f"Error fetching {slug}: {e}")
        return None


for folder in ["Easy", "Medium", "Hard"]:
    os.makedirs(os.path.join(ROOT, folder), exist_ok=True)

for item in os.listdir(ROOT):

    path = os.path.join(ROOT, item)

    if not os.path.isdir(path):
        continue

    if item.startswith("."):
        continue

    if item in ["Easy", "Medium", "Hard"]:
        continue

    parts = item.split("-", 1)

    if len(parts) != 2:
        continue

    slug = parts[1]

    difficulty = get_difficulty(slug)

    if difficulty is None:
        print(f"Skipping {item}")
        continue

    destination = os.path.join(ROOT, difficulty, item)

    if os.path.exists(destination):
        continue

    shutil.move(path, destination)

    print(f"{item} -> {difficulty}")

print("Done!")

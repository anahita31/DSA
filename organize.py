import os
import shutil

DIFFICULTY = {
    1: "Easy",
    15: "Medium",
    88: "Easy",
    125: "Easy",
    167: "Medium",
    169: "Easy",
    217: "Easy",
    268: "Easy",
    344: "Easy",
    414: "Easy",
    448: "Easy",
    645: "Easy",
    792: "Easy",
    1019: "Easy",
    1603: "Easy",
    2917: "Medium",
}

ROOT = os.path.dirname(os.path.abspath(__file__))

# Create folders if they don't exist
for folder in ["Easy", "Medium", "Hard"]:
    os.makedirs(os.path.join(ROOT, folder), exist_ok=True)

for item in os.listdir(ROOT):
    path = os.path.join(ROOT, item)

    if not os.path.isdir(path):
        continue

    if item.startswith(".") or item in ["Easy", "Medium", "Hard"]:
        continue

    try:
        problem_no = int(item.split("-")[0])
    except ValueError:
        continue

    difficulty = DIFFICULTY.get(problem_no)

    if difficulty is None:
        print(f"Skipping {item} (difficulty unknown)")
        continue

    destination = os.path.join(ROOT, difficulty, item)

    if os.path.exists(destination):
        shutil.rmtree(destination)

    shutil.move(path, destination)
    print(f"Moved {item} -> {difficulty}")

print("Finished organizing.")

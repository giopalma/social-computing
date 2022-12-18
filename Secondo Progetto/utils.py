import json
import os


def serealize_json(folder, filename, data):
    if not os.path.exists(folder):
        os.makedirs(folder,exist_ok=True)
    with open(f"{folder}/{filename}.json", "w", encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)
        f.close()
    print(f"Data serialized to path: {folder}/{filename}.json")

def read_json(path):
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
    except ValueError:
        print("Path not found, check the correctness of the path")
import json
import os

DATA_DIR = os.getenv("DATA_DIR", "data")
os.makedirs(DATA_DIR, exist_ok=True)

def _path(key: str) -> str:
    filename = key if key.endswith(".json") else f"{key}.json"
    return os.path.join(DATA_DIR, filename)

def cargar_json(key: str) -> dict:
    path = _path(key)
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def guardar_json(key: str, data: dict):
    path = _path(key)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)

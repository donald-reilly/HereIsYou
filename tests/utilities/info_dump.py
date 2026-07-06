from pathlib import Path
import json

def save_inspection(data):
    path = Path()
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default= str)

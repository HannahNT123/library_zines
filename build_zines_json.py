import yaml
import json
from pathlib import Path

zines = []

for meta in Path("zines").rglob("metadata.yaml"):
    with open(meta, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    zine_dir = meta.parent

    pdfs = list(zine_dir.glob("*.pdf"))
    covers = list(zine_dir.glob("cover.*"))

    if not pdfs or not covers:
        continue

    zines.append({
        "title": data.get("title"),
        "tags": data.get("tags", []),
        "pdf": str(pdfs[0]),
        "cover": str(covers[0])
    })

with open("zines.json", "w", encoding="utf-8") as f:
    json.dump(zines, f, indent=2)

print(f"Wrote {len(zines)} zines to zines.json")

import os
import json
from pathlib import Path
import pandas as pd

genre_dir = Path("./genrepredictions")
results = []

for json_file in genre_dir.glob("*.json"):
    docid = json_file.stem
    with open(json_file, "r") as f:
        try:
            genres = json.load(f)
            # genres might be a list or a dict depending on version
            if isinstance(genres, dict) and "genres" in genres:
                genres = genres["genres"]
            fiction_pages = sum(1 for g in genres if g.lower().startswith("fic"))
            total_pages = len(genres)
            results.append({
                "docid": docid,
                "fiction_pages": fiction_pages,
                "total_pages": total_pages,
                "fiction_ratio": fiction_pages / total_pages if total_pages > 0 else 0
            })
        except Exception as e:
            print(f"Error processing {docid}: {e}")

df = pd.DataFrame(results)
df.to_csv("fiction_page_ratios.csv", index=False)
print(df.head())

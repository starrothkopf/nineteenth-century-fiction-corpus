from htrc_features import Volume
import pandas as pd

with open("my_docids.txt", "r") as f:
    vol_ids = [line.strip() for line in f if line.strip()]

summaries = []

for vol_id in vol_ids:
    try:
        vol = Volume(vol_id)
        meta = vol.parser.meta

        summaries.append({
            'id': meta.get('id', ''),
            'title': meta.get('title', ''),
            'year': meta.get('pub_date', ''),
            'page_count': meta.get('page_count', ''),
            'genre': meta.get('genre', ''),
            'source_institution': meta.get('source_institution', ''),
        })

    except Exception as e:
        print(f"Error with {vol_id}: {e}")

df = pd.DataFrame(summaries)
print(df.head())
df.to_csv("metadata_summary.csv", index=False)

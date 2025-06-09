import os
import pandas as pd
from htrc_features import Volume

ef_dir = "ef_data/"
ef_files = []

for root, dirs, files in os.walk(ef_dir):
    for file in files:
        if file.endswith(".json.bz2"):
            ef_files.append(os.path.join(root, file))

print("Number of EF files:", len(ef_files))

summaries = []

for filepath in ef_files:
    try:
        vol = Volume(filepath)
        tokenlist = vol.tokenlist(pos=False, case=False, drop_section=True)
        token_count = tokenlist['count'].sum()
        meta = vol.parser.meta

        summaries.append({
            'id': meta.get('id'),
            'token_count': token_count,
            'page_count': meta.get('page_count'),
            'pub_date': meta.get('pub_date'),
            'genre': meta.get('genre'),
            'source_institution': meta.get('source_institution'),
        })

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

df = pd.DataFrame(summaries)
df.to_csv("ef_features_summary.csv", index=False)

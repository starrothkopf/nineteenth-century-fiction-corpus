import os
import pandas as pd
from htrc_features import Volume
import multiprocessing

ef_dir = "ef_data/"
ef_files = []
summaries = []

for root, dirs, files in os.walk(ef_dir):
    for file in files:
        if file.endswith(".json.bz2"):
            ef_files.append(os.path.join(root, file))

for i, filepath in enumerate(ef_files):
    try:
        vol = Volume(filepath)
        # tokenlist = vol.tokenlist(pos=False, case=False, drop_section=True)
        token_count = None
        meta = vol.parser.meta

        summaries.append({
            'id': meta.get('id'),
            'page_count': meta.get('page_count'),
            'pub_date': meta.get('pub_date'),
            'genre': meta.get('genre'),
            'source_institution': meta.get('source_institution'),
        })

        if i % 100 == 0:
            print(f"Processed {i}/{len(ef_files)} files")

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

df = pd.DataFrame(summaries)
df.to_csv("ef_features_summary.csv", index=False)

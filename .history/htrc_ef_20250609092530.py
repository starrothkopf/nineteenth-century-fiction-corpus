import os
import pandas as pd
from htrc_features import Volume

ef_dir = "ef_data/"  # change this if needed

summaries = []

for filename in os.listdir(ef_dir):
    if filename.endswith(".json.bz2"):
        try:
            vol = Volume(os.path.join(ef_dir, filename))
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
            print(f"Error reading {filename}: {e}")

# Save to CSV
df = pd.DataFrame(summaries)
df.to_csv("ef_features_summary.csv", index=False)

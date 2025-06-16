import os
import numpy as np
import pandas as pd
from htrc_features import Volume

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
        meta = vol.parser.meta

        sentence_counts = vol.sentence_counts()
        line_counts = vol.line_counts()
        tokens_per_page = vol.tokens_per_page()
        cap_alpha_seq = vol.cap_alpha_seq()

        summaries.append({
            "id": meta.get("id"),
            "access_rights": meta.get("accessRights"),
            "avg_sentence_count": np.mean(sentence_counts) if sentence_counts else None,
            "var_sentence_count": np.var(sentence_counts) if sentence_counts else None,
            "avg_line_count": np.mean(line_counts) if line_counts else None,
            "var_line_count": np.var(line_counts) if line_counts else None,
            "avg_tokens_per_page": np.mean(tokens_per_page) if tokens_per_page is not None else None,
            "var_tokens_per_page": np.var(tokens_per_page) if tokens_per_page is not None else None,
            "cap_alpha_freq": np.mean(cap_alpha_seq) if cap_alpha_seq else None,
            "page_count": meta.get("pageCount"),
            "genre_tag": meta.get("genre"),
            "lcc_category": meta.get("category"),
            "part_of_journal": meta.get("isPartOf", {}).get("journalTitle") if meta.get("isPartOf") else None,
        })

        if i % 100 == 0:
            print(f"Processed {i}/{len(ef_files)} files")

    except Exception as e:
        print(f"Error reading {filepath}: {e}")

df = pd.DataFrame(summaries)
df.to_csv("ef_rich_features_summary.csv", index=False)

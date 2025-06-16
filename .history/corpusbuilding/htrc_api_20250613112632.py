import requests
import time
import pandas as pd

df = pd.read_csv("ef_rich_features_cleaned.csv")
df_missing = df[df["page_count"].isna()]

results = []

for i, row in df_missing.iterrows():
    htid = row["id"]
    url = f"http://catalog.hathitrust.org/api/volumes/full/htid/{htid}.json"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            meta = data.get("records", {}).get(htid, {}).get("record", {})
            page_count = meta.get("numberOfPages") or None
            access_rights = meta.get("accessRights") or None
            part_of_journal = meta.get("isPartOf", {}).get("journalTitle", None)
            results.append({
                "id": htid,
                "page_count": page_count,
                "access_rights": access_rights,
                "part_of_journal": part_of_journal
            })
        else:
            print(f"{htid} failed: {res.status_code}")
    except Exception as e:
        print(f"{htid} error: {e}")

    time.sleep(1.5)  # Slow down to avoid throttling

meta_df = pd.DataFrame(results)
meta_df.to_csv("bib_metadata_fill.csv", index=False)

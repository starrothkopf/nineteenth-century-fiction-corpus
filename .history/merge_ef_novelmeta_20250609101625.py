import pandas as pd

meta_df = pd.read_csv("filtered_titlemeta_with_gender.tsv", sep="\t")
ef_df = pd.read_csv("ef_features_summary_cleaned.csv")

ef_df = ef_df.rename(columns={"id": "docid"})

# Normalize EF docids
def normalize_id(htid):
    return htid.replace(':', '+').replace('/', '=')

ef_df['docid'] = ef_df['docid'].apply(normalize_id)

# Ensure consistent string type
meta_df['docid'] = meta_df['docid'].apply(str)

# Merge on normalized docid
merged_df = pd.merge(meta_df, ef_df, on="docid", how="inner")

# Save to CSV
merged_df.to_csv("merged_metadata_with_ef.csv", index=False)

# Print results
print(f"Merged dataset has {len(merged_df)} rows.")
print("Saved to merged_metadata_with_ef.csv")

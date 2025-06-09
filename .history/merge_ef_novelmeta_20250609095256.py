import pandas as pd

meta_df = pd.read_csv("filtered_titlemeta_with_gender.tsv", sep="\t")
ef_df = pd.read_csv("ef_features_summary_cleaned.csv")

# Rename 'id' to 'docid' to match
ef_df = ef_df.rename(columns={"id": "docid"})

# Merge on 'docid'
merged_df = pd.merge(meta_df, ef_df, on="docid", how="inner")

# Save merged result
merged_df.to_csv("merged_metadata_with_ef.csv", index=False)

# Print a quick summary
print(f"Merged dataset has {len(merged_df)} rows.")
print(merged_df[['docid', 'author', 'pub_date', 'page_count', 'genre']].head())

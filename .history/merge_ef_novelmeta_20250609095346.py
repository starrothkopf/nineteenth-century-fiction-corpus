import pandas as pd

meta_df = pd.read_csv("filtered_titlemeta_with_gender.tsv", sep="\t")
ef_df = pd.read_csv("ef_features_summary_cleaned.csv")

ef_df = ef_df.rename(columns={"id": "docid"})

# merge on docid
merged_df = pd.merge(meta_df, ef_df, on="docid", how="inner")
merged_df.to_csv("merged_metadata_with_ef.csv", index=False)

print(f"Merged dataset has {len(merged_df)} rows.")
print(merged_df.head())

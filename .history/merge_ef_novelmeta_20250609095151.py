import pandas as pd
import os

ef_df = pd.read_csv("ef_features_summary_cleaned.csv")
titlemeta_df = pd.read_csv("filtered_titlemeta_with_gender.tsv", sep='\t')

def clean_ef_id(val):
    base = os.path.basename(val)
    return base.split("____")[0].replace(".txt", "").replace(".json.bz2", "")

ef_df['docid'] = ef_df['id'].apply(clean_ef_id)

# Merge on 'docid'
merged_df = pd.merge(titlemeta_df, ef_df, on='docid', how='left')

# Save the merged output
merged_df.to_csv("merged_metadata_with_ef.csv", index=False)

# Print summary
print(f"Merged dataset contains {len(merged_df)} rows.")
print("Example rows with EF data:")
print(merged_df[~merged_df['page_count'].isna()].head())

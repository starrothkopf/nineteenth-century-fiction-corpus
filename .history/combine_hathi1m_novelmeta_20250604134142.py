import pandas as pd

# hathi1M dataset
df_hathi = pd.read_csv("Enriched_Feature_Set_Fiction.csv")

# novelTM metadata subset (filtered for 1800–1913, British/Irish, novels only)
df_noveltm = pd.read_csv("filtered_titlemeta_with_gender.tsv")

df_noveltm['docid'] = df_noveltm['docid'].str.strip()
df_hathi['htid'] = df_hathi['htid'].str.strip()

# Filter Hathi1M where htid is in NovelTM docid list
filtered_df = df_hathi[df_hathi['htid'].isin(df_noveltm['docid'])]

# Summary
print(f"{len(filtered_df)} pages matched out of {len(df_hathi)} total Hathi1M pages.")

# Save
filtered_df.to_csv("Hathi1M_matched_with_NovelTM.csv", index=False)
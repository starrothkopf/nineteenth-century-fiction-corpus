import pandas as pd

# Load both datasets
meta_df = pd.read_csv("noveltm_ef.csv")
fic_df = pd.read_csv("fiction_proportions.csv")

# Just in case, normalize IDs to ensure match
def normalize_id(htid):
    return htid.replace(':', '+').replace('/', '=')

meta_df['docid'] = meta_df['docid'].apply(normalize_id)
fic_df['docid'] = fic_df['docid'].apply(normalize_id)

# Merge on docid
merged_df = meta_df.merge(fic_df[['docid', 'pct_fic']], on='docid', how='left')

# Create binary fiction label
merged_df['label_fiction'] = merged_df['pct_fic'].apply(lambda x: 1 if x >= 0.7 else 0 if pd.notnull(x) else None)

# Optional: drop rows with no label if you're training a classifier
labeled_df = merged_df.dropna(subset=['label_fiction'])

# Save the result
labeled_df.to_csv("noveltm_with_fiction_labels.csv", index=False)

print(f"Labeled fiction in {labeled_df.shape[0]} volumes.")
print(labeled_df['label_fiction'].value_counts())

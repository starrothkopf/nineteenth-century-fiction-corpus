import pandas as pd

# Load and normalize
meta_df = pd.read_csv("filtered_titlemeta_with_gender.tsv", sep="\t")
ef_df = pd.read_csv("ef_features_summary_cleaned.csv")

# Rename and normalize ef docids
ef_df = ef_df.rename(columns={"id": "docid"})

def normalize_id(htid):
    # Replace slashes and colons, but keep the = after 'ark'
    norm = htid.replace('/', '+').replace(':', '=')
    if 'ark=' in norm and not norm.startswith('uc2.ark+=') and '+13960=' in norm:
        norm = norm.replace('ark=', 'ark+=')
    return norm

ef_df['docid'] = ef_df['docid'].apply(normalize_id)

# Normalize meta_df docids just in case
meta_df['docid'] = meta_df['docid'].apply(str)  # ensure string type

# Check what’s missing
meta_ids = set(meta_df['docid'])
ef_ids = set(ef_df['docid'])

missing_in_ef = meta_ids - ef_ids
missing_in_meta = ef_ids - meta_ids

print(f"\nDocIDs in meta but not in EF: {len(missing_in_ef)}")
print(list(missing_in_ef)[:10])  # preview first 10

print(f"\nDocIDs in EF but not in meta: {len(missing_in_meta)}")
print(list(missing_in_meta)[:10])  # preview first 10

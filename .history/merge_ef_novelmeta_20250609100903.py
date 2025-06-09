import pandas as pd

# Load and normalize
meta_df = pd.read_csv("filtered_titlemeta_with_gender.tsv", sep="\t")
ef_df = pd.read_csv("ef_features_summary_cleaned.csv")

# Rename and normalize ef docids
ef_df = ef_df.rename(columns={"id": "docid"})

def normalize_id(htid):
    # Step 1: replace only the first slash and colon (for ark:/ and ark:)
    if htid.startswith("uc2.ark:/") or htid.startswith("uiuo.ark:/"):
        htid = htid.replace("ark:/", "ark+=")
    elif "ark:" in htid:
        htid = htid.replace("ark:", "ark+=")

    # Step 2: replace remaining / with +, but leave = untouched
    htid = htid.replace('/', '+')
    return htid


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

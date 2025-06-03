import pandas as pd

df = pd.read_csv('metadata/volumemeta.tsv', sep='\t', encoding='utf-8')

# 19th century
df = df[df['inferreddate'].between(1789, 1913, inclusive='both')]

# genre double check
if 'genres' in df.columns:
    # Remove probable non-fiction genres
    exclude_terms = ['biography', 'travel', 'folklore', 'essays']
    mask = ~df['genres'].fillna('').str.lower().str.contains('|'.join(exclude_terms))
    df = df[mask]

# british/irish
british_irish_codes = ['enk', 'stk', 'ie', 'uk', 'xxk'] 
df = df[df['place'].str.lower().isin(british_irish_codes)]

# clean + deduplicate
df = df[df['inferreddate'] > 0]
df_dedup = df.drop_duplicates(subset=['author', 'shorttitle', 'inferreddate'])

print(f"Deduplicated: from {len(df)} rows to {len(df_dedup)}")

# Save deduplicated results
df_dedup.to_csv('filtered_deduplicated_nineteenth_century_fiction.tsv', sep='\t', index=False)


df.to_csv('filtered_nineteenth_century_fiction.tsv', sep='\t', index=False)

print(f"Filtered dataset saved. Total rows: {len(df)}")

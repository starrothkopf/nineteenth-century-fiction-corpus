import pandas as pd

df = pd.read_csv('metadata/volumemeta.tsv', sep='\t', encoding='utf-8')

# STEP 1: Filter by publication year (use 'inferreddate')
df = df[df['inferreddate'].between(1789, 1913, inclusive='both')]

# STEP 2: Optional double-check on genre
# All volumes are likely fiction, but we can exclude travel/biography if genres field helps
if 'genres' in df.columns:
    # Remove probable non-fiction genres
    exclude_terms = ['biography', 'travel', 'folklore', 'essays']
    mask = ~df['genres'].fillna('').str.lower().str.contains('|'.join(exclude_terms))
    df = df[mask]

# STEP 3: Filter by British/Irish publication place
# 'place' uses MARC country codes – let's keep ones for UK and Ireland
british_irish_codes = ['enk', 'stk', 'ie', 'uk', 'xxk']  # England, Scotland, Ireland, UK, Unknown UK
df = df[df['place'].str.lower().isin(british_irish_codes)]

# STEP 4: Remove entries with missing or zero date
df = df[df['inferreddate'] > 0]

# Save the filtered dataset
df.to_csv('filtered_nineteenth_century_fiction.tsv', sep='\t', index=False)

print(f"Filtered dataset saved. Total rows: {len(df)}")

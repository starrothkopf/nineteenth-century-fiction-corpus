import pandas as pd

titlemeta = pd.read_csv('metadata/titlemeta.tsv', sep='\t', encoding='utf-8')
manual = pd.read_csv('metadata/manual_title_subset.tsv', sep='\t', encoding='utf-8')

british_irish_codes = ['enk', 'stk', 'ie', 'uk', 'xxk']

def clean_and_filter(df, name):
    print(f"\nProcessing: {name}")
    
    df = df[df['inferreddate'].fillna(0).astype(int) > 0]
    
    df = df[(df['inferreddate'] >= 1789) & (df['inferreddate'] <= 1913)]
    
    if df = titlemeta
    df = df[df['place'].str.lower().isin(british_irish_codes)]
    
    # Flag as British/Irish
    df['nationality'] = 'British or Irish'
    
    # Remove duplicates by title + author + year
    df = df.drop_duplicates(subset=['author', 'shorttitle', 'inferreddate'])

    # Keep only relevant columns
    cols_to_keep = ['author', 'inferreddate', 'gender', 'shorttitle', 'nationality']
    df = df[[col for col in cols_to_keep if col in df.columns]]
    
    print(f"{name} final count: {len(df)} rows")
    
    # Save filtered file
    outname = f"filtered_{name.replace(' ', '_').lower()}.tsv"
    df.to_csv(outname, sep='\t', index=False)
    print(f"Saved to {outname}")
    
    return df

# 19th century
df = df[df['inferreddate'].between(1789, 1913, inclusive='both')]

# remove non-fiction genres
if 'genres' in df.columns:
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

df_dedup.to_csv('filtered_deduplicated_nineteenth_century_fiction.tsv', sep='\t', index=False)

print(f"Dataset saved. Total rows: {len(df)}")

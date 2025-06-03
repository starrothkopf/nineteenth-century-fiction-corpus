import pandas as pd

titlemeta = pd.read_csv('metadata/titlemeta.tsv', sep='\t', encoding='utf-8')
manual = pd.read_csv('metadata/manual_title_subset.tsv', sep='\t', encoding='utf-8')

british_irish_codes = ['enk', 'stk', 'ie', 'uk', 'xxk', 'ir']

def clean_and_filter(df, name):
    print(f"\nProcessing: {name}")
    
    df = df[df['inferreddate'].fillna(0).astype(int) > 0]
    df = df[(df['inferreddate'] >= 1789) & (df['inferreddate'] <= 1913)]

    if 'place' in df.columns:
        df = df[df['place'].str.lower().isin(british_irish_codes)]
    elif 'nationality' in df.columns:
        df = df[df['nationality'].str.lower().isin(british_irish_codes)]

    if 'category' in df.columns:
        df = df[df['category'] == 'longfiction']

    if 'genres' in df.columns:
    # exclude clearly non-novel categories
        exclude_genres = ['short stories', 'humorous stories', 'adventure stories', 'western stories',
                        'biography', 'autobiography', 'bibliographies', "publishers' advertisements",
                        'juvenile literature', 'satire']
        
        def is_excluded(genres):
            if pd.isna(genres): return False
            genres_lower = genres.lower()
            return any(ex in genres_lower for ex in exclude_genres)

        df = df[~df['genres'].apply(is_excluded)].copy()

    df = df.drop_duplicates(subset=['author', 'shorttitle', 'inferreddate'])

    cols_to_keep = ['author', 'inferreddate', 'gender', 'shorttitle', 'nationality', 'place', 'category']
    df = df[[col for col in cols_to_keep if col in df.columns]]
    
    print(f"{name} final count: {len(df)} rows")
    
    outname = f"filtered_{name.replace(' ', '_').lower()}.tsv"
    df.to_csv(outname, sep='\t', index=False)
    print(f"Saved to {outname}")
    
    return df

titlemeta_filtered = clean_and_filter(titlemeta, 'TitleMeta')
manual_filtered = clean_and_filter(manual, 'ManualTitleSubset')

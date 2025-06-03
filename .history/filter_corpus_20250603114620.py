import pandas as pd

titlemeta = pd.read_csv('metadata/titlemeta.tsv', sep='\t', encoding='utf-8')
manual = pd.read_csv('metadata/manual_title_subset.tsv', sep='\t', encoding='utf-8')

british_irish_codes = ['enk', 'stk', 'ie', 'uk', 'xxk', 'ir']

relevant_genres = set([
    'novel', 'domestic fiction', 'historical fiction', 'psychological fiction',
    'mystery fiction', 'detective and mystery stories', 'love stories',
    'suspense fiction', 'science fiction', 'fantasy fiction', 'biographical fiction',
    'bildungsromans', 'bildungsromane', 'adventure fiction', 'political fiction',
    'christian fiction', 'humorous fiction', 'autobiographical fiction',
    'romantic suspense fiction', 'romantic suspense novels', 'mystery and detective fiction', 'occult fiction',
    'horror fiction', 'fantastic fiction'
])

def filter_by_genre(df):
    if 'genres' not in df.columns:
        return df 

    def is_relevant(genres):
        tags = [tag.strip().lower() for tag in str(genres).split('|')]
        return any(tag in relevant_genres for tag in tags)

    return df[df['genres'].apply(is_relevant)].copy()

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
    

    df = filter_by_genre(df)

    df = df.drop_duplicates(subset=['author', 'shorttitle', 'inferreddate'])

    cols_to_keep = ['author', 'inferreddate', 'gender', 'shorttitle', 'nationality', 'place', 'category', 'genres']
    df = df[[col for col in cols_to_keep if col in df.columns]]
    
    print(f"{name} final count: {len(df)} rows")
    
    outname = f"filtered_{name.replace(' ', '_').lower()}.tsv"
    df.to_csv(outname, sep='\t', index=False)
    print(f"Saved to {outname}")
    
    return df

titlemeta_filtered = clean_and_filter(titlemeta, 'TitleMeta')
manual_filtered = clean_and_filter(manual, 'ManualTitleSubset')

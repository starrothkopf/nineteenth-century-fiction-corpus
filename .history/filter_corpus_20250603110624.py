import pandas as pd

titlemeta = pd.read_csv('metadata/titlemeta.tsv', sep='\t', encoding='utf-8')
manual = pd.read_csv('metadata/manual_title_subset.tsv', sep='\t', encoding='utf-8')

british_irish_codes = ['enk', 'stk', 'ie', 'uk', 'xxk']

def clean_and_filter(df, name):
    print(f"\nProcessing: {name}")
    
    df = df[df['inferreddate'].fillna(0).astype(int) > 0]
    df = df[(df['inferreddate'] >= 1789) & (df['inferreddate'] <= 1913)]

    if 'place' in df.columns:
        df = df[df['place'].str.lower().isin(british_irish_codes)]
    elif 'nationality' in df.columns:
        df = df[df['nationality'].str.lower().isin(british_irish_codes)]

    cols_to_keep = ['author', 'inferreddate', 'gender', 'shorttitle', 'nationality', 'place']
    df = df[[col for col in cols_to_keep if col in df.columns]]
    
    print(f"{name} final count: {len(df)} rows")
    
    outname = f"filtered_{name.replace(' ', '_').lower()}.tsv"
    df.to_csv(outname, sep='\t', index=False)
    print(f"Saved to {outname}")
    
    return df

titlemeta_filtered = clean_and_filter(titlemeta, 'TitleMeta')
manual_filtered = clean_and_filter(manual, 'ManualTitleSubset')

print(f"TitleMeta size: {len(titlemeta_filtered)}")
print(f"ManualTitleSubset size: {len(manual_filtered)}")

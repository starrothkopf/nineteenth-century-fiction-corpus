import pandas as pd

df = pd.read_csv("merged_metadata_with_ef.csv")

def combine_genres(row):
    ef_genre = row.get('genre', '')
    novel_genres = row.get('genres', '')

    if pd.isna(novel_genres):
        return 'Fiction' if ef_genre == 'fiction' else 'unknown'
    
    if 'fiction' in novel_genres.lower():
        return novel_genres

    # Prepend 'Fiction' if EF said it's fiction
    if ef_genre == 'fiction':
        return f"Fiction|{novel_genres}"
    
    return novel_genres

# Apply and clean
df['genre'] = df.apply(combine_genres, axis=1)
df = df.drop(columns=['genres', 'source_institution'])

# Reorder columns
cols = ['docid', 'author', 'inferreddate', 'enumcron', 'volnum',
        'nonficprob', 'place', 'first_name', 'estimated_gender',
        'page_count', 'pub_date', 'genre']
df = df[cols]

# Save
df.to_csv("merged_metadata_cleaned.csv", index=False)

print(f"✅ Final dataset saved as merged_metadata_cleaned.csv with {len(df)} rows.")

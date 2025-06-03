import pandas as pd

df = pd.read_csv('metadata/titlemeta.tsv', sep='\t', encoding='utf-8')

genre_series = df['genres'].dropna().astype(str).str.lower().str.split('|')
all_genres = [g.strip() for sublist in genre_series for g in sublist]
genre_counts = Counter(all_genres)

# Print top genres
for genre, count in genre_counts.most_common(30):
    print(f"{genre}: {count}")
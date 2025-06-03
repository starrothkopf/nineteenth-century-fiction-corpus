import pandas as pd
from collections import Counter

df = pd.read_csv('filtered_titlemeta_with_gender.tsv', sep='\t')

genre_series = df['genres'].dropna().astype(str).str.lower().str.split('|')
all_genres = [g.strip() for sublist in genre_series for g in sublist]
genre_counts = Counter(all_genres)

# top genres
for genre, count in genre_counts.most_common(50):
    print(f"{genre}: {count}")
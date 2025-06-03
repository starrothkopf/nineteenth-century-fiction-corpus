import pandas as pd
from collections import Counter

df = pd.read_csv('filtered_titlemeta_with_gender.tsv', sep='\t')
print(f"\nTotal entries: {len(df)}")

genre_series = df['genres'].dropna().astype(str).str.lower().str.split('|')
all_genres = [g.strip() for sublist in genre_series for g in sublist]
genre_counts = Counter(all_genres)

# top genres
for genre, count in genre_counts.most_common(50):
    print(f"{genre}: {count}")

# pub years
if 'inferreddate' in df.columns:
    print("\n Publication year distribution:")
    print(df['inferreddate'].value_counts().sort_index().tail(20))  # or .head() for earliest years

# top authors
if 'author' in df.columns:
    print("\n Most common authors:")
    print(df['author'].value_counts().head(15))
import pandas as pd
from collections import Counter

df = pd.read_csv('noveltm_ef.csv')
print(f"\ntotal entries: {len(df)}")

genre_series = df['genre'].dropna().astype(str).str.lower().str.split('|')
all_genres = [g.strip() for sublist in genre_series for g in sublist]
genre_counts = Counter(all_genres)

# top genres
for genre, count in genre_counts.most_common(25):
    print(f"{genre}: {count}")

# pub years
if 'inferreddate' in df.columns:
    df['year_bucket'] = (df['inferreddate'] // 10 * 10).astype(int)
    print("\npublication year distribution by decade:")
    print(df['year_bucket'].value_counts().sort_index())

# top authors
if 'author' in df.columns:
    print("\nmost common authors:")
    print(df['author'].value_counts().head(15))

# top places (no ireland?)
if 'place' in df.columns:
    print("\nmost common MARC country codes:")
    print(df['place'].value_counts().head(10))

avg_nonficprob = df.groupby("genre")["nonficprob"].mean().sort_values(ascending=False)
print("\nnonfic probs:")
print(avg_nonficprob.loc[["Fiction", "unknown"]])

df['docid'].dropna().to_csv('my_docids.txt', index=False, header=False)
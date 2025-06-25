import pandas as pd

# Load your CSV
df = pd.read_csv("rich_noveltm_ef.csv")

# Clean title fields and ensure string type
df['title'] = df['title'].fillna("").astype(str).str.strip().str.lower()
df['shorttitle'] = df['shorttitle'].fillna("").astype(str).str.strip().str.lower()

# Use shorttitle when available, otherwise fall back to title
df['group_title'] = df['shorttitle'].where(df['shorttitle'] != "", df['title'])

# Group by title + author to better identify works
df['author'] = df['author'].fillna("").astype(str).str.strip().str.lower()
df['volume_key'] = df['group_title'] + "::" + df['author']

# Count how many rows would be collapsed if we only kept one row per volume_key
volume_groups = df.groupby('volume_key')
collapsed_df = volume_groups.first().reset_index()

original_count = len(df)
collapsed_count = len(collapsed_df)
rows_lost = original_count - collapsed_count

print(f"Original rows: {original_count}")
print(f"Collapsed rows: {collapsed_count}")
print(f"Rows lost if collapsing volumes: {rows_lost}")

# Optional: output high-volume groups for inspection
multi_volume_works = volume_groups.size().reset_index(name='volume_count')
multi_volume_works = multi_volume_works[multi_volume_works['volume_count'] > 1]
multi_volume_works.to_csv("multi_volume_candidates.csv", index=False)

import pandas as pd

df = pd.read_csv('metadata/volumemeta.tsv', sep='\t', encoding='utf-8')

print("Columns:", df.columns.tolist())

# filter by publication year
df = df[df['date'].between(1789, 1913, inclusive='both')]

# STEP 2: Keep only fiction (many NovelTM lists already filtered this, but double check)
# This depends on the available columns — try filtering by 'genres' or 'class' if present
if 'genres' in df.columns:
    df = df[df['genres'].str.contains('fiction', case=False, na=False)]
elif 'class' in df.columns:
    df = df[df['class'].str.contains('fiction', case=False, na=False)]

# STEP 3: Filter by British/Irish origin
# Check if there's a column like 'place', 'pubplace', or 'nationality'
if 'place' in df.columns:
    df = df[df['place'].str.contains('London|Dublin|Edinburgh|Oxford|Cambridge|Britain|England|Ireland|Scotland', case=False, na=False)]
elif 'author_nationality' in df.columns:
    df = df[df['author_nationality'].str.contains('British|Irish|English|Scottish|Welsh', case=False, na=False)]

# Save filtered dataset
df.to_csv('filtered_nineteenth_century_fiction.tsv', sep='\t', index=False)

print("Filtered corpus saved as filtered_nineteenth_century_fiction.tsv")

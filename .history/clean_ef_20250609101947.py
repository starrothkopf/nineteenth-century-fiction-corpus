import pandas as pd

# Load merged dataset
df = pd.read_csv("merged_metadata_with_ef.csv")

# Inspect unique values in the genre columns
print("\nUnique `genre` values from EF:")
print(df['genre'].dropna().unique())

print("\nUnique `genres` values from NovelTM:")
print(df['genres'].dropna().unique())

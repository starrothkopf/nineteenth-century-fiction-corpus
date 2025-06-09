import pandas as pd
import ast

# Load the CSV
df = pd.read_csv("ef_features_summary.csv")

# Clean genre column
def simplify_genre(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        if 'fiction' in [g.lower() for g in genres]:
            return 'fiction'
        else:
            return 'unknown'
    except:
        return 'unknown'

df['genre'] = df['genre'].apply(simplify_genre)

# Save cleaned version
df.to_csv("ef_features_summary_cleaned.csv", index=False)

# Optional: print a summary
print(df['genre'].value_counts())

import pandas as pd
import ast

# Load the dataset
df = pd.read_csv("PATH/TO/YOUR/FINAL_DATASET.csv")

# Utility to safely parse list-like strings
def parse_list(val):
    if pd.isna(val) or val.strip() in ("", "[]"):
        return []
    try:
        parsed = ast.literal_eval(val)
        return [str(x).strip().lower() for x in parsed]
    except:
        return [val.strip().lower()]

df['genre_tag'] = df['genre_tag'].apply(parse_list)
df['lcc_category'] = df['lcc_category'].apply(parse_list)

# Define blocked genres and LCC categories
blocked_genres = {
    "biography", "autobiography", "bibliography", "dictionary", "encyclopedia",
    "survey of literature", "legal article", "government publication",
    "law report or digest", "catalog"
}

blocked_lcc = {
    "french literature - italian literature - spanish literature - portuguese literature",
    "american literature",
    "france - andorra - monaco",
    "german literature - dutch literature - flemish literature since 1830 - afrikaans literature - scandinavian literature - old norse literature:old icelandic and old norwegian - modern icelandic literature - faroese literature - danish literature - norwegian literature - swedish literature",
    "asia", "africa", "hunting sports", "oceania (south seas)",
    "history (general)", "psychology",
    "languages and literatures of eastern asia, africa, oceania",
    "history of the americas",
    "oriental languages and literatures",
    "british america (including canada)"
}

df = df[~df['genre_tag'].apply(lambda genres: any(g in blocked_genres for g in genres))]
df = df[~df['lcc_category'].apply(lambda lccs: any(l in blocked_lcc for l in lccs))]

df.to_csv("ef_rich_features_filtered.csv", index=False)
print("Filtered dataset saved as ef_rich_features_filtered.csv")

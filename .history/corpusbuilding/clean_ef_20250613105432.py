import pandas as pd
import ast
import numpy as np

# Step 1: Read the CSV safely
df = pd.read_csv("ef_rich_features_summary.csv", dtype=str)

# Step 2: Convert numeric columns
numeric_cols = [
    'avg_sentence_count', 'var_sentence_count',
    'avg_line_count', 'var_line_count',
    'avg_tokens_per_page', 'var_tokens_per_page',
    'page_count'
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# fix cap_alpha_freq — convert stringified Series to single float
def extract_mean_cap_alpha(val):
    if isinstance(val, str) and "Name:" in val:
        try:
            # get only the part before "Name:"
            lines = val.split("Name:")[0].strip().split("\n")
            values = [int(line.split()[-1]) for line in lines if line.strip()]
            return np.mean(values)
        except Exception:
            return np.nan
    try:
        return float(val)
    except:
        return np.nan

df['cap_alpha_freq'] = df['cap_alpha_freq'].apply(extract_mean_cap_alpha)

def parse_list(val):
    if pd.isna(val) or val.strip() in ("", "[]"):
        return []
    try:
        return ast.literal_eval(val)
    except Exception:
        return [val.strip()]

df['genre_tag'] = df['genre_tag'].apply(parse_list)
df['lcc_category'] = df['lcc_category'].apply(parse_list)

df.to_csv("ef_rich_features_cleaned.csv", index=False)
print("cleaned CSV saved as ef_rich_features_cleaned.csv")

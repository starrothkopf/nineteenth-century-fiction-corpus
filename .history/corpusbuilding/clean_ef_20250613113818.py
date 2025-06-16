import pandas as pd
import ast
import numpy as np

# Load CSV
df = pd.read_csv("/Users/starrothkopf/Desktop/HDW/noveltmmeta/corpusbuilding/ef_rich_features_summary.csv", dtype=str)

# Convert numeric columns
numeric_cols = [
    'avg_sentence_count', 'var_sentence_count',
    'avg_line_count', 'var_line_count',
    'avg_tokens_per_page', 'var_tokens_per_page',
    'page_count'
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

def extract_mean_cap_alpha(val):
    if isinstance(val, str):
        # find all numbers at the end of lines (after whitespace)
        numbers = re.findall(r'\s+(\d+)$', val, flags=re.MULTILINE)
        if numbers:
            values = [int(n) for n in numbers]
            return np.mean(values)
    try:
        return float(val)
    except:
        return np.nan

df['cap_alpha_freq'] = df['cap_alpha_freq'].apply(extract_mean_cap_alpha)

# print average
mean_cap_alpha = df['cap_alpha_freq'].mean()
print(f"Average cap_alpha_freq: {mean_cap_alpha:.3f}")

# Parse list columns
def parse_list(val):
    if pd.isna(val) or val.strip() in ("", "[]"):
        return []
    try:
        parsed = ast.literal_eval(val)
        if isinstance(parsed, list):
            return parsed
        else:
            return [parsed]
    except Exception:
        return [val.strip()]

df['genre_tag'] = df['genre_tag'].apply(parse_list)
df['lcc_category'] = df['lcc_category'].apply(parse_list)

mean_cap_alpha = df['cap_alpha_freq'].mean()
print(f"Average cap_alpha_freq: {mean_cap_alpha:.3f}")

# Save cleaned file
df.to_csv("ef_rich_features_cleaned.csv", index=False)
print("Cleaned CSV saved as ef_rich_features_cleaned.csv")

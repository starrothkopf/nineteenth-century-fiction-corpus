import pandas as pd

df = pd.read_csv("Enriched_Feature_Set_Fiction.csv")

df = df[(df['Year'] >= 1800) & (df['Year'] <= 1913)]

# prefixes for known UK/Irish libraries (customize as needed)
british_irish_prefixes = ['ucl', 'oxf', 'cam', 'stk', 'ie', 'irl']  # e.g. 'ucl' = UCL, 'oxf' = Oxford, etc.

# Function to extract the prefix from the htid (before the dot)
df['prefix'] = df['htid'].apply(lambda x: x.split('.')[0])

# Filter to rows with a UK/Ireland prefix
df_uk = df[df['prefix'].isin(british_irish_prefixes)]

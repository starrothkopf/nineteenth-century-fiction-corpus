import pandas as pd

df = pd.read_csv('metadata/titlemeta.tsv', sep='\t', encoding='utf-8')

# print unique genres (drop NaNs, lowercase, split by delimiter if needed)
print(df['genres'].dropna().unique())

import pandas as pd

df = pd.read_csv('metadata/titlemeta.tsv', sep='\t', encoding='utf-8')

# print unique genres
print(df['genres'].dropna().unique())

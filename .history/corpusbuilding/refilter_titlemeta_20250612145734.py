import pandas as pd

df = pd.read_csv("novelmeta/tedunderwood/metadata/titlemeta.tsv", sep='\t')
print(df.columns.tolist())
import pandas as pd

df = pd.read_csv("/tedunderwood/metadata/titlemeta.tsv", sep='\t')
print(df.columns.tolist())


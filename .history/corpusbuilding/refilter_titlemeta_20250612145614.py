import pandas as pd

df = pd.read_csv("/Users/starrothkopf/Desktop/HDW/noveltmmeta/tedunderwood/metadata/titlemeta.tsv", sep='\t')
print(df.columns.tolist())
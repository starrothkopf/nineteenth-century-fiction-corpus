import pandas as pd

df = pd.read_csv("Enriched_Feature_Set_Fiction.csv")

df = df[(df['Year'] >= 1800) & (df['Year'] <= 1913)]

# prefixes for known UK/Irish libraries ??
british_irish_prefixes = ['ucl', 'ox', 'cam', 'trincoll'] 
df['prefix'] = df['htid'].apply(lambda x: x.split('.')[0])
df_uk = df[df['prefix'].isin(british_irish_prefixes)]

print("Total rows after year filter:", len(df))
print("Rows from British/Irish institutions:", len(df_uk))
print("Proportion British/Irish:", round(len(df_uk) / len(df) * 100, 2), "%")
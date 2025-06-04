import pandas as pd

df = pd.read_csv("Enriched_Feature_Set_Fiction.csv")

df = df[(df['Year'] >= 1800) & (df['Year'] <= 1913)]

# prefixes for known UK/Irish libraries ??
british_irish_prefixes = ['ucl', 'ox', 'cam', 'trincoll'] 
df['prefix'] = df['htid'].apply(lambda x: x.split('.')[0])
df_uk = df[df['prefix'].isin(british_irish_prefixes)]

print("Total rows in original dataset:", len(df))
print("Total rows after UK/Irish institution filter:", len(df_uk))
print("Unique institutions:", df_uk['prefix'].unique())
print("Year range:", df_uk['Year'].min(), "-", df_uk['Year'].max())

# Save to CSV
df_uk.to_csv("Filtered_Enriched_Feature_Set_UK_Ireland.csv", index=False)
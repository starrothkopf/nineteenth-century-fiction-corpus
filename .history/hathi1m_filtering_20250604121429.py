import pandas as pd

df = pd.read_csv("Enriched_Feature_Set_Fiction.csv")

df = df[(df['Year'] >= 1800) & (df['Year'] <= 1913)]

print("Total rows after year filter:", len(df))


df['year_bucket'] = (df['Year'] // 10 * 10).astype(int)
print("\n publication year distribution by decade:")
print(df['year_bucket'].value_counts().sort_index())

df.to_csv("Filtered_Enriched_Feature_Set_19th.csv", index=False)
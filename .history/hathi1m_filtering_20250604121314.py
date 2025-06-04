import pandas as pd

df = pd.read_csv("Enriched_Feature_Set_Fiction.csv")

df = df[(df['Year'] >= 1800) & (df['Year'] <= 1913)]

print("Total rows after year filter:", len(df))
print("Rows from British/Irish institutions:", len(df_uk))
print("Proportion British/Irish:", round(len(df_uk) / len(df) * 100, 2), "%")
print("Unique institutions:", df_uk['prefix'].unique())
print("Year range:", df_uk['Year'].min(), "-", df['Year'].max())

df_uk.to_csv("Filtered_Enriched_Feature_Set_19th.csv", index=False)
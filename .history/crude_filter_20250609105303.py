import pandas as pd

df = pd.read_csv("final_merged_metadata.csv")  # or whatever your latest merged file is

for threshold in [30, 50, 70, 100, 120, 150, 200, 250]:
    filtered = df[df['page_count'] >= threshold]
    print(f"Threshold: {threshold} pages → Remaining entries: {len(filtered)} ({len(filtered)/len(df):.2%})")

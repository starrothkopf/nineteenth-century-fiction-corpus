import pandas as pd

df = pd.read_csv("noveltm_ef.csv")  

for threshold in [30, 50, 70, 100, 120, 1, 200, 250]:
    filtered = df[df['page_count'] >= threshold]
    print(f"Threshold: {threshold} pages → Remaining entries: {len(filtered)} ({len(filtered)/len(df):.2%})")

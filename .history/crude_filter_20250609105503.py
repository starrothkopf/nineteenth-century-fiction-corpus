import pandas as pd

df = pd.read_csv("noveltm_ef.csv")  

for threshold in [30, 50, 70, 100, 125, 150, 200, 250]:
    filtered = df[df['page_count'] >= threshold]
    print(f"threshold: {threshold} pages → remaining entries: {len(filtered)} ({len(filtered)/len(df):.2%})")

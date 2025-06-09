import pandas as pd

df = pd.read_csv("noveltm_ef.csv")  

for threshold in [70, 100, 125, 150, 200, 250]:
    filtered = df[df['page_count'] >= threshold]
    print(f"threshold: {threshold} pages → remaining entries: {len(filtered)} ({len(filtered)/len(df):.2%})")


"""
threshold: 70 pages → remaining entries: 10394 (98.81%)
threshold: 100 pages → remaining entries: 10296 (97.88%)
threshold: 125 pages → remaining entries: 10178 (96.76%)
threshold: 150 pages → remaining entries: 9996 (95.03%)
threshold: 200 pages → remaining entries: 9529 (90.59%)
threshold: 250 pages → remaining entries: 8720 (82.90%)
"""
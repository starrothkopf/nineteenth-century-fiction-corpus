import pandas as pd

df = pd.read_csv("short_story_seed_volumes.csv")

selected_rows = []

manual_ids = [
    "nyp.33433088073691",
    "njp.32101071963480",
    "hvd.hn2u4x",
    "nyp.33433074918859",
    "mdp.39015024477674",
    "uc2.ark+=13960=t9t14wb76",
    "njp.32101048392763",
    "nyp.33433087358507",
    "hvd.hwkd81",
    
]

for docid in manual_ids:
    match = df[df['docid'] == docid]
    if not match.empty:
        selected_rows.append(match.iloc[0]) 

short_story_df = pd.DataFrame(selected_rows)

short_story_df.to_csv("short_story_seed_manual.csv", index=False)
print(f"saved {len(short_story_df)} manually selected volumes")

import pandas as pd

df = pd.read_csv("short_story_seed_volumes.csv")

selected_rows = []

manual_ids = [
    "nyp.33433074913496",

]

for docid in manual_ids:
    match = df[df['docid'] == docid]
    if not match.empty:
        selected_rows.append(match.iloc[0])  # grab the first matching row

# Convert list to DataFrame
short_story_df = pd.DataFrame(selected_rows)

# Save it
short_story_df.to_csv("short_story_seed_manual.csv", index=False)
print(f"Saved {len(short_story_df)} manually selected volumes.")

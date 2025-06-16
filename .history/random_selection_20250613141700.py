import pandas as pd

df = pd.read_csv("short_story_seed_volumes.csv")


# Randomly sample 100 rows
sample = df.sample(n=100, random_state=42)  # set seed for reproducibility

# Save to new CSV for manual inspection
sample.to_csv("short_story_sample_for_manual_check.csv", index=False)

print("Saved 100 random short story candidates to 'short_story_sample_for_manual_check.csv'")

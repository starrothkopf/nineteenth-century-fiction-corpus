from htrc_features import Volume
import pandas as pd

with open("my_docids.txt", "r") as f:
    vol_ids = [line.strip() for line in f if line.strip()]

summaries = []

for vol_id in vol_ids:
    try:
        vol = Volume(vol_id)
        tokenlist = vol.tokenlist(pos=False, case=False, drop_section=True)
        total_tokens = tokenlist['count'].sum()
        
        summaries.append({
            'id': vol.id,
            'title': vol.title,
            'year': vol.year,
            'token_count': total_tokens
        })

    except Exception as e:
        print(f"Error with {vol_id}: {e}")

# Step 3: Put in DataFrame
df = pd.DataFrame(summaries)
print(df.head())

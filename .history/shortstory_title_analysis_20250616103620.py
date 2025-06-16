import pandas as pd
import re
from pathlib import Path

# Load your full dataset
df = pd.read_csv("rich_noveltm_ef_filtered.csv").fillna("")
title_fields = df[['title', 'parttitle', 'shorttitle']].astype(str)

# Combine title fields for matching
df['full_title'] = title_fields.apply(lambda x: ' '.join(x).lower(), axis=1)

# Keywords to check
keywords = [
    "stories", "tales", "sketches", "narratives", "fables", "anecdotes",
    "legends", "yarns", "episodes", "chronicles", "recollections",
    "short stories", "collection", "miscellanies", "selections", "scenes"
]

# Output folder
output_dir = Path("keyword_analysis_outputs")
output_dir.mkdir(exist_ok=True)

# For summary
summary = []

for kw in keywords:
    # Build regex pattern, word boundaries optional depending on specificity
    pattern = rf'\b{re.escape(kw)}\b'
    
    # Match volumes
    df[kw + '_match'] = df['full_title'].str.contains(pattern, regex=True)
    match_df = df[df[kw + '_match']].copy()

    # Save sample of matches
    sample = match_df[['docid', 'title', 'parttitle', 'shorttitle']].head(20)
    sample.to_csv(output_dir / f"{kw}_sample.csv", index=False)

    # Save all matches if needed
    match_df.to_csv(output_dir / f"{kw}_all_matches.csv", index=False)

    # Add to summary
    summary.append({
        "keyword": kw,
        "match_count": len(match_df),
        "example_docid": sample['docid'].tolist()
    })

# Save keyword summary
pd.DataFrame(summary).to_csv(output_dir / "keyword_summary.csv", index=False)

print("✅ Analysis complete. Check the 'keyword_analysis_outputs' folder.")

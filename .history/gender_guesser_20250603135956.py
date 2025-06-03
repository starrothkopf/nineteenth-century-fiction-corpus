import gender_guesser.detector as gender
import pandas as pd
import re

df = pd.read_csv('filtered_titlemeta.tsv', sep='\t', encoding='utf-8')

detector = gender.Detector()

def extract_first_name(author):
    if pd.isna(author):
        return None
    # Remove titles, initials, and punctuation
    author = re.sub(r'(mr|mrs|ms|miss|dr|sir|lady|lord)\.?\s+', '', author.lower())
    author = re.sub(r'[^a-zA-Z\s]', '', author)
    parts = author.strip().split()
    return parts[0].capitalize() if parts else None
import gender_guesser.detector as gender
import pandas as pd
import re

df = pd.read_csv('filtered_titlemeta.tsv', sep='\t', encoding='utf-8')

detector = gender.Detector()

def extract_first_name(author):
    if pd.isna(author):
        return None
    author = re.sub(r'(mr|mrs|ms|miss|dr|sir|lady|lord)\.?\s+', '', author.lower())
    author = re.sub(r'[^a-zA-Z\s]', '', author)
    parts = author.strip().split()
    return parts[0].capitalize() if parts else None

def get_gender_from_author(author):
    first = extract_first_name(author)
    return detector.get_gender(first) if first else 'unknown'
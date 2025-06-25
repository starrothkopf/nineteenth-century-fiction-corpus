import requests
import os
import csv
import pandas as pd
from urllib.parse import quote
from difflib import get_close_matches
from tqdm import tqdm
from rapidfuzz import fuzz, process

# my local Gutendex API
BASE_URL = "http://127.0.0.1:8000/books/"
OUTDIR = "gutenberg_texts"
os.makedirs(OUTDIR, exist_ok=True)

def search_book(title, author=None):
    query = quote(f"{title} {author}" if author else title)
    response = requests.get(f"{BASE_URL}?search={query}")
    if response.ok:
        return response.json().get("results", [])
    return []

def find_text_url(book):
    formats = book.get("formats", {})
    for key, url in formats.items():
        if "text/plain" in key and "utf-8" in key:
            return url
    return None

def download_text(url, out_path):
    r = requests.get(url)
    if r.ok:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(r.text)
        return True
    return False

# load and clean metadata
df = pd.read_csv("/Users/starrothkopf/Desktop/HDW/noveltmmeta/shortstoryclassifier/short_story_seed_volumes.csv")
df = df.dropna(subset=["title", "author"])
df = df.drop_duplicates(subset=["title", "author"])
books_to_fetch = list(df[["title", "author"]].itertuples(index=False, name=None))

success_count = 0

def fuzzy_match_title(title, titles):
    result = process.extractOne(title, titles, scorer=fuzz.token_sort_ratio)
    if result and result[1] > 70:  # similarity score threshold (0–100)
        return result[0]  # return best matching title
    return None

for title, author in tqdm(books_to_fetch):
    results = search_book(title, author)
    if not results:
        print(f"Not found: {title} by {author}")
        continue

    titles = [b['title'] for b in results]
    match = process.extractOne(title, titles, scorer=fuzz.token_sort_ratio)
    if match and match[1] >= 75:  # similarity score threshold (0–100)
        matched_title = match[0]
        chosen = next(b for b in results if b["title"] == matched_title)


print(f"\nfinished! successfully downloaded {success_count} out of {len(books_to_fetch)} books.")

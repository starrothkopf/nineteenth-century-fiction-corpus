import requests
import os
import pandas as pd
from tqdm import tqdm

BASE_URL = "http://127.0.0.1:8000/books/"
CSV_IN = "/Users/starrothkopf/Desktop/HDW/noveltmmeta/shortstoryclassifier/gutenberg_british_irish_filtered.csv"
OUTDIR = "/Users/starrothkopf/Desktop/HDW/noveltmmeta/shortstoryclassifier/gutenberg_texts"
os.makedirs(OUTDIR, exist_ok=True)

df = pd.read_csv(CSV_IN)
gutenberg_ids = df['gutenberg_id'].astype(int).tolist()

def find_text_url(book):
    """Find plain text UTF-8 URL in the formats field."""
    formats = book.get("formats", {})
    for mime, url in formats.items():
        if "text/plain" in mime and "utf-8" in mime:
            return url
    return None

def download_text(url, out_path):
    try:
        r = requests.get(url, timeout=30)
        if r.ok:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(r.text)
            return True
    except Exception as e:
        print(f"✘ Error downloading {url}: {e}")
    return False

success_count = 0

for gid in tqdm(gutenberg_ids, desc="Downloading texts"):
    # Query API for the book by ID
    response = requests.get(f"{BASE_URL}{gid}")
    if not response.ok:
        print(f"Failed to fetch metadata for Gutenberg ID {gid}")
        continue

    book = response.json()

    text_url = find_text_url(book)
    if not text_url:
        print(f"No plain text UTF-8 format found for ID {gid} - '{book.get('title', 'Unknown title')}'")
        continue

    # Safe filename: id + sanitized title
    safe_title = "".join(c if c.isalnum() else "_" for c in book.get("title", "untitled"))[:50]
    filename = f"{gid}_{safe_title}.txt"
    filepath = os.path.join(OUTDIR, filename)

    if download_text(text_url, filepath):
        success_count += 1
    else:
        print(f"Failed to download text for ID {gid}")

print(f"\nFinished! Successfully downloaded {success_count} out of {len(gutenberg_ids)} books.")

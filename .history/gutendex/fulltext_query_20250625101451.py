import requests
import os
import pandas as pd
from tqdm import tqdm

BASE_URL = "http://127.0.0.1:8000/books/"
CSV_IN = "/Users/starrothkopf/Desktop/HDW/noveltmmeta/shortstoryclassifier/gutenberg_british_irish_filtered.csv"
OUTDIR = "/Users/starrothkopf/Desktop/HDW/noveltmmeta/shortstoryclassifier/gutenberg_shortstories"
os.makedirs(OUTDIR, exist_ok=True)

df = pd.read_csv(CSV_IN)
gutenberg_ids = df['gutenberg_id'].astype(int).tolist()

def find_text_url(book):
    formats = book.get("formats", {})

    # prefer UTF-8, fallback to other plain-text
    preferred_order = [
        "text/plain; charset=utf-8",
        "text/plain; charset=us-ascii",
        "text/plain; charset=iso-8859-1",
        "text/plain"
    ]

    for encoding in preferred_order:
        for mime, url in formats.items():
            if mime.startswith(encoding):
                return url

    # final fallback: any plain text at all
    for mime, url in formats.items():
        if mime.startswith("text/plain"):
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
        print(f"✘ error downloading {url}: {e}")
    return False

success_count = 0

for gid in tqdm(gutenberg_ids, desc="downloading texts"):
    # query API for the book by ID
    response = requests.get(f"{BASE_URL}{gid}")
    if not response.ok:
        print(f"failed to fetch metadata for gutenberg ID {gid}")
        continue

    book = response.json()

    text_url = find_text_url(book)
    if not text_url:
        print(f"no plain text UTF-8 format found for ID {gid} - '{book.get('title', 'Unknown title')}'")
        continue

    # safe filename: id + sanitized title
    safe_title = "".join(c if c.isalnum() else "_" for c in book.get("title", "untitled"))[:50]
    filename = f"{gid}_{safe_title}.txt"
    filepath = os.path.join(OUTDIR, filename)

    if download_text(text_url, filepath):
        success_count += 1
    else:
        print(f"failed to download text for ID {gid}")

print(f"\nfinished! successfully downloaded {success_count} out of {len(gutenberg_ids)} books.")

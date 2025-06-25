import requests
import os
import pandas as pd
from urllib.parse import quote
from tqdm import tqdm
from rapidfuzz import process, fuzz

BASE_URL = "http://127.0.0.1:8000/books/" # my API
OUTDIR = "gutenberg_texts"
CSV_OUT = "matched_books.csv"
os.makedirs(OUTDIR, exist_ok=True)

df = pd.read_csv("/Users/starrothkopf/Desktop/HDW/noveltmmeta/shortstoryclassifier/short_story_seed_volumes.csv")
df = df.dropna(subset=["title", "author"])
df = df.drop_duplicates(subset=["title", "author"])
books_to_fetch = list(df[["docid", "title", "author"]].itertuples(index=False, name=None))

results_metadata = []
success_count = 0

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
    try:
        r = requests.get(url, timeout=10)
        if r.ok:
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(r.text)
            return True
    except Exception as e:
        print(f"✘ Error downloading {url}: {e}")
    return False

for docid, title, author in tqdm(books_to_fetch):
    candidates = search_book(title, author)
    if not candidates:
        print(f"Not found: {title} by {author}")
        continue

    match = process.extractOne(title, [b["title"] for b in candidates], scorer=fuzz.token_sort_ratio)
    if match and match[1] >= 75:
        matched_title = match[0]
        chosen = next(b for b in candidates if b["title"] == matched_title)
        url = find_text_url(chosen)
        if url:
            filename = f"{title.replace(' ', '_')[:50]}_{chosen['id']}.txt"
            path = os.path.join(OUTDIR, filename)
            if download_text(url, path):
                success_count += 1
                print(f"✔ Downloaded {title}")
                results_metadata.append({
                    "hathi_id": docid,
                    "title": title,
                    "author": author,
                    "gutenberg_id": chosen["id"],
                    "download_url": url,
                    "saved_filename": filename
                })
            else:
                print(f"✘ failed to download {title}")
        else:
            print(f"no plain text URL for: {title}")
    else:
        print(f"No close match found for: {title}")

# Save metadata to CSV
pd.DataFrame(results_metadata).to_csv(CSV_OUT, index=False)
print(f"\nfinished! successfully downloaded {success_count} out of {len(books_to_fetch)} books.")
print(f"metadata saved to {CSV_OUT}")

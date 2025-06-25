import requests
import os
import csv
from urllib.parse import quote
from difflib import get_close_matches
from tqdm import tqdm

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

df = pd.read_csv("/Users/starrothkopf/Desktop/HDW/noveltmmeta/shortstoryclassifier/short_story_sample_for_manual_check.csv")
df = df.dropna(subset=["title", "author"])

# Optional: drop duplicates just in case
df = df.drop_duplicates(subset=["title", "author"])

# Create list of (title, author) tuples
books_to_fetch = list(df[["title", "author"]].itertuples(index=False, name=None))

# Preview first 5
for book in books_to_fetch[:5]:
    print(book)

books_to_fetch = [
    ("Pride and Prejudice", "Jane Austen"),
    ("The Yellow Wallpaper", "Charlotte Perkins Gilman"),
    ("A Tale of Two Cities", "Charles Dickens")
]

for title, author in tqdm(books_to_fetch):
    results = search_book(title, author)
    if not results:
        print(f"Not found: {title} by {author}")
        continue

    titles = [b['title'] for b in results]
    match = get_close_matches(title, titles, n=1)
    if match:
        chosen = next(b for b in results if b["title"] == match[0])
        url = find_text_url(chosen)
        if url:
            filename = f"{title.replace(' ', '_')[:50]}_{chosen['id']}.txt"
            path = os.path.join(OUTDIR, filename)
            if download_text(url, path):
                print(f"✔ Downloaded {title}")
            else:
                print(f"✘ Failed to download {title}")
        else:
            print(f"No .txt URL found for {title}")
    else:
        print(f"No close match found for {title}")

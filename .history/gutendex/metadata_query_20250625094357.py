import requests
import csv

params = {
    "topic": "short stories",
    "languages": "en",
    "copyright": "false",
    "min_year": 1789,
    "max_year": 1913,
}

BASE_URL = "http://127.0.0.1:8000/books/"
outfile = "gutenberg_short_stories_metadata.csv"

with open(outfile, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["gutenberg_id", "title", "author"])

    next_url = BASE_URL
    while next_url:
        response = requests.get(next_url, params=params)
        if response.ok:
            data = response.json()
            for book in data["results"]:
                gutenberg_id = book.get("id")
                title = book.get("title", "").strip()
                authors = "; ".join([a["name"] for a in book.get("authors", [])])
                writer.writerow([gutenberg_id, title, authors])
            
            next_url = data.get("next")
            params = {}  # only send params on the first request
        else:
            print("error:", response.status_code)
            break

print(f"exported metadata to {outfile}")

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

def flatten_person_list(person_list):
    # format a list of persons into a semi-colon separated string of names (with birth/death years)
    return "; ".join(
        f"{p.get('name','Unknown')} ({p.get('birth_year','?')}-{p.get('death_year','?')})" 
        for p in person_list
    ) if person_list else ""

def flatten_formats(formats_dict):
    # Flatten the formats dict into a single string of mime-type=url pairs
    return "; ".join(f"{k}={v}" for k, v in formats_dict.items()) if formats_dict else ""

with open(outfile, mode="w", newline="", encoding="utf-8") as f:
    # Define headers for CSV including the main fields plus nested ones you want
    headers = [
        "gutenberg_id", "title", "subjects", "bookshelves", "languages", "copyright", "media_type",
        "download_count", "authors", "translators", "summaries", "formats"
    ]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    next_url = BASE_URL
    while next_url:
        response = requests.get(next_url, params=params)
        if response.ok:
            data = response.json()
            for book in data["results"]:
                row = {
                    "gutenberg_id": book.get("id"),
                    "title": book.get("title", "").strip(),
                    "subjects": "; ".join(book.get("subjects", [])),
                    "bookshelves": "; ".join(book.get("bookshelves", [])),
                    "languages": "; ".join(book.get("languages", [])),
                    "copyright": book.get("copyright"),
                    "media_type": book.get("media_type"),
                    "download_count": book.get("download_count"),
                    "authors": flatten_person_list(book.get("authors", [])),
                    "translators": flatten_person_list(book.get("translators", [])),
                    "summaries": "; ".join(book.get("summaries", [])),
                    "formats": flatten_formats(book.get("formats", {})),
                }
                writer.writerow(row)

            next_url = data.get("next")
            params = {}  # only send params on the first request
        else:
            print("Error:", response.status_code)
            break

print(f"Exported metadata to {outfile}")

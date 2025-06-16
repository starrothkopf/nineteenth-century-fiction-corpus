input_file = "your_ids.txt"  # Replace with the actual filename
output_file = "hathitrust_links.txt"

with open(input_file, "r") as f:
    ids = [line.strip() for line in f if line.strip()]

links = [f"https://babel.hathitrust.org/cgi/pt?id={id_}" for id_ in ids]

with open(output_file, "w") as f:
    for link in links:
        f.write(link + "\n")

print(f"Saved {len(links)} links to {output_file}")

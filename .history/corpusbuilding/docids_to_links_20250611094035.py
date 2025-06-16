input_file = "my_docids_short.txt"
output_file = "my_docids_short_links.txt"

with open(input_file, "r") as f:
    ids = [line.strip() for line in f if line.strip()]

links = [f"https://babel.hathitrust.org/cgi/pt?id={id_}, outpu" for id_ in ids]

with open(output_file, "w") as f:
    for link in links:
        f.write(link + "\n")

print(f"saved {len(links)} links to {output_file}")

import shutil
from pathlib import Path

def normalize(htid):
    return htid.replace(':', '+').replace('/', '=')

with open("corpusbuilding/vol_ids.txt") as f:
    normalized_ids = [normalize(line.strip()) for line in f]

with open("corpusbuilding/vol_ids_normalized.txt", 'w') as out:
    out.write('\n'.join(normalized_ids))

vol_ids = set(line.strip() for line in open("corpusbuilding/vol_ids_normalized.txt"))
source_dir = Path("/Users/starrothkopf/Desktop/HDW/1279201/fiction") 
dest_dir = Path("/Users/starrothkopf/Desktop/HDW/noveltmmeta/genrepredictions")
dest_dir.mkdir(exist_ok=True)

for vol_id in vol_ids:
    json_path = source_dir / f"{vol_id}.json"
    if json_path.exists():
        shutil.copy(json_path, dest_dir / f"{vol_id}.json")

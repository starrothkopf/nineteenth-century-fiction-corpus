import shutil
from pathlib import Path

vol_ids = set(line.strip() for line in open("corpusbuilding/my_docids.txt"))
source_dir = Path("/Users/starrothkopf/Desktop/HDW/1279201/fiction") 
dest_dir = Path("/Users/starrothkopf/Desktop/HDW/noveltmmeta/genrepredictions")
dest_dir.mkdir(exist_ok=True)

for vol_id in vol_ids:
    json_path = source_dir / f"{vol_id}.json"
    if json_path.exists():
        print(f"Copying: {json_path.name}")
        shutil.copy(json_path, dest_dir / f"{vol_id}.json")
    else:
        print(f"Missing: {json_path.name}")

        

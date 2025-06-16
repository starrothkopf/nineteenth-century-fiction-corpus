from pagealigner import Alignment
import shutil
from pathlib import Path

vol_ids = set(line.strip() for line in open("vol_ids.txt"))
source_dir = Path("/Users/starrothkopf/Desktop/HDW/1279201/fiction")  # or 'all1800-1899', etc.
dest_dir = Path("/Users/starrothkopf/Desktop/HDW/noveltmmeta/genrepredictions")
dest_dir.mkdir(exist_ok=True)

for vol_id in vol_ids:
    json_path = source_dir / f"{vol_id}.json"
    if json_path.exists():
        shutil.copy(json_path, dest_dir / f"{vol_id}.json")


with open('corpusbuilding/vol_ids.txt', 'r') as f:
    volume_ids = [line.strip() for line in f if line.strip()]

alignedvols = Alignment(
    volume_ids,
    genrepath='./genrepredictions/',
    datapath='./ef_data/',
    datatype='ef'
)

# ["fiction", "fiction", "nonfiction", "unknown", ...]  one label per page

for volid, successflag, volume in alignedvols:

    if successflag != "success":
       
        print(successflag + " in " + volid)

        continue

    for page in volume:

        text = page[0]

        genre = page[1]

        if genre == "fic":

            add to a df 
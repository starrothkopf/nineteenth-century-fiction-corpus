import pandas as pd
from pagealigner import Alignment

with open('corpusbuilding/my_docids.txt', 'r') as f:
    volume_ids = [line.strip() for line in f if line.strip()]

alignedvols = Alignment(
    volume_ids,
    genrepath='./genrepredictions/',
    datapath='./ef_data/',
    datatype='ef'
)

summary_data = []

for volid, successflag, volume in alignedvols:

    if successflag != "success":
        print(f"{successflag} in {volid}")
        continue

    count_ fiction_pages = sum(1 for page in volume if page[1] == "fic")

    summary_data.append({
        "docid": volid,
        "fiction_pages_count": fiction_pages,
    })

# Convert to DataFrame and save
df = pd.DataFrame(summary_data)
df.to_csv("fiction_percentages_by_volume.csv", index=False)
print(df.head())

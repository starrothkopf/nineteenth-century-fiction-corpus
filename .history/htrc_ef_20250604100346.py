from htrc_features import Volume

vol = Volume("hvd.32044013656061") 
print(vol.title, vol.year, vol.page_count)

with open("my_docids.txt", "r") as f:
    vol_ids = [line.strip() for line in f if line.strip()]

from htrc_features import Volume

with open("my_docids.txt", "r") as f:
    vol_ids = [line.strip() for line in f if line.strip()]

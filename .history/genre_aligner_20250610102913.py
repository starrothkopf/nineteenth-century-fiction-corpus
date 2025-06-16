from pagealigner import Alignment

with open('corpusbuilding/my_docids.txt', 'r') as f:
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
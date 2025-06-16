from pagealigner import Alignment


with open('vol_ids.txt', 'r') as f:
    volume_ids = [line.strip() for line in f if line.strip()]

alignedvols = Alignment(listofvolstoget)
alignedvols = Alignment(
    volume_ids,
    genrepath='./genrepredictions/',
    datapath='./ef_data/',
    datatype='ef'
)

for volid, successflag, volume in alignedvols:

    if successflag != "success":
       
        print(successflag + " in " + volid)

        continue

    for page in volume:

        text = page[0]

        genre = page[1]

        if genre == "fic":

            add to a df 
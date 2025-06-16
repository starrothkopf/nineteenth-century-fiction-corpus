from pagealigner import Alignment

listofvolstoget = []

alignedvols = Alignment(listofvolstoget)
alignedvols = Alignment(listofvols, genrepath = '/root/genretarfiles/', datapath = './ef_data/', 
    datatype = 'json.bz2', tarscompressed = False)
    aligned_volumes = Alignment(
    volume_ids,
    genrepath='./genrepredictions/',
    datapath='./ef_data/',
    datatype='ef'  # important: tell it we're using EF, not zip
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
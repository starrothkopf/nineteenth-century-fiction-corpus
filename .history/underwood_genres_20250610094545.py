from pagealigner import Alignment


alignedvols = Alignment(listofvolstoget)
alignedvols = Alignment(listofvols, genrepath = '/root/genretarfiles/', datapath = '/root/ef_data/', 
    datatype = 'json.bz2', tarscompressed = False)
    

for volid, successflag, volume in alignedvols:

    if successflag != "success":
       
        print(successflag + " in " + volid)

        continue

    for page in volume:

        text = page[0]

        genre = page[1]

        if genre == "fic":

            add to a df 
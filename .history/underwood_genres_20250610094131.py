from pagealigner import Alignment


alignedvols = Alignment(listofvols, genrepath = '/root/genretarfiles/', datapath = '/root/hathi/', 
    datatype = 'ziptext', tarscompressed = True)

alignedvols = Alignment(listofvols, genrepath = '/root/genretarfiles/', datapath = '/root/ef_data/', 
    datatype = 'ziptext', tarscompressed = True)
    

for volid, successflag, volume in alignedvols:

    if successflag != "success":
       
        print(successflag + " in " + volid)

        continue

    for page in volume:

        text = page[0]

        genre = page[1]

        if genre == "fic":

            add to a df 
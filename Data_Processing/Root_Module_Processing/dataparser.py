import os


with open('./raw_data/b.txt') as infile, open('./processed_data/b_processed.txt','w') as outfile:
    data = infile.read()
    data = data.replace("[","")
    data = data.replace("]","")
    data = data.replace(" ","")
    data = data.replace("\n",",")
    outfile.write(data)
    outfile.seek(0, os.SEEK_END)
    outfile.seek(outfile.tell() - 1,0)
    outfile.truncate()






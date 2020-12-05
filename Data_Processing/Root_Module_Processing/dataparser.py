import os
path = './raw_data'
files = os.listdir(path)
for file in files:
    with open('./raw_data/'+file) as infile, open('./processed_data/'+file[0:len(file)-4]+'_processed.txt','w') as outfile:
        data = infile.read()
        data = data.replace("\n[]","")
        data = data.replace("[","")
        data = data.replace("]","")
        data = data.replace(" ","")
        data = data.replace("\n",",")
        outfile.write(data)
        outfile.seek(0, os.SEEK_END)
        outfile.seek(outfile.tell() - 1,0)
        outfile.truncate()
    print(file)

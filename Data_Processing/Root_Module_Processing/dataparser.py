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


path = './raw_imu'
files = os.listdir(path)
for file in files:
    with open('./raw_imu/'+file) as infile:
        accel_file = open('./pdata_accel/'+file[0:len(file)-4]+'_a.txt','w')
        gyro_file = open('./pdata_gyro/'+file[0:len(file)-4]+'_g.txt','w')

        for line in infile:
            line_split = line.split(':')
            
            if line_split[0] == 'a':
                comma_split = line_split[1].split(',')
                if len(comma_split) == 3:
                    accel_file.write(line_split[1])
            
            if line_split[0] == 'g':
                comma_split = line_split[1].split(',')
                if len(comma_split) == 3:
                    gyro_file.write(line_split[1])     
    print(file)       
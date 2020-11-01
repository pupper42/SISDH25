import numpy as np
import os 

#Hours since 1st Jan
veraison_start = 1098 #start of 15th Feb
veraison_end = 2538 #approximately end of 15th April (start of 16th)

data_dir = "./Interpolated/"
save_dir = "./DH25/"

station = []
dh25p = []

for files in os.listdir(data_dir):
    data_file = data_dir + files
    save_file = save_dir + files

    diff25 = []
    dh = []

    temp = np.loadtxt(data_file, delimiter = ",")[veraison_start:veraison_end + 1]

    for i in np.arange(0, veraison_end - veraison_start + 1, 1):
        dh.append(temp[i, 1])
        if (temp[i,1] - 25 > 0):
            diff25.append(temp[i,1] - 25)

    dh25_total = sum(diff25)
    dh_total = sum(dh)

    dh25_percent = dh25_total / dh_total

    station.append(files[4:10])
    dh25p.append(dh25_percent)

station = np.array(station)
dh25p = np.array(dh25p)

final = np.column_stack((station, dh25p))
print(final)

final_file = save_dir + "station_dh25_extra.csv"
print(final_file)

np.savetxt(final_file, final, delimiter = ",", fmt = "%s")
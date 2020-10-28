import numpy as np 
from scipy.interpolate import PchipInterpolator as pchip
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob

for subdir, dirs, files in os.walk("./Data/Max"):
    for filename in files:
        max_temp = subdir + os.sep + filename
        if max_temp.endswith(".csv"):
            print(max_temp)
            max_array = np.genfromtxt(max_temp, skip_header = 1, delimiter = ",", usecols = (2, 3, 4, 5), filling_values = -99)
            maxrows, maxcols = max_array.shape
            max_time = np.arange(9, maxrows * 24, 24)
            max_temp_time = np.column_stack((max_array, max_time))
            savedir = "./MaxTime/" + filename
            np.savetxt(savedir, max_temp_time, delimiter = ",")

for subdir, dirs, files in os.walk("./Data/Min"):
    for filename in files:
        min_temp = subdir + os.sep + filename
        if min_temp.endswith(".csv"):
            min_array = np.genfromtxt(min_temp, skip_header = 1, delimiter = ",", usecols = (2, 3, 4, 5), filling_values = -99)
            minrows, mincols = min_array.shape
            min_time = np.arange(0, minrows * 24, 24)
            min_temp_time = np.column_stack((min_array, min_time))
            savedir = "./MinTime/" + filename
            np.savetxt(savedir, min_temp_time, delimiter = ",")

for file in os.listdir("./MinTime/"):
    print(file)
    print(file[11:17])
    os.rename(f"./MinTime/{file}", f"./MinTime/{file[11:17]}.csv")

for file in os.listdir("./MaxTime/"):
    print(file)
    print(file[11:17])
    os.rename(f"./MaxTime/{file}", f"./MaxTime/{file[11:17]}.csv")

for max in os.listdir("./MaxTime/"):
    for min in os.listdir("./MinTime/"):
        if (max == min):
            maxpath = "./MaxTime/" + max
            minpath = "./MinTime/" + min
            temppath = "./TempTime/" + max

            max_array = np.loadtxt(maxpath, delimiter = ",")
            min_array = np.loadtxt(minpath, delimiter = ",")

            temperature = np.concatenate((min_array, max_array))
            temp_sort = temperature[temperature[:, 4].argsort()]

            np.savetxt(temppath, temp_sort, delimiter = ",")
'''
x = temp_sort[:, 4]
y = temp_sort[:, 3]

plt.plot(x, y, 'o')

x = np.array([0, 8, 22, 36, 42, 60, 72])
y = np.array([10, 20, 12, 25, 13, 23, 11])

inter = pchip(x, y)

xnew = np.linspace(1, 72, 72)

#plt.plot(x, pchip(x), 'o')

plt.plot(xnew, inter(xnew), 'o')
plt.plot(x, y, 'ro')

plt.show()

'''



import numpy as np
import os 

#Hours since 1st Jan
veraison_start = 1098 #start of 15th Feb
veraison_end = 2538 #approximately end of 15th April (start of 16th)

data_dir = "./Interpolated/"
save_dir = "./DH25Test/"

test_file = data_dir + "int_047053.csv"
save_file = save_dir + "test.csv"

temp = np.loadtxt(test_file, delimiter = ",")[veraison_start:veraison_end + 1]

diff25 = []


def calcDH25(temp):
    for i in np.arange(0, veraison_end - veraison_start + 1, 1):
        if (temp[i,1] - 25 > 0):
            diff25.append(temp[i,1] - 25)

print(calcDH25(temp))
print(sum(diff25))

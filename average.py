import numpy as np 
from scipy.interpolate import PchipInterpolator as pchip
import math
import os

data_dir = "./TempTime/"

for files in os.listdir(data_dir):
    data_source = "./TempTime/" + files
    save_dir = "./Interpolated/int_" + files
    print(data_source)
    temperature = np.loadtxt(data_source, delimiter = ",")
    x, y = temperature.shape
    
    min_days = np.arange(0, 300, 2)
    max_days = np.arange(1, 301, 2)

    av_min = []
    av_max = []

    for d in min_days:
        minArr = []
        for i in np.arange(0, math.floor(x/730), 1):        
            minArr.append(temperature[i*730 + d, 3])
        
        minArr = np.array(minArr)
        av_min.append(minArr[minArr != -99].mean())

    for d in max_days:
        maxArr = []
        for i in np.arange(0, math.floor(x/730), 1):        
            maxArr.append(temperature[i*730 + d, 3])
        
        maxArr = np.array(maxArr)
        av_max.append(maxArr[maxArr != -99].mean())

    try:
        av_min = np.array(av_min)
        av_max = np.array(av_max)

        min_time = np.arange(0, 3600, 24)
        max_time = np.arange(9, 3600, 24)

        min_temp_time = np.column_stack((av_min, min_time))
        max_temp_time = np.column_stack((av_max, max_time))


        av_temp_time = np.concatenate((min_temp_time, max_temp_time))


        av_temp_time_inorder = av_temp_time[av_temp_time[:, 1].argsort()]


        x_axis = av_temp_time_inorder[:, 1]
        y_axis = av_temp_time_inorder[:, 0]

        
        inter = pchip(x_axis, y_axis)

        x_new = np.arange(0, 3600, 0.5)
        y_new = inter(x_new)

        av_temp_interpolated = np.column_stack((x_new, y_new))
        np.savetxt(save_dir, av_temp_interpolated, delimiter = ",")
    except Exception as e:
        print(e)
        pass






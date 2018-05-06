import numpy as np
from scipy.spatial.distance import euclidean
from scipy.interpolate import spline
import scipy.fftpack
from scipy.signal import savgol_filter
from fastdtw import fastdtw
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd

folder  = sys.argv[1]

file = 'acceleration.csv';

path = os.path.join(folder,file)
f = open(path)
d = pd.read_csv(f)
f.close()

t = d['Time']
x = d['X']
y = d['Y']
z = d['Z']

# reset time to start at 0
t = np.array(t)
t = t-t[0]

area_test = [x[0]]
for i in range(len(x)-1):
	area_test.append(x[i+1]+y[i])

savgol6 = savgol_filter(x,249,6)

plt.figure
plt.plot(x, label='original')
plt.plot(savgol6, label='savgol6')
plt.plot(area_test, label='area')
plt.legend()
plt.show()

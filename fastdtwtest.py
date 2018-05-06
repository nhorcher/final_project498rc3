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

file = 'gyroscope.csv';

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

lin =  np.linspace(-2,2,1000)
sinc = -4*np.sinc(lin)


## Spline smoothing
## Toooooo slow
# t_sm = np.array(t)
# z_sm = np.array(z)
# Takes forever to run
# t_smooth = np.linspace(t_sm.min(), t_sm.max(), len(t))
# z_smooth = spline(t, z, t_smooth)

## FFT method, fast and smooth, but loses peaks
w = scipy.fftpack.rfft(z)
f = scipy.fftpack.rfftfreq(len(t), t[1]-t[0])
spectrum = w**2
cutoff_idx = spectrum < (spectrum.max()/5)
w2 = w.copy()
w2[cutoff_idx] = 0
y2 = scipy.fftpack.irfft(w2)

## SavGol Filter
# savgol3 = savgol_filter(z,249,3)
# savgol5 = savgol_filter(z,249,5)
savgol6 = savgol_filter(z,249,6)

# savgol6[abs(savgol6) < 1] = 0

## DTW
# Not really a well developed library. too hard to figure out
# distance, path = fastdtw(z[100:300], sinc, dist=euclidean)
# xpath = [z[100+i[0]] for i in path]
# ypath = [sinc[i[1]] for i in path]
# print(distance)

plt.figure()
plt.plot(z, label='Original')
# plt.plot(z_smooth, label='Splining')
# plt.plot(savgol3, label='SavGol3')
# plt.plot(savgol5, label='SavGol5')
plt.plot(savgol6, label='SavGol6')
# plt.plot(y2, label='FFTMethod')
plt.plot(np.linspace(0,200,1000),sinc, label='match')
# plt.plot(xpath, z[100:300], label='xpath')
# plt.plot(np.linspace(100,len(ypath),300)ypath, label='ypath')
plt.legend()
plt.show()


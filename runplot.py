import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

folder  = sys.argv[1]

for file in os.listdir(folder):
	if '.csv' in file and 'aggregate' not in file:
		path = os.path.join(folder,file)
		f = open(path)
		d = pd.read_csv(f)
		f.close()

		plt.figure()
		plt.subplot(311)
		plt.title(file.strip('.csv'))
		plt.plot(d['X'])
		plt.xlabel('X')

		plt.subplot(312)
		plt.plot(d['Y'])
		plt.xlabel('Y')

		plt.subplot(313)
		plt.plot(d['Z'])
		plt.xlabel('Z')
		plt.pause(0.1)
plt.show()
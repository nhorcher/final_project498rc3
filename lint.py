import sys
import os
import pandas as pd

folder = sys.argv[1]
l = ['acc', 'gyro', 'mag']
nmap = {'acc':'acceleration', 'gyro':'gyroscope', 'mag':'magnetometer'}

for file in os.listdir(folder):
	if any(phrase in file for phrase in l):
		filepath = os.path.join(folder,file)
		f = open(filepath)
		d = pd.read_csv(f, sep='\t')
		d.columns = ['Time','TimeRedundant','X','Y','Z']
		d.drop('TimeRedundant', axis=1)
		# filename = file.split('-')[2].split('_')[0] + '.csv'
		filename = file.strip('.txt')
		filename = nmap[filename] + '.csv'
		d.to_csv(os.path.join(folder, filename))
		f.close()
	os.remove(os.path.join(folder,file))

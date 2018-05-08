import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath

run_lint = sys.argv[2]
folder = sys.argv[1]

if run_lint == 'lint':
	l = ['acc', 'gyro', 'mag']
	nmap = {'acc':'acceleration', 'gyro':'gyroscope', 'mag':'magnetometer'}

	for file in os.listdir(folder):
		if any(phrase in file for phrase in l):
			filepath = os.path.join(folder,file)
			d = pd.read_csv(filepath, sep='\t')
			d.columns = ['Time','TimeRedundant','X','Y','Z']
			d.drop('TimeRedundant', axis=1)
			filename = file.split('-')[2].split('_')[0]
			# filename = file.strip('.txt')
			# filename = nmap[filename/]
			filename = filename + '.csv'
			d.to_csv(os.path.join(folder, filename))
		os.remove(os.path.join(folder,file))



folder  = sys.argv[1]
file = 'gyroscope.csv';
path = os.path.join(folder,file)
d = pd.read_csv(path)

x = d['X']
y = d['Y']
d['Z'] = -d['Z']
z = d['Z']

right_steps = np.zeros(len(z))
left_steps = np.zeros(len(z))

right_threshold = -1.7
left_threshold  = 1.1

for i in range(len(z)):
	if z[i] < right_threshold:
		right_steps[i] = 1
	if z[i] > left_threshold:
		left_steps[i] = 1

win = 5
step_on = 0
gap = 0
step_size = 0
right_step_count = 0

rsteeeps = np.zeros(len(right_steps))
for point,i in zip(right_steps,range(len(right_steps))):

	if point == 1:
		step_size = step_size+1
		gap = 0
		if step_size > win:
			step_on = 1

	elif point == 0:
		if step_on == 1:
			if gap > win:
				gap = 0
				step_on = 0
				step_size = 0
				right_step_count = right_step_count + 1
				rsteeeps[i] = 5;
			else:
				gap = gap + 1

# print(right_step_count, 'Right Steps')

### Same thing with left
win = 10
step_on = 0
gap = 0
step_size = 0
left_step_count = 0

lsteeeps = np.zeros(len(left_steps))
for point,i in zip(left_steps,range(len(left_steps))):

	if point == 1:
		step_size = step_size+1
		gap = 0
		if step_size > win:
			step_on = 1

	elif point == 0:
		if step_on == 1:
			if gap > win:
				gap = 0
				step_on = 0
				left_step_count = left_step_count + 1
				lsteeeps[i] = 5;
			else:
				gap = gap + 1

# print(left_step_count/2, 'Left Steps')

if left_step_count/2 >= right_step_count:
	dist = right_step_count*3.0
else:
	dist = right_step_count*2.6

print('Steps: ', right_step_count*2)
print('Distance: ', dist)

folder  = sys.argv[1]
file = 'acceleration.csv';
path = os.path.join(folder,file)
d = pd.read_csv(path)
x = d['X']


# rsteeeps[rsteeeps!=0] = x[np.where(rsteeeps!=0)[0]]
# print(np.where(rsteeeps!=0)[0])
rsteeeps[rsteeeps==0] = float('nan')

circ = mpath.Path.unit_circle()

plt.figure()
plt.plot(x)
plt.plot(-rsteeeps/5, marker=circ)
plt.title('X Acceleration')
plt.xlabel('Sample (n)')
plt.ylabel('Magnitude')
plt.show()

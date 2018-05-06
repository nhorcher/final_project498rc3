import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import sys
import os
import numpy as np

folder  = sys.argv[1]

file = 'gyroscope.csv';

path = os.path.join(folder,file)
f = open(path)
d = pd.read_csv(f)
f.close()

x = d['X']
y = d['Y']
z = d['Z']

right_steps = np.zeros(len(z))
left_steps = np.zeros(len(z))
divisions = np.zeros(len(z))

right_threshold = -1.7
left_threshold  = 1.1

divisions[0::150] = 5;

for i in range(len(z)):
	if z[i] < right_threshold:
		right_steps[i] = 1
	if z[i] > left_threshold:
		left_steps[i] = 1

theta = np.zeros(len(z-1))
theta2 = np.zeros(len(z-1))
theta3 = np.zeros(len(z-1))
window = 5

for i in range(len(z)-1):
	theta[i] = z[i+1] - z[i]

# for i in range(len(z)-window-1):
# 	theta2[i] = (sum(z[i+1:i+1+window]) - sum(z[i:i+window]))/(window)

# for i in range(len(z)-2*window-1):
# 	theta3[i] = (sum(z[i+1:i+1+2*window]) - sum(z[i:i+2*window]))/((2*window))

win = 10
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
				right_step_count = right_step_count + 1
				rsteeeps[i] = 5;
			else:
				gap = gap + 1

print(right_step_count, 'Right Steps')


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

print(left_step_count, 'Left Steps')

plt.figure()
plt.title('z and left steps')
plt.plot(z)
plt.plot(right_steps)
plt.plot(rsteeeps)
# plt.plot(lsteeeps)
# plt.plot(left_steps)
# plt.plot(divisions)
# plt.plot(theta)
# plt.plot(theta2[window:])
# plt.plot(theta3[window*2:])
plt.show()
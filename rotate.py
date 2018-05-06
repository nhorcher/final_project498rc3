# import skinematics as skin
from skinematics import imus
import sys
import os
import pandas as pd
import numpy as np

in_file = sys.argv[1]

class MyIMU(imus.IMU_Base):
	def get_data(self, in_file, in_data=None):
		g = 'gyroscope.csv'
		a = 'acceleration.csv'
		m = 'magnetometer.csv'

		path = os.path.join(in_file,'aggregate.csv')
		merged = pd.read_csv(path,index_col=False)
		merged.set_index('Time')

		g = merged.as_matrix(['gX','gY','gZ'])
		a = merged.as_matrix(['aX','aY','aZ'])
		m = merged.as_matrix(['mX','mY','mZ'])

		in_data = {'rate':100,
		'acc':   a,
		'omega': np.deg2rad(g),
		'mag':   m}
		self._set_data(in_data)

# initial position is x_rot and z_rot
test_instance = MyIMU('kitchen', 'kalman', R_init=np.matrix([[1,0,0],[0,0,1],[0,-1,0]])*np.matrix([[0,-1,0],[1,0,0],[0,0,1]]))
test_instance.get_data(in_file)

q = test_instance.quat
p = test_instance.pos

pd.DataFrame(q).to_csv(os.path.join(in_file,'quat.csv'))
pd.DataFrame(p).to_csv(os.path.join(in_file,'pos.csv'))





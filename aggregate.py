import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

in_file = sys.argv[1]

g = 'gyroscope.csv'
a = 'acceleration.csv'
m = 'magnetometer.csv'

gpath = os.path.join(in_file,g)
apath = os.path.join(in_file,a)
mpath = os.path.join(in_file,m)
cols = ['Time','X','Y','Z']

g = pd.read_csv(gpath,index_col=False,usecols=cols)
g['Time'] = round(g['Time'],2)
g = g.set_index('Time')
g = g.rename(index=str,columns={'Time':'Time','X':'gX','Y':'gY','Z':'gZ'})

a = pd.read_csv(apath,index_col=False,usecols=cols)
a['Time'] = round(a['Time'],2)
a = a.set_index('Time')
a = a.rename(index=str,columns={'Time':'Time','X':'aX','Y':'aY','Z':'aZ'})

m = pd.read_csv(mpath,index_col=False,usecols=cols)
m['Time'] = round(m['Time'],2)
m = m.set_index('Time')
m = m.rename(index=str,columns={'Time':'Time','X':'mX','Y':'mY','Z':'mZ'})

merged = g.join(a,how='inner')
merged = merged.join(m,how='inner')
merged.index.name = 'Time'
merged = merged[~merged.index.duplicated(keep='first')]

merged.to_csv(os.path.join(in_file,'aggregate.csv'))

l = len(merged)
print('g:',l/len(g))
print('a:',l/len(a))
print('m:',l/len(m))
merged.plot()
plt.show()
import lint
import runplot
import os
import sys

arg = sys.argv[1]

os.system('python lint.py ' + arg)
os.system('aggregate.py' + arg)
os.system('python runplot.py ' + arg)

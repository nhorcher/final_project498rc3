import lint
import runplot
import os
import sys

arg = sys.argv[1]

os.system('python lint.py ' + arg)
input('Finished linting...')
os.system('python aggregate.py ' + arg)
os.system('python runplot.py ' + arg)
os.system('python steps.py ' + arg)

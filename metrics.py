import string
#import pandas as pd
import numpy as np
import os
import os.path as op
import sys
#import matplotlib.pyplot as plt

f = open("FallenMagus_2.txt","r")
m = f.read()
m = m.split()

print len(m)
for i,mm in enumerate(m):
    if 'void' in mm:
        print m[i:i+5]

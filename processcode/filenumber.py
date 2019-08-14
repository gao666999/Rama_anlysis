import os
n = 0
path = '/Users/xg666/Desktop/getTER/pdbfile'
filename = os.listdir(path)
#filename_list = list(filename)

for name in filename:
    n += 1
    print n
    print name

#import glob
import re,os
#import numpy as np
from shutil import copyfile
f1 = open('pdbnonid.txt')
f2 = open('filename.txt','w+')
linetxts= f1.readlines()
line_number = 0
h = 0
for i in range(100,301):
    line_number += 1
    print line_number
    line_split1 = linetxts[i].strip().split()
    n = 0
    while (n < 10):
        a = str(line_split1[n])
        #print a
        n += 1
        #print n
        a = a.lower()
        a =a[0:4]
        pdb_name = 'pdb' + a +'.ent'
        print>> f2,pdb_name
        base_path ='/home/csrc/Desktop/psp/DataSet/pdb/'
        pdb = base_path + pdb_name
        print pdb

        if os.access("/home/csrc/Desktop/psp/DataSet/pdb/"+pdb_name,os.F_OK):
            base_path_or ='/home/csrc/Desktop/psp/DataSet/pdb/'
            base_path_new = '/home/csrc/Desktop/position/pdbfile/'
            src = base_path_or + pdb_name
            dst = base_path_new + pdb_name
            copyfile(src,dst)
            h += 1
            print h
f2.close()
f1.close()
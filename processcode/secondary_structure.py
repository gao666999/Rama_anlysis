import glob
import pandas as pd
import re,os
import numpy as np
#import sys
from numpy import *
#flage = 0
def write_line(line, lenth):
    #global flage
    for i in range(0, lenth):
        flage = 0
        global flage
    #print a[i][0],a[i][1],line[22:26]
        if int(a[i][0]) <= int(line[22:26]) <= int(a[i][1]):
            line = ''
            flage = 1
            break
        else:
            continue
    return flage,line
f = open('pdbnonid.txt')
#f = open('test.txt')
linetxts= f.readlines()
lenth = len(linetxts)
print lenth
line_number = 0
h = 0
#if line_nu<200:
#for linetxt in linetxts:
f_new = open('structure_new.pdb','a')

for i in range(0,200):
    line_number += 1
    print line_number
    line_split1 = linetxts[i].strip().split()
    #l = len(line_split1)
    #print l
    #print line_split1
    n = 0
    while (n < 10):
        a = str(line_split1[n])
        #print a
        n += 1
        #print n
        a = a.lower()
        a =a[0:4]
        pdb_name = 'pdb' + a +'.ent'
        #print pdb_name
        base_path ='/home/csrc/Desktop/psp/DataSet/pdb/'
        pdb = base_path + pdb_name
        print pdb
           
        if os.access("/home/csrc/Desktop/psp/DataSet/pdb/"+pdb_name,os.F_OK):
            base_path ='/home/csrc/Desktop/psp/DataSet/pdb/'
            #os.path.exists(/home/csrc/Desktop/psp/DataSet/pdb/pdb_name)
            pdb = base_path + pdb_name
            print pdb
            h += 1
            print h
            #print 'hahahahah'
            a = np.zeros(shape=(0,2))
            #with open('1crn.pdb','rw') as f:
            with open(pdb,'rw') as f:
                lines = f.readlines()
                #print 'aaa'
                for line_pdb in lines:
                    line_split2 = line_pdb.split()
                    #print line_split2
                    #print h
                  
                    if line_split2[0] == 'HELIX':
                        start = line_pdb[21:25].strip()
                        #start = line_split[5]
                        #end = line_split[8]
                        end = line_pdb[33:37].strip()
                        row = ([start, end])
                        a = np.row_stack((a, row))
                    elif line_split2[0] == 'SHEET':
                        start = line_pdb[22:26].strip()
                        end = line_pdb[33:37].strip()
                        row = ([start, end])
                        a = np.row_stack((a, row))
                    #sort the arry by the fir column
                a = a.tolist()
                
                a = sorted(a, key = (lambda x:x[0]))
                #f_new = open('structure_new.pdb','a')
                #print a
                #f_new.write(a)
            
                #with open(pdb,'rw') as f:
                #with open('new.pdb','rw') as f:
                #lines = f.readlines()
                pdb_lenth = len(lines)
                row_lenth = len(a)
                flage1 = flage2 = 0
                for l in range(0,pdb_lenth):
                    line_split = lines[l].split()
                    #flage1 = flage2 = 0
                    if line_split[0] == 'ATOM':
                        flage2,line = write_line(lines[l], row_lenth)
                        #print line
                        if flage1 == flage2:
                            f_new.write(line)
                        elif flage1 == 0 and flage2 == 1:
                            f_new.write(line)
                            f_new.write('TER\n')
                            flage1 = flage2
                        elif flage1 == 1 and flage2 == 0:
                            f_new.write(line)
                            flage1 = flage2
                        elif line_split[0] == 'END':
                            f_new.write('TER\n')
                            #f_new.write('END\n')
f_new.write('TER\n')                           
f_new.close()
                
f.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def remove_ter1(orfile,newfile):
    with open (orfile,'r') as file:
        lines = file.readlines()
        length = len(lines)
        length_range = length - 2
        n = 0
        m = 0
        with open (newfile,'w+') as newfile:
            for i in range (0,length):
                if i < length - 2:
                    if lines[i][:4].strip()== 'TER' and lines[i+1][:4].strip() == 'END' and lines[i+2][:4].strip() =='TER':
                        m += 1
                        print i
                        print m
                        print 'mmmmmmmm'
                        lines[i+2] = ''
                        newfile.write(lines[i])
                        #newfile.write(lines[i+1])
                        #newfile.write(lines[i+2])
                    else:
                        newfile.write(lines[i])
                else:
                    newfile.write(lines[i])
    return length

def remove_ter2(orfile,newfile):
    with open (orfile,'r') as file:
        lines = file.readlines()
        length = len(lines)
        n = 0
        m = 0
        with open (newfile,'w+') as newfile:
            for i in range (0,length):
                if i < length - 1:
                    if lines[i][:4].strip() == 'TER' and lines[i+1][:4].strip() == 'TER':
                        n += 1
                        #print lines[i]
                        #print n
                        #print 'nnnnnnn'
                        lines[i+1] = ''
                        #print lines[i+1]
                        newfile.write(lines[i])
                    else:
                        newfile.write(lines[i])
                else:
                    newfile.write(lines[i])
    return length

if __name__ == '__main__':

    path = '/Users/xg666/Desktop/getTER/moredata/loopdata/'
    newpath = '/Users/xg666/Desktop/getTER/moredata/cleaneddata/'
    filenames=os.listdir(path)
    for filename in filenames:
        print filename
        orfile = path + filename
        cleaned_name = filename[4:]
        print cleaned_name
        '''
        newfile = newpath +cleaned_name
        length1 = remove_ter1(orfile,newfile)
        orfile = newfile
        newfile = newpath + 'seconded_cleaned'+ cleaned_name
        length2 = remove_ter2(orfile,newfile)
        if length2 != length1:
            length1 = length2
            orfile = newfile
            for n in range(2,9):
                name = str(n) + cleaned_name
                newfile = newpath + name
                length2 = remove_ter2(orfile,newfile)
                print length2
                if length2 != length1:
                    length1 = length2
                    orfile = newfile
                    continue
                else:
                    print newfile
                    break
                    '''
import glob
import os
#MM means a pdbfile has more than one model


'''
def get_MM_filename(pdbfile):
    with open (pdbfile) as file:
        for line in file:
            if line[:5].strip() == 'MODEL':
                print line
    return filename
'''

if __name__ == '__main__':
    path = '/Users/xg666/Desktop/getTER/pdbfile/'
    filename = os.listdir(path)
    n = 0
    for name in filename:
        n += 1
        if n < 200:
            or_file = path + name
            with open (or_file,'r') as file:
                for line in file:
                    if line[:5].strip() == 'MODEL':
                        print line
                        print name
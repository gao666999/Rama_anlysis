import numpy as np

def clean_data(or_file,new_file):
    temp_atom = []
    temp_residues = []
    Re_order = 0
    Residue_number = 0
    with open (or_file,'r') as oldfile:
        with open (new_file,'w+') as newfile:
            lines = oldfile.readlines()
            length = len(lines)
            #print length
            for i in range(0,length):
                #print i
                if lines[i][:4].strip() == 'ATOM':
                    if lines[i][13:17].strip() == 'N' and lines[i+1][13:17].strip() == 'CA' and lines[i+2][13:17].strip() == 'C':
                        #print lines[i][13:17]
                        if lines[i][22:26].strip() == lines[i+1][22:26].strip() == lines[i+2][22:26].strip():
                            #print 'hhhhh'
                            #print lines[i][22:26]
                            if Re_order == 0:
                                Re_order = int(lines[i][22:26].strip())
                                temp_atom.append(lines[i])
                                temp_atom.append(lines[i+1])
                                temp_atom.append(lines[i+2])
                                for l in temp_atom:
                                    temp_residues.append(l)
                                Residue_number += 1
                                temp_atom = []
                            else:
                                temp = int(lines[i][22:26].strip())
                                if temp == Re_order +1:
                                    #print Re_order
                                    temp_atom.append(lines[i])
                                    temp_atom.append(lines[i+1])
                                    temp_atom.append(lines[i+2])
                                    for l_line in temp_atom:
                                        temp_residues.append(l_line)
                                    Residue_number += 1
                                    Re_order = temp
                                    temp_atom = []
                                else:
                                    if Residue_number >= 3:
                                        for f_line in temp_residues:
                                            newfile.write(f_line)
                                            print f_line
                                        newfile.write('TER\n')
                                        Residue_number = 0
                                        temp_residues = []
                                    else:
                                        Re_order = 0
                                        Residue_number = 0
                                        temp_residues = []
                                        continue
                        else:
                            if Residue_number >= 3:
                                for f_line in temp_residues:
                                    newfile.write(f_line)
                                    print f_line
                                newfile.write('TER\n')
                                Re_order = 0
                                Residue_number = 0
                                temp_residues = []
                            else:
                                Residue_number = 0
                                temp_residues = []
                                continue
                    else:
                        continue
                elif lines[i][:4].strip() == 'TER':
                    if Residue_number >= 3:
                        for f_line in temp_residues:
                            newfile.write(f_line)
                            print f_line
                        print lines[i]
                        newfile.write(lines[i])
                        Residue_number = 0
                        temp_residues = []
                    else:
                        Residue_number = 0
                        temp_residues = []
                        continue
                else:
                    continue
if __name__ == '__main__':
    or_file = '/Users/xg666/Desktop/getTER/standard/data12001-.pdb'
    new_file = '/Users/xg666/Desktop/getTER/standard/NCAC12001-.pdb'
    clean_data(or_file,new_file)
    print '123'

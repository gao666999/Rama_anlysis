from Bio.PDB import *
import numpy as np
import os

def add_array(lines, i):
    v1 = Vector(float(lines[i-1][30:38]), float(lines[i-1][38:46]), float(lines[i-1][46:54]))
    v2 = Vector(float(lines[i][30:38]), float(lines[i][38:46]), float(lines[i][46:54]))
    v3 = Vector(float(lines[i+1][30:38]), float(lines[i+1][38:46]), float(lines[i+1][46:54]))
    v4 = Vector(float(lines[i+2][30:38]), float(lines[i+2][38:46]), float(lines[i+2][46:54]))
    v5 = Vector(float(lines[i+3][30:38]), float(lines[i+3][38:46]), float(lines[i+3][46:54]))
    alpha = vectors.calc_dihedral(v1,v2,v3,v4)
    beta = vectors.calc_dihedral(v2,v3,v4,v5)
    pair_xy = ([alpha,beta])
    #AAcid_array = np.row_stack((AAcid_array,pair_xy))
    return pair_xy
if __name__ == '__main__':
    basepath = '/Users/xg666/Desktop/getTER/moreloopdata/NCACdata/'
    path = '/Users/xg666/Desktop/getTER/moreloopdata/angleresult/'
    ALA_array = np.zeros(shape = (0,2))
    ARG_array = np.zeros(shape = (0,2))
    ASN_array = np.zeros(shape = (0,2))
    ASP_array = np.zeros(shape = (0,2))
    CYS_array = np.zeros(shape = (0,2))
    GLN_array = np.zeros(shape = (0,2))
    GLY_array = np.zeros(shape = (0,2))
    GLU_array = np.zeros(shape = (0,2))
    HIS_array = np.zeros(shape = (0,2))
    LYS_array = np.zeros(shape = (0,2))
    LEU_array = np.zeros(shape = (0,2))
    ILE_array = np.zeros(shape = (0,2))
    MET_array = np.zeros(shape = (0,2))
    PRO_array = np.zeros(shape = (0,2))
    PHE_array = np.zeros(shape = (0,2))
    SER_array = np.zeros(shape = (0,2))
    TRP_array = np.zeros(shape = (0,2))
    THR_array = np.zeros(shape = (0,2))
    TYR_array = np.zeros(shape = (0,2))
    VAL_array = np.zeros(shape = (0,2))
    filenames=os.listdir(basepath)
    n = 0
    for filename in filenames:
        n += 1
        print n
        print filename
        file = basepath + filename
        with open(file,'r') as file:
            lines = file.readlines()
            length = len(lines)
            i = 0
            while (i < length):
                print i
                if (i == 0):
                    i = i + 3
                    name = lines[i][17:20].strip()
                    if (name == 'ALA'):
                        ALA_pair = add_array(lines, i)
                        ALA_array = np.row_stack((ALA_array,ALA_pair))
                    elif (name == 'VAL'):
                        VAL_pair = add_array(lines, i)
                        VAL_array = np.row_stack((VAL_array,VAL_pair))
                    elif (name == 'LEU'):
                        LEU_pair = add_array(lines, i)
                        LEU_array = np.row_stack((LEU_array,LEU_pair))
                    elif (name == 'ILE'):
                        ILE_pair = add_array(lines, i)
                        ILE_array = np.row_stack((ILE_array,ILE_pair))
                    elif (name == 'PRO'):
                        PRO_pair = add_array(lines, i)
                        PRO_array = np.row_stack((PRO_array,PRO_pair))
                    elif (name == 'PHE'):
                        PHE_pair = add_array(lines, i)
                        PHE_array = np.row_stack((PHE_array,PHE_pair))
                    elif (name == 'TRP'):
                        TRP_pair = add_array(lines, i)
                        TRP_array = np.row_stack((TRP_array,TRP_pair))
                    elif (name == 'MET'):
                        MET_pair = add_array(lines, i)
                        MET_array = np.row_stack((MET_array,MET_pair))
                    elif (name == 'GLY'):
                        GLY_pair = add_array(lines, i)
                        GLY_array = np.row_stack((GLY_array,GLY_pair))
                    elif (name == 'SER'):
                        SER_pair = add_array(lines, i)
                        SER_array = np.row_stack((SER_array,SER_pair))
                    elif (name == 'CYS'):
                        CYS_pair = add_array(lines, i)
                        CYS_array = np.row_stack((CYS_array,CYS_pair))
                    elif (name == 'TYR'):
                        TYR_pair = add_array(lines, i)
                        TYR_array = np.row_stack((TYR_array,TYR_pair))
                    elif (name == 'ASN'):
                        ASN_pair = add_array(lines, i)
                        ASN_array = np.row_stack((ASN_array,ASN_pair))
                    elif (name == 'GLN'):
                        GLN_pair = add_array(lines, i)
                        GLN_array = np.row_stack((GLN_array,GLN_pair))
                    elif (name == 'LYS'):
                        LYS_pair = add_array(lines, i)
                        LYS_array = np.row_stack((LYS_array,LYS_pair))
                    elif (name == 'ARG'):
                        ARG_pair = add_array(lines, i)
                        ARG_array = np.row_stack((ARG_array,ARG_pair))
                    elif (name == 'HIS'):
                        HIS_pair = add_array(lines, i)
                        HIS_array = np.row_stack((HIS_array,HIS_pair))
                    elif (name == 'ASP'):
                        ASP_pair = add_array(lines, i)
                        ASP_array = np.row_stack((ASP_array,ASP_pair))
                    elif (name == 'GLU'):
                        GLU_pair = add_array(lines, i)
                        GLU_array = np.row_stack((GLU_array,GLU_pair))
                    elif (name == 'THR'):
                        THR_pair = add_array(lines, i)
                        THR_array = np.row_stack((THR_array,THR_pair))
                    i = i + 3
                    continue
                elif (lines[i][:4].strip() != 'TER' and lines[i+3][:3] != 'TER'):
                    name = lines[i][17:20].strip()
                    if (name == 'ALA'):
                        ALA_pair = add_array(lines, i)
                        ALA_array = np.row_stack((ALA_array,ALA_pair))
                    elif (name == 'VAL'):
                        VAL_pair = add_array(lines, i)
                        VAL_array = np.row_stack((VAL_array,VAL_pair))
                    elif (name == 'LEU'):
                        LEU_pair = add_array(lines, i)
                        LEU_array = np.row_stack((LEU_array,LEU_pair))
                    elif (name == 'ILE'):
                        ILE_pair = add_array(lines, i)
                        ILE_array = np.row_stack((ILE_array,ILE_pair))
                    elif (name == 'PRO'):
                        PRO_pair = add_array(lines, i)
                        PRO_array = np.row_stack((PRO_array,PRO_pair))
                    elif (name == 'PHE'):
                        PHE_pair = add_array(lines, i)
                        PHE_array = np.row_stack((PHE_array,PHE_pair))
                    elif (name == 'TRP'):
                        TRP_pair = add_array(lines, i)
                        TRP_array = np.row_stack((TRP_array,TRP_pair))
                    elif (name == 'MET'):
                        MET_pair = add_array(lines, i)
                        MET_array = np.row_stack((MET_array,MET_pair))
                    elif (name == 'GLY'):
                        GLY_pair = add_array(lines, i)
                        GLY_array = np.row_stack((GLY_array,GLY_pair))
                    elif (name == 'SER'):
                        SER_pair = add_array(lines, i)
                        SER_array = np.row_stack((SER_array,SER_pair))
                    elif (name == 'CYS'):
                        CYS_pair = add_array(lines, i)
                        CYS_array = np.row_stack((CYS_array,CYS_pair))
                    elif (name == 'TYR'):
                        TYR_pair = add_array(lines, i)
                        TYR_array = np.row_stack((TYR_array,TYR_pair))
                    elif (name == 'ASN'):
                        ASN_pair = add_array(lines, i)
                        ASN_array = np.row_stack((ASN_array,ASN_pair))
                    elif (name == 'GLN'):
                        GLN_pair = add_array(lines, i)
                        GLN_array = np.row_stack((GLN_array,GLN_pair))
                    elif (name == 'LYS'):
                        LYS_pair = add_array(lines, i)
                        LYS_array = np.row_stack((LYS_array,LYS_pair))
                    elif (name == 'ARG'):
                        ARG_pair = add_array(lines, i)
                        ARG_array = np.row_stack((ARG_array,ARG_pair))
                    elif (name == 'HIS'):
                        HIS_pair = add_array(lines, i)
                        HIS_array = np.row_stack((HIS_array,HIS_pair))
                    elif (name == 'ASP'):
                        ASP_pair = add_array(lines, i)
                        ASP_array = np.row_stack((ASP_array,ASP_pair))
                    elif (name == 'GLU'):
                        GLU_pair = add_array(lines, i)
                        GLU_array = np.row_stack((GLU_array,GLU_pair))
                    elif (name == 'THR'):
                        THR_pair = add_array(lines, i)
                        THR_array = np.row_stack((THR_array,THR_pair))
                    i = i + 3
                    continue
                elif (lines[i][:3] == 'TER'):
                    i = i + 4
                    continue
                elif (lines[i][:3] != 'TER' and lines[i+3][:3] == 'TER'):
                    i = i + 7
                    continue
    #for i in range(0,3):
    file1 = path + 'ALA.txt'
    print file1
    #file1 = '/Users/xg666/Desktop/getTER/result/ALA3.txt'
    np.savetxt(file1, ALA_array,fmt = '%.4f')
    file2 = path + 'ARG.txt'
    #file2 = '/Users/xg666/Desktop/getTER/result/ARG3.txt'
    np.savetxt(file2, ARG_array,fmt = '%.4f')
    file3 = path + 'ASN.txt'
    #file3 = '/Users/xg666/Desktop/getTER/result/ASN3.txt'
    np.savetxt(file3, ASN_array,fmt = '%.4f')
    file4 = path + 'ASP.txt'
    #file4 = '/Users/xg666/Desktop/getTER/result/ASP3.txt'
    np.savetxt(file4, ASP_array,fmt = '%.4f')
    file5 = path + 'CYS.txt'
    #file5 = '/Users/xg666/Desktop/getTER/result/CYS3.txt'
    np.savetxt(file5, CYS_array,fmt = '%.4f')
    file6 = path + 'GLN.txt'
    #file6 = '/Users/xg666/Desktop/getTER/result/GLN3.txt'
    np.savetxt(file6, GLN_array,fmt = '%.4f')
    file7 = path +'GLY.txt'
    #file7 = '/Users/xg666/Desktop/getTER/result/GLY3.txt'
    np.savetxt(file7, GLY_array,fmt = '%.4f')
    file8 = path +'GLU.txt'
    #file8 = '/Users/xg666/Desktop/getTER/result/GLU3.txt'
    np.savetxt(file8, GLU_array,fmt = '%.4f')
    file9 = path +'HIS.txt'
    #file9 = '/Users/xg666/Desktop/getTER/result/HIS3.txt'
    np.savetxt(file9, HIS_array,fmt = '%.4f')
    file10 = path +'LYS.txt'
    #file10 = '/Users/xg666/Desktop/getTER/result/LYS3.txt'
    np.savetxt(file10, LYS_array,fmt = '%.4f')
    file11 = path +'LEU.txt'
    #file11 = '/Users/xg666/Desktop/getTER/result/LEU3.txt'
    np.savetxt(file11, LEU_array,fmt = '%.4f')
    file12 = path +'ILE.txt'
    #file12 = '/Users/xg666/Desktop/getTER/result/ILE3.txt'
    np.savetxt(file12, ILE_array,fmt = '%.4f')
    file13 = path +'MET.txt'
    #file13 = '/Users/xg666/Desktop/getTER/result/MET3.txt'
    np.savetxt(file13, MET_array,fmt = '%.4f')
    file14 = path +'PRO.txt'
    #file14 = '/Users/xg666/Desktop/getTER/result/PRO3.txt'
    np.savetxt(file14, PRO_array,fmt = '%.4f')
    file15 = path +'PHE.txt'
    #file15 = '/Users/xg666/Desktop/getTER/result/PHE3.txt'
    np.savetxt(file15, PHE_array,fmt = '%.4f')
    file16 = path +'SER.txt'
    #file16 = '/Users/xg666/Desktop/getTER/result/SER3.txt'
    np.savetxt(file16, SER_array,fmt = '%.4f')
    file17 = path +'TRP.txt'
    #file17 = '/Users/xg666/Desktop/getTER/result/TRP3.txt'
    np.savetxt(file17, TRP_array,fmt = '%.4f')
    file18 = path +'THR.txt'
    #file18 = '/Users/xg666/Desktop/getTER/result/THR3.txt'
    np.savetxt(file18, THR_array,fmt = '%.4f')
    file19 = path +'TYR.txt'
    #file19 = '/Users/xg666/Desktop/getTER/result/TYR3.txt'
    np.savetxt(file19, TYR_array,fmt = '%.4f')
    file20 = path +'VAL.txt'
    #file20 = '/Users/xg666/Desktop/getTER/result/VAL3.txt'
    np.savetxt(file20, VAL_array,fmt = '%.4f')


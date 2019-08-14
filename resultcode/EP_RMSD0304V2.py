from rmsd import calc_rmsd as cm
from calc_angle import ProbabilityProduct
from calc_angle import ProMatrix
import numpy as np
import os
import EnergyForLoop as EL
from fnmatch import fnmatchcase as match
from multiprocessing import Pool
import multiprocessing

def listdirInMac(path):
    os_list = os.listdir(path)
    for item in os_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            os_list.remove(item)
    return os_list

def save_PERM(filename,filepath,resultpath):
    #print 'nnnnnnnnnnnnnnnnnn'
    matrix = EL.load_EnergyMatrix()
    #print 'matrix'
    #print filepath
    ProbabMatrixforLoop,ProbabMatrixforStand = ProMatrix()
    Pl_Ps_EG_RM = np.zeros(shape = (0,4))
    looppath = os.path.join(filepath,str('flanked/'))
    #print 'mmmmmmmmmmmmmmmmmmmm'
    globalpath = os.path.join(filepath,str('global/'))
    #print looppath,globalpath
    loopnames = os.listdir(looppath)
    globalnames = os.listdir(globalpath)
    #print len(loopnames),len(globalnames),looppath,globalpath
    iniloop = os.path.join(filepath,'inipdbloop.pdb')
    if len(loopnames) == len(globalnames):
        for i in range(0,len(loopnames)):
            for j in range(0,len(globalnames)):
                if loopnames[i][7:] == globalnames[j]:
                    loopfile = os.path.join(looppath,loopnames[i])
                    wholefile = os.path.join(globalpath , globalnames[j])
                    # for test,to make sure whether loopfile correspond to correct globalfile
                    print loopnames[i],globalnames[j]
                    Rmsd = cm.main(iniloop,loopfile)
                    if Rmsd != 10000:

                        # get the probability of the loop
                        Probasedloop,Probasedstand = ProbabilityProduct(loopfile,ProbabMatrixforLoop,ProbabMatrixforStand)
                        #get the rmsd of the loop
                        print iniloop,loopfile
                        #Rmsd = cm.main(iniloop,loopfile)
                        #calculate the energy of the loop
                        energy = EL.calculate_Energy(wholefile,loopfile, matrix)
                        #save the resul as a array
                        P_E_RM = (Probasedloop,Probasedstand,energy,Rmsd)
                        Pl_Ps_EG_RM = np.row_stack((P_E_RM,Pl_Ps_EG_RM))
                    else:
                        continue
        savePERM = os.path.join(resultpath,filename+'.txt' )
        np.savetxt(savePERM,Pl_Ps_EG_RM,fmt = '%.9f')
def multiprocess_run(datapath,resultpath):
    filenames = listdirInMac(datapath)
    filenamesuseful = []
    for filename in filenames:
        pathcontent = listdirInMac(os.path.join(datapath,filename))
        if 'inipdbloop.pdb' in pathcontent:
            filenamesuseful.append(filename)
    processnum = len(filenamesuseful)
    pool = multiprocessing.Pool(processes = processnum)
    for process_n in range(processnum):
        filepath = os.path.join(datapath,filenamesuseful[process_n])
        print filenamesuseful[process_n],filepath
        filenameuseful = filenamesuseful[process_n]
        save_PERM(filenameuseful,filepath,resultpath)
        #get_startid_endid_inifile(filepath,reportpath,pdbpath)
        #pool.apply_async(save_PERM,(filenameuseful,filepath,resultpath))
    #pool.close()
    #pool.join()
'''
def main(datapath,resultpath):
    filenames = listdirInMac(datapath)
    for filename in filesnames:
        if match(,'*_*'):
            filepath = os.path.join(datapath,filename)
            # the prediction always named as id1_id2.BL00000*.pdb,so we can use *-*
            save_PERM(filename,filepath,resultpath)
'''

if __name__ == "__main__":
    datapath = '/public/home/xgao/Desktop/looppredict/pdbfile0303/'
    resultpath = '/public/home/xgao/Desktop/looppredict/result0304v2/'
    multiprocess_run(datapath,resultpath)

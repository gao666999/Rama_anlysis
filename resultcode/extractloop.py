import os
from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PDBIO
from Bio.PDB import Select
from multiprocessing import Pool
import multiprocessing
# rewrite ResidueSelect class,so that PDBIO can use this class to save the structure we want
class ResidueSelect(Select):
    def __init__(self,id1,id2):
        self.id1 = id1
        self.id2 = id2

    def accept_residue(self,residue):
        if residue.get_parent().get_id() =='A':
            #print residue.get_id()[1]
            if self.id1 <= residue.get_id()[1] <= self.id2:
            #print residue.get_id()[1]
                return True
        else:
            return False
# this function can return a list contain all the file'name in one directory excpte .Dstore
def listdirInMac(path):
    os_list = os.listdir(path)
    for item in os_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            os_list.remove(item)
    return os_list
#use Bio.PDB create the pdb strcuture
def make_structure_for_pdbfile(file,structure_id):
    p = PDBParser(PERMISSIVE = 1)
    structure = p.get_structure(structure_id,file)
    return structure
#save the loop
def save_loop(globalfile,structure_id,loopfile,id1,id2):
    structure = make_structure_for_pdbfile(globalfile,structure_id)
    io = PDBIO()
    p = PDBParser(PERMISSIVE = 1)
    io.set_structure(structure)
    io.save(loopfile, ResidueSelect(id1,id2))
def save_loopfile(pdbpath,filename):
    globalpath = os.path.join(pdbpath,filename+str('/global/'))
    globalnames = listdirInMac(globalpath)
    loopfilepath = os.path.join(pdbpath,filename+str('/flanked/'))
    if not os.path.isdir(loopfilepath):
        os.makedirs(loopfilepath)
    for globalfilename in globalnames:
        globalfile = os.path.join(globalpath,globalfilename)
        id1_id2 = globalfilename.split('.')[0]
        id1 = int(id1_id2.split('-')[0])
        id2 = int(id1_id2.split('-')[1])
        loopfile = os.path.join(loopfilepath,str('flanked') + globalfilename)
        structure_id = globalfilename
        save_loop(globalfile,structure_id,loopfile,id1,id2)
def multiprocess_run(pdbpath):
    filenames = listdirInMac(pdbpath)
    filenamesuseful = []
    for filename in filenames:
        pathcontent = listdirInMac(os.path.join(pdbpath,filename))
        if 'inipdbloop.pdb' in pathcontent:
            filenamesuseful.append(filename)
    processnum = len(filenamesuseful)
    pool = multiprocessing.Pool(processes = processnum)
    for process_n in range(processnum):
        print filenamesuseful[process_n]
        #get_startid_endid_inifile(filepath,reportpath,pdbpath)
        pool.apply_async(save_loopfile,(pdbpath,filenamesuseful[process_n]))
    pool.close()
    pool.join()


if __name__ == "__main__":
    pdbpath = '/public/home/xgao/Desktop/looppredict/pdbfile0301/'
    multiprocess_run(pdbpath)

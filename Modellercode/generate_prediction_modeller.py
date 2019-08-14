# -*- coding: utf-8 -*
# Run this script with something like
#    python loop.py N > N.log
# where N is an integer from 1 to the number of models.
# ModLoop does this for N from 1 to 300 (it runs the tasks in parallel on a
# compute cluster), then returns the single model with the best (lowest)
# value of the Modeller objective function.
import _modeller
from modeller import *
from modeller.automodel import *
import sys
import os
from Bio.PDB import *
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PDBIO
from Bio.PDB import Select
from fnmatch import fnmatchcase as match
from multiprocessing import Pool
import multiprocessing
# to get different starting models for each task
#taskid = int(sys.argv[1])


class MyLoop(loopmodel):

    def __init__(self,startid,endid,report_path,pdb_path,env, sequence, alnfile=None, knowns=[], inimodel=None,
                 deviation=None, library_schedule=None, csrfile=None,
                 inifile=None, assess_methods=None, loop_assess_methods=None):
        loopmodel.__init__(self, env, sequence, alnfile, knowns, inimodel,
                 deviation, library_schedule, csrfile,
                 inifile, assess_methods, loop_assess_methods)
        self.startid = startid
        self.endid = endid
        self.report_path = report_path
        self.pdb_path = pdb_path

    def write(self, file, model_format='PDB', no_ter=False, extra_data=''):
        """Write coordinates to a file"""
        if 'BL' in file:
            if not os.path.isdir(self.pdb_path):
                os.makedirs(self.pdb_path)
            pdbfile = self.pdb_path + file
            fh = modfile._get_filehandle(pdbfile, 'w')
        else:
            fh = modfile._get_filehandle(file, 'w')
        return _modeller.mod_model_write(self.modpt, self.env.libs.modpt, (),
                                         fh.file_pointer, model_format,
                                         no_ter, True, extra_data)

    def new_loop_trace_file(self,id1,id2):
        """Open a new loop optimization trace file"""
        if self.trace_output > 0:
            filename = modfile.default(file_ext='', file_id='.DL',
                                       root_name=self.sequence, id1=id1,
                                       id2=id2)
            if not os.path.isdir(self.report_path):
                os.makedirs(self.report_path)
            report_file =self.report_path+filename

            return open(report_file, 'w')

            #return open(filename, 'w')
        else:
            return None

    def select_loop_atoms(self):
        rngs = (
           self.residue_range(self.startid, self.endid),
           #self.residue_range('43:A','48:A'),
        )
        for rng in rngs:
            if len(rng) > 30:
                raise ModellerError("loop too long")
        s = selection(rngs)
        if len(s.only_no_topology()) > 0:
            raise ModellerError("some selected residues have no topology")
        return s

def listdirInMac(path):
    os_list = os.listdir(path)
    for item in os_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            os_list.remove(item)
    return os_list

def make_structure_for_pdbfile(file,structure_id):
    p = PDBParser(PERMISSIVE = 1)
    structure = p.get_structure(structure_id,file)
    #model = structure[0]
    return structure

def get_looplength(file,filename):
    model = make_structure_for_pdbfile(file,filename)[0]
    residues = model.get_residues()
    sequence_ids = []
    for residue in residues:
        S_id = residue.get_id()[1]
        #S_chainid = residue.get_full_id()[2]
        id_chain = str(S_id) + str(':A')
        sequence_ids.append(id_chain)
    sequence_length = len(sequence_ids)
    return sequence_length,sequence_ids

def select_standardsequence(looppath):
    length_standard = 100
    sequence_standard = []
    filenames = listdirInMac(looppath)
    for filename in filenames:
        if match(filename,'Flanked*'):
            file = os.path.join(looppath,filename)
            length,sequence = get_looplength(file,filename)
            #print length
            if length < length_standard:
                length_standard = length
                sequence_standard = sequence
    return sequence_standard[0],sequence_standard[-1]

def generate_prediction(startid,endid,report_path,pdb_path,inifile):
    taskid = 300
    env = environ(rand_seed=-1000-taskid)
    #start_id = str(startid)
    #end_id = str(endid) + str(':A')
    m = MyLoop(startid,endid,report_path,pdb_path,env, inimodel=inifile,
               sequence = str(startid[:-2]) +str('-')+ str(endid[:-2]))
    m.loop.md_level = refine.slow
    m.loop.starting_model = 1
    m.loop.ending_model = 300
    m.make()

def get_startid_endid_inifile(filepath,reportpath,pdbpath):
    names = listdirInMac(filepath)
    for name in names:
        #print name
        #print '############################################'
        #if match(name,'refe-structure.pdb
        inifile = os.path.join(filepath,'refe-structure_new.pdb')

        if match(name,'*_*'):
            #print name
            #print 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
            looppath = os.path.join(filepath,name)
            start_id,end_id = select_standardsequence(looppath)
            report_path = os.path.join(reportpath,name+str('/'))
            pdb_path = os.path.join(pdbpath,name+str('/global/'))
            generate_prediction(start_id,end_id,report_path,pdb_path,inifile)
            print 'gaogaogaogaogaogaogaoagoagagahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'


def multiprocess_run(datasetpath,reportpath,pdbpath):
    filenames = listdirInMac(datasetpath)
    processnum = len(filenames)
    pool = multiprocessing.Pool(processes = processnum)
    for process_n in range(processnum):
        filepath = os.path.join(datasetpath,filenames[process_n])
        #print filepath
        get_startid_endid_inifile(filepath,reportpath,pdbpath)
        #pool.apply_async(get_startid_endid_inifile,(filepath,reportpath,pdbpath))
    #pool.close()
    #pool.join()


if __name__ == "__main__":
    datasetpath = '/Users/xg666/Desktop/looppredict/testdata0226/'
    reportpath = '/Users/xg666/Desktop/looppredict/report0228/'
    pdbpath = '/Users/xg666/Desktop/looppredict/pdbfile0228/'
    multiprocess_run(datasetpath,reportpath,pdbpath)
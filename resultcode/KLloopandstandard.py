import numpy as np
import os
from scipy import stats
import pandas as pd
from sklearn.metrics import mean_squared_error

def listdirInMac(path):
    os_list = os.listdir(path)
    for item in os_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            os_list.remove(item)
    return os_list

def save_as_excel(value1,value2,value3,value4,value5,value6,value7,newexcelpath,excelname):
    s0 = pd.Series(value1)
    s1 = pd.Series(value2)
    s2 = pd.Series(value3)
    s3 = pd.Series(value4)
    s4 = pd.Series(value5)
    s5 = pd.Series(value6)
    s6 = pd.Series(value7)
    #row=((AAname,MSEsigle,SAmount,LAmount,KLD,CEP,SLratio))
    df = pd.DataFrame({"AAname":s0,'MSE':s1,'SAmount':s2,'LAmount':s3,'KlD':s4,'CEP':s5,'SLratio':s6})
    cols = ["AAname",'MSE','SAmount','LAmount','KlD','CEP','SLratio']
    df = df.ix[:,cols]
    #del_file(path)
    excelfile = os.path.join(newexcelpath,excelname)
    writer = pd.ExcelWriter(excelfile)
    df.to_excel(writer, sheet_name = 'LOOPStatistic')
    writer.save()

def calculateKL(P,Q):
    P = P.flatten()
    Q = Q.flatten()
    kl1 = stats.entropy(P,Q)
    kl2 = stats.entropy(Q,P)
    print kl1,kl2,'kkkkkkkkkkkkkkkkk'
    kl = (kl1+kl2)/2
    kl = '%.5f'%kl
    return kl

def MSE(P,Q):
    P = P.flatten()
    Q = Q.flatten()
    mse=mean_squared_error(P,Q)
    mse='%.8f'%mse
    return mse
# a is L,y is S
def cross_entropy(a, y):
    a = a.flatten()
    y = y.flatten()
    #loss = np.mean(-np.sum(y*np.log(a),axis=1))
    #loss = np.mean(-np.sum(a*np.log(y),axis=1))
    #return loss
    return np.sum(np.nan_to_num(-y*np.log(a)-(1-y)*np.log(1-a)))
    #return np.sum(np.nan_to_num(-a*np.log(y)-(1-a)*np.log(1-y)))

def sample_matrix(bin,filename):
    array_smaple = np.loadtxt(filename)
    Amount=len(array_smaple)
    phi = array_smaple[:,0]
    psi = array_smaple[:,1]
    SampMatrix, binx, biny = np.histogram2d(phi,psi,bins = bin)
    AllSampAmount = sum(sum(SampMatrix))
    #newMatrix = np.zeros((bin,bin))
    for n in range(bin):
        for m in range(bin):
            if SampMatrix[n][m]==0:
                SampMatrix[n][m] = 0.001
    print SampMatrix.shape
    print AllSampAmount
    SampMatrix = SampMatrix/AllSampAmount
    return SampMatrix,Amount
#this function can return the matrix of samples

def GetFile(path_loop,path_standard,resultpath,excelfile):
    bin=20
    loopfiles=listdirInMac(path_loop)
    loopfiles.sort()
    standardfiles=listdirInMac(path_standard)
    standardfiles.sort()
    length=len(loopfiles)
    #Result = np.zeros(shape = (0,4))
    LAmountList=[]
    MSEList=[]
    SAmountList=[]
    KLlist=[]
    CElist=[]
    filenamelist=[]
    for f in range(length):
        filename=loopfiles[f][:3]
        filenamelist.append(filename)
        Lfile=os.path.join(path_loop,loopfiles[f])
        Sfile=os.path.join(path_standard,standardfiles[f])
        LMatrix,Lamount=sample_matrix(bin,Lfile)
        LAmountList.append(Lamount)
        SMatrix,Samount=sample_matrix(bin,Sfile)
        SAmountList.append(Samount)
        MSEone=MSE(LMatrix,SMatrix)
        MSEList.append(MSEone)
        KlD=calculateKL(LMatrix,SMatrix)
        KLlist.append(KlD)
        CE=cross_entropy(LMatrix,SMatrix)
        CElist.append(CE)
        #print KlD,CE
    ResultArray = np.zeros(shape = (0,7))
    SumLA=sum(LAmountList)
    SumSA=sum(SAmountList)
    #LAmountList=LAmountList/float(SumLA)
    #SAmountList=SAmountList/float(SumSA)
    for k in range(length):
        AAname=filenamelist[k]
        LAmount=LAmountList[k]/float(SumLA)
        SAmount=SAmountList[k]/float(SumSA)
        SLratio=float(SAmount)/float(LAmount)
        MSEsigle=MSEList[k]
        KLD=KLlist[k]
        CEP=CElist[k]
        row=((AAname,MSEsigle,SAmount,LAmount,KLD,CEP,SLratio))
        print row
        ResultArray = np.row_stack((ResultArray,row))
    value1=ResultArray[:,0]
    value2=ResultArray[:,1]
    value3=ResultArray[:,2]
    value4=ResultArray[:,3]
    value5=ResultArray[:,4]
    value6=ResultArray[:,5]
    value7=ResultArray[:,6]

    save_as_excel(value1,value2,value3,value4,value5,value6,value7,resultpath,excelfile)


if __name__ == '__main__':
    path_loop = '/Users/xg666/Desktop/loop/getTER/moreloopdata/angleresult/'
    path_standard = '/Users/xg666/Desktop/loop/getTER/standard/angledatafinally/'
    resultpath = '/Users/xg666/Desktop/loop/LoopResult/Excel'
    excelfile='KL_CE_RatioComplete.xlsx'
    GetFile(path_loop,path_standard,resultpath,excelfile)
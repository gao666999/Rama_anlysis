# -*- coding: utf-8 -*-
from matplotlib import pyplot
import numpy as np
import types

def drawHist(heights):
    #创建直方图
    #第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
    #第二个参数为划分的区间个数
    '''
    pyplot.hist(heights,200)
    pyplot.xlabel('Number of Neighbor pairs')
    pyplot.ylabel('Frequency')
    pyplot.title('the frequency about the number of neighbor pairs(negaitive)')
    pyplot.show()
    '''

    pyplot.hist(heights,200)
    pyplot.xlabel('Loop length')
    pyplot.ylabel('Frequency')
    pyplot.title('Frequency histogram for loop length')
    pyplot.show()

if __name__ =='__main__':
    a = np.load('/Users/xg666/Desktop/loop/getTER/result/save_drnew.npy')
    print a.shape
    #length = len(a)
    a = a[:,0]
    a = np.sort(a)
    a = a[:-122]
    #print a[10000:]
    #print len(a)
    #print a.shape

    #print a[100000:1006664]
    #print a.shape
    #print a[:3]
    #a = a.reshape((-1,1))
    #a = a[np.lexsort(a[:,:: -1].T)]
    #b = a[:6000]
    '''
    length1 = len(a)
    print length
    print a.shape
    print a
    print b
    length2 = len(b)
    print length2
    print isinstance(a,list)
    print type(b)
    '''
    drawHist(a)



# l means data of loop, s means data of standard
from __future__ import division
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
#campute the denstity of loop data
bin = 10
arrloop = np.loadtxt('/Users/xg666/Desktop/loop/getTER/moreloopdata/angleresult/ALA.txt')
aloop = np.zeros((bin,bin))
phil = arrloop[:,0]
psil = arrloop[:,1]
hl, xl, yl = np.histogram2d(phil,psil,bins = bin)
print hl.shape
print 'hhhhhhhhh'
sl = hl.sum()
for i in range(0,bin):
    for j in range(0,bin):
        resultl = hl[i][j] / sl
        print resultl
        print 'meee'
        if resultl < 0:
            print resultl
            print 'lllllll'
        #print resultl
        #aloop[i][j] = '%.2f'%resultl
        aloop[i][j] = resultl
suml = aloop.sum()
print aloop
print suml
print xl

'''
# campute the denstity of standard data
arrstandard = np.loadtxt('/Users/xg666/Desktop/loop/getTER/standard/angledatafinally/ALA.txt')
astandard = np.zeros((bin,bin))
phis = arrstandard[:,0]
psis = arrstandard[:,1]
hs, xs, ys = np.histogram2d(phis,psis,bins = bin)
ss = hs.sum()
for i in range(0,bin):
    for j in range(0,bin):
        results = hs[i][j] / ss
        if results < 0:
            print results
            print 'sssssss'
        astandard[i][j] = results
sums = astandard.sum()
print astandard
print sums

# compute the ratio
#ls means loop/standard
#sl means standard/loop
ratiols = np.zeros((bin,bin))
ratiosl = np.zeros((bin,bin))
n = 0
m = 0
d = 0
for i in range(0,bin):
    for j in range(0,bin):
        if aloop[i][j] == 0 and astandard[i][j] == 0:
            print aloop[i][j]
            n += 1
            ratiols[i][j] = 0
            ratiosl[i][j] = 0
        elif aloop[i][j] == 0 and astandard[i][j] != 0:
            m += 1
            ratiols[i][j] = -100
            ratiosl[i][j] = 100
        elif astandard[i][j] == 0 and aloop[i][j] != 0:
            d += 1
            ratiols[i][j] == 100
            ratiosl[i][j] == -100
        else:
            ratiols[i][j] = aloop[i][j] / astandard[i][j]
            ratiosl[i][j] = astandard[i][j] / aloop[i][j]

        if ratiosl[i][j] < 0:
            print ratiosl[i][j]
            print 'ratiosl'
        if ratiols[i][j] < 0:
            print ratiols[i][j]
            print 'ratiols'
print n,m,d
'''

'''
#ax = plt.subplots(figsize = (10,8),nrows = 2)
#np.random.seed(sum(map(ord, 'categorical')))
#flights = flights.pivot(index='phi', columns='psi',  values='Density of ratio')
#aloop = aloop.pivot(index = xl,columns = yl,values = aloop)
'''
'''
f, (ax1,ax2) = plt.subplots(figsize = (12, 9),nrows=2)
#sns.heatmap(ratiols,cmap = 'YlGnBu',robust = False,xticklabels = False,yticklabels = False,ax = ax1)
#sns.heatmap(ratiols,robust = False,xticklabels = False,yticklabels = False,ax = ax1)
sns.heatmap(ratiols,robust = False,xticklabels = False,yticklabels = False,ax = ax1)
ax1.set_title('Density of ratio(ls)')
ax1.set_xlabel('phi')
ax1.set_ylabel('psi')
#sns.heatmap(ratiosl,cmap = 'YlGnBu',robust = False,xticklabels = False,yticklabels = False,ax = ax2)
sns.heatmap(ratiosl,robust = False,xticklabels = False,yticklabels = False,ax = ax2)
ax2.set_title('Density of ratio(sl)')
ax2.set_xlabel('phi')
ax2.set_ylabel('psi')
plt.show()
'''
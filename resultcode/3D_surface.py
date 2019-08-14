#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from matplotlib import cm
#import mpl_finance

bins = 60
fig = plt.figure()
ax = Axes3D(fig)
#ax.set_title('Dihedral angle distribution for LEU(Loop)')
ax.set_title('Ramachandran plot for LEU(Loop)')
#ax.set_title('Ramachandran plot for LEU(Standard)')
#ax.set_title('Dihedral angle distribution of LEU(Standard)')
ax.set_xlabel('phi')
ax.set_ylabel('psi')
ax.set_zlabel('frequency')
a = np.loadtxt('/Users/xg666/Desktop/loop/getTER/moreloopdata/angleresult/LEU.txt')
#a = np.loadtxt('/Users/xg666/Desktop/loop/getTER/standard/angledatafinally/LEU.txt')
b = a[:,0]
c = a[:,1]
z, x, y = np.histogram2d(b,c,bins = bins)

x = x[0:bins]
y = y[0:bins]
X, Y = np.meshgrid(x, y)
print X.shape
#print Xls

print Y.shape
print Y
print z
s = z.sum()

print s
Z = z/s

ax.plot_surface(X, Y, Z, rstride = 1,   # row 行步长
                 cstride = 2,           # colum 列步长
                 cmap=plt.cm.hot )      # 渐变颜色

'''
ax.plot_surface(X, Y, Z, rstride = 1,   # row 行步长
                 cstride = 1,           # colum 列步长
                 cmap=cm.coolwarm)      # 渐变颜色
#ax.set_zlim(-2, 2)
'''

'''
ax.contourf(, y, z,
            zdir='z',  # 使用数据方向
            offset=-2, # 填充投影轮廓位置
            cmap=plt.cm.hot)
ax.set_zlim(-2, 2)
'''

plt.show()

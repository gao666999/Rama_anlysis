import matplotlib.pyplot as plt
import numpy as np
array = np.load('/Users/xg666/Desktop/loop/getTER/result/save_DRN.npy')
Dis = array[:,0]
Rad = array[:,1]
Num = array[:,2]
'''
b = np.reshape(a,(-1, 2))
c = a[np.lexsort(a[:,::-1].T)]
print 'this is cccc'
print c
d = c[0:60000,0]
e = c[0:60000,1]
print 'this is dddd'
print d
print 'this is eeeee'
print e
lengthd = len(d)
print lengthd
length = len(b)
print length
print c.shape
print d.shape
print e.shape
'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('scatter Plot for Radius of Gyration and number of residues ')
plt.xlabel('Radius of Gyration')
plt.ylabel('number of residues')
plt.scatter(Rad,Num, color = 'red',marker = '.')
plt.show()

import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as lin
from timeit import default_timer as timer


# number of paricles = number of boides = number of cells
n = 100

# seting the X (and global) list: 
   ## 'X' is the size of the fild on x, i.e. the size of the x-space (x-universe) where the boides are allowed to accupy;
   ## 'bin_size' is the size of the side of the boxes in x and y - they are a square; 'bin_size ~> rl';
   ## 'n_binX' is the number os boxes (bins) in this x-universe; the idea is that the number of boxes need to be in the way that the boxes length ('bin_size') be higher than the interection radio ('rl'), but just a litlle higher;
   ## 'n_boxes' is the number of boxes in the total xy-universe; if 3 boxes in x-universe and 2 in the y-universe = 6 boxes in the xy-universe;
X = 80
Y = 80
bin_size = 1.7
n_binX = int(X/bin_size) + 1
n_binY = int(Y/bin_size) + 1
n_boxes = n_binX * n_binY
   ## 'listX' is a list of 'n_binX' sub-lists, i.e. if the x-universe is divided in 9 boxes, 'listX' will have 9 entries, 9 sub-lists;
   ## 'boxes' is the list containing all the 'n_boxes' in the xy-universe;
listX = [[] for i in range(n_binX)]
boxes = [[] for i in range(n_boxes)]

# seting the coordinates particles:
   ## 'x' and 'y' are n-vectors correspoding to n-boides; the particle 15 will the the one with coordinates x[14],y[14]: 
      ### ex: if for this boide 2*bin_size < x[14] < 3*bin_size that boide will be appended to 'lisX[2]' ('listX[2].append(14)');         
x = np.random.uniform(0,X,n)
y = np.random.uniform(0,Y,n)


# test to see if the programe is seting the particles aproprabaly in each boxe; for this test use:
   ## X = Y = 10; bin_size = 1.0
#for k in range(n/11):
#   for i in range(n/11):
#      x[i+k*n/11] = i*bin_size
#      y[i+k*n/11] = k*bin_size
#print len(listX), '\n', n_boxes
   ## to used after the list interations - if needed:
#print listX
#print n_boxes


#*******************************************************************************************
#********************************  Inicio do programa***************************************
#*******************************************************************************************

#***** timer ********:
   ## for 500 particles and 6561 boxes ~ 1.6 ms (1.6e-3s);
   ## for 500 particles and 2034 boxes ~ 1.5 ms (1.5e-3s);
   ## for 500 particles and 123 boxes ~ 1.5 ms (1.5e-3s);
   ## for 200 particles and 2034 boxes ~ 0.65 ms (6.5e-4s);
   ## for 100 particles and 2034 boxes ~ 0.34 ms (3.4e-4s);
start = timer()
#********************

# seting the 'n' particles into all the 'n_binX' boxes in x-universe: #retangulos#
   ## 'i in range(n)' rolls all the 'i' particles positions in the x-universe; 
   ## 'j' is the index of the 'x box' wich each 'i' particles are going to be allocated: 
      ### if 'x[i=9] = 0' than the '10' particle will belong to the 'x box 0' ('listX[0].append(9)') 
for i in range(n): 				
   j = int((x[i])/bin_size)
   listX[j].append(i)

# seting the 'n' particles into all the 'n_boxes' in the xy-universe: #boxes#
   ##'k in range(n_binX)' rolls all the 'k' boxes in the 'listX';
   ## them for each 'listX[k]' check the y position of all the kk particals into the listX[k];
   ## if ther is a particle kk in the listX[k], this particles will be appended to the respective 'boxes[j]' by the metric:
      ### ex: just read the line you layze boy! 
for k in range(n_binX):
   for kk in listX[k]:
      j = int(y[kk]/bin_size)*n_binX + k
      boxes[j].append(kk)


#***** timer ********
delta_t = timer() - start
print 'tempo de processamento =', delta_t,'s'
#********************


plt.grid()
plt.plot(x,y,'go')
plt.show()


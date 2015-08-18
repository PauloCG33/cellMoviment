import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as lin
from timeit import default_timer as timer


# number of paricles = number of boides = number of cells
n = 100

# seting the X list: 
   ## 'X' is the size of the fild on x, i.e. the size of the x-space (x-universe) where the boides are allowed to accupy;
   ## 'n_binX' is the number os boxes (bins) in this x-universe; the idea is that the number of boxes need to be in the way that the boxes length ('bin_size') be higher than the interection radio ('rl'), but just a litlle higher;
   ## 'bin_sizeX' is the size of the boxes in x; here is set totaly arbitrary to meke esyer...
   ## 'listX' is a list of 'n_binX' sub-lists, i.e. if the x-universe is divided in 9 boxes, 'listX' will have 9 entries, 9 sub-lists
X = 9
n_binX = 9
bin_sizeX = X/n_binX
listX = [[] for i in range(n_binX)]


# seting the Y list: U.C., but it will probably work just like 'X'; 
Y = 6

# seting the coordinates particles:
   ## 'x' and 'y' are n-vectors correspoding to n-boides; the particle 15 will the the one with coordinates x[14],y[14]; 
   ### ex: if for this boide 2*bin_sizeX < x[14] < 3*bin_sizeX that boide will be appended to 'lisX[2]' ('listX[2].append(14)');         
x = np.random.uniform(0,X,n)
y = np.random.uniform(0,Y,n)

# seting the 'n' particles into the 'n_binX' x boxes:
   ## 'i in range(n)' rolls all the 'i' particles positions in the x-universe; 
   ## 'j' is the x box index wich each 'i' particles are going to be allocated: 
   ### if 'x[i=9] = 0' than the '10' particle will belong to the 'x box 0' ('listX[0].append(9)') 
for i in range(n): 				
   j = int((x[i])/bin_sizeX)
   listX[j].append(i)


print listX


plt.grid()
plt.plot(x,y,'go')
plt.show()


#******************** Determinando o tamanho do bin para x *************************
#xmax = max(x) ; xmin = min(x) ; ymax = max(y) ; ymin = min(y)
#delta_x = xmax - xmin
#print delta_x, xmax, xmin, bin_size
#bin_size = bin_size*1.0001		#Correcao para incluir o maior valor do array.
#***********************************************************************************

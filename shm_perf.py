#! /bin/python3

from time import time
import matplotlib.pyplot as plt
import shm
import numpy as np

#test using various grid spacings (h=delta_t)
h_vec = [0.1, 0.05, 0.01, 0.005 ]

times_an = np.zeros(len(h_vec))
times_f = np.zeros(len(h_vec))
times_m =  np.zeros(len(h_vec))
an_solns = []
FDf_solns = []
FDm_solns = []

#Calculate solution using three methods (all in the for loop below)
# 1) using the analytical equation (basically cos(t), 2) a finite difference inspired 'forward solver'
# 3) a matrix based finite diference scheme
for i in range(len(h_vec)):
    start = time()
    an = shm.SHM_an( h_vec[i] )
    end = time()
    times_an[i] = end-start
    an_solns.append(an)

    startf = time()
    f = shm.SHM_FDfor( h_vec[i] )
    endf = time()
    times_f[i] = endf-startf
    FDf_solns.append( f )

    startm = time()
    m = shm.SHM_FDmat( h_vec[i] )
    endm = time()
    times_m[i] = endm-startm
    FDm_solns.append( m )

print('Elapsed Time Analytical:', times_an, '\n\nElapsed Times FD Forward: ',times_f, 
              '\n\nElapsed Times FD Matrix',times_m, '\n' )

plt.plot(h_vec, times_an,'*', label = 'Analytical')
plt.plot(h_vec, times_f ,'*', label = 'Forward Solver Finite Difference')
plt.plot(h_vec, times_m, '*', label = 'Matrix Finite Difference')
plt.xlabel = 'h'
plt.ylabel = 'times (s)'
plt.title = 'Elapsed time (s) for various h values'
plt.legend()
plt.savefig('SHM_3ways_times.png')

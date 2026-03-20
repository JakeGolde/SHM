#! /bin/python3

from time import time
import matplotlib.pyplot as plt
import shm
import numpy as np

h_vec = [0.1, 0.05, 0.01, 0.005, 0.001]

times_an = np.zeros(len(h_vec))
times_f = np.zeros(len(h_vec))
times_m =  np.zeros(len(h_vec))
an_solns = []
FDf_solns = []
FDm_solns = []

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


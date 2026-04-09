#! /bin/python3
import os
import numpy as np
from time import time
import matplotlib.pyplot as plt
import ctypes as ct

path = os.getcwd()
clibrary = ct.CDLL(os.path.join(path,'shm.so'))

# calculation parameters
#dt = 0.001   # delta t
t0 = 0       # initial time
tf = 10      # final time

# vector of step sizes to test
dt_vec = [0.1, 0.01, 0.001, 0.0001] #, 0.00001]

# initialize result vectors
FD_time_vec   = np.zeros(len(dt_vec))  # times for FD calculation
FDC_time_vec  = np.zeros(len(dt_vec))  # times for FD Ctypes calculation
an_time_vec   = np.zeros(len(dt_vec))  # times for analytical solution calculation
error_FD_vec  = np.zeros(len(dt_vec))  # errors b/w FD and analytical cals
error_FDC_vec = np.zeros(len(dt_vec))  # errors b/w FD Ctypes and analytical calcs
error_vec     = np.zeros(len(dt_vec))  # errors b/w FD and FD Ctypes calcs

# Loop over dt values contained in dt_vec list
for i in range(len(dt_vec)):

    ###--- Finite Diference Forward Solver --- ##
    fd_start = time()

    # initialize grids
    t=np.arange(t0,tf,dt_vec[i]) # construct time grid
    x=np.zeros(len(t))    # construct soln gid

    # set initial conditions
    x[0] = 1
    x[1] = 1

    # implement forward solver
    for j in range(1,len(t)-1):
        x[j+1] = ( 2 - dt_vec[i]**2)*x[j]-x[j-1]

    fd_end = time()
    FD_time_vec[i] = fd_end-fd_start       # save calculation time


    ###--- Finite Diference Forward Solver - CTYPES ---###

    fdC_start = time()

    # set C specific parameters
    knum = int( ( tf - t0 ) / dt_vec[i] )  # size of solution array
    array = (ct.c_double * knum)()         # define array to save solution

    # set C argument and result types
    clibrary.SHM_FDfor.argtypes = [ct.POINTER(ct.c_double), ct.c_double, ct.c_int]
    clibrary.SHM_FDfor.restype = ct.POINTER(ct.c_double)

    # call the C function
    sol = clibrary.SHM_FDfor(array, dt_vec[i], knum)

    # save Ctypes array into a numpy array for further processing
    Cx = np.zeros(len(t))
    for j in range(knum):
        Cx[j] = sol[j]
#       print(Cx[i])
    fdC_end = time()
    FDC_time_vec[i] = fdC_end - fdC_start   # save calculation time

    ###--- Analytical Solution ---###
    an_start = time()

    # initialize 'an_sol' analytical solution vector
    an_sol=np.zeros(len(t))

    # populate analytical solution vector
    an_sol=np.cos(t)

    an_end = time()
    an_time_vec[i] = an_end - an_start

    # save errors
    error_FD = np.zeros(len(t))        # error b/w FD and analytical soln
    error_FD = np.abs( an_sol - x )
    error_FD_vec[i] = np.sum(error_FD)

    error_FDC = np.zeros(len(t))        # error b/w FD Ctypes and analytical soln
    error_FDC = np.abs( an_sol - Cx )
    error_FDC_vec[i] = np.sum(error_FDC)

    error  = np.zeros(len(t))        # error b/w FD & FD Ctypes solns
    error  = np.abs( x - Cx )
    error_vec[i] = np.sum(error)



print("\nError between forward solver and analytical soln: ",        error_FD_vec )
print("\nError between Ctypes forward solver and analytical soln: ", error_FDC_vec )
print("\nError between Ctypes and Python forward solvers: ",         error_vec )



## Plotting ##
plt.plot(dt_vec, FD_time_vec, '*',  label = 'Finite Difference')
plt.plot(dt_vec, an_time_vec, '*',  label = 'Analytical Solution')
plt.plot(dt_vec, FDC_time_vec,'*',  label = 'Ctypes Finite Difference')
plt.xscale('log')
plt.xlabel('Dt (s)')
plt.ylabel('Computation Time (s)')
plt.title('Computation Time vs. Dt')
plt.legend()
plt.savefig('shm_dt_analysis.png')

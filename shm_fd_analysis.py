#! /bin/python3
import os
import numpy as np
from time import time
import matplotlib.pyplot as plt
import ctypes as ct

path = os.getcwd()
clibrary = ct.CDLL(os.path.join(path,'shm.so'))

# calculation parameters
dt = 0.001   # delta t
t0 = 0       # initial time
tf = 10      # final time


###--- Finite Diference Forward Solver --- ###

fd_start = time()

# initialize grids
t=np.arange(t0,tf,dt) # construct time grid
x=np.zeros(len(t))    # construct soln grid

# set initial conditions
x[0] = 1
x[1] = 1

# implement forward solver
for i in range(1,len(t)-1):
    x[i+1] = ( 2 - dt**2)*x[i]-x[i-1]
    #print(x[i])


fd_end = time()


# PRINT RESULTS
print( "FD forward solver elapsed time: ", fd_end-fd_start)
#print( "FD Solution")
#for i in range(len(t)):
#    print(x[i])


###--- Finite Diference Forward Solver - CTYPES ---###

fdC_start = time()

# set C specific parameters
knum = int( ( tf - t0 ) / dt )  # size of solution array
array = (ct.c_double * knum)()  # define array to save solution

# set C argument and result types
clibrary.SHM_FDfor.argtypes = [ct.POINTER(ct.c_double), ct.c_double, ct.c_int]
clibrary.SHM_FDfor.restype = ct.POINTER(ct.c_double)

# call the C function
sol = clibrary.SHM_FDfor(array, dt, knum)

# save Ctypes array into a numpy array for further processing
Cx = np.zeros(len(t))
for i in range(knum):
    Cx[i] = sol[i]
#    print(Cx[i])
fdC_end = time()

print( "\nFD Ctypes forward solver elapsed time: ", fdC_end-fdC_start)
#print( "FD Ctypes Solution")
#for i in range(knum):
#    print(sol[i])


###--- Analytical Solution ---###
an_start = time()

# initialize 'an_sol' analytical solution vector
an_sol=np.zeros(len(t))

# populate analytical solution vector
an_sol=np.cos(t)

an_end = time()
print( "\nanalytical solution time: ", an_end-an_start)
#print( "Analytical Solution")
#for i in range(knum):
#    print(an_sol[i])


## Error ##
error  = np.zeros(len(t))
error_FD  = np.zeros(len(t))
error_FDC = np.zeros(len(t))
error_FD  = np.abs(an_sol - x )      # error between FD and analytical soln
error_FDC = np.abs(an_sol - Cx )     # error between Ctypes FD and analytical soln
error     = np.abs(x - Cx )          # error between Ctypes and Python FD solutions
print("\nError between forward solver and analytical soln: ", np.sum(error_FD) )
print("\nError between Ctypes forward solver and analytical soln: ", np.sum(error_FDC) )
print("\nError between Ctypes and Python forward solvers: ", np.sum(error) )



## Plotting ##
plot_start = time()
plt.plot(t,x,'*' , label = 'Finite Difference')
plt.plot(t,an_sol, label = 'Analytical Solution')
plt.plot(t,Cx    , label = 'Ctypes Finite Difference')
plt.xlabel('t')
plt.ylabel('x')
plt.title('x(t) For a Simple Spring')
plt.legend()
plt.savefig('shm_analysis.png')

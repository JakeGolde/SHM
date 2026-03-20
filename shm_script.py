#! /bin/python3
import numpy as np
from time import time
import matplotlib.pyplot as plt

start = time()

#set up t grid
# delta_t = h (finite difference)
h = 0.1
t0 = 0
tf = 10
t=np.arange(t0,tf,h)

# x(t) will be saved in x below
x=np.zeros(len(t))


## Finite Diference Forward Solver

#set initial conditions
x[0] = 1
x[1] = 1
for i in range(1,len(t)-1):
    x[i+1] = ( 2 - h**2)*x[i]-x[i-1]
    #print(x[i])


sim_end = time()

print( "FD forward solver elapsed time: ", sim_end-start)

## Analytical Solution ##
an_start = time()

# initialize 'an_sol' analytical solution vector
an_sol=np.zeros(len(t))
# populate analytical solution vector
an_sol=np.cos(t)
an_end = time()
print( "\nanalytical solution time: ", an_end-an_start)


## Finite Difference Matrix Solution ##
mat_start = time()
def create_tridiagonal(n, a, b, c):
    matrix = np.zeros((n,n))
    np.fill_diagonal(matrix, a)
    np.fill_diagonal(matrix[1:,:-1], b)
    np.fill_diagonal(matrix[2:,:-2], c)
    return matrix

#define relevant parameters to construct tridiagonal matrix
n=len(t)
a = -1    #diagonal terms
b = 2-h**2         # terms to the left (-1) of the diagonal
c = -1        # terms to the left (-2) of the diagonal

A = create_tridiagonal(n, a, b, c) #create tridiagonal matrix


#include initial 'velocity' condition x'(0) = 0, through x' difference eq -> x(1)=1
A[0,0] = 1
A[1,1] = 1
A[1,0] = 0

# now solve the matrix equation A*w = vec
# where A is our tridiagonal matrix, w is the vector of solutions w_i
# and vec is the vector (mostly zeros, vec[0]=1, vec[pi/h]=-(2+h^2))

vec = np.zeros(len(t))

# incorporate 'boundardy' conditions
vec[0] = 1     # initial condition
vec[1] = 1     # initial 'velocity' condition
#print(vec)
# use matrix inversion to solve for w
# w = A-1*vec
w = np.linalg.solve(A,vec)

mat_end = time()
print( "\nFD matrix elapse time: ", mat_end-mat_start)

## Error ##
errorVec = np.zeros(len(t))
error_FD = np.zeros(len(t))
errorVec = np.abs(an_sol - x )
error_FD = np.abs(x-w)
print("\nError between forward solver and analytical soln: ", np.sum(errorVec) )
print("\nError between methods: ", np.sum(error_FD))


## Plotting ##
plot_start = time()
plt.plot(t,x,'*',      label='Finite Difference')
plt.plot(t,an_sol,'*', label='Analytical Solution')
plt.plot(t, w,         label = 'Vectorized Finite Diference')
plt.xlabel('t')
plt.ylabel('x')
plt.title('x(t) For a Simple Spring')
plt.legend()
plt.savefig('shm.png')

plot_end = time()
#print( "plot time: ", plot_end-plot_start)
#print(A)

#! /bin/python3
import numpy as np

def SHM_FDfor(h):
    #set up the grid
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

    return x

def SHM_an( h ):
    #set up the grid
    t0 = 0
    tf = 10
    t=np.arange(t0,tf,h)

    # x(t) will be saved in x below
    x=np.zeros(len(t))

    ## Analytical Solution ##
    x=np.cos(t)
    return x

def create_tridiagonal(n, a, b, c):
    matrix = np.zeros((n,n))
    np.fill_diagonal(matrix, a)
    np.fill_diagonal(matrix[1:,:-1], b)
    np.fill_diagonal(matrix[2:,:-2], c)
    return matrix

def SHM_FDmat( h ):
    #set up the grid
    t0 = 0
    tf = 10
    t=np.arange(t0,tf,h)

    # x(t) will be saved in x below
    x=np.zeros(len(t))

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

    # now solve the matrix equation A*x = vec
    # where A is our tridiagonal matrix, x is the vector of solutions w_i
    # and vec is the vector (mostly zeros, vec[0]=1, vec[pi/h]=-(2+h^2))

    vec = np.zeros(len(t))

    # incorporate 'boundardy' conditions
    vec[0] = 1     # initial condition
    vec[1] = 1     # initial 'velocity' condition
    # use matrix inversion to solve for x
    # x = A-1*vec
    x = np.linalg.solve(A,vec)
    return x

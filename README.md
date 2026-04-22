## SHM
Finite Difference Simple Harmonic Motion Solver

This repo contains files for solving a simple harmonic oscillator [with k=1, m=1] using two Finite Difference inspired techniques:

1) A 'forward solver'
	The initial conditions [x(0) = 1, v(0) = 0] are converted to 'boundary' conditions [x(0) = 1, x(1) = 1] through applying the discrete first derivative [difference equation: x(n+h) -x(n) / h ] to the initial conditions.
	A  central finite difference equation [x(t+h) = (2-h^2^)*x(t) -x(t-h)] is then applied to each grid point sequentially
2) A matrix solution, implementing the central finite difference method based on the more standard method of solving FD problems
	The boundary conditions are the same as approach 1) above  
  
**Files:**  
Python functions are saved in: *shm.py*  
A script comparing the two approaches described above with the analytical solution is found at: *shm_script.py*  
Performance at different grid resolutions is analyzed in: *shm_perf.py*

# Comparison with C
The 'forward solver' is implemented in C (*shm.c*) and compiled in a shared library (*shm.so* - working in Debian 13 )  
  
The C forward solver (implemented using Ctypes) is compared with the Python based forward solver in: *shm_dt_analysis.py*  
  
*shm_time_analysis.png* contained in */figures* shows the computation time improvements between the techniques as the number of grid points is increased


# SHM
Finite Difference Simple Harmonic Motion Solver

This repo contains files for solving a simple harmonic oscillator [with k=1, m=1] using two Finite Difference inspired techniques:

1) A 'forward solver'
	The initial conditions [x(0) = 1, v(0) = 0] are converted to 'boundary' conditions [x(0) = 1, x(1) = 1] through applying the discrete first derivative [difference equation: x(n+h) -x(n) / h ] to the initial conditions.
	A  central finite difference equation [x(t+h) = (2-h^2)x(t) -x(t-h)] is then applied to each grid point sequentially
2) A matrix solution, implementing the central finite difference method based on the more standard method of solving FD problems
	The boundary conditions are the same as approach 1) above

Functions are saved in: shm.py
A script for a simple system is contined in: shm_script.py
Elapsed time for each approach is characterized in shm_perf.py

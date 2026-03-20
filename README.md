# SHM
Finite Difference Simple Harmonic Motion Solver

This repo contains files for solving a simple harmonic oscillator [with k=1, m=1] using a Finite Difference technique. The initial conditions [x(0) = 1, v(0) = 0] are converted to 'boundary' conditions [x(0) = 1, x(1) = 1] through applying the discrete first derivative [difference equation: x(n+h) -x(n) / h ] to the initial conditions. The solution is calculated two using two approaches: 1) A 'forward solver' applying the central finite difference equation [x(t+h) = (2-h^2)x(t) -x(t-h)] to each grid point sequentially; 2) A matrix solution, based on the more standard method of solving FD problems

Functions are saved in: shm.py
A script for a simple system is contined in: shm_script.py
Performance for each approach is characterized in shm_perf.py

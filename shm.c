
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// This function uses pass by refference to populate an uninitialized array>
void grid_construct(double grid[], double step_size, int knum )  {
  grid[0] = (double)0;
  grid[1] = (double)step_size;
  for( int i = 1;  i < knum - 1; i++ ) {  //fill in grid from index 2 to fin>
   grid[i+1] = grid[i] + (double)step_size;
  }
}

// This function uses pass by refference to calculate the FD forward solver solution
double* SHM_FDfor( double soln[], double step_size, int knum )  {
  soln[0] = (double)1;   // Initial condition
  soln[1] = (double)1;   // Initial condition
  for( int i = 1; i < knum - 1; i++)  {
   soln[i+1] = (2 - step_size*step_size)*soln[i] - soln[i-1];
  }
  return soln;
}


int main( void )  {

 // define simulation parameters (move this to an init file later on)
 int t0 =      0;              // start time
 int tf =      1;              // end time
 double dt = 0.1;              // delta time
 int tnum = (tf - t0) / dt;    // number of time points
 double time_grid[tnum];       // initialize timegrid
 double soln[tnum];            // initialize solution grid

 // populate grid using parameters defined above
 grid_construct(time_grid,dt,tnum);
 // calculate soln using parameters defined above
 double* test =  SHM_FDfor(soln,dt,tnum);
 printf("third value of solution = %lf\n", *(test+2));
// grid_construct(time_grid,dt,tnum);
 for( int i = 0; i < tnum; i++)  {
  printf( "time_grid[%d]: %lf\n",i, time_grid[i]);
  printf("      soln[%d]: %lf\n",i, soln[i]);
  }
}


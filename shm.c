#include<stdio.h>
#include<stdlib.h>
#include<time.h>

/* Function to construct a time grid, with initial time point t0
   final time point = tf, and delta t = h */

double* grid_construct(int t0, int tf,  double h )  {
 // Calculate number of time values (a constant)
 const int kt_num = (tf - t0) / h ;
 // Allocate memory for the array of time values
 double* time_grid = (double*)malloc(kt_num * sizeof(double));
 // Check if memory allocation was successful
 if (time_grid == NULL) {
    printf("Memory allocation failed!\n");
    exit(1); // Exit the program if allocation fails
   }
 // Construct the Array of Time Values
 time_grid[0] = (double)t0;  // set initial value
 for( int i = 1; i < kt_num + 1; i++)  {
  time_grid[i] = time_grid[i-1] + h;
 }

 // Return the pointer to the allocated array
 return time_grid;
}

/* Finite Difference Forward Solver for Simple Harmonic Motion
   w/ m=, h=0 */

double* SHM_FDfor( int t_num, double h )  {
 // Allocate memory for the solution array [x(t)]
 double* x = (double*)malloc(t_num * sizeof(double));
 // Check if memory allocation was successful
 if (x == NULL) {
    printf("Memory allocation failed!\n");
    exit(1); // Exit the program if allocation fails
   }
 // Cacluate Solution array
 x[0] = (double)1;   // Initial condition
 x[1] = (double)1;   // Initial condition
 for( int i = 1; i < t_num; i++)  {
  x[i+1] = (2 - h*h)*x[i] - x[i-1];
 }
 return x;
}



int main( void )  {
 clock_t start = clock();
 // Define the grid constructor input parameters
 int    t0 = 0;
 int    tf = 10;
 double h  = 0.0001;
 int t_num = (tf - t0) / h; // we have to redefine here to print

 /* Call the grid constructor function to create the time
    grid and store the returned pointer */
 double* times = grid_construct( t0, tf, h);

 /* Call the solution function to create the solution array
    and return pointer */
 double* x = SHM_FDfor( t_num, h );

 clock_t end = clock();
 double elapsedT = (double)(end - start) / CLOCKS_PER_SEC;
 // Print the elements of the time array
 printf("Time Values: ");
 for (int i = 0; i < t_num + 1 ; i++) {

  printf("%lf ", times[i]);
 }
 printf("\n\n");

 // Print the elements of the solution array
 printf("X(t) Values: ");
 for (int i = 0; i < t_num + 1 ; i++) {

  printf("%lf ", x[i]);
 }
 printf("\n\n\n");

 // Print Elapsed Time
 printf("Time elapsed = %f\n", elapsedT);

 // Free the allocated memory to avoid memory leaks
 free(times);
 free(x);

 return 0;
}

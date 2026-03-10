#include <stdio.h>
#include <omp.h>
#include <unistd.h>

int main() {
    int N = 20;

    // Choose static or dynamic scheduling
    #pragma omp parallel for schedule(dynamic)
    for (int i = 0; i < N; i++) {
        sleep(1); // simulate variable workload

        #pragma omp critical
        {
            printf("Iteration %d is being processed by thread %d.\n",
                   i, omp_get_thread_num());
        }
    }

    return 0;
}

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ gcc -fopenmp -O3 -o task2 Task2_parallel_loop.c

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ OMP_NUM_THREADS=5

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 3 is being processed by thread 0.
// Iteration 16 is being processed by thread 4.
// Iteration 17 is being processed by thread 4.
// Iteration 18 is being processed by thread 4.
// Iteration 19 is being processed by thread 4.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 6 is being processed by thread 1.
// Iteration 7 is being processed by thread 1.
// Iteration 12 is being processed by thread 3.
// Iteration 13 is being processed by thread 3.
// Iteration 14 is being processed by thread 3.
// Iteration 15 is being processed by thread 3.
// Iteration 8 is being processed by thread 2.
// Iteration 9 is being processed by thread 2.
// Iteration 10 is being processed by thread 2.
// Iteration 11 is being processed by thread 2.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ OMP_NUM_THREADS=7

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 6 is being processed by thread 2.
// Iteration 7 is being processed by thread 2.
// Iteration 8 is being processed by thread 2.
// Iteration 9 is being processed by thread 3.
// Iteration 10 is being processed by thread 3.
// Iteration 11 is being processed by thread 3.
// Iteration 18 is being processed by thread 6.
// Iteration 19 is being processed by thread 6.
// Iteration 15 is being processed by thread 5.
// Iteration 16 is being processed by thread 5.
// Iteration 17 is being processed by thread 5.
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 3 is being processed by thread 1.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 12 is being processed by thread 4.
// Iteration 13 is being processed by thread 4.
// Iteration 14 is being processed by thread 4.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 6 is being processed by thread 2.
// Iteration 7 is being processed by thread 2.
// Iteration 8 is being processed by thread 2.
// Iteration 12 is being processed by thread 4.
// Iteration 13 is being processed by thread 4.
// Iteration 14 is being processed by thread 4.
// Iteration 18 is being processed by thread 6.
// Iteration 19 is being processed by thread 6.
// Iteration 15 is being processed by thread 5.
// Iteration 16 is being processed by thread 5.
// Iteration 17 is being processed by thread 5.
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 3 is being processed by thread 1.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 9 is being processed by thread 3.
// Iteration 10 is being processed by thread 3.
// Iteration 11 is being processed by thread 3.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 6 is being processed by thread 2.
// Iteration 7 is being processed by thread 2.
// Iteration 8 is being processed by thread 2.
// Iteration 3 is being processed by thread 1.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 18 is being processed by thread 6.
// Iteration 19 is being processed by thread 6.
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 15 is being processed by thread 5.
// Iteration 16 is being processed by thread 5.
// Iteration 17 is being processed by thread 5.
// Iteration 12 is being processed by thread 4.
// Iteration 13 is being processed by thread 4.
// Iteration 14 is being processed by thread 4.
// Iteration 9 is being processed by thread 3.
// Iteration 10 is being processed by thread 3.
// Iteration 11 is being processed by thread 3.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 18 is being processed by thread 6.
// Iteration 19 is being processed by thread 6.
// Iteration 12 is being processed by thread 4.
// Iteration 13 is being processed by thread 4.
// Iteration 14 is being processed by thread 4.
// Iteration 9 is being processed by thread 3.
// Iteration 10 is being processed by thread 3.
// Iteration 11 is being processed by thread 3.
// Iteration 15 is being processed by thread 5.
// Iteration 16 is being processed by thread 5.
// Iteration 17 is being processed by thread 5.
// Iteration 3 is being processed by thread 1.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 6 is being processed by thread 2.
// Iteration 7 is being processed by thread 2.
// Iteration 8 is being processed by thread 2.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 3 is being processed by thread 1.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 15 is being processed by thread 5.
// Iteration 16 is being processed by thread 5.
// Iteration 17 is being processed by thread 5.
// Iteration 6 is being processed by thread 2.
// Iteration 7 is being processed by thread 2.
// Iteration 8 is being processed by thread 2.
// Iteration 12 is being processed by thread 4.
// Iteration 13 is being processed by thread 4.
// Iteration 14 is being processed by thread 4.
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 18 is being processed by thread 6.
// Iteration 19 is being processed by thread 6.
// Iteration 9 is being processed by thread 3.
// Iteration 10 is being processed by thread 3.
// Iteration 11 is being processed by thread 3.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 18 is being processed by thread 6.
// Iteration 19 is being processed by thread 6.
// Iteration 3 is being processed by thread 1.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 12 is being processed by thread 4.
// Iteration 13 is being processed by thread 4.
// Iteration 14 is being processed by thread 4.
// Iteration 15 is being processed by thread 5.
// Iteration 16 is being processed by thread 5.
// Iteration 17 is being processed by thread 5.
// Iteration 9 is being processed by thread 3.
// Iteration 10 is being processed by thread 3.
// Iteration 11 is being processed by thread 3.
// Iteration 6 is being processed by thread 2.
// Iteration 7 is being processed by thread 2.
// Iteration 8 is being processed by thread 2.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task2
// Iteration 0 is being processed by thread 0.
// Iteration 1 is being processed by thread 0.
// Iteration 2 is being processed by thread 0.
// Iteration 18 is being processed by thread 6.
// Iteration 19 is being processed by thread 6.
// Iteration 9 is being processed by thread 3.
// Iteration 10 is being processed by thread 3.
// Iteration 11 is being processed by thread 3.
// Iteration 12 is being processed by thread 4.
// Iteration 13 is being processed by thread 4.
// Iteration 14 is being processed by thread 4.
// Iteration 15 is being processed by thread 5.
// Iteration 16 is being processed by thread 5.
// Iteration 17 is being processed by thread 5.
// Iteration 3 is being processed by thread 1.
// Iteration 4 is being processed by thread 1.
// Iteration 5 is being processed by thread 1.
// Iteration 6 is being processed by thread 2.
// Iteration 7 is being processed by thread 2.
// Iteration 8 is being processed by thread 2.

// 1. What do you notice about the output?
// Different threads process different iterations. The order of printed lines is not sequential.

// 2. Is the output the same every time?
// No, the order changes each run because threads execute concurrently and the OS schedules them nondeterministically.

// 3. How could the output be made "ordered"?
// Wrap the printf in a #pragma omp critical block to avoid interleaving, or store results in an array and print them after the loop.
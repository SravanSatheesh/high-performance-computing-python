#include <stdio.h>
#include <omp.h>

int main() {


    

    #pragma omp parallel
    {
        int thread_id = omp_get_thread_num();
        int total_threads = omp_get_num_threads();

        printf("Hello from thread %d of a total of %d threads.\n",
               thread_id, total_threads);
    }

    return 0;
}


// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ gcc -fopenmp -O3 -o task1 task1_openmp_threads.c

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task1
// Hello from thread 2 of a total of 8 threads.
// Hello from thread 0 of a total of 8 threads.
// Hello from thread 4 of a total of 8 threads.
// Hello from thread 5 of a total of 8 threads.
// Hello from thread 3 of a total of 8 threads.
// Hello from thread 6 of a total of 8 threads.
// Hello from thread 1 of a total of 8 threads.
// Hello from thread 7 of a total of 8 threads.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task1
// Hello from thread 3 of a total of 8 threads.
// Hello from thread 6 of a total of 8 threads.
// Hello from thread 1 of a total of 8 threads.
// Hello from thread 4 of a total of 8 threads.
// Hello from thread 5 of a total of 8 threads.
// Hello from thread 2 of a total of 8 threads.
// Hello from thread 0 of a total of 8 threads.
// Hello from thread 7 of a total of 8 threads.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task1
// Hello from thread 3 of a total of 8 threads.
// Hello from thread 5 of a total of 8 threads.
// Hello from thread 4 of a total of 8 threads.
// Hello from thread 0 of a total of 8 threads.
// Hello from thread 6 of a total of 8 threads.
// Hello from thread 1 of a total of 8 threads.
// Hello from thread 2 of a total of 8 threads.
// Hello from thread 7 of a total of 8 threads.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task1
// Hello from thread 4 of a total of 8 threads.
// Hello from thread 0 of a total of 8 threads.
// Hello from thread 3 of a total of 8 threads.
// Hello from thread 6 of a total of 8 threads.
// Hello from thread 5 of a total of 8 threads.
// Hello from thread 2 of a total of 8 threads.
// Hello from thread 1 of a total of 8 threads.
// Hello from thread 7 of a total of 8 threads.

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ OMP_NUM_THREADS=99

// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ ./task1
// Hello from thread 1 of a total of 99 threads.
// Hello from thread 75 of a total of 99 threads.
// Hello from thread 39 of a total of 99 threads.
// Hello from thread 78 of a total of 99 threads.
// Hello from thread 43 of a total of 99 threads.
// Hello from thread 46 of a total of 99 threads.
// Hello from thread 87 of a total of 99 threads.
// Hello from thread 47 of a total of 99 threads.
// Hello from thread 90 of a total of 99 threads.
// Hello from thread 92 of a total of 99 threads.
// Hello from thread 0 of a total of 99 threads.
// Hello from thread 50 of a total of 99 threads.
// Hello from thread 57 of a total of 99 threads.
// Hello from thread 91 of a total of 99 threads.
// Hello from thread 56 of a total of 99 threads.
// Hello from thread 29 of a total of 99 threads.
// Hello from thread 83 of a total of 99 threads.
// Hello from thread 60 of a total of 99 threads.
// Hello from thread 64 of a total of 99 threads.
// Hello from thread 61 of a total of 99 threads.
// Hello from thread 65 of a total of 99 threads.
// Hello from thread 68 of a total of 99 threads.
// Hello from thread 51 of a total of 99 threads.
// Hello from thread 72 of a total of 99 threads.
// Hello from thread 94 of a total of 99 threads.
// Hello from thread 37 of a total of 99 threads.
// Hello from thread 30 of a total of 99 threads.
// Hello from thread 4 of a total of 99 threads.
// Hello from thread 5 of a total of 99 threads.
// Hello from thread 27 of a total of 99 threads.
// Hello from thread 93 of a total of 99 threads.
// Hello from thread 12 of a total of 99 threads.
// Hello from thread 14 of a total of 99 threads.
// Hello from thread 9 of a total of 99 threads.
// Hello from thread 18 of a total of 99 threads.
// Hello from thread 17 of a total of 99 threads.
// Hello from thread 13 of a total of 99 threads.
// Hello from thread 7 of a total of 99 threads.
// Hello from thread 16 of a total of 99 threads.
// Hello from thread 95 of a total of 99 threads.
// Hello from thread 20 of a total of 99 threads.
// Hello from thread 10 of a total of 99 threads.
// Hello from thread 33 of a total of 99 threads.
// Hello from thread 3 of a total of 99 threads.
// Hello from thread 21 of a total of 99 threads.
// Hello from thread 2 of a total of 99 threads.
// Hello from thread 8 of a total of 99 threads.
// Hello from thread 19 of a total of 99 threads.
// Hello from thread 24 of a total of 99 threads.
// Hello from thread 49 of a total of 99 threads.
// Hello from thread 31 of a total of 99 threads.
// Hello from thread 6 of a total of 99 threads.
// Hello from thread 53 of a total of 99 threads.
// Hello from thread 59 of a total of 99 threads.
// Hello from thread 26 of a total of 99 threads.
// Hello from thread 28 of a total of 99 threads.
// Hello from thread 32 of a total of 99 threads.
// Hello from thread 23 of a total of 99 threads.
// Hello from thread 22 of a total of 99 threads.
// Hello from thread 69 of a total of 99 threads.
// Hello from thread 36 of a total of 99 threads.
// Hello from thread 11 of a total of 99 threads.
// Hello from thread 71 of a total of 99 threads.
// Hello from thread 73 of a total of 99 threads.
// Hello from thread 97 of a total of 99 threads.
// Hello from thread 70 of a total of 99 threads.
// Hello from thread 35 of a total of 99 threads.
// Hello from thread 40 of a total of 99 threads.
// Hello from thread 44 of a total of 99 threads.
// Hello from thread 67 of a total of 99 threads.
// Hello from thread 66 of a total of 99 threads.
// Hello from thread 85 of a total of 99 threads.
// Hello from thread 76 of a total of 99 threads.
// Hello from thread 63 of a total of 99 threads.
// Hello from thread 62 of a total of 99 threads.
// Hello from thread 45 of a total of 99 threads.
// Hello from thread 48 of a total of 99 threads.
// Hello from thread 15 of a total of 99 threads.
// Hello from thread 58 of a total of 99 threads.
// Hello from thread 89 of a total of 99 threads.
// Hello from thread 55 of a total of 99 threads.
// Hello from thread 54 of a total of 99 threads.
// Hello from thread 52 of a total of 99 threads.
// Hello from thread 96 of a total of 99 threads.
// Hello from thread 86 of a total of 99 threads.
// Hello from thread 82 of a total of 99 threads.
// Hello from thread 25 of a total of 99 threads.
// Hello from thread 88 of a total of 99 threads.
// Hello from thread 42 of a total of 99 threads.
// Hello from thread 84 of a total of 99 threads.
// Hello from thread 34 of a total of 99 threads.
// Hello from thread 81 of a total of 99 threads.
// Hello from thread 38 of a total of 99 threads.
// Hello from thread 80 of a total of 99 threads.
// Hello from thread 41 of a total of 99 threads.
// Hello from thread 79 of a total of 99 threads.
// Hello from thread 77 of a total of 99 threads.
// Hello from thread 74 of a total of 99 threads.
// Hello from thread 98 of a total of 99 threads.


// The order changes because threads run concurrently and the operating system schedules them independently, so each thread may reach the `printf` at different times.

// 1. What happens when you create 1,000 threads?

// Creating 1,000 threads usually slows the program down or may fail, because the system has limited CPU cores and each thread adds overhead for scheduling and memory.

// 2. Why is the order of the outputs not fixed?

// The order is not fixed because threads run concurrently and the operating system schedules them independently, so each thread may reach the printf at different times.

// 3. What would happen if two threads used printf at the same time?

// The output could interleave or mix together, causing garbled text, because printf is not atomic unless protected by a #pragma omp critical block.
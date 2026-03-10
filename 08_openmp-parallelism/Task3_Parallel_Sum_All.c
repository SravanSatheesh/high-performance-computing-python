#include <stdio.h>
#include <omp.h>

int main() {
    long long N = 100000000;   // 100 million
    long long sum_no_reduction = 0;
    long long sum_reduction = 0;
    long long sum_critical = 0;

    long long correct = N * (N + 1) / 2;
    double start, end;

    printf("Correct sum = %lld\n\n", correct);

    // -----------------------------
    // 1. Without reduction (race condition)
    // -----------------------------
    start = omp_get_wtime();
    #pragma omp parallel for
    for (long long i = 1; i <= N; i++) {
        sum_no_reduction += i;  // shared variable without protection
    }
    end = omp_get_wtime();
    printf("Sum without reduction: %lld\n", sum_no_reduction);
    printf("Time (no reduction): %f seconds\n\n", end - start);

    // -----------------------------
    // 2. With reduction
    // -----------------------------
    start = omp_get_wtime();
    #pragma omp parallel for reduction(+:sum_reduction)
    for (long long i = 1; i <= N; i++) {
        sum_reduction += i;
    }
    end = omp_get_wtime();
    printf("Sum with reduction: %lld\n", sum_reduction);
    printf("Time (reduction): %f seconds\n\n", end - start);

    // -----------------------------
    // 3. With critical
    // -----------------------------
    start = omp_get_wtime();
    #pragma omp parallel for
    for (long long i = 1; i <= N; i++) {
        #pragma omp critical
        sum_critical += i;
    }
    end = omp_get_wtime();
    printf("Sum with critical: %lld\n", sum_critical);
    printf("Time (critical): %f seconds\n", end - start);

    return 0;
}



// Comprehension Questions

// 1. Why does variant a (no reduction) not work reliably?
// Because multiple threads try to update the shared variable simultaneously, causing race conditions and incorrect results.

// 2. How does reduction ensure correct results?
// Each thread keeps a private copy of the sum and OpenMP combines them at the end safely, preventing race conditions.

// Additional Questions

// 1. Why is reduction faster than critical?
// Reduction allows threads to accumulate locally and combine only once, while critical forces every iteration to wait for access, which slows execution.

// 2. When is the critical version still useful?
// When threads need to perform complex operations on shared data that cannot be expressed as a simple reduction (e.g., updating arrays, data structures, or performing conditional updates)

// ###MSYS2_OUT###
// srava@SravanSatheesh MINGW64 /S/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8
// $ gcc -fopenmp -O3 -o task3 Task3_Parallel_Sum_All.c
// export OMP_NUM_THREADS=4   # change number of threads
// ./task3
// Correct sum = 5000000050000000

// Sum without reduction: 2187500012500000
// Time (no reduction): 0.010000 seconds

// Sum with reduction: 5000000050000000
// Time (reduction): 0.009000 seconds

// Sum with critical: 5000000050000000
// Time (critical): 1.983000 seconds



// ###python_out###
// PS S:\Studies and Docs\TU Dortmund\SEMESTER 3\python lab\Day8> & C:\Users\srava\AppData\Local\Programs\Python\Python314\python.exe "s:/Studies and Docs/TU Dortmund/SEMESTER 3/python lab/Day8/task3.py"
// Python sum: 5000000050000000
// Time: 1.547478437423706 seconds
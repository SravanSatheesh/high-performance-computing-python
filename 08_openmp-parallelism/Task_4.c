#include <omp.h>

// Use long long to avoid integer overflow
long long sum_parallel(int N) {
    long long sum = 0;

    #pragma omp parallel for reduction(+:sum)
    for (int i = 1; i <= N; i++) {
        sum += i;
    }

    return sum;
}
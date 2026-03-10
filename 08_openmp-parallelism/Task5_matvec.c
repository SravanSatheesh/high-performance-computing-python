#include <omp.h>

// Matrix-vector multiplication: y = A * x
void matvec_parallel(double* A, double* x, double* y, int N) {
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        double sum = 0.0;
        for (int j = 0; j < N; j++) {
            sum += A[i * N + j] * x[j];  // Row-major order
        }
        y[i] = sum;
    }
}
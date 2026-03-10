#include <omp.h>
#include <stddef.h>

// -----------------------------
// 1. Incorrect version (no synchronization)
// -----------------------------
void compute_histogram_incorrect(unsigned char* data, int* histogram, int size) {
    #pragma omp parallel for
    for (int i = 0; i < size; i++) {
        unsigned char value = data[i];
        histogram[value]++;  // race condition occurs
    }
}

// -----------------------------
// 2. Atomic version (correct)
// -----------------------------
void compute_histogram_atomic(unsigned char* data, int* histogram, int size) {
    #pragma omp parallel for
    for (int i = 0; i < size; i++) {
        unsigned char value = data[i];
        #pragma omp atomic
        histogram[value]++;
    }
}

// -----------------------------
// 3. Reduction version (correct, faster)
// -----------------------------
void compute_histogram_reduction(unsigned char* data, int* histogram, int size) {
    #pragma omp parallel
    {
        int local_hist[256] = {0};  // local histogram per thread

        #pragma omp for
        for (int i = 0; i < size; i++) {
            unsigned char value = data[i];
            local_hist[value]++;
        }

        #pragma omp critical
        for (int j = 0; j < 256; j++) {
            histogram[j] += local_hist[j];
        }
    }
}
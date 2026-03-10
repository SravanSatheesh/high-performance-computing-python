#include <stdio.h>
#include <omp.h>
#include <unistd.h>

int main() {
    int i;
    int N = 10;

    #pragma omp parallel for
    for (i = 0; i < N; i++) {
        sleep(1);
        printf("Iteration %d von Thread %d\n", i, omp_get_thread_num());
    }

    return 0;
}
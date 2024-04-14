#include <stdio.h>
#include <stdlib.h>

void matrix_matrix_product(float *A, float *B, float *C, int n)
{
    for (int i = 0; i < n; i++){
        float sum = 0.0f;
        for (int j = 0; j < n; j++) {
            sum += A[i * n + j] * v_in[j];
        }
        v_out[i] = sum;
    }
}
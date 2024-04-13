#include <stdio.h>

__global__ void hello_cuda() {
    printf("hello Cuda \n");
    printf("blockIdx.x: %d, blockIdx.y: %d, threadidx.x: %d, threadIdx.y: %d, threadidx.z: %d\n",
    blockIdx.x, blockIdx.y, threadIdx.x, threadIdx.y, threadIdx.z);

}

int main(int argc, char **argv) {
    hello_cuda<<<3, 4>>>();
    cudaDeviceSynchronize();
    return 0;
}
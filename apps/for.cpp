#include <iostream>
#include <time.h>


int main(){
    int x, y;

    clock_t start = clock(); // 計測開始

    for(int i = 0; i < 100000; i++){
        for(int j = 0; j < 100000; j++){
            x*y;
        }
    }

    clock_t end = clock(); // 計測終了

    double time = (double)(end - start) / CLOCKS_PER_SEC*1000;
    printf("%.2f ms\n", time);


    return 0;
}
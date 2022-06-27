// 행렬 전치 프로그램 #1

#include <stdio.h>
#define ROWS 3
#define COLS 3

// 행렬 전치 함수
void matrix_transpose(int A[ROWS][COLS], int B[ROWS][COLS]) {
    for (int r = 0; r < ROWS; r++)
        for (int c = 0; c < COLS; c++)
            B[c][r] = A[r][c];
}


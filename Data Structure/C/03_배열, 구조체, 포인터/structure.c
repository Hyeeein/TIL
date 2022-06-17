// 배열: 타입이 같은 데이터의 모임
// 구조체(structure): 타입이 다른 데이터를 묶는 방법

#include <stdio.h>

typedef struct studentTag {
    char name[10];  // 문자배열로 된 이름
    int age;        // 나이를 나타내는 정수값
    double gpa;     // 평균평점을 나타내는 실수값
} student;

int main(void) {
    student a = {'kim', 20, 4.3};
    student b = {'park', 21, 4.2};
    return 0;
}
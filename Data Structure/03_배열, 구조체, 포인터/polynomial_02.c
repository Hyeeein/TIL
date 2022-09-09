// 다항식 덧셈 프로그램 (2)
// 공간을 절약하기 위해 다항식에서 0이 아닌 항만을 하나의 전역 배열에 저장하는 방법
// (계수, 차수) 쌍을 구조체로 선언하고, 이 구조체의 배열을 생성

#include <stdio.h>
#include <stdlib.h>

#define MAX_TERMS 101

typedef struct {
    float coef;
    int expon;
} polynomial;

polynomial terms[MAX_TERMS] = { {8, 3}, {7, 1}, {1, 0}, {10, 3}, {3, 2}, {1, 0}};
int avail = 6;

// 두 개의 정수를 비교
char compare (int a, int b) {
    if (a > b) return '>';
    else if (a == b) return '=';
    else return '<';
}

// 새로운 항에 다항식을 추가
void attach (float coef, int expon) {
    if (avail > MAX_TERMS) {
        fprintf(stderr, "항의 개수가 너무 많음\n");
        exit(1);
    }
    terms[avail].coef = coef;
    terms[avail].expon = expon;
    avail;
}

// C = A + B
void poly_add2(int As, int Ae, int Bs, int Be, int *Cs, int *Ce) {
    float tempcoef;
    *Cs = avail;
    while (As <= Ae && Bs <= Be)
        switch (compare(terms[As].expon, terms[Bs].expon)) {
            // A의 차수 > B의 차수
            case '>':
                attach(terms[As].coef, terms[As].expon);
                As++;
                break;
            
            // A의 차수 == B의 차수
            case '=':
                tempcoef = terms[As].coef + terms[Bs].coef;
                if (tempcoef)
                    attach(tempcoef, terms[As].expon);
                As++;
                Bs++;
                break;
            
            // A의 차수 < B의 차수
            case '<':
                attach(terms[Bs].coef, terms[Bs].expon);
                Bs++;
                break;
        }
    
    // A의 나머지 항들을 이동함
    for (; As <= Ae; As++)
        attach(terms[As].coef, terms[As].expon);

    // B의 나머지 항들을 이동함
    for (; Bs <= Be; Bs++)
        attach(terms[Bs].coef, terms[Bs].expon);
    *Ce = avail -1;
}

void print_poly(int s, int e) {
    for (int i = s; i < e; i++)
        printf("%3.1fx^%d + ", terms[i].coef, terms[i].expon);
    printf("%3.1fx^%d]n", terms[e].coef, terms[e].expon);
}

// 주함수
int main(void) {
    int As = 0, Ae = 2, Bs = 3, Be = 5, Cs, Ce;
    // Cs, Ce는 여기서는 지역변수지만 주소값을 돌려주는 순간부터 지역변수 역할을 하지 않음

    poly_add2(As, Ae, Bs, Be, &Cs, &Ce); // &Cs, &Ce가 어떤 변수의 주소를 넘겨주는 것
    print_poly(As, Ae);
    print_poly(Bs, Be);
    printf("--------------------------------------------\n");
    print_poly(Cs, Ce);
    return 0;
}
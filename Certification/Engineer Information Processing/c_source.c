// 1번
#include <stdio.h>
void main () {
    int i, j;
    int temp;
    int a[5] = {75, 95, 75, 100, 50}

    for (i=0; i<4; i++) {
        for (j=0; j<4-i; j++) {
            if(a[j] > a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }

    for (i=0; i<5; i++) {
        printf("%d ", a[i])
    }
}

// 2번
#include <stdio.h>
void main() {
    int i=0, c=0;

    while (i<10) {
        i++;
        c *= i;
    }
    printf("%d", c);
}

// 3번
#include <stdio.h>
int r1() {
    return 4;
}
int r10() {
    return (30+r1());
}
int r10() {
    return (200+r10());
}
int main() {
    printf("%d\n", r100());
    return 0;
}

// 4번
#include <stdio.h>
void main() {
    char *p = "KOREA";
    print("%s\n", p);
    print("%s\n", p+3);
    print("%c\n", *p);
    print("%c\n", *(p+3));
    print("%c\n", *p+2);
}

// 5번
#include <stdio.h>
struct Soojebi {
    char name[10];
    int age;
};

void main() {
    struct Soojebi s[] = {"Kim", 28, "Lee", 38, "Seo", 50, "Park", 35};
    struct Soojebi *p;
    p = s;
    p++;
    printf("%s\n", p->name);
    printf("%d\n", p->age);
}

// 6번
#include <stdio.h>
void main() {
    int ary[3] = {1};
    int s = 0;
    int i = 0;

    ary[1] = *(ary+0)+2;
    ary[2] = *ary+3;

    for (i=0; i<3; i++) {
        s = s + ary[i];
    }

    printf("%d", s);
}

// 7번
#include <stdio.h>
int Soojebi(int base, int exp) {
    int i, result = 1;
    for (i=0; i<exp; i++)
        result *= base;
    return result;
}
void main() {
    printf("%d", Soojebi(2, 10));
}

// 8번
#include <stdio.h>
void main() {
    int *arr[3];
    int a = 12, b = 24, c = 36;
    arr[0] = &a;
    arr[1] = &b;
    arr[2] = &c;

    printf("%d\n", *arr[1] + **arr + 1);
}

// 9번
#include <stdio.h>
struct Soojebi {
    char name[20];
    int os, db, hab1, hab2;
};

void main() {
    struct Soojebi s[3] = {{"데이터1", 95, 88},
                           {"데이터2", 84, 91},
                           {"데이터3", 86, 75}};
    struct Soojebi *p;

    p = &s[0];
    (p+1)->hab1 = (p+1)->os+(p+2)->db;
    (p+1)->hab2 = (p+2)->hab1 + p->os + p->db;

    print("%d\n", (p+1)->hab1 + (p+1)->hab2);
}

// =============
// 10번
#include <stdio.h>
void main() {
    int a = 5;
    int s = 0;

    switch(a/2) {
        case 2 : s++;
        case 3 : a += s;
        default : a++;
    }

    printf("%d %d", s, a);
}

// 11번
#include <stdio.h>
void main() {
    int a = 3;
    int b = 7;

    switch(a%2) {
        case 3 : b += a;
    }
    
    print("%d %d", a, b);
}

// 12번
#include <stdio.h>
struct KEY {
    int a;
    int b;
};

void main() {
    struct KEY y;
    struct KEY *p;
    p = &y;
    y.a = 100;
    y.b = 200;
    printf("%d", p->a);
}

// 13번
#include <stdio.h>
void main() {
    int a = 2;
    int b = 5;
    int c = 3;

    b /= a;
    c %= a;

    print("%d %d", b, c);
}

// 14번
#include <stdio.h>
void main() {
    int x=1;
    int y=2;
    int m = x>y ? x:y;

    printf("%d", m);
}

// 15번
#include <stdio.h>
void main() {
    int a[5] = {2, 4, 1, 3, 0};
    int s = 0;

    printf("%d %d", a[a[4]], a[3]+a[1]);
}

// 16번
#include <stdio.h>
void main() {
    int a = 4;
    int r = 3 > 5? ++a : --a;

    print("%d", r);
}

// 17번
#include <stdio.h>
void main() {
    int i=3, j=4;

    printf("%d", 2 && 3);
    printf("%d", i<2 || j<3);
}

// 18번
#include <stdio.h>
void main() {
    int a = 5;
    int b = 7;

    printf("%d\n", a++ + ++b);
    printf("%d %d\n", ++a, ++b);
}

// 19번
#include <stdio.h>
int main() {
    int a = 3, b = 4, c = 2;
    int r1, r2, r3;

    r1 = b <= 4 || c == 2;
    r2 = (a > 0) && (b < 5);
    r3 = !c;

    printf("%d", r1+r2+r3);
    return 0;
}

// 20번
#include <stdio.h>
int fn(int n) {
    if (n <= 1)
        return 1;
    else
        return n*fn(n-1);
}
void main() {
    printf("%d", fn(4));
}

// 21번
#include <stdio.h>
int f(int i);

void main() {
    print("%d %d %d", f(1), f(5), f(-2));
}

int f(int i) {
    if (i<=2)
        return 1;
    else
        return f(i-1)+f(i-2);
}

// 22번
#include <stdio.h>
int fn(int n) {
    if (n <= 0)
        return 1;
    else
        printf("%d ", n);
    
    fn(n-1);
}

int main() {
    fn(5);
    return 0;
}

// 23번
#include <stdio.h>
int fn(int n) {
    if (n <= 0) return 0;
    return n + fn(n-1);
}

void main() {
    printf("%d", fn(12));
}

// 24번
#include <stdio.h>
int main(int argc, char *argv[]){
    int a[2][2] = {{11, 22}, {44, 55}};
    int i, sum = 0;
    int *p;
    p = a[0];
    for (i=1; i<4; i++)
        sum += *(p+i)
    printf("%d", sum);
    return 0;
}

// 25번
#include <stdio.h>
int main(int argc, char *argv[]) {
    char a;
    a = 'A' + 1;
    printf("%d", a);
    return 0;
}

// ========
// 26번
#include <stdio.h>
void main() {
    int a = 105;
    char c = 'Z';

    switch(a/10) {
        case 10 :
        case 9 : c = 'A'; break;
        case 8 : c = 'B'; break
        default : c = 'F';
    }

    printf("%c\n", c);
}

// 27번
#include <stdio.h>
void main() {
    int ret = 4;

    switch(++ret) {
        case 5 : ret+=2;
        case 3 : ret++; break;
        case 4 : ret++;
        default : ret*=2;
    }
    printf("%d\n", ret);
}

// 28번
#include <stdio.h>
void main() {
    int a[] = {1, 2, 3, 4};
    int b[] = {5, 6, 7, 8};
    int *pa[] = {a, b};
    print("%d", *(pa[1]+1));
}

// 29번
#include <stdio.h>
void main() {
    char *str = 'zjavb';
    int i;
    for (i=4; i>=0; i--)
        printf("%c", *(str+i));
}

// 30번
#include <stdio.h>
int num (int a, int b) {
    if (a > b) {
        return a;
    }
    else {
        return b;
    }
}
void main() {
    printf("%d", num(10, 20) + num(30, 20));
}

// 31번
#include <stdio.h>

// 32번
#include <stdio.h>

// 33번
#include <stdio.h>

// 34번
#include <stdio.h>

// 35번
#include <stdio.h>

// 36번
#include <stdio.h>

// 37번
#include <stdio.h>

## 에라토스테네스의 체 : 소수 찾기 알고리즘 / 프로그램

### 알고리즘
# Eratos(a[], n)
#     // 2부터 각 배수에 해당하는 수를 모두 0으로 바꿈
#     for (i = 2; i < n+1; i = i+1) do {
#         // 이미 지워진 수일 경우 건너뛰기
#         if (a[i] == 0) then continue;
#         // 이미 지워진 수가 아닐 경우 해당 숫자의 배수부터 모든 수 바꿈
#         for (j = 2*i; j < n; j = j+i) do {    
#             a[j] = 0;
#         }
#     }
    
#     // 남아 있는 모든 수 출력
#     for (int k = 0; k < n; k++) {
#         if (a[k] != 0) then print('%d', a[k]);
#     }
# end Eratos()

# # 이외의 답
# Eratos(a[], n)
#     a[1] <- 0

#     for (i<-2, i<= (n-1)/2, i<-i+1) {
#         if (a[i] != 0) then
#             for (j <- 2*i, j<n, j<-j+i)
#                 a[j]<-0;
#     }
# Eratos()

# -----------------------------------------------------------

### 프로그램 코딩

import math

n = 1000                              # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화


for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인

    # i가 소수인 경우 (남은 수인 경우) i를 제외한 i의 모든 배수를 지우기
    if array[i] == True: 
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
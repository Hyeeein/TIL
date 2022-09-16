# 쉘 정렬 (shell sort) : 

### 알고리즘 (ADL)
# shellSort(a[], n)
#     for (h <- 1; h < n; h <- 3*h + 1) do {};  // 첫 번째 h 값 계산
#     for ( ; h > 0; h <- h/3) do {             // h 값을 감소시키며 진행
#         for (i <- h + 1; i <= n; i <- i + 1) do {
#             v <- a[i];
#             j <- i;
#             while (j <- h and a[j-h] > v) do {
#                 a[j] <- a[j-h];
#                 j <- j-h;
#             }
#             A[j] <- v;
#         }
#     }
# end shellSort()


### 파이썬 프로그래밍

# 쉘 정렬 함수
def shellSort(a, n):
    h = 1
    while h < n:
        h = 3 * h + 1
    while h > 0:
        for i in range(h+1, n+1):
            v, j = a[i], i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j -= h
            a[j] = v
        h = int(h/3)
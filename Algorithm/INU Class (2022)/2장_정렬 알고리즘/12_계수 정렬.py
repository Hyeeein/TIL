### 계수 정렬 알고리즘
# countingSort(a[], n, m)
#     for (j <- 1; j <= m; j <- j + 1) do
#         count[j] <- 0;
#     for (i <- 1; i <= n; i <- i + 1) do
#         count[a[i]] <- count[a[i]] + 1;
#     for (j <- 2; j <= m; j <- j + 1) do
#         count[j] <- count[j-1] + count[j];
#     for (i <- N; i >= 1; i <- i + 1) do
#         b[count[a[i]]] <- a[i]
#         count[a[i]] <- count[a[i]] - 1;
#     }
#     for (i <- 1; i <= n; i <- i + 1) do
#         a[i] <- b[i]
# end countingSort()

### 계수 정렬 파이썬 프로그래밍

def countingSort(a, n, m):
    b = [0]*(n+1)
    count = [0] * (m+1)

    for j in range(1, m+1): count[j] = 0
    for i in range(1, n+1): count[a[i]] += 1
    for j in range(2, m+1): count[j] += count[j-1]
    for i in range(n, 0, -1):
        b[count[a[i]]] = a[i]
        count[a[i]] -= 1
    for i in range(1, n+1): a[i] = b[i]

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

import random, time
M = 1000
N = 100000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, M))
start_time = time.time()
countingSort(a, N, M)
end_time = time.time() - start_time
print('계수 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)



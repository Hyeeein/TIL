# 히프 정렬

### 히프 정렬 알고리즘
# heapSort(a[], n)
#     for (i <- n/2; i >= 1; i <- i-1) do
#         heapify(a, i, n)
#     for (i <- n-1; i >= 1; i <- i-1) do {
#         a[1]과 a[i+1]을 교환;
#         heapify(a, 1, i);
#     }
# end heapSort()

### 히프화 알고리즘
# heapify(a[], h, m)
#     v <- a[h];
#     for (j <- 2 * h; j <= m; j <- 2*j) do {
#         if (j < m and a[j] < a[j + 1]) then j <- j + 1;
#         if (v >= a[j]) then break;
#         else a[j/2] <- a[j];
#     }
#     a[j/2] <- v;
# end heapify();

# --------------------------------------------------------------------------------------

### 히프 정렬 프로그래밍

def heapSort(a, n):
    for i in range(int(n/2), 0, -1):
        heapify(a, i, n)
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a, 1, i)

def heapify(a, h, m):
    v, j = a[h], 2*h
    while j <= m:
        if (j < m and a[j] < a[j+1]):
            j = j+1
        if (v >= a[j]): break
        else: a[int(j/2)] = a[j]
        j *= 2
    a[int(j/2)] = v

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]): isSorted = False
        if (not isSorted): break
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')


import random, time

# N 값 10만부터 20만 단위로 5번 측정 (90만까지)
N = 100000
a = []; b = []; c = []
a.append(None); b.append(None); c.append(None)

# (1) 정렬된 배열
for i in range(N):
    a.append(i)

start_time = time.time()
heapSort(a, N)
end_time = time.time() - start_time

print('히프 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 역순 배열
for i in range(N, 0, -1):
    b.append(i)

start_time = time.time()
heapSort(b, N)
end_time = time.time() - start_time

print('히프 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 난수 배열
for i in range(N):
    c.append(random.randint(1, N))

start_time = time.time()
heapSort(c, N)
end_time = time.time() - start_time

print('히프 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(c, N)
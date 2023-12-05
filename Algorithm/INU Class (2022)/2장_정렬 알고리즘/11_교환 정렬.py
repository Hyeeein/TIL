### 교환 정렬 알고리즘
# exchangeSort(a[], n)
#     for (i <- 1; i < n; i <- i + 1) do
#         for (j <- i + 1; j <= n; j <- j + 1) do
#             if (a[i] < a[j]) then a[i]와 a[j]를 교환;
# end exchangeSort()

### 교환 정렬 파이썬 프로그래밍

def exchangeSort(arr, n):
    for i in range(1, n):
        for j in range(i+1, n+1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return 

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]): isSorted = False
        if (not isSorted): break
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')

import random, time

# N 값 5000부터 5천 단위로 4번 측정 (2만까지)
N = 20000
a = []; b = []; c = []
a.append(None); b.append(None); c.append(None)

# (1) 정렬된 배열
for i in range(N):
    a.append(i)

start_time = time.time()
exchangeSort(a, N)
end_time = time.time() - start_time

print('교환 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 역순 배열
for i in range(N, 0, -1):
    b.append(i)

start_time = time.time()
exchangeSort(b, N)
end_time = time.time() - start_time

print('교환 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 난수 배열
for i in range(N):
    c.append(random.randint(1, N))

start_time = time.time()
exchangeSort(c, N)
end_time = time.time() - start_time

print('교환 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(c, N)
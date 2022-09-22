### 합병 정렬

### 합병 정렬 알고리즘

# mergeSort(a[], l, r)
#     if (r > l) then {
#         m <- (r + l) / 2;
#         mergeSort(a[], l, m);
#         mergeSort(a[], m+1, r);
#         merge(a[], l, m, r);
#     }
# end mergeSort()

# merge(a[], l, m, r)
#     i <- l; j <- m+1; k <- l:
#     while (i <= m and j <= r) do {
#         if (a[i] < a[j]) then {
#             b[k] <- a[i];
#             i <- i + l;
#             k <- k + l;
#         }
#         else {
#             b[k] <- a[i];
#             j <- j + l;
#             k <- k + l;
#         }
#     }

#     if (i > m) then
#         for (p <- j; p <= r; p <- p + 1) do {
#             b[k] <- a[p];
#             k <- k + 1;
#         }
#     else
#         for (p <- i; p <= m; p <- p + 1) do {
#             b[k] <- a[p];
#             k <- k + 1;
#         }
#     for (p <- l; p <= r; p <- p + 1) do
#         a[p] <- b[p];
# end merge()

# --------------------------------------------------------------------------------------

### 합병 정렬 프로그래밍

def mergeSort(a, l, r):
    if r > l:
        mid = (r + l) // 2
        mergeSort(a, l, mid)
        mergeSort(a, mid + 1, r)
        merge(a, l, mid, r)

def merge(a, l, m, r):
    i = l; j = m + 1; k = l
    while (i <= m and j <= r):
        if (a[i] < a[j]):
            b[k] = a[i]
            i += 1
            k += 1
        else:
            b[k] = a[i]
            j += 1
            k += 1
    
    if i > m:
        for p in range(j, r+1):
            b[k] = a[p]
            k += 1
    else:
        for p in range(i, m+1):
            b[k] = a[p]
            k += 1
    
    for p in range(l, r+1):
        a[p] = b[p]

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]): isSorted = False
        if (not isSorted): break
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')


import random, time

N = 100000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))

b = a.copy()
start_time = time.time()
mergeSort(a, 1, N)

end_time = time.time() - start_time
print('합병 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)
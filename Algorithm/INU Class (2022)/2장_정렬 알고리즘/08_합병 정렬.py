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
        mid = int((r+l)/2)
        mergeSort(a, l, mid)
        mergeSort(a, mid+l, r)

        for i in range(mid+1, 1, -1):
            b[i-1] = a[i-1]
        i -= 1

        for j in range(mid, r):
            b[r+mid-j] = a[j+1]
        j += 1

        for k in range(l, r+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1

# def merge(a, l, m, r):
#     i = l; j = m + 1; k = l
#     while (i <= m and j <= r):
#         if (a[i] < a[j]):
#             b[k] = a[i]
#             i += 1
#             k += 1
#         else:
#             b[k] = a[i]
#             j += 1
#             k += 1
    
#     if i > m:
#         for p in range(j, r+1):
#             b[k] = a[p]
#             k += 1
#     else:
#         for p in range(i, m+1):
#             b[k] = a[p]
#             k += 1
    
#     for p in range(l, r+1):
#         a[p] = b[p]

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

a_copy = a.copy()
start_time = time.time()
mergeSort(a, 1, N)
end_time = time.time() - start_time

print('합병 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 역순 배열
for i in range(N, 0, -1):
    b.append(i)

b_copy = b.copy()
start_time = time.time()
mergeSort(b, 1, N)
end_time = time.time() - start_time

print('합병 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 난수 배열
for i in range(N):
    c.append(random.randint(1, N))

c_copy = c.copy()
start_time = time.time()
mergeSort(c, 1, N)
end_time = time.time() - start_time

print('합병 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(c, N)


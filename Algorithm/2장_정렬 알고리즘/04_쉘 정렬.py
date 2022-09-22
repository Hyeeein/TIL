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

# --------------------------------------------------------------------------------------

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

# 정렬 오류 확인 함수
def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')

import random, time

# 쉘 정렬 실행 시간 출력 (원소의 개수 작게 하니까 엄청 빨라서 10만개부터 시작)
# N 값은 100000~900000으로 20만 단위로 바꿔서 돌리기 (추가 경우의 수 5가지)
N = 900000
a = []; b= []; c = []
a.append(-1); b.append(-1); c.append(-1)


# (1) 배열이 정렬된 순
for i in range(N):
    a.append(i)

start_time = time.time()
shellSort(a, N)
end_time = time.time() - start_time

print('쉘 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 배열이 역순
for i in range(N, 0, -1):
    b.append(i)

start_time = time.time()
shellSort(b, N)
end_time = time.time() - start_time

print('쉘 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 배열이 랜덤한 순
for i in range(N):
    c.append(random.randint(1, N))

start_time = time.time()
shellSort(c, N)
end_time = time.time() - start_time

print('쉘 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(c, N)


'''
N이 100000일 때

쉘 정렬의 실행 시간 (N = 100000) : 0.158
정렬 완료
쉘 정렬의 실행 시간 (N = 100000) : 0.260
정렬 완료
쉘 정렬의 실행 시간 (N = 100000) : 0.801
정렬 완료
'''

'''
N이 300000일 때

쉘 정렬의 실행 시간 (N = 300000) : 0.477
정렬 완료
쉘 정렬의 실행 시간 (N = 300000) : 1.038
정렬 완료
쉘 정렬의 실행 시간 (N = 300000) : 3.247
정렬 완료
'''

'''
N이 500000일 때

쉘 정렬의 실행 시간 (N = 500000) : 0.963
정렬 완료
쉘 정렬의 실행 시간 (N = 500000) : 1.594
정렬 완료
쉘 정렬의 실행 시간 (N = 500000) : 6.380
정렬 완료
'''

'''
N이 700000일 때

쉘 정렬의 실행 시간 (N = 700000) : 1.398
정렬 완료
쉘 정렬의 실행 시간 (N = 700000) : 2.448
정렬 완료
쉘 정렬의 실행 시간 (N = 700000) : 10.345
정렬 완료
'''

'''
N이 900000일 때

쉘 정렬의 실행 시간 (N = 900000) : 1.835
정렬 완료
쉘 정렬의 실행 시간 (N = 900000) : 3.161
정렬 완료
쉘 정렬의 실행 시간 (N = 900000) : 14.112
정렬 완료
'''
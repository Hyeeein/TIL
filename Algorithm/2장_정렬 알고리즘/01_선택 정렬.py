# 선택정렬(selection sort): 잘못된 위치에 들어가 있는 원소를 찾아 그것을 올바른 위치로 옮겨주는 원소 교환으로 정렬

### 알고리즘
# selectionSort(a[], n)
#     for (i <-1; i < n; i <- i+1) do {
#         minIndex <- i;
#         for (j <- i + 1; j <= n; j <- j+1) do
#             if (a[j] < a[minIndex]) then minIndex <- j;
#         a[i]와 a[minIndex]를 교환;
#     }
# end selectionSort()

# -----------------------------------------------------------

### 정렬 선택 프로그램

import random, time

# 선택 정렬 함수
def selectionSort(a, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i+1, n+1):
            if a[minIndex] > a[j]: minIndex = j
            a[minIndex], a[i] = a[i], a[minIndex]

# 정렬 함수 오류 검사 함수
def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')

# 선택 정렬 실행 시간 출력 (원소의 개수 5000개)
# N 값은 10000, 15000, 20000으로 바꿔서 돌리기 (추가 경우의 수 3가지)
N = 20000
a = []; b= []; c = []
a.append(None); b.append(None); c.append(None)


# (1) 배열이 정렬된 순
for i in range(N):
    a.append(i)

start_time = time.time()
selectionSort(a, N)
end_time = time.time() - start_time

print('선택 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 배열이 역순
for i in range(N, 0, -1):
    b.append(i)

start_time = time.time()
selectionSort(b, N)
end_time = time.time() - start_time

print('선택 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 배열이 랜덤한 순
for i in range(N):
    c.append(random.randint(1, N))

start_time = time.time()
selectionSort(c, N)
end_time = time.time() - start_time

print('선택 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(c, N)


'''
N이 5000일 경우

선택 정렬의 실행 시간 (N = 5000) : 2.350
정렬 완료
선택 정렬의 실행 시간 (N = 5000) : 1.937
정렬 완료
선택 정렬의 실행 시간 (N = 5000) : 1.903
정렬 오류 발생
'''

'''
N이 10000일 경우

선택 정렬의 실행 시간 (N = 10000) : 5.839
정렬 완료
선택 정렬의 실행 시간 (N = 10000) : 6.084
정렬 완료
선택 정렬의 실행 시간 (N = 10000) : 6.434
정렬 오류 발생
'''

'''
N이 15000일 경우

선택 정렬의 실행 시간 (N = 15000) : 17.096
정렬 완료
선택 정렬의 실행 시간 (N = 15000) : 16.799
정렬 완료
선택 정렬의 실행 시간 (N = 15000) : 17.612
정렬 오류 발생
'''

'''
N이 20000일 경우

선택 정렬의 실행 시간 (N = 20000) : 28.845
정렬 완료
선택 정렬의 실행 시간 (N = 20000) : 30.875
정렬 완료
선택 정렬의 실행 시간 (N = 20000) : 33.152
정렬 오류 발생
'''

# 결론 : 입력 배열 순서에 민감하지 않고, 입력된 수가 커질수록 더 많은 시간이 소요됨
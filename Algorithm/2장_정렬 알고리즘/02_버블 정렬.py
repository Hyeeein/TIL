# 버블 정렬(bubble sort) : 리스트를 검사하여 두 인접한 원소가 오름차순 정렬 순서에 맞지 않으면 이들을 서로 교환하는 것

### 알고리즘
# bubbleSort(a[], n)
#     for (i <- n; i >= 1; i <- i-1) do
#         for (j <- 1; j < i; j <- j+1) do
#             if (a[j] > a[j+1]) then a[j]와 a[j+1]을 교환;
# end bubbleSort()

# -----------------------------------------------------------

### 버블 정렬 프로그램
import random, time

# 버블 정렬 함수
def bubbleSort(a, n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

# 실행시간 출력 함수
def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break

    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')


# 버블 정렬 실행 시간 출력 (원소의 개수 5000개)
# N 값은 10000, 15000, 20000으로 바꿔서 돌리기 (추가 경우의 수 3가지)
N = 5000
a = []; b= []; c = []
a.append(None); b.append(None); c.append(None)


# (1) 배열이 정렬된 순
for i in range(N):
    a.append(i)

start_time = time.time()
bubbleSort(a, N)
end_time = time.time() - start_time

print('버블 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 배열이 역순
for i in range(N, 0, -1):
    b.append(i)

start_time = time.time()
bubbleSort(b, N)
end_time = time.time() - start_time

print('버블 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 배열이 랜덤한 순
for i in range(N):
    c.append(random.randint(1, N))

start_time = time.time()
bubbleSort(c, N)
end_time = time.time() - start_time

print('버블 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(c, N)


'''
N이 5000인 경우


'''

'''
N이 10000인 경우

'''

'''
N이 15000인 경우

'''

'''
N이 20000인 경우

'''


# 결론 : 
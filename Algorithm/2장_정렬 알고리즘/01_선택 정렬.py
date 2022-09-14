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
N = 5000
a = []
a.append(None)

for i in range(N):
    a.append(random.randint(1, N))

start_time = time.time()
selectionSort(a, N)
end_time = time.time() - start_time

print('선택 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(a, N)
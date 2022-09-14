# 삽입 정렬 (insertion sort) : 매 단계에서 삽입해야 될 새로운 원소 v를 U의 왼쪽 끝에서 꺼내서 S의 적절한 위치에 삽입

### 알고리즘
# insertionSort(a[], n)
#     // 원소 v는 a[i], 1 <= i <= n,
#     // 원소 v(=a[i], 1 <= i <= n)를 부분 배열 a[1:i-1]에 오름차순으로 삽입
#     for (i <- 2; i <= n; i <- i+1) do {     // 두 번째 원소 a[2]부터
#         v <- a[i];      // v는 임시 저장소
#         j <- i;
#         while (a[j-1] > v) do {
#             a[j] <- a[j-1];     // a[j-1]을 오른쪽으로 한자리 이동시켜 빈자리를 만듦
#             j <- j-1;
#         }  // while
#         A[j] <- v;      // v를 빈자리에 삽입
#     }   // for
# end insertionSort()

# --------------------------------------------------------------------------------------

# 삽입 정렬 프로그램

# 삽입 정렬 함수
def insertionSort(a, n):
    for i in range(2, n+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] = a[j-1]
            j -= 1
        a[j] = v

# 정렬 오류 확인 함수
def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted): break
    
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')

import random, time

N = 5000
a = []
a.append(-1)

for i in range(N):
    a.append(random.randint(1, N))

start_time = time.time()
insertionSort(a, N)
end_time = time.time() - start_time
print('삽입 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(a, N)

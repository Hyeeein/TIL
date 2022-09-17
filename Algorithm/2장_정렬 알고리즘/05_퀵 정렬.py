# 퀵 정렬: 분할 정복 기법을 사용한 정렬 방법의 하나

# 퀵 정렬의 단계
# (1) 배열 a[1:r]에서 가장 오른쪽에 있는 원소를 피봇(pivot)으로 선정 / 피봇 (= 분할원소)
# (2) a[] 원소들을 두 개의 파티션으로 분할하는데 정렬 후, 피봇이 들어가는 정확한 위치가 됨

### 퀵 정렬 알고리즘
# quickSort(a[], 1, r)
#     // 배열 a[]의 부분 배열 a[1:r]을 오름차순으로 정렬
#     if (r > 1) then {
#         i <- partition(a[], 1, r);
#         // i는 파티션이 끝난 뒤에 사용된 피봇의 인덱스
#         quickSort(a[], 1, i-1);
#         quickSort(a[], i+1, r);
#     }
# end quickSort()

# --------------------------------------------------------------------------------------

### 분할 알고리즘
# partition(a[], 1, r)
#     // 가장 오른쪽 원소 a[r]을 피봇으로 하여 a[]를 분할
#     v <- a[r];      // 가장 오른쪽 원소를 피봇으로 정함
#     i <- l-1;       // 왼쪽에서 오른쪽으로 움직이는 포인터
#     j <- r;         // 오른쪽에서 왼쪽으로 움직이는 포인터

#     for ( ; ; ) do {
#         do { i <- i+1; } while (a[i] < v);  // 피봇 값보다 작으면 i 값 증가
#         do { j <- j+1; } while (a[j] > v);  // 피봇 값보다 크면 j 값 감소
#         if (i >= j) then break;             // 왼쪽과 오른쪽 포인터가 교차하면 중지
#         a[i]와 a[j]를 교환;
#     } 
#     a[i]와 a[r]를 교환;
#     return i;
# end partition()

# --------------------------------------------------------------------------------------

### 퀵 정렬 프로그램

def quickSort(a, l, r):
    if r > 1:
        v, i, j = a[r], l-1, r
        while True:
            i += 1
            while a[i] < v: i += 1
            j -= 1
            while a[j] > v: j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

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
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
quickSort(a, 1, N)
end_time = time.time() - start_time
print('퀵 정렬의 실행 시간 (N=%d) : %0.3f' %(N, end_time))
checkSort(a, N)
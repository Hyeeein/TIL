# 작은 부분화일 (small subfile)
# 퀵 정렬의 수행 중 처리해야 할 원소의 개수가 상수 M보다 작아지게 되면 거의 정렬된 화일이 만들어짐. 이를 작은 부분화일이라고 함.
# 이렇게 작은 부분화일이 만들어질 경우, 삽입 정렬 알고리즘을 수행하면 성능 향상 가능

# 여기서 보통 M의 범위는 5~25 사이
# 적절한 M 값을 선택한 경우, 약 10~20% 정도의 성능 향상 효과가 있음

# --------------------------------------------------------------------------------------

### 작은 부분화일을 고려한 퀵 정렬 프로그램

def insertionSort(a, l, r):
    for i in range(l+1, r+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] == a[j-1]
            j -= 1
        a[j] = v
    
def quickSort(a, l, r):
    if r-1 <= M:
        insertionSort(a, l, r)
    else:
        v, o, j = a[r], l-1, r
        while True:
            i += 1
            while a[i] < v: i += 1
            j -= 1
            while a[j] > v: j -= 1
            if i >= j: break
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

N = 10000
M = 15
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
quickSort(a, 1, N)
end_time = time.time() - start_time
print('퀵 정렬의 실행 시간 (N = %d): %0.3f' %(N, end_time))
checkSort(a, N)

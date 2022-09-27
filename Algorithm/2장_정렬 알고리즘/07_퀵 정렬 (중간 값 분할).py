# 중간 값 분할 : 분할 원소를 선택할 때 왼쪽, 가운데, 오른쪽 원소 중 값이 중간인 원소를 선택하는 것
# 최악의 경우가 발생하는 확률을 낮추어 주고, 감시 키를 사용할 필요가 없음

# 원소의 개수가 100,000개일 때, 중간 값 분할을 사용한 퀵 정렬 프로그램

def quickSort(a, l, r):
    if r-1 > 1:
        mid = int((l+r)/2)
        if a[l] > a[mid]:
            a[l], a[mid] = a[mid], a[l]
        if a[mid] > a[r]:
            a[mid], a[r] = a[r], a[mid]
        if a[l] > a[mid]:
            a[l], a[mid] = a[mid], a[l]
        a[mid], a[r-l] = a[r-l], a[mid]
        v, i, j = a[r-1], l, r-l

        while True:
            i += 1
            while a[i] < v: i += 1
            j -= 1
            while a[j] > v: j -= 1
            if i >= j: break
            a[i], a[j] = a[j], a[i]

        a[i], a[r-l] = a[r-l], a[i]
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)
    
    elif a[l] > a[r]:
        a[l], a[r] = a[r], a[l]


def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]): isSorted = False
        if (not isSorted): break
    
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')


import random, timeㅋ

a = []
N = 100000
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
quickSort(a, 1, N)
end_time = time.time() - start_time
print('퀵 정렬의 실행 시간 (N = %d): %0.3f' %(N, end_time))
checkSort(a, N)

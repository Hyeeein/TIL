# 칵테일 세이커 정렬 알고리즘: 버블 정렬을 수정하여 매번 반복할 때마다 방향을 바꿔가며 원소의 위치를 결정하는 기법

# 루프를 반복할 때마다 한 번은 가장 큰 원소를 가장 오른쪽 위치로 보내고
# 그 다음에는 가장 작은 원소를 가장 왼쪽 위치로 보내면서 수행 (= 양방향 버블 정렬)

### 칵테일 세이커 알고리즘 (ADL)
# cocktailShakerSort(a[], n)
#     d <- true; i <- 1; k <- n;
#     while (i < k) do {
#         if (d = true) then {
#             for (j <- i + 1; j <= k; j <- j + 1) do
#                 if (a[j] < a[j-1]) then a[j]와 a[j-1]을 교환;
#             k <- k -1;
#         }
#         else {
#             for (l <- k; l > 1; l <- l-1) do
#                 if (a[l] < a[l-1]) then a[l]과 a[l-1]을 교환;
#             i <- i + 1;
#         }
#         d <- not d;
#     }
# end cocktailShakerSort()

### 칵테일 쉐이커 정렬 파이썬 프로그래밍
def cocktailShakerSort(arr, n):
    r = n; l = 1; i = 1

    while l < r:
        if i % 2 == 1:
            for j in range(l+1, r+1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
            r -= 1
        else:
            for k in range(r, l, -1):
                if arr[k] < arr[k-1]:
                    arr[k], arr[k-1] = arr[k-1], arr[k]
            l += 1
        # print(f"{i}번째 패스 종료 후 arr = {arr}")
        i += 1
    return arr

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]): isSorted = False
        if (not isSorted): break
    if isSorted: print('정렬 완료')
    else: print('정렬 오류 발생')

import random, time

# N 값 5000부터 5천 단위로 4번 측정 (2만까지)
N = 20000
a = []; b = []; c = []
a.append(None); b.append(None); c.append(None)

# (1) 정렬된 배열
for i in range(N):
    a.append(i)

start_time = time.time()
cocktailShakerSort(a, N)
end_time = time.time() - start_time

print('칵테일 쉐이커 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 역순 배열
for i in range(N, 0, -1):
    b.append(i)

start_time = time.time()
cocktailShakerSort(b, N)
end_time = time.time() - start_time

print('칵테일 쉐이커 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 난수 배열
for i in range(N):
    c.append(random.randint(1, N))

start_time = time.time()
cocktailShakerSort(c, N)
end_time = time.time() - start_time

print('칵테일 쉐이커 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(c, N)


# 버블 정렬과의 차이점 : 정렬 방향이 한 방향이 아니라, 양방향으로 바뀌면서 속도가 빨라진다
# 참고 사이트
# https://velog.io/@swhan9404/%EB%B2%84%EB%B8%94%EC%A0%95%EB%A0%AC-%EC%B9%B5%ED%85%8C%EC%9D%BC%EC%A0%95%EB%A0%AC-%EB%B9%97%EC%A7%88%EC%A0%95%EB%A0%AC
# https://library-of-k.tistory.com/21


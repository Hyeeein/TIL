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

### 삽입 정렬 프로그램

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

# 버블 정렬 실행 시간 출력 (원소의 개수 5000개)
# N 값은 10000, 15000, 20000으로 바꿔서 돌리기 (추가 경우의 수 3가지)
N = 25000
a = []; b= []; c = []
a.append(-1); b.append(-1); c.append(-1)


# (1) 배열이 정렬된 순
for i in range(N):
    a.append(i)

start_time = time.time()
insertionSort(a, N)
end_time = time.time() - start_time

print('삽입 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(a, N)

# ------------------------------------------------------------

# (2) 배열이 역순
for i in range(N, 0, -1):
    b.append(i)

start_time = time.time()
insertionSort(b, N)
end_time = time.time() - start_time

print('삽입 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(b, N)

# ------------------------------------------------------------

# (3) 배열이 랜덤한 순
for i in range(N):
    c.append(random.randint(1, N))

start_time = time.time()
insertionSort(c, N)
end_time = time.time() - start_time

print('삽입 정렬의 실행 시간 (N = %d) : %0.3f' %(N, end_time))
checkSort(c, N)

'''
N이 5000인 경우

삽입 정렬의 실행 시간 (N = 5000) : 0.001
정렬 완료
삽입 정렬의 실행 시간 (N = 5000) : 2.570
정렬 완료
삽입 정렬의 실행 시간 (N = 5000) : 1.350
정렬 완료
'''

'''
N이 10000인 경우

삽입 정렬의 실행 시간 (N = 10000) : 0.002
정렬 완료
삽입 정렬의 실행 시간 (N = 10000) : 8.788
정렬 완료
삽입 정렬의 실행 시간 (N = 10000) : 4.925
정렬 완료
'''

'''
N이 15000인 경우

삽입 정렬의 실행 시간 (N = 15000) : 0.002
정렬 완료
삽입 정렬의 실행 시간 (N = 15000) : 37.246
정렬 완료
삽입 정렬의 실행 시간 (N = 15000) : 21.110
정렬 완료
'''

'''
N이 20000인 경우

삽입 정렬의 실행 시간 (N = 20000) : 0.003
정렬 완료
삽입 정렬의 실행 시간 (N = 20000) : 37.349
정렬 완료
삽입 정렬의 실행 시간 (N = 20000) : 19.648
정렬 완료
'''

'''
N이 25000인 경우


'''

# 결론 : 입력 배열의 순서에 민감함. 정렬된 배열의 경우, 속도가 거의 0초에 해당할 정도로 빠르지만, 다른 것은 그렇지 않음
# 입력된 수가 커질수록 역순 배열과 난수 배열은 시간이 더 많이 소요되지만, 정렬된 배열의 속도는 크게 차이 안남.
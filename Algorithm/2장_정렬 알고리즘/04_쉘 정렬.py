# 쉘 정렬 (shell sort) : 

### 알고리즘 (ADL)
# shellSort(a[], n)
#     for (h <- n/2; h > 0; h = h/2) do {     // h 값 계산, h 값을 감소시키며 진행
#
#         // 왼쪽에서 출발하는 i
#         for (i <- 0; i < h; i <- i + 1) do {
# 
#             // 오른쪽에서 출발하는 j (h 간격에 있는 데이터)
#             for (j = i + h; j < n; j = j + h) do {
#                 tmp = a[j];
#                 tmp_index = j;
# 
#                 // a[i]가 a[j]보다 클 경우 찾기
#                 while (tmp_index > h-1 and a[i] > tmp) do {
#                     a[j] = a[i];
#                     j = i;
#                 }
#                 a[i] = tmp
#             }
#         }
#     }
# end shellSort()


### 파이썬 프로그래밍
def shellSort(a, n):

    
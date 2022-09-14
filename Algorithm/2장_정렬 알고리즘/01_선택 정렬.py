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

### 선택 정렬 프로그램
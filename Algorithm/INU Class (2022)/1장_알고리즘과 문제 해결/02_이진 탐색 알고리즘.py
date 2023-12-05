## 이진 탐색 알고리즘

def binarySearch(a, key, left, right):
     # 괄호 안 순서대로 배열, 찾고자 하는 값, 가장 작은 값, 가장 큰 값

    if left <= right:
        # 가장 큰 값과 작은 값의 중앙값의 인덱스
        mid = (left + right) // 2

        if key == a[mid]: return mid
        elif key < a[mid]: return binarySearch(a, key, left, mid-1)
        elif key > a[mid]: return binarySearch(a, key, mid+1, right)

    # key 값이 존재하지 않는 경우
    else:
        return -1

# 이진 탐색은 점점 커지는 순서 배열을 가져야 탐색할 수 있다 !!
a = [1, 2, 3, 4, 5]
print('배열:', a)

while True:
    num = int(input('원하는 값을 입력하시오: '))
    print('찾고자 하는 값:', num, ' 위치:', binarySearch(a, num, 0, len(a))+1)
    print()
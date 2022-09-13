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

a = [3, 2, 5, 1, 4]
print('배열:', a)

while True:
    num = int(input('원하는 값을 입력하시오: '))
    print('찾고자 하는 값:', num, ' 위치:', binarySearch(a, num, 0, len(a)))
    print()
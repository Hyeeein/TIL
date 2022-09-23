# 칵테일 세이커 정렬 알고리즘: 버블 정렬을 수정하여 매번 반복할 때마다 방향을 바꿔가며 원소의 위치를 결정하는 기법

# 루프를 반복할 때마다 한 번은 가장 큰 원소를 가장 오른쪽 위치로 보내고
# 그 다음에는 가장 작은 원소를 가장 왼쪽 위치로 보내면서 수행 (= 양방향 버블 정렬)

### 칵테일 세이커 알고리즘 (ADL)
# Shaker_Sort(arr[], N)Sort  ← 1;// 1 = TRUE , 0 = FALSEleft  ← N;// N = 데이터 개수right ← 1;while(right > left) do {for (i ← right; I < left; i ← i+1) do {if (arr[i] > arr[i+1]) then {temp ← arr[i];arr[i] ← arr[i+1];arr[i+1] ← temp;}}left ← left – 1;for (i ← left; i > right; i ← i-1) do {if (arr[i] < arr[i-1]) then {temp ← arr[i];arr[i] ← arr[i-1];arr[i-1] ← temp;}}right ← right + 1;}end Shaker_Sort(arr[], N)
# 출처: https://ikso2000.tistory.com/49 [띠그랭                      :티스토리]

### 칵테일 쉐이커 정렬 파이썬 프로그래밍
def cocktailSort(arr):
    a = -1; b = len(arr) + 1

    swapped = True # True면 정방향, False면 역방향

    # 방향이 정방향으로 가고 있을 경우
    while swapped == True:
        swapped = False

        for i in range(a, b):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if swapped == False: break

        swapped = False
        b -= 1

        for i in range(b-1, a-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        a += 1



# 버블 정렬과의 차이점 : 정렬 방향이 한 방향이 아니라, 양방향으로 바뀌면서 속도가 빨라진다
# 참고 사이트
# https://velog.io/@swhan9404/%EB%B2%84%EB%B8%94%EC%A0%95%EB%A0%AC-%EC%B9%B5%ED%85%8C%EC%9D%BC%EC%A0%95%EB%A0%AC-%EB%B9%97%EC%A7%88%EC%A0%95%EB%A0%AC
# https://library-of-k.tistory.com/21


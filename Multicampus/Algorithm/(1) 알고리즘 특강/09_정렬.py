## 선택 정렬 1 (완전)
import random

## 함수
def findMinIndex(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

## 전역
before = [ random.randint(100, 200) for _ in range(20)]
after = []

## 메인
print('정렬 전-->', before)
for _ in range(len(before)) :
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬 전-->', after)
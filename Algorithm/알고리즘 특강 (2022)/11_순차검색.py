## 순차 검색
import random

## 함수
def seqSearch(ary, fData) :
    pos = -1
    size = len(ary)
    for i in range(0, size, 1) : # (size)
        if (ary[i] == fData) :
            pos = i
            break
    return pos

## 전역
SIZE = 10
dataAry = [ random.randint(1, 99) for _ in range(20)]
findData = dataAry[random.randint(0,SIZE-1)]
#findData = -99

## 메인
print('배열-->', dataAry)
positon = seqSearch(dataAry, findData)
if positon == -1 :
    print(findData, '없어요 ㅠ')
else :
    print(findData, '가 ', positon, ' 에 있음')
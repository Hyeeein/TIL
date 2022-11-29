# KMP 스트링 탐색 프로그램

def initNext(p, m):
    next[0] = -1
    i = 0
    j = -1
    global count

    while i < m:
        if j != -1 and p[i] == p[j] : next[i] = next[j]
        else: next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1

        count += 1   # 비교할 때마다 횟수 추가

def KMP(p, t, k, m, n):
    initNext(p, m)
    i = k
    j = 0
    while j < m and i < n:
        while j >= 0 and t[i] != p[j]:
            j = next[j]
            print(i, j)
        i += 1
        j += 1
    if j == m: return i - m
    else: return i

next = [0] * 50
text = 'ababacabcbababcacacaababca'
pattern = 'ababca'
M = len(pattern)
N = len(text)
K = 0
count = 0         # 총 비교횟수 (전역변수로 선언)

while True:
    pos = KMP(pattern, text, K, M, N)
    K = pos + M

    if K <= N: print('패턴이 나타난 위치 :', pos)
    else: break

# 마지막 패턴을 인식하지 못하면 텍스트 마지막에 널 문자 추가
text = text + '\0'
print('널 문자를 추가한 text:', text, '(널 문자가 있는지 확인)')

print('총 비교횟수:', count)
print("스트링 탐색 종료")
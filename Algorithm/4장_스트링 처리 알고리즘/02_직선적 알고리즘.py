#### 직선적 알고리즘 파이썬 프로그래밍

# 텍스트 ababacabcbababcacacbcaababca에 대하여 패턴 ababca를 탐색
# 실행 결과로 패턴이 나타난 위치 출력, 마지막 패턴 인식하지 못하면 마지막에 널 문자 추가
# 텍스트와 패턴에 있는 문자에 대한 총 비교횟수 출력

def bruteForce(p, t, k):
    M = len(p)  # 패턴의 길이
    N = len(t)  # 텍스트의 길이

    i = k
    j = 0
    global count

    while j < M and i < N:

        # 텍스트와 패턴이 같지 않을 때
        if t[i] != p[j]:
            i -= j
            j = -1
        
        # 텍스트와 패턴이 같을 때
        i += 1
        j += 1

        count += 1   # 비교할 때마다 횟수 추가

    if j == M: return i - M
    else: return i

text = 'ababacabcbababcacacbcaababca'
pattern = 'ababca'

M = len(pattern)  # 패턴의 길이
N = len(text)     # 텍스트의 길이
K = 0             # 탐색을 시작하는 위치
count = 0         # 총 비교횟수 (전역변수로 선언)

while True:
    pos = bruteForce(pattern, text, K)   # pos: 패턴이 나타난 위치
    K = pos + M
    
    # 탐색 위치가 텍스트 길이 안에 있을 때 if문 사용
    if K < N: print('패턴이 나타난 위치:', pos)
    else: break
        
# 마지막 패턴을 인식하지 못하면 텍스트 마지막에 널 문자 추가
# text = text + '\0'
# print('널 문자를 추가한 text:', text, '(널 문자가 있는지 확인)')

print('총 비교횟수:', count)
print('스트링 탐색 종료')
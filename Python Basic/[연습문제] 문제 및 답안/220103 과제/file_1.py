# 문제 1 : Yesterday 단어들 목록, 단어별 개수 출력
# 만든 날짜 : 2022-01-03
# 만든이 : 박혜인

# 리스트, 세트, 딕셔너리 등의 자료구조 이용
# 단어들은 모두 소문자로 변환하여 사용

f = open('yesterday.txt', 'r')
lyrics = f.readlines()
words = {}

for i in lyrics:
    # 1) 소문자로 바꾸기
    lyrics_lower = i.lower()
    lyrics_split = lyrics_lower.split(' ')

    # 2) 띄어쓰기를 중심으로 나누기
    for word in lyrics_split:
        # 3-1) 단어 앞 뒤에 있는 공백 제거
        word = word.strip()
        # 3-2) 해당 단어가 공백일 경우 pass
        if word == '':
            pass
        # 4) 해당 단어가 사전에 등록 혹은 카운트
        elif word not in words:
            words[word] = 1
        elif word in words:
            words[word] = words[word] + 1

# items : 키-값 쌍을 모두 가져옴
# keys : 키를 모두 가져옴
# values : 값을 모두 가져옴

# 알파벳 순으로 정렬
sort_words = sorted(words.items())   # 튜플 자료형으로 리턴됨

# 최종 출력
for key, value in sort_words:
    print(f'{key} : {value}')

## close가 빠져있는데 close를 써주는게 좋음
## 쓰지 않을거면 with 문을 사용하면 좋다



### ---------------------- ###
# 강사님 예시 답안
#
# f = open('yesterday.txt', 'r')
# yesterday = f.readlines()
# f.close()
# f = open('yesterday.txt', 'r')
# yesterday2 = f.read()
# f.close()
#
# words = []
# words2 = yesterday.split()
#
# print(words2)
#
# for line in yesterday:
#     for w in line.split():
#         words.append(w.lower())
#
# wordL = list(set(words))
# wordL.sort()
#
# wordDict = dict()
# for w in wordL:
#     wordDict[w] = words.count(w)
#
# for w in wordDict.items():
#     print(w)


### ---------------------- ###
### 다른 분들 예시 답안 ###
# with open('yesterday.txt', 'r') as f:
#     a = f.read().lower().replace(',', '')
# lst = a.split()
#
# my_set = set(lst)
# my_set = sorted(my_set)
#
# with open('output.txt', 'w') as f:
#     for s in my_set:
#         f.write(f'{s} : {lst.count(s)}\n')

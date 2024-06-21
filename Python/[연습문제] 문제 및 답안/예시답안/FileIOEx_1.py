# 1. 텍스트파일로 되어 있는 가사의 단어 카운트

# 방법1
# f = open('yesterday.txt','r')
# yesterday  = f.readlines()
# f.close()
# words = []
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
# for w in wordDict.items():
#     print(w)

# 방법2
with open('yesterday.txt','r') as f:
    yesterday = f.read()
words = yesterday.split()
words = [i.lower() for i in words]
wordL = list(set(words))
wordL.sort()
wordDict = dict()
for w in wordL:
    wordDict[w] = words.count(w)
for w, c in wordDict.items():
    print(f'{w}:{c}')


# 이유진 작성
#
# path = '/Users/iyujin/develop/pythonProject/Day8_0103/FileIO'
#
# d ={}
# with open('Yesterday.txt','r') as f:
#     data = f.read().split()
#     data = [i.lower() for i in data]
#
# for i in data:
#     val = data.count(i)
#     d[i] = val
#
# print(sorted(d.items()))


# 이재원 작성
# f = open("yesterday.txt", 'r')
#
# data = f.read().lower()
# data1 = data.split()
#
# print(data1)
# d = {}
#
# for i in data1:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i]  = 1
# print(d)
# for x ,y  in d.items():
#     print(x + ':' + str(y))


# 강중모 작성
# with open('yesterday.txt', 'r') as f:
#     a = f.read().lower().replace(',', '')
# lst = a.split()
#
# my_set = set(lst)
# my_set = sorted(my_set)
#
# with open('output.txt', 'w') as f:
#     for s in my_set:
#         f.write(f"'{s}' : {lst.count(s)}\n")
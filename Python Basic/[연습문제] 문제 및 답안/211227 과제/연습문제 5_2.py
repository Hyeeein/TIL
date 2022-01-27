## 연습문제 5-2
# 만든 날짜 : 2021-12-27
# 만든이 : 박혜인

word = {}  # 영어단어 사전 리스트

## 단어 등록
while True:
    english_word = input('영어 단어 등록 (종료는 quit) : ')
    if english_word == 'quit':
        break;

    # 등록된 단어가 없을 경우
    if english_word not in word:
        korean_word = input('%s의 뜻입력 (종료는 quit) : ' % english_word)
        word[english_word] = korean_word

    # 등록된 단어가 있을 경우
    elif english_word in word:
        print('%s는 이미 등록된 단어 입니다.' % english_word)
    print()

print(word)
print()

## 단어 검색
while True:
    search = input('검색할 단어 입력 (종료는 quit) : ')

    if search == 'quit':
        print()
        print('종료합니다.')
        break

    # 등록된 단어가 있을 경우
    if search in word:
        print('%s의 뜻은 %s입니다' % (search, word[search]))

    # 등록된 단어가 없을 경우
    else:
        print('%s는 사전에 없는 단어 입니다.' % search)

    print()


# # 예시 답안
#
# # 영어 단어 등록
# eng_dic = dict()
#
# while True:
#     eng = input('영어 단어 등록 (종료는 quit) : ')
#     if eng == 'quit':
#         break
#     elif eng not in eng_dic:
#         kor = input('%s의 뜻 입력 (종료는 quit) : ' % eng)
#     else:
#         print(f'{eng}는 이미 등록된 단어입니다')
# print()
#
# # 영어 단어 검색
# while True:
#     eng = input('검색할 영어 단어 입력 (종료는 quit) : ')
#     if eng == 'quit':
#         break
#     elif eng in eng_dic:
#         print(f'{eng}의 뜻은 {eng_dic[eng]}입니다.')
#     else:
#         print(f'{eng}는 사전에 없는 단어입니다.')
#
# print('종료합니다')
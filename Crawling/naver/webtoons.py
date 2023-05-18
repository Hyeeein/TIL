# -*- coding:utf-8 *-
# 해당 파이썬 파일은 utf 파일로 인코딩 됨 (주석 안에 써야 적용됨)

from bs4 import BeautifulSoup
import requests
import json

# requests는 movies에서 했던 역할과 같음
url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url)
# print(resp)
# print(resp.text)

# 받아온 데이터를 가지고 BeautifulSoup이 parsing 진행
soup = BeautifulSoup(resp.text, 'html.parser')

# '수요 전체 웹툰'의 제목과 별점 가져오기 (딕셔너리 형태, class_와 같은 의미)
webtoons = soup.find('ul', {'class': 'img_list'})

# dl 태그 가지고 와서 a 태그 안의 title / div 안에 있는 strong 태그를 가져와 star로 저장
dl_list = webtoons.select('dl')  # select는 css 선택자

# json 형태로 바꾸어서 제목과 별점을 저장
lst = list()
for dl in dl_list:
    title = dl.find('a')['title']   # title 안에 있는 값이 이미 text라서 .text 처리 안함
    star = dl.find('strong').text

    # 이 내용을 딕셔너리 형태로 만들어줌
    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star

    # 만든 딕셔너리를 lst에 넣어줌
    lst.append(tmp)

# 다시 딕셔너리 형태로 저장 : res에 저장된 값이 json 형태로 만든 값이랑 똑같음 (문자열로 되어있음)
res = dict()
res['webtoons'] = lst

# 딕셔너리 데이터를 다시 json 형태로 바꿈
res_json = json.dumps(res, ensure_ascii=False) # dumps ?
print(res_json)

with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)

from bs4 import BeautifulSoup
import urllib.request

# urllib : 파이썬 라이브러리 / 클라이언트 역할 (요청)
# -> request가 있으니까 클라이언트가 서버한테 요청함 -> 응답받은 내용은 객체로 저장 (doc 형태)
resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver#')

# 객체로 응답받아온 것을 html.parser 형태로 받아와 parse tree를 만들어줌
# 받아온 파일의 type은 class, 즉 객체
soup = BeautifulSoup(resp, 'html.parser')

# 영화 제목과 별점 가져오기
# 개발자 도구로 가서 html에서 사용한 태그 확인 -> dl 태그 / class는 'lst_doc'
movies = soup.find_all('dl', class_='lst_dsc')

for movie in movies:
    # 제목 : a 태그에 쌓여있으므로, a 태그를 찾아옴 -> a 태그 안의 textcontent를 가져옴 (.get_text 사용)
    title = movie.find('a').get_text()
    # 별점 : class = num인 span 태그를 찾아옴
    star = movie.find('span', class_='num').text
    print(f'{title} [{star}]')

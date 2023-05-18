from bs4 import BeautifulSoup
import requests

url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=5&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='

# 이 링크에서 5페이지 게시판의 파일 제목만 불러오기
resp = requests.get(url)     # get 방식으로 응답 받음
soup = BeautifulSoup(resp.text, 'html.parser')

# class가 title인 span 태그 가져오기 (그 안에 있는 글씨가 제목)
titles = soup.find_all('span', class_='title')
for title in titles:
    print(title.text.strip())
    # strip() : 공백 제거

# -----
# 같은 페이지에서 아래에 페이지 선택하는 부분 문자열 불러오기 (1~10을 리스트로)
# find와 find_all의 차이 ?
pages = soup.find('nav', class_='pagination')
page_lst = list()

for page in pages:
    if page.text.isdigit():
        page_lst.append(page.text)

print(page_lst)

# 한 줄로 쓴다면?
page_list = list(filter(None, map(lambda x : x.text if x.text.isdigit() else None, pages)))
# print(page_list)

# -----
# 1페이지부터 10페이지까지 제목들 모두 가져오기
sub_url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage='

for i in page_list:
    soup = BeautifulSoup(requests.get(sub_url+i).text, 'html.parser')
    titles = soup.select('span[class=title]')
    for title in titles:
        print(title.text.strip())


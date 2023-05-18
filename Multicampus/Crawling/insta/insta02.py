from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tags: ')
url = f'https://www.instagram.com/explore/tags/{tag}'

service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)  # service라는 속성에 service 값을 넣어줌
# chrome은 경로를 말하는 webdriver.chrome.service => chromedriver.exe가 자동으로 제어할 수 있게 selenium이 만들어줌
# Chrome은 객체 Chrome을 생성하는 것

driver.implicitly_wait(3)  # 3초 기다렸다가 url 가져와주세요
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser') # 드라이브가 지금 보고 있는 페이지 소스보기한 데이터를 가져와라
img_list = soup.find_all('div', class_='KL4Bh') # 실제로 데이터 받아와져 있는 문서를 가지고 원하는 것 찾아올 수 있게 됨

for img in img_list:
    print(img)

# 실행하고 나면 터미널에 주르륵 코드 뜨고, 크롬에는 'Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다'라고 뜸
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id 입력 : ')
input_pw = input('pw 입력 : ')

service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('http://www.instagram.com/')
sleep(5)   # 5초동안 쉬어라

# 취소선은 사용은 가능한데 사용하지 말라는 뜻 => find_element로 바뀜
id = driver.find_element(By.NAME, 'username')
id.send_keys(input_id)

pw = driver.find_element(By.NAME, 'password')
pw.send_keys(input_pw)
sleep(2)

driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)").click()

# 로그인 버튼이 애매하게 눌려만 있으면 아래 24-25번 사용 (근데 난 안되니까 쓰지말자)
# sleep(7)
# driver.refresh()

later = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
later.click()

# 구글은 자동화 로그인 아예 막혀있음

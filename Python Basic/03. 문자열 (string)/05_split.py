# 문자열 분리 함수

# split()
cities = '인천 대구 대전 부산 울산 청주 춘천'
cities_split = cities.split()
print(cities_split)

names = '성춘향;변학도;이몽룡;방자'
names_split = names.split(';')
print(names_split)

for name in names_split:
    print(name)

## 연습문제 1 : 생년월일을 입력하고 연도, 월, 일을 구분해서 출력
# 생일 입력(연/월/일) : 2000/02/01
# 당신은 2000년에 태어났고, 생일은 02월 07일에 태어났군요

birth = input('생일 입력(연/월/일) : ')
birth_split = birth.split('/')

print(f'당신은 {birth_split[0]}년에 태어났고\n생일은 {birth_split[1]}월 {birth_split[2]}일이군요')

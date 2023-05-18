from xml.etree import ElementTree
import requests
import re

# service_key = notion에서 확인
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'
# print(url)

resp = requests.get(url) # url은 xml 형태의 document가 응답 -> 문자열 형태
print(resp.text)

# 문자열로 객체로 만들어줌 (parse tree로 만들기)
tree = ElementTree.fromstring(resp.text)

# tree는 element
# 1은 response의 1번지인 <body> / 0은 body의 0번지인 <item>
for item in tree[1][0]:

    # 우리는 gubun 태그의 합계를 이용하고 싶음
    if item.find('gubun').text == '합계':
        ## 출력화면은 다음과 같게 출력
        # [22/02/09]
        # 일일합계:49567
        # 국내발생:49402
        # 해외발생:165

        stdDay = re.sub(r'(\D)+', '', item.find('stdDay').text)         # 정규표현식 (스스로 공부)
        stdDay = stdDay[2:4] + "/" + stdDay[4:6] + "/" + stdDay[6:8]

        incDec = item.find('incDec').text
        localOccCnt = item.find('localOccCnt').text
        overFlowCnt = item.find('overFlowCnt').text
        print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{localOccCnt}\n해외발생:{overFlowCnt}')

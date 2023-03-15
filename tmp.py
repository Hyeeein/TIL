import dart_fss as dart
import pandas as pd
import pymysql
from dart_fss.errors import NotFoundConsolidated
import multiprocessing as mp
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Open DART API KEY 설정
    api_key = ''
    dart.set_api_key(api_key=api_key)

    # con = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='temp',
    #                       charset='utf8')  # 한글처리 (charset = 'utf8')


    # cur = con.cursor()

    # DART 에 공시된 회사 리스트 불러오기
    all = dart.api.filings.get_corp_code()
    df = pd.DataFrame(all)
    df_listed = df[df['stock_code'].notnull()]
    print(df_listed)
    df_listed['modify_date'].sort_values(ascending=False)
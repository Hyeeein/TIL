# 로그파일 작성

import os

if not os.path.isdir('log'):
    os.mkdir('log')

if not os.path.exists('log/countlog.txt'):
    f = open('log/countlog.txt', 'w', encoding='utf-8')
    f.write('기록시작\n')
    f.close()

# 파일에 로그 기록
with open('log/countlog.txt', 'a', encoding='utf-8') as f:
    import datetime, random
    for _ in range(10):
        stamp = str(datetime, datetime.now())
        value = random.random() * 1000000
        log_line = stamp + '\t' + str(value) + '값 생성\n'
        f.write(log_line)


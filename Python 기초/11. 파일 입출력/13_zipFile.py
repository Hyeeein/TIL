# 파일 압축 및 풀기

import zipfile

# 파일 압축
new = zipfile.ZipFile('c:/pythonStudy/11. 파일 입출력/11. 파일 입출력.zip', 'w')
new.write('c:/pythonStudy/11. 파일 입출력/FileI0/test2.txt', compress_type=zipfile.ZIP_DEFLATED)
new.close()

# 압축파일 풀기
ext = zipfile.ZipFile('c:/pythonStudy/11. 파일 입출력/11. 파일 입출력.zip', 'r')
ext.extractall('c:/pythonStudy/11. 파일 입출력/')
ext.close()

# 파일 또는 디렉터리 존재 여부 확인 : os.path.exist()

import os.path

print(os.path.exists('/'))
print(os.path.exists('c:/pythonStudy/test.py'))

# 디렉터리인지 파일인지 구분

print(os.path.isfile('/'))
print(os.path.isdir('c:/pythonStudy/test.py'))
# 디렉토리 목록 보기

import os

for dirNmae, subDir, fnames in os.walk('c:/pythonStudy/11. 파일 입출력'):
    for fname in fnames:
        # print(os.path.join(dirName, fname))
        print(fname)

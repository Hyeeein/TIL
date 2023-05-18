## 디렉토리 생성

import os
import shutil

# os.mkdir('log')
shutil.rmtree('log')


## 기존 디렉토리 확인

import os.path

if not os.path.isdir('log'):
    os.mkdir('log')

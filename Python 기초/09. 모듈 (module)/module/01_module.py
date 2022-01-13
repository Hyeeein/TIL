## 표준 모듈

import sys

builtModules = sys.builtin_module_names
print(builtModules)

# ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk',
#  '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections',
#  '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io',
#  '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator',
#  '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre',
#  '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc',
#  '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit',
#  'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc',
#  'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg',
#  'xxsubtype', 'zlib')


## 모듈 이용 방법

# 1) 모듈 전체 참조
# import 모듈명
# import random

# import 모듈명 as 별칭
# 모듈명이 길거나 모듈명이 동일한 경우 별칭으로 사용
# import pandas as pd

# 모듈 내 함수를 참조
# import 모듈
# 모듈.함수명

# 2) 모듈 내에서 일부만 참조
#   형식 1) from 모듈명 import 변수명 or 함수명
# from random import randint, randrange

#   형식 2) from random import * 은 import random과 같지만
# 차이가 있다면, 모듈 내에서 __로 시작하는 스페셜 변수나 매직 메소드를 제외한 모든 것을 참조함

#   형식 3) from 모듈명 import 변수명 또는 함수명 as 별칭
# from random import randint, randrange as rnd


## calculater 파일을 만들고 직접 import해서 사용해보기

# 모듈 참조형식1
# import calculater
# print(calculater.add(10, 3))

# 모듈 참조형식2
# from calculater import add, sub
# print(add(10, 3))
# print(div(10, 3)) # 오류발생

# 모듈 참조형식3
# from calculator import *
# print(add(10, 3))
# print(div(10, 3))

# 모듈 참조형식4
# import calculater as cal
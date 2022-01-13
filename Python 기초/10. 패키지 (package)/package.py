# 10. 패키지 (package) : 모듈들을 모아놓은 디렉토리 (폴더)

# 일반적인 디렉토리와의 차이점
# 패키지는 디렉터리 안에 __init__.py가 존재 (빈 파일)

# 패키지를 사용할 경우 모듈 import

# import 패키지.모듈
# import 패키지.모듈 as 별칭
# from 패키지.모듈 import 함수
# from 패키지.모듈 import **

# 패키지를 파이참으로 구성하는 방법
# [파일] - [New] - [Python Package] - package 이름
# 패키지가 생성되면 __init__.py가 생성됨을 볼 수 있음

# -----
# import 패키지. 모듈
# import mypack.pack1.module11
#
# mypack.pack1.module11.func11()

# import 패키지.모듈 as 별칭
# import mypack.pack1.modul11 as mm1
#
# mm1.func11()
#
# from 패키지.모듈 import 함수
# from mypack.pack1.module11 import func11, func111
# from mypack.pack1.module12 import func12
#
# func12()
#
# from 패키지.모듈 import *
# from mypack.pack1.module11 import *
# func11()
# func111()

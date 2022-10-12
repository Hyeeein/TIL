1. 외부 통신 오류

```
fatal: unable to access 'https://github.com/Hyeeein/TIL/': Could not resolve host: github.com
```

- 인터넷 연결이 안된지 다시 확인 => 이번에는 와이파이 다시 연결하니까 됐음



2. git master Merging 충돌 해결하기

- 해결 방법 링크 : https://velog.io/@sg-moomin/GIT-master-Merging-%EC%B6%A9%EB%8F%8C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95



3. Github와 로컬 연결하기

```
# git 시작
git init

# 원격 저장소 등록
git remote add origin <주소>

# 원격 저장소 조회
git remote -v

# 원격 저장소 업로드
git add ~
git commit -m ''
git push origin master
```


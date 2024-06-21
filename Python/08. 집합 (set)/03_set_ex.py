# 문제.
partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}
# partyA = set(['Park', 'Kim', 'Lee'])
# partyB = set(['Park', '길동', '몽룡'])
print(partyA)
print(partyB)
print('파티에 참석한 모든 사람')
print(partyA | partyB)
print('---------------------------')
print('2개 파티에 모두 참석한 사람')
print(partyA & partyB)
print('---------------------------')
print('파티A에만 참석한 사람')
print(partyA - partyB)
print('---------------------------')
print('파티B에만 참석한 사람')
print(partyB - partyA)
# break & continue

for i in range(10):
    if i % 2 == 0:
        break
    print(i)

print('-------------------------------')

for i in range(10):
    if i % 2 == 1:
        continue
    print(i)

print('-------------------------------')

i=1
while i<10:
    if i % 2 == 0:
        break
    print(i)
    i += 1

print('-------------------------------')

i=0
while i<10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
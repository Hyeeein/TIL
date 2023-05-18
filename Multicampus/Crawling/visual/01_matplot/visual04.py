import matplotlib.pyplot as plt
import random

"""
ax01 = fig.add_subplot(2, 2, 1)
ax02 = fig.add_subplot(2, 2, 2)
ax03 = fig.add_subplot(2, 2, 3)
ax04 = fig.add_subplot(2, 2, 4)
이 문장들을 한 문장으로 작성한게 12번째 줄
"""

fig, ax = plt.subplots(2, 2, figsize=(10, 10))

x = list(range(50))
y01 = list(random.randint(0, 50) for i in range(50))
y02 = list(random.randint(0, 50) for i in range(50))
y03 = list(random.randint(0, 50) for i in range(50))
y04 = list(random.randint(0, 50) for i in range(50))

print(x)
print(y01)
print(y02)
print(y03)
print(y04)

# cf) 데이터 분석은 데이터가 정확하게 잘 정제되어 있어야 분석하기에 용이

# 산점도 (scatter)
ax[0, 0].scatter(x, y01, color='red')
ax[0, 1].scatter(x, y02, color='green')
ax[1, 0].scatter(x, y03, color='blue')
ax[1, 1].scatter(x, y04, color='yellow')

ax[0, 0].set_title('y01')
ax[0, 1].set_title('y02')
ax[1, 0].set_title('y03')
ax[1, 1].set_title('y04')

fig.tight_layout()
plt.show()

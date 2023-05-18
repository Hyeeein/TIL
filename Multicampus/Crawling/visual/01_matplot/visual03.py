import matplotlib.pyplot as plt

# 도화지의 크기 조절
fig = plt.figure(figsize=(10, 5))

ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(1, 2, 2)

x = [1, 2, 3, 4, 5]
y01 = list(map(lambda x: x**2, x))
y02 = list(map(lambda x: x**3, x))

ax01.plot(x, y01, color='r', label='pow2')
ax01.plot(x, y02, color='b', label='pow3')

plt.legend()
plt.show()

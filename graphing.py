import matplotlib.pyplot as plt

y = [i for i in range(-10,10, 2)]
x = [i for i in range(len(y))]

plt.plot(x, y)
plt.scatter(x, y)
plt.show()

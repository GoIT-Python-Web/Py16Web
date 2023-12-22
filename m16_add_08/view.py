import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

x = np.linspace(-1, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Налаштувати графік
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 1])
ax.axhline(y=4, color='gray', linestyle='--')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
fill_x = np.linspace(a, b)
fill_y = f(fill_x)
ax.fill_between(fill_x, fill_y, color='gray', alpha=0.5)


plt.grid()
plt.show()


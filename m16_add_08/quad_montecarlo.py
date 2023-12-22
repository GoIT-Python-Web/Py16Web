import numpy as np
import scipy.integrate as integrate


def f(x):
    return x**2


result, err = integrate.quad(f, 0, 2)  # noqa
print(result)

a = 0
b = 2
num_points = 10000000

x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, f(b), num_points)

under_curve = np.sum(y_random < f(x_random))

area = (b - a) * f(b) * under_curve / num_points

print(area)


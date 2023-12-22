import scipy.integrate as integrate


def f(x):
    return x ** 2


result, err = integrate.quad(f, a, b)  # noqa
print(result)

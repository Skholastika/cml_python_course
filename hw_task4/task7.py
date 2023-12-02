import numpy as np


def task7(v, s, last=False):
    a_tr = v.reshape(v.size, 1)
    b = np.random.randint(0, 10, size=(s, v.size))
    result = np.dot(b, a_tr)
    if last:
        return np.maximum(result, 0), b
    else:
        return np.sin(result), b


x = 5
a = np.random.randint(0, 10, size=x)
print(task7(a, 10))
print(task7(task7(a, 10)[0], 10))
print(task7(task7(task7(a, 10)[0], 10)[0], 5, True))

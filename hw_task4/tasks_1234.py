import numpy as np

print('------TASK 1------')
for item in sorted(np.random.random(10)):
    print(item)

print('\n-----TASK 2------')
m = np.zeros([8, 8], int)
m[::2, 1::2] = 1
m[1::2, ::2] = 1
print(m)

print('\n-----TASK 3------')
m1 = np.random.randint(0, 100, size=(8, 4))
m2 = np.random.randint(0, 100, size=(4, 2))
print(np.dot(m1, m2))

print('\n-----TASK 4------')
print(np.linspace(0, 1, 11, False)[1:])

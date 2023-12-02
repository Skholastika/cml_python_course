import numpy as np


def task5(a):
    if type(a) is int and a > 3:
        check = 0
        for n in range(2, a):  # range(2, round(15/2)) if we consider that M(n,m)=M(m,n)
            if a % n == 0:
                check = 1
                print('-----------------------------------')
                print(np.random.randint(0, 100, size=(n, a // n)))
        if not check:
            print(f'\nCan not bild any matrix for <{a}>\n')
        else:
            print('-----------------------------------')
            print(f'All matrices for <{a}> are build\n')
    else:
        print(f'\nCan not bild any matrix for <{a}>\n')


task5(12)
task5(5)

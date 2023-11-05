from typing import Union


def numberInInterval(number: Union[int, float]):
    if number < -100 or number > 100:
        print('-')
    else:
        print('+')


# numberInInterval(56)
# numberInInterval(-6546.8768)

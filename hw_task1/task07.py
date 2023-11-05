from typing import Union


def how_many_days(y: int, m: int):
    print(f"{y} year(s) and {m} month(s) is {(y * 12 + m)*29} day(s).")


# how_many_days(0,1)
# how_many_days(1,24)
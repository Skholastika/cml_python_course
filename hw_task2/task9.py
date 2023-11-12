import time


def timing(fn):
    current_fnc = False

    def wrapper(*args, **kwargs):
        nonlocal current_fnc
        if current_fnc:
            return fn(*args, **kwargs)
        else:
            start = time.perf_counter_ns()
            current_fnc = True
            result = fn(*args, **kwargs)
            current_fnc = False
            print(f'Taken time: {time.perf_counter_ns() - start} nanoseconds')
            return result

    return wrapper


@timing
def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


@timing
def factorial(number: int):
    result: int = 1
    for n in range(0, number):
        result *= n + 1
    return result

# print(fibonacci(20))
# print(factorial(20))

def decor(fn):
    def wrapper(*args, **kwargs):
        try:
            print(f'Function name: {fn.__name__}')
            fn(*args, **kwargs)
        except Exception as exc:
            exc = f'Error in function {fn.__name__}'
            print(exc)

    return wrapper


@decor
def fnc1():
    return '2' + 1


@decor
def fnc2(a, b):
    return a + b

# fnc1()
# fnc2(1,2)
# fnc2('1','2')
# fnc2(1, '2')

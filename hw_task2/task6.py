def not_int_exc(fn):
    def wrapping(*args, **kwargs):
        result = fn(*args, **kwargs)
        if type(result) is not int:
            raise Exception()
        else:
            return result

    return wrapping


@not_int_exc
def fn1(*args):
    result = args[0]
    for arg in args[1:]:
        result += arg
    return result


@not_int_exc
def fn2(*args):
    return args[0]

# print(fn1(55, 54, 78))
# print(fn1('55', '54', '78'))
# print(fn1(55.5, 54.0, 78))
# print(fn2(55, 54, 78))
# print(fn2('55', '54', '78'))
# print(fn2(55, 'list', 5.5))
# print(fn1(55, 'list', 5.5))

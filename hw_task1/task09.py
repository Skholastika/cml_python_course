def factorial(number: int):
    if number >= 0:
        result: int = 1
        for n in range(0, number):
            result *= n + 1
        return result
    else:
        return 'error'

#print(factorial(5))
# print(factorial(-5))
# print(factorial(0))

def factorial(number: int):
    result: int = 1
    for n in range(0, number):
        result *= n + 1
    return result


#print(factorial(5))


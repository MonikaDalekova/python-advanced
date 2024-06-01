def func_executor(*args): # аргс ми дава два тюпъла
    result = []
    for func, data in args: # тюпълът се състои от референция на функция и аргументите към нея
        result.append(f"{func.__name__} - {func(*data)}") # резултатът дава името на функцията и това, което тя връща

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
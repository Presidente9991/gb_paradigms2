"""
Задание: Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи.
Входные данные:
Число n.
Выходные данные:
n-ое число Фибоначчи.
"""


def fibonacci(n):
    if n < 1:
        return 0
    elif n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(15))

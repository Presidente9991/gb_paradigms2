"""
Задание: Напишите функцию, которая принимает массив чисел и значение X.
Функция должна возвращать массив подмассивов так, чтобы сумма чисел в каждом подмассиве была меньше или равна X.
Входные данные:
Массив чисел длиной N.
Число X.
Выходные данные:
Массив подмассивов.
"""


def subarray(array, x):
    if len(array) == 0:
        return []

    value = array[0]
    result = [[value]]
    line_sum = value
    i = 0

    for v in array:
        if v > x:
            print("Число в массиве не может быть больше чем X")
            return
        elif line_sum + v > x:
            result.append([v])
            i += 1
            line_sum = v
        else:
            result[i].append(v)
            line_sum += v

    return result


main_array = [1, 7, 3, 4, 5, 8, 2, 3, 9]
print(subarray(main_array, 10))

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        res = num_1 / num_2
    except ZeroDivisionError:
        return 'Ошибка: num_2 не может быть 0'
    except ValueError:
        return 'Ошибка: неверный тип введённых данных'
    return res
print(my_func(input("Введите num_1 = "), input("Введите num_2 = ")))
# 3. Реализовать функцию my_func(),торая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

# Решение 1

def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    return sum(sorted(my_list)[1:])
print(my_func(5, -4, 13))

#Решение 2

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 +g3
    else:
        return arg2 + arg3

print(f'Сумма наибольших аргументов равна: {my_func(float(input("Первый аргумент: ")), float(input("Второй аргумент: ")), float(input("Третий аргумент: ")))}')

#Решение 3 (разбор ДЗ)
def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Enter only a numbers'
print(my_func(5, -14, 13))

#Решение 4 (разбор ДЗ)
my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2,arg_3)
print(my_func(5, -14, 13))
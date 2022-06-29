# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

from datetime import date
birth_date = date(1990, 2, 17)
years = date.today().year - birth_date.year
if (date.today() - birth_date.replace(year=date.today().year)).days >= 0:
     age = years
else:
    age = years - 1

my_list = ['Анастасия', age, 1.77, None, True, False]

print(my_list)
print(my_list [0], type(my_list [0]))
print(my_list [1], type(my_list [1]))
print(my_list [2], type(my_list [2]))
print(my_list [3], type(my_list [3]))
print(my_list [4], type(my_list [4]))
print(my_list [5], type(my_list [5]))

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = input("Введите данные через пробел: ").split()  #  my_list разделен по пробелам. split() возвращает список подстрок
for item in range(0, len(my_list)-1, 2):                  # где for  in - цикл, range - присваивает последовательность чисел индексов item в соответствии с количеством введенных данных,
                                                          # 0: начало последовательности, len(my_list)-1: окончание последовательности, но не включая его, 2: step
                                                          # len(my_list) - 1, len - начнает с 1, а  range - начинает с 0, при нечетном количестве у последнего индекса не будет пары на замену - выдает ошибку
    my_list[item], my_list[item + 1] = my_list[item + 1], my_list[item]
print(my_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month_number = int(input("Введните номер месяца:   "))
season_list = ['зима', 'весна','лето','осень']
season_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}

if month_number == 1 or month_number == 2 or month_number == 12:
    print(season_list[0])
    print(season_dict.get(1))
elif month_number == 3 or month_number == 4 or month_number ==5:
    print(season_list[1])
    print(season_dict.get(2))
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(season_list[2])
    print(season_dict.get(3))
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(season_list[3])
    print(season_dict.get(4))
else:
    print("Ошибка ввода данных")


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

string = input("Введите строку из нескольких слов, разделённых пробелами: ").split()
ind = 1
for el in string:
    print(str(ind) + ': ' + el[0:10])
    ind += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент рейтинга:  '))
new_el = int(new_el)
while True:
    idx = None
    for id, el in enumerate(my_list):
     if new_el > el:
        idx = id
     if idx is None:
        my_list.append(new_el)
     else:
        my_list.insert(idx, new_el)
     break

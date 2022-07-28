# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

file = open('my_file.txt', 'w')
line = input('Введите текст \n')
while line:
    file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

file.close()

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# Решение 1
file = open(r'C:\Users\Illa\PycharmProjects\pythonProject1\file_for_task_2.txt', 'r', encoding='utf-8')
string = file.readlines()
print(f'Количество строк - {len(string)}')

file = open(r'C:\Users\Illa\PycharmProjects\pythonProject1\file_for_task_2.txt', 'r')
string = file.readlines()
ind_line = 0
ind_words = 0
for word in string:
    words = word.split()
    ind_words = len(words)
    ind_line += 1
    print(f'Строка: {ind_line}, слов: {ind_words}')

file.close()

# Решене №2 (из разбора)
with open(r'C:\Users\Illa\PycharmProjects\pythonProject1\file_for_task_2.txt', 'r', encoding='utf-8') as f:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')

lines_n = 0
words_n = 0
f = open(r'C:\Users\Illa\PycharmProjects\pythonProject1\file_for_task_2.txt', 'r')
for line in f:
    lines_n += 1
    words = line.split()
    words_n += len(words)
f.close()
print(lines_n)
print(words_n)


# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open(r'C:\Users\Illa\PycharmProjects\pythonProject1\file_for_task_3.txt', 'r', encoding='utf_8') as my_file:
    sum = 0
    lastnames = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        i[1] = float(i[1])
        sum += i[1] / len(my_list)
        if i[1] < 20000.00:
            lastnames.append(i[0])
    print(f'{lastnames}, \n средний оклад: {sum}')
my_file.close()

#Решение 2 (с разбора ДЗ)
with open(r'C:\Users\Illa\PycharmProjects\pythonProject1\file_for_task_3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

#Решение 1

en = ['one', 'two', 'three', 'four']
ru = ['один', 'два', 'три', 'четыре']

translate = dict(zip(en, ru))

with open('file_for_task_4.txt', 'r', encoding='utf-8') as my_file:
    with open('file_for_task_4n.txt', 'w', encoding='utf-8') as new_file:
        for line in my_file:
            for word in en:
                line = line.replace(word, translate[word])
            new_file.write(line)

#Решение 2 - с разбора

rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('file_for_task_4n.txt', 'w', encoding='utf-8') as new_file:
    with open('file_for_task_4.txt', 'r', encoding='utf-8') as my_file:
        new_file.write(str([line.replace(line.split()[0], rus.get(line.split()[0])) for line in my_file]))

from googletrans import Translator
with open('file_for_task_4n.txt', 'w', encoding='utf-8') as new_file:
    with open('file_for_task_4.txt', 'r', encoding='utf-8') as my_file:
        text = my_file.read()
    t = Translator()
    a = t.translate(text)
    print(a)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

#Решение 1

import random
with open('file_for_task_5.txt', mode='w+', encoding='utf-8') as f:
    i = 0
    list = []
    while i < 4:
        num = random.randint(0, 5)
        list = list + [num]
        i += 1
    for n in list:
        s = str(n)
        f.write(s + ' ')
    print(sum(list))

# Решение 2 - с разбора

from random import randint
with open('file_for_task_5.txt', mode='w+', encoding='utf-8') as f:
    f.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))

# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
#Решение 1
import re
my_dict = {}
with open('file_for_task_6.txt', 'r', encoding="utf-8") as f:
    for line in f:
        subject, total = line.split(':')
        my_list = total
        num = [int(num) for num in re.findall(r'-?\d+\.?\d*', my_list)]
        print(subject, ':', sum(num))

#Решение 2 - с разбора
mydict = {}
with open("file_for_task_6.txt", encoding="utf-8") as f:
    for line in f:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        mydict[name] = name_sum
print(f"{mydict}")

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
## Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста

#Решение 1
import json

with open('file_for_task_7.json', 'w') as jsn_file:
    with open('file_for_task_7.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        positive_avr_profit = [g for g in profit.values() if g >= 0]
        result = [profit, {'avarage_profit': sum(positive_avr_profit) / len(positive_avr_profit)}]

    json.dump(result, jsn_file)


#Решение 2 - из разбора
import json

with open('7.json', 'w') as fw:
    with open('7.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, fw, ensure_ascii=False, indent=4)
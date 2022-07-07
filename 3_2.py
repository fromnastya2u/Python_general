#2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, phone_number):
     return' '.join([name, surname, year, city, email, phone_number])
print(my_func(surname = 'Фамилия', name = 'Имя', year = '1995', city = 'Город', email = 'example@mail.ru', phone_number = '8-911-100-22-33'))
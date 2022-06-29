#1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

a = 'мой кот спит по'
b = 20
c = 'часов в день'
print (a, b, c)

a = input ('Введите имя вашего кота: ')
b = int (input ('Сколько часов спит ваш кот?'))
print (a, 'спит', b, 'часов в день')

#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

SECOBDS_IN_HOUR = 3600
SECONDS_IN_MINUTES = 60

time = int(input('Inter time in seconds: '))
hours = time // SECOBDS_IN_HOUR
minutes = (time // SECONDS_IN_MINUTES) - (hours * SECONDS_IN_MINUTES)
seconds = time % SECONDS_IN_MINUTES
print(f"{hours:02}:{minutes:02}:{seconds:02}")

#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input ('Inter number: ')
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n +n) + int(n + n + n)}")


n = input ('Inter number: ')
nn = n + n
nnn = n + n + n
i = int(n) + int(nn) + int (nnn)
print (n, '+', nn, '+', nnn, '=', i)

#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# моё решение:
# number = int(input('Введите целое положительное число:'))
# num_max = 0
# n = number
# while i > 0:
#     n = i % 10
#     if n > num_max:
#        num_max = n
#        if max == 9:
#        break
#     i = i // 10
# print(f'самая большая цифра числе {number} равна {num_max}')

# разбор
number = int(input('Введите целое положительное число:'))
num_max = number % 10
num = number

while num > 0:
    digit = num % 10
    if digit > num_max:
       num_max = digit
       if digit == 9:
           break
    num //= 10
print(f'самая большая цифра числе {number} равна {num_max}')

#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

revenue = float(input('Введите значение выручки:  '))
costs = float(input('Введите значение издержек:  '))
result = revenue - costs
if result > 0:
    print(f'Фирма работает с прибылью: {result}')
elif result == 0:
    print(f'Работаете в 0')
else:
    print(f'Убыток фирмы составляет: {-result}')

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = float(input('Введите значение выручки:  '))
costs = float(input('Введите значение издержек:  '))
result = revenue - costs
if result > 0:
    print(f'Фирма работает с прибылью: {result}, рублей')
    print(f'Рентабильность выручки составляет: {100 * (result / revenue):.2f}%')
    d = int(input('Укажите количество сотрудников:  '))
    print (f'Прибыль фирмы в расчёте на одного сотрудника составляет: {result / costs:.2f}, рублей')
elif c == 0:
    print(f'Работаете в 0')
else:
    print(f'Убыток фирмы составляет: {-result}, рублей')


# 7. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

while True:
    first_result = float(input('First day result in km.:   '))
    target_km = float(input('Target kilometers:   '))
    day_number = 1
    if first_result > target_km:
        print('Error')
    else:
        while first_result < target_km:
            first_result *= 1.1       #first_result = first_result + (first_result / 100 * 10)
            days += 1                 #day_number = day_number + 1

        print(f'Target reached at {day_number} day')
        break

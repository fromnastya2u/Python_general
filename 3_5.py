#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_num():
   sum = 0
   while True:
       list = input('Enter number or q to exit:  ').split()
       for num in list:
           try:
              number = float(num)
              sum += number
           except:
              if num == 'q':
                  print(f'Sum result: {sum}')
              else:
                  print(f'Error')
print(sum_num())



#Решение (разбор ДЗ)

# def sum_num():
#   s = 0
#   while True:
#       in_list = input('Введите числа или Q для выхода:  ').split()
#       for num in in_list:
#           if num == 'q':
#               return s
#           else:
#              try:
#                 s += int(num)
#              except ValueError:
#                 print('Для выхода нажмите q - ')
#
#       print(f'Сумма чисел = {s}')
#
# print(sum_num())
#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func():
  word = input('Input words:  ')
  print(word.title())
  if not word.isascii() and not word.isalpha():
    raise ValueError (f'Должны быть только латинские символы')

int_func()

#Решение (с разбора ДЗ)
# def int_func(word):
#     latin_char = 'qwertyuiopasdfghjklzxcvbnm'
#     return word.title() if not set(word).difference(latin_char) else False
#
# words = input('Введите строку из слов разделенных проблемами').split()
# for w in words:
#     result = int_func(w)
#     if result:
#        print(int_func(w), '  ')
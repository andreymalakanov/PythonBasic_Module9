# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 8. Колонтитул')

# Нам нужно написать программу для печати важных объявлений.
# Сверху объявления должен располагаться вот такой колонтитул:
#  ~~~~~~~~~~!!!!!!~~~~~~~~~~
# Восклицательные знаки всегда располагаются по центру строки,
# причём в зависимости от важности объявления количество восклицательных знаков может быть разным.
#
# Напишите программу,
# которая спрашивает у пользователя сначала общую длину колонтитула в символах,
# потом желаемое количество восклицательных знаков,
# после чего выводит на экран готовую строку

length = int(input('Введите длину строки: '))
EPlenght = int(input('Введите количесво восклицательных знаков: '))

if length > EPlenght:
  print('~' * ((length - EPlenght) // 2 + (length - EPlenght) % 2) + '!' * EPlenght + '~' * ((length - EPlenght) // 2))
else:
  print('!' * length)

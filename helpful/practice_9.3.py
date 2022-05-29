# Andrey Malakanov
# Skillbox PythonBasic

# Practice 9.3 - 1 
print('Задача 1. Python!')

# Напишите программу, которая выводит в отдельную строчку каждый символ фразы “Python!”.

phrase = 'Python!' 
# phrase = input('Введите фразу: ')

for symbol in phrase:
  print(symbol)

print()
print('=' * 20)
print()

# Practice 9.3 - 2
print('Задача 2. Вирус')

# Ваня экспериментирует с различного рода компьютерными вирусами, которые портят жизнь людям. На просторах Интернета он нашёл код довольно необычного вируса, который “поворачивает” весь текст в документе и повторяет каждый символ 3 раза.

#Пользователь вводит текст. Напишите программу, которая выводит каждый символ текста в отдельной строке и три раза.

# Пример:
#Введите текст: Привет!
#ППП
#ррр
#иии
#ввв
#еее
#ттт
#!!!

phrase = input('Введите текст: ')

for symbol in phrase:
  print(symbol * 3)
  
print()
print('=' * 20)
print()

# Practice 9.3 - 3
print('Задача 3.')

# Мы входим в команду разработки нового текстового редактора и нам поручили разработать для него подсчёт нужного символа в тексте, а именно - буквы Ы. Причём отдельно с верхним регистром и отдельно с нижним.

# Напишите программу, которая считает количество больших и количество маленьких букв Ы в тексте и выводит ответ на экран.

# Пример:
# Введите текст: Прыг скок
# Больших букв Ы: 0
# Маленьких букв Ы: 1

phrase = input('Введите текст: ')
BigYiCounter = 0
SmallYiCounter = 0

for symbol in phrase:
  if symbol == 'Ы':
    BigYiCounter += 1
  elif symbol == 'ы':
    SmallYiCounter += 1

print('Больших "Ы" найдено в тексте =', BigYiCounter)
print('Мальнеких "ы" найдено в тексте =', SmallYiCounter)

print()
print('=' * 20)
print()
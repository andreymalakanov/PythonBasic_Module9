# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 7. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
# 
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
# 
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5


text = input('Введите текст: ')
letterCounter = 0
lettersMax = 0

for symbol in text:
  if symbol != ' ':
    letterCounter += 1
  else:
    letterCounter = 0
  if letterCounter > lettersMax:
    lettersMax = letterCounter

print('Длина самого длинного слова:', lettersMax)
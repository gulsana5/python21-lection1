  #"===================strings/строки==================="
# строки - тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки
# строки - неизменяемый тип данных
# Синтаксис:
string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error = 'не правильная строка"
string3 = "Don't" # внутри двойных кавычек все одинарные - просто символы
string4 = '"Makers bootcamp"' # внутри одинарных кавычек все двойные - просто символы

string5 = '''
Многострочный текст 
в одинарных кавычках
Тут можно ставить "любые" 'кавычки'
"""""
'''
string6 = """
Многострочный текст 
в двойных кавычках
Тут можно ставить "любые" 'кавычки'
'''''
"""
string7 = 'hello' + '' 


"============ЭКРАНИЗАЦИЯ СТРОК============"
# экранизация спец-символов
# '\n'  перенос на новую строку
# '\t'  табуляция, таб 
# '\\'  отображение слеша(т.к он является инструкцией, которая влияет на наш код)
# '\'' отображение '
# "\"" отображение "
# '\r' возвращение каретки в начало строки
# '\v' перенос на новую строку со смещением вправо на длину предыдущей строки


'hello\nworld' 
# hello
# world

'hello\tworld'
# hello    world

'чтобы эранировать нужен символ \\'
# чтобы эранировать нужен символ \

'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello\vworld'
# hello
#      world


"=============Форматирование строк================"
title = 'Плов'
price = 1300
format1 = f'Название: {title}, Цена: {price}'
# Название: Плов, Цена: 1300

format2 = 'Название: %s, Цена: %s'
print(format2 % ("Гуляш", "250"))
print(format2 % ("Самсы", "70"))
# Название: Гуляш, Цена: 250
# Название: Самсы, Цена: 70

format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35

# методы строк

# методы типов данных - функции, к которым мы обращаемся через точку
# dir(str)  данная функция позволяет посмотреть все методы класса (типа данных)


# 'HELLO'.lower() - 'hello'
# 'hello'.upper() - 'HELLO'
# 'hello'.swapcase() - 'hELLO'
# 'heLLo'.title() - 'hello'
# 'hello world'.title() - 'Hello World'
# 'hello world'.capitalize() 'Hello world'
# 'hello'.center(11) - '  hello  '
# 'hello'.center(11, '-') - '---hello---'
# 'hello'.count('l') - 2
# 'hello hello'.count('hello') - 2
# 'hello'.count('w') - 0

# 'hello world'.startswith('hell') - True
# 'hello world'.startswith('H') - False
# 'hello world'.endswith('ld') - True

'hello world'.find(' ') #5
'hello world'.find('o') #4
'hello world'.find('wo') #6

'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hell', ' w', 'rld']

'$'.join(['hello', 'world']) # 'hello$world'
' '.join(['hello', 'world']) # 'hello world'
''.join(['hello', 'world']) # 'helloworld'


"=============Индексы================="
# индекс - порядковый номер символа в строке

# 'h e l l o   w o r l d' 
#  0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
# string[0] - "h"
# string[10] - "d"
# string[5] - " "


#срезы - это подстрока строки
# string[0:5] - 'hello'
# string[0:6] - 'hello'
# string[2:4] - 'll'
# string[0:6][2:4] - 'll'


# string[:5] - 'hello'
# string[6:] - "world"
# string[:] - 'hello world'
# string[0:11:2] - 'hlowrd'
# string[::3] - 'hlwl'
# string[::-1] - 'dlrow olleh'
# string[::-2] - 'drwolh'


#  конкатенация  - склеивание строк

# 'hello' + 'world' ---- 'helloworld'
# 'hello' + ' ' + 'world' ----- 'hello world'

# ДОП ИНФА

a = 5
b = 5
print(id(a))
print(id(b))
print(hash(a))
print(hash(b))
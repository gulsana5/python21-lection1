"=======Типы данных, Числа========"

# Tasks 1 
# Объявите переменную num со значением типа данных int и распечатайте ее
num = 3
print(num)

# Task 2 
# Объявите переменную word со значением типа данных str и распечатайте ее
word = 'hello'
print(word)

# Task 3
# Объявите переменные number и string.
# Переменной number присвойте числовое значение (целое число от 1 до 10),
# Переменной string присвойте строку (не более 10 символов).
# Умножьте переменную string на number
# Распечатайте результат
number = 5
string = 'hello'
print(number * string)

# Task 4
# Объявите две переменные x, y со значениями в виде целых чисел.
# Сложите их и распечатайте результат

x = 5
y = 5 

print(x + y)

# Task 5
# Создайте две переменные x, y со значением типа int.
# Разделите первое на второе и распечатайте результат

x = 1
y = 5
print(x / y)

# Task 6
# Создайте 2 переменные positive и negative

# positive - положительное целое число
# negative - отрицательное целое число
# Распечатать модули этих чисел, при помощи встроенной функции abs()
positive = 5
negative = -5
print(abs(positive))
print(abs(negative))

# Task 7
# Создайте целое число x.
# Возведите его в куб с помощью встроенной функции
# Распечатайте результат.
x = 5
print(pow(x, 3))

# Task 8
# Создать две переменные x, y со значением типа int.
# Найдите остаток от деления первого на второе и распечатайте результат.
x = 9
y = 5
print(x % y)

# Task 9
# Создать целое число y.
# Возведите его в квадрат и найдите остаток от деления на 5 и распечатайте результат.
y = 5
print(y ** 2 % 5)

# Task 10
# Примите от пользователя 3 числа inp1, inp2, inp3 из вкладки INPUT,
# Перемножьте первые два числа,
# Найдите остаток от деления на третье число.
# Распечатайте полученный результат.
inp1 = int(input())
inp2 = int(input())
inp3 = int(input())
res = inp1 * inp2 % inp3
print(res)

# Task 11
# Примите от пользователя 2 целых числа num1, num2,
# Cоздайте ещё одну переменную num3 со значением типа float.
# Найдите остаток от деления первых двух чисел,
# Умножьте остаток на третье число
# Распечатайте результат
num1 = int(input())
num2 = int(input())
num3 = float()
num4 = num1 % num2
num5 = num4 * num3
print(num5)

# Task 12
# Создать десятичное число с переменной decimal.
# Найдите и распечатайте его квадрат, куб, квадратный корень.
# Note: Каждое вычисление записывайте в новый принт
decimal = 5.6
print(decimal ** 2)
print(decimal ** 3)
print(decimal ** 0.5)

# Task 13
# В переменные a, b запишите два числа, которые будут обозначать два катета прямоугольного треугольника .
# Рассчитайте длину гипотенузы треугольника c, воспользовавшись теоремой Пифагора.
# Note: Теорема Пифагора: a ** 2 + b ** 2 = c ** 2.

# Распечатайте результат
a = 2 
b = 2
c = (a ** 2 + b ** 2) ** 0.5
print(c)

# Task 14
# Задать радиус окружности в переменной r.
# Рассчитайте площадь окружности в переменной s.
# Для получения числа π можете воспользоваться модулем math.
# Распечатайте результат
from math import pi
r = 12
s = pi * r ** 2
print(s) 

# Task 15
# Объявите три переменные с целочисленными значениями first, second, third.
# Затем обменяйте их значения в одно действие.
# Переменной first присвойте значение переменной second.
# Переменной third присвойте значение переменной first.
# Переменной second присвойте значение переменной third.

first = 4
second = 5
third = 6
first, third, second = second, first, third



"=======================Строки========================="
# Task 1
# Присвойте переменной string любую строку.
# Распечатайте первый символ этой строки.

string = 'hello'
print(string[0])

# Task 2 
# Присвойте переменной string любую строку.
# Выведите последний символ этой строки.

string = 'hello'
print(string[-1])

# Task 3
# Задайте любую строку переменной string,
# Распечатайте последние 2 символа.

string = 'hello'
print(string[-2:])

# Task 4
# Объявите переменную string со значением в виде любой строки.
# Затем переверните её и распечатайте результат.
# Например, если перевернуть строку:

# python 
# получим в результате:nohtyp 

string = 'bootcamp'
print(string[::-1])

# Task 5
# Объявите две переменные string1, string2 со значениями в виде любых строк.
# Затем склейте их в одну строку через пробел.
# Выведите получившуюся строку в терминал.
# Например, если в переменных хранятся строки 'makers' и 'bootcamp', в результате получим:

# makers bootcamp 

string1 = 'makers'
string2 = 'bootcamp'
print(string1, string2)

# Task 6
# Объявите переменную string со значением в виде любой строки.
# Продублируйте ее 4 раза.
# Распечатайте результат. Например, если в переменной string будет строка 'hey', в результате получим:
# heyheyheyhey 
# размножить строку можно с помощью арифметического оператора умножения

string = 'hey'
print(string * 4)

#Task 7
# Объявите переменную string со значением в виде любой строки.
# Выведите её длину в консоль.
# К примеру, если в string хранится строка 'world', результат будет:

# 5 
# для вывода длины строк, списков, словарей, множеств в Python существует встроенная функция len()

string = 'world'
print(len(string))

# Task 8
# Создайте переменную string со значением 'The quick brown fox jumps over the lazy dog'.
# Замените все повторения буквы o символом * и сохраните результат в новой переменной.
# Распечатайте новую переменную.
# Результат должен быть:

# The quick br*wn f*x jumps *ver the lazy d*g

# Создайте переменную string со значением 'The quick brown fox jumps over the lazy dog'.
# Замените все повторения буквы o символом * и сохраните результат в новой переменной.
# Распечатайте новую переменную.
# Результат должен быть:

# The quick br*wn f*x jumps *ver the lazy d*g

string = 'The quick brown fox jumps over the lazy dog'
new_string = string.replace('o', '*')
print(new_string)

#Task 9
# Создайте переменную string со значением в виде любой строки.
# Переведите все её символы в верхний регистр.
# Распечатайте результат.
# К примеру, если в string у нас строка:

# world 
# результатом будет:

# WORLD 
# используйте встроенные метод upper()

string = ' world'
print(string.upper())   #результат WORLD

# Task 10
# Объявите переменную string со значением в виде любой строки.
# Переведите все её символы в нижний регистр.
# К примеру, если в string хранится строка:

# БЕГИ ФОРЕСТ, БЕГИ!
# результат в терминале будет:

# беги форест, беги! 

string = 'WORLD'
print(string.lower())

# Task 11
# Создайте переменную string со значением в виде любой строки.
# Обменяйте местами первый и последний символы и выведите результат в консоль.(ваш код должен работать со строками любой длины)
# К примеру, если в string хранится строка:

# Hello
# результат в терминале будет:

# oellH 
# используйте срезы(индексацию строк) и конкатенацию(склеивание строк)

string = 'Hello world'
result = string[-1] + string[1:-1] +string[0]
print(result)

# Task 14
# Создайте переменную string со значением в виде любой строки.
# Выведите только символы с нечётными индексами при помощи срезов.
# Например, если в string хранится строка:

# 'Makers bootcamp' 
# в результате получим:

# aesbocm 

string = 'bootcamp'
result = string[1::2]
print(result)

# Task 15
# Объявите переменную string со значением в виде любой строки.
# Поменяйте шестую букву на K.
# Например, если в переменной хранится данная строка:

# 'abracadabra' 
# в результате получим:

# abracKdabra 
string = 'bootcamp'
result = string[:5] + 'K' + string[6:]
print(result)



#  "======= Логические Выражения if .... else ======="
# Task 1

# Дано число введенное пользователем в переменной number.
# Если число в переменной number больше 0 вывести True, иначе False.
# Для проверки кода введите число в поле во вкладке INPUT.
# Например, если в number ввели число:

# 21 
# в результате получим:

# True 

number = int(input())
if number > 0:
    print(True)
else:
    print(False)

# Task 2
# Проверить переменную string, куда попадает строка введенная пользователем.
# Если длина строки больше 5 символов вывести True, иначе False.
# Для проверки кода введите строку в поле во вкладке INPUT.
# Например, если в string ввели:

# 'Here, there, and everywhere' 
# результат должен быть:

# True 
string = input()
if len(string) > 5:
    print(True)
else:
    print(False)

# Task 3
# Проверить введенное переменную mark, куда попадает введенное пользователем значение.
# Если значение mark больше или равно 90, вывести строку Отлично, Ваша оценка 5!,
# Если значение больше или равно 80, вывести Здорово, Ваша оценка 4!,
# Если значение больше или равно 70, вывести Хорошо, Ваша оценка 3!,
# Если значение больше или равно 60, вывести Вам стоит подучить материал,
# в других случаях вывести строку Вы не сдали экзамен.
# Для проверки кода введите значение в поле во вкладке INPUT.
# Если в mark ввели:

# 95 
# результат будет:

# Отлично, Ваша оценка 5! 
mark = int(input())

if mark >= 90:
    print('Отлично, Ваша оценка 5!')
elif mark >= 80:
    print('Здорово, Ваша оценка 4!')
elif mark >= 70:
    print('Хорошо, Ваша оценка 3!')
elif mark >= 60:
    print('Вам стоит подучить материал')
else:
    print('Вы не сдали экзамен')

# Task 4
# Проверить введенное пользователем число в переменной number:
# Если число отрицательное вывести строку negative,
# если положительное то positive,
# если number равно 0 то вывести zero.
# Для проверки кода введите значение в поле во вкладке INPUT.
# Например, если в number число:

# 0 
# результат будет:
# zero 
number = int(input())

if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    print('zero')

# Task 5
# Создать два целых числа x, y.
# Выведите значение наименьшего из них.
# Например, если в наших переменных хранятся числа 42 и 24, результат будет:

# 24 
x = 5 
y = 4
if x < y:
    print(x)
else:
    print(y)

# Task 6
# Создать три целых числа x, y, z.
# Выведите значение наименьшего из них.
# К примеру, если в переменных у нас числа: 102, 36, 90, вывод в терминал будет

# 36 
x = 6
y = 4
z = 8
if x < y and x < z:
    print(x)
elif y < x and y < z:
    print(y)
else:
    print(z)

# Task 7
# Создать три целых числа в переменных x, y, z. Определите, сколько среди них совпадающих.

# Программа должна вывести одно из чисел:

# 3 - если все числа совпадают,
# 2 - если два числа совпадают
# 0 - если все три числа разные.
# Например, если в переменных у нас числа - 32, 32 и 100, вывод будет:
x = 5
y = 5
z = 8
if x == y and y == z:
    print(3)
elif x == y or y == z or z == x:
    print(2)
else:
    print(0)

# Task 8
# В переменные x, y попадают числа вводимые пользователем. Проверить делится ли первое число на второе без остатка.
# Программа должна вывести на экран следующую информацию:
# частное - выводить в любом случае
# если число делится с остатком, вывести остаток от деления
# Например, если во вкладке INPUT ввести числа 675 и 23, вывод должен быть:
# x не делится на y
# Частное: 29
# Остаток: 11
# если в переменные получили числа 10 и 2, вывод должен быть

# x делится на y
# Частное: 5
x = int(input())
y = int(input())

if x % y == 0:
    print('x делится на y')
    print('Частное:', x // y)
elif x % y != 0:
    print('x не делится на y')
    print('Частное:', x // y)
    print('Остаток:', x % y)

# Task 9
# В переменную year попадает число-год от пользователя.
# Определите, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Note: в соответствии с григорианским календарем, год является високосным в двух случаях: 1) если число года делится без остатка на 4 и НЕ делится на 100, 2) либо число года делится без остатка на 400.
# Например, если в INPUT введен год 1996, вывод должен быть:

# YES 
# т.к число 1996 делится без остатка на 4, но не делится на 100
year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print('YES')
else:
    print('NO')

# Task 10
# Создайте список чисел nums и число target.
# С помощью условных операторов выведите, есть ли число в этом списке, если есть выведите в консоль Да, если нет выведите Нет.
# Например, если дан список [1, 15, 36, 88], а в переменной target хранится число 15, вывод будет:

# Да 
nums = [1, 15, 36, 88]
target = 15
if target in nums:
    print('Да')
else:
    print('Нет')

# Task 11
# В переменную num из вкладки INPUT попадает число, которое обозначает код символа по таблице ASCII(https://ru.wikipedia.org/wiki/ASCII)
# Определить, является ли введенное число кодом английской буквы.
# Если число является кодом буквы, вывести сообщение:

# Это буква "буква" 
# в ином случае, вывести сообщение:

# Это не буква, а символ "символ" 
# Например, если число num равно 43:

# Это не буква, а символ "+"
# Для числа 65:

# Это буква "А"
# найдите и используйте специальную функцию Python, возвращающую числовое значение Unicode элемента
num = int(input())
if chr(num) in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
    print(f'Это буква "{chr(num)}"')
else:
    print(f'Это не буква, а символ "{chr(num)}"')
#                  ВВЕДЕНИЕ В ООП

# Task1   OOP

# Создайте класс для песен Song. Каждая песня имеет название - title, автора - author и год выпуска - year.

# Добавьте три метода:

# show_author

# show_title

# show_year

# выводящие утверждения о каждом атрибуте экземпляра класса Song.

# Создайте экземпляр song класса Song с вашей любимой песней и примените все методы.

# Например:

# song.show_title()
# song.show_author()
# song.show_year()
# Вывод:

# Название этой песни Happy
# Автор этой песни Pharrell Williams
# Эта песня вышла в 2013 году

class Song:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_title(self):
        return f'Название этой песни {self.title}'
    
    def show_author(self):
        return f'Автор этой песни {self.author}'

    def show_year(self):
        return f'Эта песня вышла в {self.year} году'

song = Song('Happy', 'Pharrell Wllliams', 2013)
print(song.show_title())
print(song.show_author())
print(song.show_year())


# Task 2


# Cоздайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, в переменной color, и число Пи(3.14) - в переменной pi.

# Экземпляры класса Circle в свою очередь должны иметь обязательное свойство - радиус, в переменной radius.

# К примеру, создадим объект с радиусом 2:

# circle = Circle(2) 
# Также, класс должен иметь метод расчета площади круга - get_area():

# circle.get_area() 
# Возвращает:

# 12.56 
# формула расчета площади: число Пи умножить на радиус в квадрате

# cоздайте экземпляр класса,
# переопределите цвет экземпляра и
# примените метод get_area().
# Распечатывать результат не нужно, методы должны возвращать результат ключевым словом return.

class Circle:
    color = "Синий"
    pi = 3.14
    def __init__(self,radius):
       self.radius = radius

    def get_area(self):
        return self.pi * self.radius ** 2

circle = Circle(2)
circle.color = "Красный"
print(circle.color)
print(circle.get_area())

# Task 3
# Создайте класс BankAccount, у объектов данного класса есть аттрибут balance со значением по умолчанию 0: balance = 0.

# Определите метод withdraw с параметром amount, который будет отнимать сумму от баланса и распечатывать текущий баланс.

# Добавьте еще один метод deposit, который также имеет параметр amount и соответсвенно добавляет сумму к балансу и распечатывает баланс.

# Например:

# account.deposit(1000) 
# account.withdraw(500) 
# Получим такой вывод:

# Ваш баланс: 1000 сом 
# Ваш баланс: 500 сом 
# в начале, увеличили переменную balance на 1000, затем уменьшили на 500, и получили в итоге 500.

class BankAccount:
    balance = 0

    def withdraw(self, amount):
        self.amount = amount
        BankAccount.balance -= amount
        print(f'Ваш баланс: {BankAccount.balance} сом')

    def deposit(self, amount):
        self.amount = amount
        BankAccount.balance += amount
        print(f'Ваш баланс: {BankAccount.balance} сом')

account = BankAccount()

account.deposit(1000) 
account.withdraw(500)

# Task 4
# Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании - name, стоимость посадки - cost, стоимость за каждый пройденный километр - cost_km.

# Добавьте к классу метод get_total_cost, принимающий параметр km - сколько километров составила поездка и возвращающий стоимость поездки.

# Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждой из них.

# Например:

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  
# Вывод:

# Такси Namba, стоимость поездки: 179 сом 
# Такси Yandex, стоимость поездки: 127 сом 
# Такси Jorgo, стоимость поездки: 238 сом  

class Taxi:

    def __init__(self, name, cost, cost_km):
        self.name = name
        self.cost = cost
        self.cost_km = cost_km

    def get_total_cost(self, km):
        sum_price = self.cost + self.cost_km * km
        return f"Такси {self.name}, стоимость поездки: {sum_price} сом"

taxi1 = Taxi("Namba", 45, 12)
taxi2 = Taxi("Jorgo", 46, 13)
taxi3 = Taxi("Yandex", 50, 14)

print(taxi1.get_total_cost(5)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(7)) 

# Task 5
# Создайте класс телефонной книги Phone. У контактов должны быть такие аттрибуты:

# name - имена
# last_name - фамилии
# phone - телефонные номера
# Добавьте метод get_info, который выводит информацию о контакте в следующем виде:

# contact.get_info()
# Вывод в терминал:

# Контакт: John Snow, телефон: +996707707707
# Затем, создайте объект от класса Phone в переменной contact и примените метод get_info.
class Phone:
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone
    
    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

contact = Phone('John', 'Snow', 996707455123)

contact.get_info()

# Task 6
# Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - percent = 8, обозначающий процент налога на ежемесячную зарплату - 8%.

# Объекты класса должны иметь, в качестве атрибутов сумму зарплаты salary и стаж работы в месяцах - experience.

# Также у класса должен быть метод count_percent, расчитывающий сумму налога заплаченного за весь стаж работы.

# Создайте экземпляр класса obj и посчитайте сумму вашего налога.

# К примеру, если у вашего объекта salary имеет значение 10000, а experience равен 10, то:

# print(obj.count_percent()) 
# Выдаст вам такой результат в терминале:

# 8000.0 
# Каждый месяц с зарплаты в 10000 сомов снимается 8% на налоги, т.е 800 сом, за 10 месяцев трудового стажа эта сумма будет 8000.0 сом

class Salary:
    percent = 8

    def __init__(self, salary, experience):
        self.salary = salary
        self.experience = experience

    def count_percent(self):
        return self.salary / 100 * 8 * self.experience 
obj = Salary(10000, 5000)

print(obj.count_percent()) 

# Task 7
# Вам дан такой код:

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())
# который выводит в терминал такие значения:

# Литература 1971 Пабло Неруда
# выиграл 51 лет назад 
# Литература 1994 Кэндзабуро Оэ 
# выиграл 28 лет назад
# Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале.

# Дату сколько лет назад была получена премия в методе get_year() не вписывать вручную, а высчитывать используя datetime

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def get_year(self):
        from datetime import datetime
        years = datetime.now().year - self.year
        return f"выиграл {years} лет назад"

winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())

# Task 8 
# В Python есть два специальных метода __str__ и __repr__. Эти методы чаще всего работают без нашего вмешательства, к примеру метод __str__ мы никогда напрямую не вызывали, но он срабатывал каждый раз как мы использовали print().

# Метод __str__ возвращает понятное человеку, строковое представление объекта. __str__ можно легко переопределять внутри класса и изменять вид в котором мы распечатываем объект.

# К примеру, у нас есть класс и созданный от него объект, который мы попробуем распечатать:

# class MyClass: 
#      def __init__(self, name): 
#          self.name = name

# obj = MyClass('первый объект')

# print(obj)
# в результате получим данную запись в терминале:

# <__main__.MyClass object at 0x7f53ba5948b0> 
# однако, если мы перепишем метод __str__, который также как и __init__ принимает в аргументы self, можем поменять поведение объекта при использовании print().

# Допустим, мы хотим чтобы в терминале выводился аттрибут объекта name:

# class MyClass: 
#      def __init__(self, name): 
#          self.name = name 

#      def __str__(self): 
#          return self.name

# obj = MyClass('первый объект') 
# print(obj) 
# здесь мы получили доступ к аттрибуту name через ссылку на сам объект в self - self.name, и возвратили в качестве конечного результата работы метода __str__ с помощью return.

# Получаем в терминале:

# первый объект 
# В свою очередь, метод __repr__ возвращает объект в том виде в котором мы можем его распечатать, при этом он не заботится о том чтобы запись была понятна обычным людям.

# Задача __str__ состоит в том чтобы быть читаемым, задача же __repr__ состоит в том чтобы быть конкретным.

#  ЗАДАНИЯ 8

# Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:

# В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15, если условие не соблюдено, должны выйти ошибка с текстом:
# Password should be longer than 8, and less than 15 
# Вторая проверка должна проверять что пароль содержит цифры, и в случае отсутствия цифр, выводить ошибку с текстом:
# Password should contain numbers too 
# Третья проверка, проверяет содержит ли пароль буквы и в случае не совпадения, выводит ошибку с текстом:
# Password should contain letters as well 
# В конце проверьте, содержит ли пароль хотя бы один из символов: '@', '#', '&', '$', '%', '!', '~', '*', если условие не выполнено выводите ошибку с текстом:
# Your password should have some symbols 
# если одно из условий не выполнено, выводите соответствующее исключение, если же все условия выполнены метод validate должен возвращать строку:

# Ваш пароль сохранен.
# Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась строка из звездочек количество которых равно длине пароля.

# К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********

# пишите код для проверки пароля в указанном порядке
class Password(str):
    def validate(self):
        if len(self) < 8 or len(self) > 15:
            raise Exception('Password should be longer than 8, and less than 15')
        letter = False
        number = False
        symbol = False
        
        for s in self:
            if s.isalpha():
                letter = True
            if s.isdigit():
                number = True
            if s in ('@', '#', '&', '$', '%', '!', '~', '*'):
                symbol = True
        
        if not number:
            raise Exception('Password should contain numbers too')
        if not letter:
            raise Exception('Password should contain letters as well')
        if not symbol:
            raise Exception('Your password should have some symbols')
        return 'Ваш пароль сохранен.'
    def __str__(self):
        return '*' * len(self)

# Task 9
# Создайте класс Math, у экземпляра которого должно быть свойство value. У классa Math должно быть 3 метода:

# get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

# get_sum - возвращает сумму цифр числа

# get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25
# 5x6=30
# 5x7=35
# 5x8=40
# 5x9=45
# 5x10=50
# Создайте экземпляр класса и примените к нему все методы.

# Например, если экземпляром класса Math является число 11,

# вызов get_factorial возвратит такой результат:

# 39916800 
# т.к 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 = 39916800

# метод get_sum, возвратит:

# 2 
# т.к число 11 состоит из двух цифр 1 и 1, сумма 1 + 1 = 2

# метод get_mul_table возвратит:

# 11 x 1 = 11 
# 11 x 2 = 22 
# 11 x 3 = 33 
# 11 x 4 = 44 
# 11 x 5 = 55 
# 11 x 6 = 66 
# 11 x 7 = 77 
# 11 x 8 = 88 
# 11 x 9 = 99 
# 11 x 10 = 110 
# результат методов возвращайте ключевым словом return, print() использовать не надо.

class Math:
    def __init__(self, value):
        self.value = value
    def get_factorial(self):
        fact = 1
        for num in range(1, self.value + 1):
            fact = fact * num
        return fact
    def get_sum(self):
        sum_ = 0
        for num in str(self.value):
            sum_ += int(num)
        return sum_
    def get_mul_table(self):
        res = ""
        for i in range(1, 11):
            res += f"{self.value}x{i}={self.value*i}\n"            
        return res
obj = Math(5)    
obj.get_factorial()
obj.get_sum()
obj.get_mul_table()
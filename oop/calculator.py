import string


class Calc:
    def __init__(self, color):  # добовляем цвет
        self.color = color


    def add(self, a, b):
        "Функция сложения"
        return a + b

    
    def sub(self, a, b):
        "Функция вычитания" 
        return a - b


    def mul(self, a, b):
        "Функция умножения"
        return a * b


    def div(self, a, b):
        "Функция деления"
        return a / b


    def true_dif(self, a, b):
        "Функция целочисленного деления"
        return a // b


    def mod(self, a, b):
        "Функция нахождения остатка от деления"
        return a % b


    def divmod(self, a, b):
        "Функция возвращает число и остаток от деления"
        return self.true_div(a, b), self.mod(a, b)


    def pow(self, a, b):
        "Функция возведения числа в степень"
        return a ** b


    def sqrt(self, a, ndigits=2):
        "Функция нахождения квадратного корня числа с округлением"
        # return A ** 0,5
        import math
        sqrt_num = math.sqrt(a)
        return round(sqrt_num, ndigits)


    def percent(self, total, _percent):
        "Функция нахождения процента от числа"
        return (total * _percent) / 100


    def __str__(self):
        return f"{self.color}" #  калькулятор


obj1 = Calc("синий")
obj2 = Calc("фиолетовый")


obj1.add(4,5) # 9
obj2.add(4,5) # 9

print(str(obj2))
print(str(obj1))



string = input()
res = eval(string) # короткий калькулятор не желательно использовать
print(res)           # exec - это как rm-rf


print(eval(input()))  # - 1 строчка места 3 строчки кода 1 в 1 верхним кодам







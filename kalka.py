number1 = int(input('Введите первое число:'))
number2 = int(input('Введите второе число:'))
number3 = input('Действие')

if number3 == '+':
    result = number1 + number2
    print(result)
elif number3 == '/':
    result = number1 / number2
    print(result)
elif number3 == '%':
    result = number1 % number2
    print(result)
elif number3 == '**':
    result = number1 ** number2
    print(result)
elif number3 == '//':
    result = number1 // number2
    print(result)
elif number3 == '*':
    result = number1 * number2
    print(result)
elif number3 == '-':
    result = number1 - number2
    print(result) 
else:
    print('Данный операции нет списке')

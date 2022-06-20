try:
    num1 = int(input('Введите первую число: '))
    num2 = int(input('Введите второе число: '))
    result = num1 / 2
except ZeroDivisionError:
    print('На ноль делить нельзя')
else:
    print(result)
finally:
    print('Программа завершена')
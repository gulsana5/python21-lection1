
import random

compGuess = random.randint(1, 30)
userGuess = 0
name = input('Приветствую! Давайте сыграем в игру. Как вас зовут? ')

while userGuess != compGuess:
    userGuess = int(input(f'{name}, введите ваше число от 1 до 30: '))
    if userGuess < compGuess:
        print('Число должно быть больше!')
    elif userGuess > compGuess:
        print('Число должно быть меньше!')
    else:
        print('Вы угадали, это число ' + str(userGuess))
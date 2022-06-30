import random
def hangman():
    print('Привет')

WORDS = ('машина трактор велосипед самакат ролик мотоцикл')
word = random.choice(WORDS)
guesses = 'уеыиаяюйо'
letters = 5

while letters > 0:
    missed = 0
for letter in letters:
    if letter  in guesses :
        print(letter,end=' ')
    else:
            print(' ',end= ' ')
            letters += 1 
            
if letters == 0:
    print('\nТы выграл!')
    

letters = input('\nНазови букву: ')
guesses += letters

if letters not in WORDS:
    letters -= 1
    print('\Не угодал. ')
    print('\n', 'осталось попыток:', turns)
    if letters < 5: print('\n | ')
    if letters < 4: print('  0  ')
    if letters < 3: print(' /|\ ')
    if letters < 2: print('  |  ')
    if letters < 1: print(' / \ ')
    if letters == 0: print('\n\nЭто слово: ',word)

ans = 'да'
while ans == 'да':
    print('Хочешь сыграть снова? (да или нет)')
    ans = input()
"========================Принципы ООП=============================="
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация

import pygame

pygame.init()


dis = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Змейка на питоне')

blue = (0,0,350)
red = (350,0,0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis,blue,[200,150,10,0])
    pygame.display.update()
pygame.quit()
quit()



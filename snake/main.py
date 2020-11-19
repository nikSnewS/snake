import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))
    # drawing snake,apple
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            dx, dy = 0, -1
        if key[pygame.K_s]:
            dx, dy = 0, 1
        if key[pygame.K_a]:
            dx, dy = -1, 0
        if key[pygame.K_d]:
            dx, dy = 1, 0






















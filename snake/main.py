import pygame
from random import randrange

RES = 1000
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 50
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10
slize = (0, 0)
game_over = False
stone = (randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE), randrange(1, 4))

pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)

img = pygame.image.load('1.jpg').convert_alpha()
img_apple = pygame.image.load('apple.png').convert_alpha()
img_face = pygame.image.load('snakeface.png').convert_alpha()
img_body = pygame.image.load('body.png').convert_alpha()
img_tail = pygame.image.load('tail.png').convert_alpha()
img_slaze = pygame.image.load('slize.png').convert_alpha()

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:
    if game_over:
        render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
        surface.blit(render_end, (RES // 2 - 200, RES // 3))
        pygame.display.flip()
        close_game()
    else:
        surface.fill('black', (0,0, RES, RES))
        surface.blit(img, (0, 0))
        # drawing snake, apple
        # [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake[1:-1]]
        [surface.blit(img_body, (i,j)) for i, j in snake[1:-1]]
        surface.blit(img_tail, snake[0])
        surface.blit(img_face, snake[-1])
        # pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
        surface.blit(img_apple, apple)
        # show score
        render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
        surface.blit(render_score, (5, 5))
        # snake movement
        speed_count += 1
        if not speed_count % snake_speed:
            x += dx * SIZE
            y += dy * SIZE
            if x < 0: x = RES - SIZE
            if x > RES - SIZE: x = 0
            if y < 0: y = RES - SIZE
            if y > RES - SIZE: y = 0
            snake.append((x, y))
            snake = snake[-length:]
    # eating food
    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        while apple in snake:
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 10)
    # stone
    pygame.draw.rect(surface, pygame.Color('grey'), (stone[0], stone[1], SIZE*stone[2], SIZE*stone[2]))

    # attack


    # game over
    if len(snake) != len(set(snake)) or (x >= stone[0] and x <= stone[0]*stone[2] + SIZE and y >= stone[1] and y <= stone[1]*stone[2] + SIZE):
        game_over = True

    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN] and game_over:
        print(key)
        game_over = False
        x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length = 1
        snake = [(x, y)]
        dx, dy = 0, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
        score = 0
        speed_count, snake_speed = 0, 10

    pygame.display.flip()
    clock.tick(fps)
    close_game()
    # controls


    if key[pygame.K_w]:
        if dirs['W']:
            if dx == 1 and dy == 0:
                img_face = pygame.transform.rotate(img_face, -90)
            elif dx == -1 and dy == 0:
                img_face = pygame.transform.rotate(img_face, 90)
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    elif key[pygame.K_s]:
        if dirs['S']:
            if dx == 1 and dy == 0:
                img_face = pygame.transform.rotate(img_face, 90)
            elif dx == -1 and dy == 0:
                img_face = pygame.transform.rotate(img_face, -90)
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    elif key[pygame.K_a]:
        if dirs['A']:
            if dx == 0 and dy == -1:
                img_face = pygame.transform.rotate(img_face, 90)
            elif dx == 0 and dy == 1:
                img_face = pygame.transform.rotate(img_face, -90)
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    elif key[pygame.K_d]:
        if dirs['D']:
            if dx == 0 and dy == -1:
                img_face = pygame.transform.rotate(img_face, -90)
            elif dx == 0 and dy == 1:
                img_face = pygame.transform.rotate(img_face, 90)
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True}
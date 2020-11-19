import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(1, 2): # 0, 1, 2
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Piece'
    return False


pygame.init()
block_size = 150
margin = 10
wigth = height = block_size * 4 + margin * 5

win_size = (wigth, height)
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Крестики нолики")

pink = (250, 5, 34)
green = (0, 255, 0)
white = (255, 255, 255)
red = (130, 9, 21)
black = (0, 0, 0)
mas = [[0] * 4 for i in range(4)]
query = 0  # 1 2 3 4 5 6 7
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit((0))
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (block_size + margin)
            row = y_mouse // (block_size + margin)
            if mas[row][col] == 0:
                if query % 2 == (0):
                    mas[row][col] = 'победил X'
                else:
                    mas[row][col] = 'Победил O'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 4 for i in range(4)]
            query=0
            screen.fill(black)

    if not game_over:
        for row in range(4):
            for col in range(4):
                if mas[row][col] == 'победил X':
                    color = red
                elif mas[row][col] == 'Победил O':
                    color = green
                else:
                    color = white
                x = col * block_size + (col + 1) * margin
                y = row * block_size + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, block_size, block_size))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + block_size - 5, y + block_size - 5), 3)
                    pygame.draw.line(screen, white, (x + block_size - 5, y + 5), (x + 5, y + block_size - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + block_size // 2, y + block_size // 2), block_size // 2 - 3, 3)
        if (query - 1) % 2 == 0:  # x
            game_over = check_win(mas, 'победил X')
        else:
            game_over = check_win(mas, 'Победил O')

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('stxingkai', 80)
            text1 = font.render(game_over, True, white)
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_width() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])

    pygame.display.update()
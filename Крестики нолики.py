import pygame
pygame.init()


def check_for_win(massive, symbol):
    zeroes = 0
    for i in massive:
        zeroes += i.count(0)
        if i.count(symbol) == 3:
            return symbol

    for col in range(3):
        if massive[0][col] == symbol and massive[1][col] == symbol and massive[2][col] == symbol:
            return symbol

    if massive[0][0] == symbol and massive[1][1] == symbol and massive[2][2] == symbol:
        return symbol

    elif massive[0][2] == symbol and massive[1][1] == symbol and massive[2][0] == symbol:
        return symbol

    elif zeroes == 0:
        return 'Ничья'

    else:
        return False

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

margin = 5    # Отступ между квадратами
square_width, square_height = 100, 100    # Длина и ширина
square_color = WHITE
squares_count_horizontal, squares_count_vertical = 3, 3    # Кол-во квадратов

screen_width = squares_count_horizontal*(square_width+margin) + margin    # Ширина экрана
screen_height = squares_count_vertical*(square_height+margin) + margin    # Высота экрана
size = screen_width, screen_height    # переменная, размеры окна
screen = pygame.display.set_mode(size)    # Окно создается

board = [[0 for i in range(3)] for j in range(3)]

query = 0    # 0, 1, 2, 3, 4, 5, 6

color = WHITE

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if event.button == 1:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                mouse_row = y_mouse // (margin+square_height)
                mouse_column = x_mouse // (margin+square_width)

                if board[mouse_row][mouse_column] == 0:
                    if query % 2 == 0:
                        board[mouse_row][mouse_column] = 'x'
                    elif query % 2 == 1:
                        board[mouse_row][mouse_column] = 'o'
                    query += 1
                else:
                    pass

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill(BLACK)
            board = [[0 for i in range(3)] for j in range(3)]
            query = 0

    for row in range(squares_count_horizontal):
        for column in range(squares_count_vertical):

            if board[row][column] == 'x':
                color = RED

            elif board[row][column] == 'o':
                color = BLUE

            else:
                color = WHITE

            x = column*square_width + (column+1)*margin
            y = row*square_height + (row+1)*margin
            pygame.draw.rect(screen, square_color, (x, y, square_width, square_height))

            if color == RED:
                pygame.draw.line(screen, color, (x, y), (x+square_width, y+square_height), 5)
                pygame.draw.line(screen, color, (x+square_width, y), (x, y+square_height), 5)

            elif color == BLUE:
                x_circle = x+(square_width//2)
                y_circle = y+(square_height//2)
                radius = square_width // 2 - 5
                circle_width = 10
                pygame.draw.circle(screen, color, (x_circle, y_circle), radius, circle_width)

            else:
                pass

    if (query-1) % 2 == 0:
        game_over = check_for_win(board, 'x')
    else:
        game_over = check_for_win(board, 'o')

    if game_over:
        screen.fill(BLACK)
        font = pygame.font.SysFont('stxingkai', 80)
        text = font.render(game_over, True, WHITE)
        text_rect = text.get_rect()
        text_x = screen_width // 2 - text_rect.width//2
        text_y = screen_height // 2 - text_rect.height//2
        screen.blit(text, (text_x, text_y))

    pygame.display.update()

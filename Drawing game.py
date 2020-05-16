# Импорт библиотеки
import pygame
# Инициализация
pygame.init()

# Цвета в RGB.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (150, 75, 0)
PURPLE = (128, 0, 128)
GRAY = (47, 79, 79)
ORANGE = (255, 91, 0)
LIGHT_BLUE = (0, 191, 255)
PINK = (255, 20, 147)

# Параметры квадрата
margin = 1    # Расстояние между квадратами
square_width, square_height = 15, 15    # Высота и ширина квадратов
square_color = BLUE    # Цвет квадрата по умолчанию
square_count_horizontal, square_count_vertical = 60, 35    # кол-во квадратов по горизонтали и вертикали

# Все что связано с цветами(почти)
colors_count = 12    # Количество цветов
# Цвета в которые можно окрасить квадрат
colors = (WHITE, RED, GREEN, BLUE, YELLOW, BROWN, PURPLE, GRAY, ORANGE, LIGHT_BLUE, PINK, BLACK)
current_color = WHITE

# Окно
display_width = square_count_horizontal * (margin + square_width) + margin    # Ширина окна
display_height = square_count_vertical * (margin + square_height)+margin + 20   # Высота экрана
size = display_width, display_height
display = pygame.display.set_mode(size)    # Рисуем это окно

# Параметры тех кнопок
rect_width = (display_width-margin*(colors_count+1)) // colors_count    # Ширина кнопки

rect_height = 20    # Высота кнопки
rect_color = WHITE    # Цвет кнопки по умолчанию

# Диапозон от начала до конца высоты прямоугольника по н координате на плоскости
y_start = display_height-(rect_height+margin)    # Начало диапохона
y_end = display_height-margin    # Конец диапозона

# Координаты тех кнопок
    # Диапозон координат кнопки отвечающей за белый цвет
rect_white_pos = [
    # Диапозон по оси х, первое значение начало диапозона, второе конец диапозона
    [margin, rect_width+margin],
    # Диапозон по оси у, первое значение начало диапозона, второе конец диапозона
    [y_start, y_end]
        ]

    # Диапозон координат кнопки отвечающей за красный цвет
rect_red_pos = [
    # Диапозон по оси х, первое значение начало диапозона, второе конец диапозона
    [rect_width+(margin*2), 2*rect_width+(margin*2)],
    # Диапозон по оси у, первое значение начало диапозона, второе конец диапозона
    [y_start, y_end]
        ]

    # Диапозон координат кнопки отвечающей за зеленый цвет
rect_green_pos = [
    # Диапозон по оси х, первое значение начало диапозона, второе конец диапозона
    [rect_width*2+(margin*3), rect_width*3+(margin*3)],
    # Диапозон по оси у, первое значение начало диапозона, второе конец диапозона
    [y_start, y_end]
        ]

    # Диапозон координат кнопки отвечающей за синий цвет
rect_blue_pos = [
    # Диапозон по оси х, первое значение начало диапозона, второе конец диапозона
    [rect_width*3+(margin*4), rect_width*4+(margin*4)],
    # Диапозон по оси у, первое значение начало диапозона, второе конец диапозона
    [y_start, y_end]
        ]

    # Диапозон координат кнопки отвечающей за желтый цвет
rect_yellow_pos = [
    # Диапозон по оси х, первое значение начало диапозона, второе конец диапозона
    [rect_width*4+(margin*5), rect_width*5+(margin*5)],
    # Диапозон по оси у, первое значение начало диапозона, второе конец диапозона
    [y_start, y_end]
        ]

rect_brown_pos = [
    [rect_width*5+(margin*6), rect_width*6+(margin*6)],
    [y_start, y_end]
]

rect_purple_pos = [
    [rect_width*6+(margin*7), rect_width*7+(margin*6)],
    [y_start, y_end]
        ]

rect_gray_pos = [
    [rect_width*7+(margin*8), rect_width*8+(margin*7)],
    [y_start, y_end]
]

rect_orange_pos = [
    [rect_width*8+(margin*9), rect_width*9+(margin*8)],
    [y_start, y_end]
]

rect_LightBlue_pos = [
    [rect_width*9+(margin*10), rect_width*10+(margin*9)],
    [y_start, y_end]
]

rect_pink_pos = [
    [rect_width*10+(margin*11), rect_width*11+(margin*10)],
    [y_start, y_end]
]

rect_black_pos = [
    [rect_width*11+(margin*12), rect_width*12+(margin*11)],
    [y_start, y_end]
]

# Модель поля
board = [[0]*square_count_horizontal for i in range(square_count_vertical)]


# Игровой цикл
while True:
    # Получаем из стека содержащий события последнее событие
    for event in pygame.event.get():
        # Случай когда нажали на крестик кнопкой мыши
        if event.type == pygame.QUIT:
            quit()    # Прекратить выполнение программы

        # Случай когда событие есть нажатие на кнопку мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение инфы насчет места нажатия на кнопку мыши
            x_mouse_pos, y_mouse_pos = pygame.mouse.get_pos()    # Координаты точки, куда нажать кнопкой мыши
            # Узнать на какой именно квадрат юзер нажал
            sqrt_mouse_row = y_mouse_pos // (square_height + margin)    # Строка
            sqrt_mouse_column = x_mouse_pos // (square_width + margin)    # Столбец
            button_mouse_row = -1
            button_mouse_column = x_mouse_pos // (rect_width + margin)

            # Будет работать толко если это левая кнопка мыши
            if event.button == 1:
                if y_mouse_pos not in range(0, display_height-(margin+rect_height)):

                    # Это ответвление кода работает если нажали на белую кнопку
                    if x_mouse_pos in range(rect_white_pos[0][0], rect_white_pos[0][1]):
                        if y_mouse_pos in range(rect_white_pos[1][0], rect_white_pos[1][1]):
                            current_color = WHITE

                    # Это ответвление кода работает если нажали на красную кнопку
                    elif x_mouse_pos in range(rect_red_pos[0][0], rect_red_pos[0][1]):
                        if y_mouse_pos in range(rect_red_pos[1][0], rect_red_pos[1][1]):
                            current_color = RED

                    # Это ответвление кода работает если нажали на зеленую кнопку
                    elif x_mouse_pos in range(rect_green_pos[0][0], rect_green_pos[0][1]):
                        if y_mouse_pos in range(rect_green_pos[1][0], rect_green_pos[1][1]):
                            current_color = GREEN

                    # Это ответвление кода работает если нажали на синию кнопку
                    elif x_mouse_pos in range(rect_blue_pos[0][0], rect_blue_pos[0][1]):
                        if y_mouse_pos in range(rect_blue_pos[1][0], rect_blue_pos[1][1]):
                            current_color = BLUE

                    # Это ответвление кода работает если нажали на желтую кнопку
                    elif x_mouse_pos in range(rect_yellow_pos[0][0], rect_yellow_pos[0][1]):
                        if y_mouse_pos in range(rect_yellow_pos[1][0], rect_yellow_pos[1][1]):
                            current_color = YELLOW

                    elif x_mouse_pos in range(rect_brown_pos[0][0], rect_brown_pos[0][1]):
                        if y_mouse_pos in range(rect_brown_pos[1][0], rect_brown_pos[1][1]):
                            current_color = BROWN

                    elif x_mouse_pos in range(rect_purple_pos[0][0], rect_purple_pos[0][1]):
                        if y_mouse_pos in range(rect_purple_pos[1][0], rect_purple_pos[1][1]):
                            current_color = PURPLE

                    elif x_mouse_pos in range(rect_gray_pos[0][0], rect_gray_pos[0][1]):
                        if y_mouse_pos in range(rect_gray_pos[1][0], rect_gray_pos[1][1]):
                            current_color = GRAY

                    elif x_mouse_pos in range(rect_orange_pos[0][0], rect_orange_pos[0][1]):
                        if y_mouse_pos in range(rect_orange_pos[1][0], rect_orange_pos[1][1]):
                            current_color = ORANGE

                    elif x_mouse_pos in range(rect_LightBlue_pos[0][0], rect_LightBlue_pos[0][1]):
                        if y_mouse_pos in range(rect_LightBlue_pos[1][0], rect_LightBlue_pos[1][1]):
                            current_color = LIGHT_BLUE

                    elif x_mouse_pos in range(rect_pink_pos[0][0], rect_pink_pos[0][1]):
                        if y_mouse_pos in range(rect_pink_pos[1][0], rect_pink_pos[1][1]):
                            current_color = PINK

                    elif x_mouse_pos in range(rect_pink_pos[0][0], rect_black_pos[0][1]):
                        if y_mouse_pos in range(rect_black_pos[1][0], rect_black_pos[1][1]):
                            current_color = BLACK

                    # Это на всякий случай чтобы не было неожиданной ошибки
                    else:
                        pass

                elif y_mouse_pos in range(0, display_height - (margin + rect_height)):
                    try:
                        if current_color == WHITE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 0

                        elif current_color == RED:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 1

                        elif current_color == GREEN:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 2

                        elif current_color == BLUE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 3

                        elif current_color == YELLOW:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 4

                        elif current_color == BROWN:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 5

                        elif current_color == PURPLE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 6

                        elif current_color == GRAY:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 7

                        elif current_color == ORANGE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 8

                        elif current_color == LIGHT_BLUE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 9

                        elif current_color == PINK:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 10

                        elif current_color == BLACK:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 11

                        else:
                            pass

                    except IndexError:
                        pass

                else:
                    pass

    # Рисование поля, рисование всех этих квадратов
    for row in range(square_count_vertical):    # Столько раз, сколько должно быть строк
        for column in range(square_count_horizontal):    # Колво итераций=колво столбцов
            if board[row][column] == 0:
                square_color = WHITE
            elif board[row][column] == 1:
                square_color = RED
            elif board[row][column] == 2:
                square_color = GREEN
            elif board[row][column] == 3:
                square_color = BLUE
            elif board[row][column] == 4:
                square_color = YELLOW
            elif board[row][column] == 5:
                square_color = BROWN
            elif board[row][column] == 6:
                square_color = PURPLE
            elif board[row][column] == 7:
                square_color = GRAY
            elif board[row][column] == 8:
                square_color = ORANGE
            elif board[row][column] == 9:
                square_color = LIGHT_BLUE
            elif board[row][column] == 10:
                square_color = PINK
            elif board[row][column] == 11:
                square_color = BLACK
            else:
                pass

            # А здесь само рисование
            square_x = column * square_width + (column+1)*margin    # Определяется х координата квадрата
            square_y = row*square_height + (row+1)*margin    # Определяется у координата квадрата
            # Неоднократное рисование квадрата, с определенными параметрами и координатами
            pygame.draw.rect(display, square_color, (square_x, square_y, square_width, square_height))
        # Обновить экран чтобы пользователь выдел изменения экрана
        pygame.display.update()

    # Здесь рисование тех прямоугольных кнопок отвечающих за переокрас квадратов в определенные цвета
    for column in range(colors_count):
        x = column*rect_width + (margin*(column + 1))    # х координата этой кнопок
        y = display_height - rect_height     # у координата этой кнопки
        # Определение цвета самой этой кнопки для хорошого воспринимания и понимания что делает эта кнопка
        rect_color = colors[column]
        # Рисование этих кнопок
        pygame.draw.rect(display, rect_color, (x, y, rect_width, rect_height))
        # Обновить экран
        pygame.display.update()

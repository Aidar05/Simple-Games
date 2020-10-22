# Импортирование PyGame
import pygame
# Инициализация pygame
pygame.init()

# Цвета в RGB
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

# Параметры квадратиков(поле состоит из квадратиков)
margin = 1    # Дистанция между квадратами
square_width, square_height = 15, 15    # ширина и высота квадратов
square_color = BLUE    # Цвет квадратов по умолчанию
square_count_horizontal, square_count_vertical = 60, 35    # Число квадратов по осям x, y

# Все что связано с цветами
colors_count = 12    # число цветов в общем
# Список цветов
colors = (WHITE, RED, GREEN, BLUE, YELLOW, BROWN, PURPLE, GRAY, ORANGE, LIGHT_BLUE, PINK, BLACK)
# Текущий цвет(в этот цвет окрасится квадрат если на него нажать), по умолчанию цвет белый
current_color = WHITE    

# Окно
display_width = square_count_horizontal * (margin + square_width) + margin    # Ширина окна
display_height = square_count_vertical * (margin + square_height)+margin + 20   # Высота окна
size = display_width, display_height
display = pygame.display.set_mode(size)   

# Параметры прямоугольников, которые будут выполнять роль кнопок(будут менять цвет квадрата)
rect_width = (display_width-margin*(colors_count+1)) // colors_count    # ширина кнопки
rect_height = 20    # высота кнопки
rect_color = WHITE    # цвет кнопки по умолчанию

# Координаты кнопок(прямоугольников) по оси y(Диапозоны) 
y_start = display_height-(rect_height+margin)    # Начало диапозона         
y_end = display_height-margin    # Конец диапозона

# Двумерный список. В первом элементе находится диапозон в котором находиться кнопка по оси x. Второй элесент ось y
rect_white_pos = [
    [margin, rect_width+margin],
    [y_start, y_end]
        ]

rect_red_pos = [
    [rect_width+(margin*2), 2*rect_width+(margin*2)],
    [y_start, y_end]
        ]

rect_green_pos = [
    [rect_width*2+(margin*3), rect_width*3+(margin*3)],
    [y_start, y_end]
        ]

rect_blue_pos = [
    [rect_width*3+(margin*4), rect_width*4+(margin*4)],
    [y_start, y_end]
        ]

rect_yellow_pos = [
    [rect_width*4+(margin*5), rect_width*5+(margin*5)],
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

# Матрица помагающая понять в какой цвет окрашивать определнный квадрат. Матрица заполнена нулями. Каждый элемент матрицы отвечает за какой-то квадрат на поле
board = [[0]*square_count_horizontal for i in range(square_count_vertical)]


# Игровой цикл
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            quit()   

        # Когда событие это нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение информации о клике
            x_mouse_pos, y_mouse_pos = pygame.mouse.get_pos()    # Координаты места на поле на которое нажали
            # Узнавание на какой квадрат нажал пользователь
            sqrt_mouse_row = y_mouse_pos // (square_height + margin)    # row
            sqrt_mouse_column = x_mouse_pos // (square_width + margin)    # column
            # Узнавание на какую кнопку нажал пользователь
            button_mouse_row = -1
            button_mouse_column = x_mouse_pos // (rect_width + margin)

            # Если пользователь нажал на левую кнопку мыши.
            if event.button == 1:
                # Если он нажал на кнопку
                if y_mouse_pos not in range(0, display_height-(margin+rect_height)):

                    # Этот код работает если нажали на белую кнопку
                    if x_mouse_pos in range(rect_white_pos[0][0], rect_white_pos[0][1]):
                        if y_mouse_pos in range(rect_white_pos[1][0], rect_white_pos[1][1]):
                            current_color = WHITE

                    # Нажата красная кнопка
                    elif x_mouse_pos in range(rect_red_pos[0][0], rect_red_pos[0][1]):
                        if y_mouse_pos in range(rect_red_pos[1][0], rect_red_pos[1][1]):
                            current_color = RED

                    # Зеленая кнопка
                    elif x_mouse_pos in range(rect_green_pos[0][0], rect_green_pos[0][1]):
                        if y_mouse_pos in range(rect_green_pos[1][0], rect_green_pos[1][1]):
                            current_color = GREEN

                    # и т.д
                    elif x_mouse_pos in range(rect_blue_pos[0][0], rect_blue_pos[0][1]):
                        if y_mouse_pos in range(rect_blue_pos[1][0], rect_blue_pos[1][1]):
                            current_color = BLUE

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

                    # На всякий случай.
                    else:
                        pass
                
                # Если пользователь нажал на какой-нибудь квадрат
                elif y_mouse_pos in range(0, display_height - (margin + rect_height)):
                    try:
                        # Цифры в определенном месте матрицы обозначают цвет квадрата ка который они отвеают
                        if current_color == WHITE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 0    # 0 - Белый

                        elif current_color == RED: 
                            board[sqrt_mouse_row][sqrt_mouse_column] = 1    # 1 - Красный
                     
                        elif current_color == GREEN:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 2    # 2 - Зеленый

                        elif current_color == BLUE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 3    # И т.д

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
    
    # Рисуем поле
    for row in range(square_count_vertical):    # Кол-во строк
        for column in range(square_count_horizontal):    # Кол-во столбцов
            # Смотрим какой значение в матрице, в месте которое отвечает за именно этот квадрат и в зависимости от этого меняем текущий цыет
            # Если 0(Как в самом начале везде) то белый
            if board[row][column] == 0:
                square_color = WHITE
            # Если цифра 1 на этом месте в массиве, то квадрат зарисуется красным
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

            # Рисование самого поля
            square_x = column * square_width + (column+1)*margin    # Координаты по оси х   
            square_y = row*square_height + (row+1)*margin   # координаты по y
            pygame.draw.rect(display, square_color, (square_x, square_y, square_width, square_height))
        pygame.display.update()

    # Рисование кнопок
    for column in range(colors_count):
        x = column*rect_width + (margin*(column + 1))    # Координаты по х
        y = display_height - rect_height     # Координаты по у
        rect_color = colors[column]    # # Цвет кнопки
        pygame.draw.rect(display, rect_color, (x, y, rect_width, rect_height))
        pygame.display.update()

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
square_width, square_height = 30, 20    # ширина и высота квадратов
square_color = BLUE    # Цвет квадратов по умолчанию
square_count_horizontal, square_count_vertical = 20, 20    # Число квадратов по осям x, y

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

                    color_index = x_mouse_pos // rect_width
                    current_color = colors[color_index]
                
                # Если пользователь нажал на какой-нибудь квадрат
                elif y_mouse_pos in range(0, display_height - (margin + rect_height)):
                    try:
                        # Цифры в определенном месте матрицы обозначают цвет квадрата ка который они отвеают
                        board[sqrt_mouse_row][sqrt_mouse_column] = color_index
                    except IndexError:
                        pass

                else:
                    pass
    
    # Рисуем поле
    for row in range(square_count_vertical):    # Кол-во строк
        for column in range(square_count_horizontal):    # Кол-во столбцов
            # Смотрим какой значение в матрице, в месте которое отвечает за именно этот квадрат и в зависимости от этого меняем текущий цыет
            # Если 0(Как в самом начале везде) то белый
            
            square_color = colors[board[row][column]]

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

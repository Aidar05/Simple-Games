# Import
import pygame
# initialization of pygame
pygame.init()

# colors in RGB
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

# square parameters(those squares is fielg for draw)
margin = 1    # Distance between fields for drawing
square_width, square_height = 15, 15    # Height and width of squares
square_color = BLUE    # Default square color
square_count_horizontal, square_count_vertical = 60, 35    # squares count in horizontal and vertical

# Anything to do with the colors
colors_count = 12    # colors count
# colors for fill a square
colors = (WHITE, RED, GREEN, BLUE, YELLOW, BROWN, PURPLE, GRAY, ORANGE, LIGHT_BLUE, PINK, BLACK)
current_color = WHITE    

# display
display_width = square_count_horizontal * (margin + square_width) + margin    # screen width
display_height = square_count_vertical * (margin + square_height)+margin + 20   # screen height
size = display_width, display_height
display = pygame.display.set_mode(size)   

# parameters of buttons
rect_width = (display_width-margin*(colors_count+1)) // colors_count    # button width
rect_height = 20    # button height
rect_color = WHITE    # default color

# y coordinate button location(diapason)
y_start = display_height-(rect_height+margin)    #    diapasons start         
y_end = display_height-margin    # diapason end

# Coordinates of every single button
# the first nailed list contains an x-coordinate range. the second nailed list contains an y-coordinate range. 
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

# The board
board = [[0]*square_count_horizontal for i in range(square_count_vertical)]


# gameplay loop
while True:
    # Check for last event
    for event in pygame.event.get():
        # The case where user click on a red cross 
        if event.type == pygame.QUIT:
            quit()    # stop running the code

        # The case when the event is a click on the mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # getting info about that click
            x_mouse_pos, y_mouse_pos = pygame.mouse.get_pos()    # coordinates of of pressed plase on the board
            # Find out which square the Users clicked on
            sqrt_mouse_row = y_mouse_pos // (square_height + margin)    # row
            sqrt_mouse_column = x_mouse_pos // (square_width + margin)    # column
            # find out which button the user clicked on
            button_mouse_row = -1
            button_mouse_column = x_mouse_pos // (rect_width + margin)

            # It will only work if pressed button is the left mouse button.
            if event.button == 1:
                if y_mouse_pos not in range(0, display_height-(margin+rect_height)):

                    # This code branch works if user pressed the white button
                    if x_mouse_pos in range(rect_white_pos[0][0], rect_white_pos[0][1]):
                        if y_mouse_pos in range(rect_white_pos[1][0], rect_white_pos[1][1]):
                            current_color = WHITE

                    # This code branch works if user pressed the red button
                    elif x_mouse_pos in range(rect_red_pos[0][0], rect_red_pos[0][1]):
                        if y_mouse_pos in range(rect_red_pos[1][0], rect_red_pos[1][1]):
                            current_color = RED

                    # This code branch works if user pressed the green button
                    elif x_mouse_pos in range(rect_green_pos[0][0], rect_green_pos[0][1]):
                        if y_mouse_pos in range(rect_green_pos[1][0], rect_green_pos[1][1]):
                            current_color = GREEN

                    # This code branch works if user pressed the blue button
                    elif x_mouse_pos in range(rect_blue_pos[0][0], rect_blue_pos[0][1]):
                        if y_mouse_pos in range(rect_blue_pos[1][0], rect_blue_pos[1][1]):
                            current_color = BLUE

                    # This code branch works if user pressed the yellow button
                    elif x_mouse_pos in range(rect_yellow_pos[0][0], rect_yellow_pos[0][1]):
                        if y_mouse_pos in range(rect_yellow_pos[1][0], rect_yellow_pos[1][1]):
                            current_color = YELLOW
                    
                    # This code branch works if user pressed the brown button 
                    elif x_mouse_pos in range(rect_brown_pos[0][0], rect_brown_pos[0][1]):
                        if y_mouse_pos in range(rect_brown_pos[1][0], rect_brown_pos[1][1]):
                            current_color = BROWN

                    elif x_mouse_pos in range(rect_purple_pos[0][0], rect_purple_pos[0][1]):
                        if y_mouse_pos in range(rect_purple_pos[1][0], rect_purple_pos[1][1]):
                            current_color = PURPLE
                            
                    # This code branch works if user pressed the gray button
                    elif x_mouse_pos in range(rect_gray_pos[0][0], rect_gray_pos[0][1]):
                        if y_mouse_pos in range(rect_gray_pos[1][0], rect_gray_pos[1][1]):
                            current_color = GRAY

                    # This code branch works if user pressed the orange button
                    elif x_mouse_pos in range(rect_orange_pos[0][0], rect_orange_pos[0][1]):
                        if y_mouse_pos in range(rect_orange_pos[1][0], rect_orange_pos[1][1]):
                            current_color = ORANGE

                    # This code branch works if user pressed the LightBlue button
                    elif x_mouse_pos in range(rect_LightBlue_pos[0][0], rect_LightBlue_pos[0][1]):
                        if y_mouse_pos in range(rect_LightBlue_pos[1][0], rect_LightBlue_pos[1][1]):
                            current_color = LIGHT_BLUE
                            
                    # This code branch works if user pressed the pink button  
                    elif x_mouse_pos in range(rect_pink_pos[0][0], rect_pink_pos[0][1]):
                        if y_mouse_pos in range(rect_pink_pos[1][0], rect_pink_pos[1][1]):
                            current_color = PINK

                    # This code branch works if user pressed the black button
                    elif x_mouse_pos in range(rect_pink_pos[0][0], rect_black_pos[0][1]):
                        if y_mouse_pos in range(rect_black_pos[1][0], rect_black_pos[1][1]):
                            current_color = BLACK

                    # It's just in case there's not an unexpected mistake.
                    else:
                        pass
                    
                # when user clicks on squares(not the buttons)
                elif y_mouse_pos in range(0, display_height - (margin + rect_height)):
                    try:
                        # the numbers indicates the color of a square
                        if current_color == WHITE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 0    # zero indicates the white color

                        elif current_color == RED: 
                            board[sqrt_mouse_row][sqrt_mouse_column] = 1    # 1 indicates the red color
                     
                        elif current_color == GREEN:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 2    # 2 indicates the green color

                        elif current_color == BLUE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 3    # 3 indicates the blue color 

                        elif current_color == YELLOW:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 4    # 4 indicates the yellow color

                        elif current_color == BROWN:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 5    # 5 indicates the brown color

                        elif current_color == PURPLE:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 6    # 6 indicates the purple color

                        elif current_color == GRAY:
                            board[sqrt_mouse_row][sqrt_mouse_column] = 7    # etc

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

    # Here is a drawing
    for row in range(square_count_vertical):    # rows count
        for column in range(square_count_horizontal):    # columns count
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

            # drawing the field
            square_x = column * square_width + (column+1)*margin    
            square_y = row*square_height + (row+1)*margin   
            # drawing
            pygame.draw.rect(display, square_color, (square_x, square_y, square_width, square_height))
        # update screen
        pygame.display.update()

    # buttons
    for column in range(colors_count):
        x = column*rect_width + (margin*(column + 1))    # All u need to know-it works    
        y = display_height - rect_height     
        # that button's color
        rect_color = colors[column]
        # drawing those buttons
        pygame.draw.rect(display, rect_color, (x, y, rect_width, rect_height))
        # update the screen
        pygame.display.update()

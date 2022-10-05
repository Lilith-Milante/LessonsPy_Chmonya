import pygame
import sys

def check_win (field_list, sign):
    emptys = 0 # пустые поля для ничьи
    for row in field_list:
        emptys += row.count(0)
        if row.count (sign) == 3: # проходимся по рядам листа
            return sign
    for col in range (3):
        if field_list [0] [col] == sign and field_list [1] [col] == sign and field_list [2] [col] == sign:
            return sign
    if field_list [0] [0] == sign and field_list [1] [1] == sign and field_list [2] [2] == sign:
        return sign
    if field_list[0][2] == sign and field_list[1][1] == sign and field_list[2][0] == sign:
        return sign
    if emptys == 0:
        return 'Dead heat'
    return False

pygame.init()
pygame.mixer.init()

FPS = 30
size_block = 100
margin = 10
width = height = size_block * 3 + margin * 4

size_window = (width, height)
screen = pygame.display.set_mode((size_window))
pygame.display.set_caption('Tic-tac-toe')
clock = pygame.time.Clock()

black = (0, 0, 0)
light_yellow = (255, 255, 224)
dark_violet = (148, 0, 211)
dark_green = (10, 153, 0)
medium_blue = (0, 0, 205)

field_list = [[0]*3 for i in range(3)] # заполняем поле нулями
change = 0 # переменная для смены цветов, увеличиваем в шагом в 1
game_over = False

running = True # запуск игры
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if field_list [row] [col] == 0:
                if change % 2 == 0:
                    field_list [row] [col] = 'X'
                else:
                    field_list [row] [col] = 'O'
                change += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # возвращаем стартовые условия по пробелу
            game_over = False
            field_list = [[0] * 3 for i in range(3)]
            change = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if field_list[row] [col] == 'X':
                    color = dark_violet
                elif field_list[row] [col] == 'O':
                    color = dark_green
                else:
                    color = light_yellow
                x = col * size_block + (col + 1)*margin # col - номер колонки
                y = row * size_block + (row + 1) * margin # row - номер ряда
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == dark_violet:
                    pygame.draw.line(screen, black, (x + 8, y + 8), (x + size_block - 8, y + size_block - 8), 7) # левый верхний правый нижний
                    pygame.draw.line(screen, black, (x + size_block - 8, y + 8), (x + 8, y + size_block - 8), 7) # правый верхний левый нижний
                elif color == dark_green:
                    pygame.draw.circle(screen, black, (x + size_block // 2, y + size_block // 2,), size_block // 2 - 8, 6) # координаты центра и радиус, в конце толщина

    if (change - 1) % 2 == 0:
        game_over = check_win (field_list, 'X') # условия выигрыша крестика
    else:
        game_over = check_win (field_list, 'O')

    if game_over:
        screen.fill (black)
        font = pygame.font.SysFont('font for game', 80)
        text1 = font.render(game_over, True, light_yellow)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, (text_x, text_y)) # прикрепление текста по координатам
    pygame.display.update() # отображаем игровое поле
import pygame
from time import sleep
from random import randint
from constants import DARK_BLUE as arr_main_color
from constants import YELLOW as arr_secondary_color
from constants import READS_GREY as background_color
from constants import GREEN
from constants import READS_GREY as linecolor
from constants import READS_GREY as middle_area_color
from constants import WIDTH, HEIGHT

from constants import DARK_BLUE as arr_main_color
from constants import YELLOW as arr_secondary_color
from constants import GREY as background_color

from constants import DARK_BLUE, YELLOW, GREY
arr_main_color = DARK_BLUE
arr_secondary_color = YELLOW
background_color = GREY

const = side_panels_width = (WIDTH - HEIGHT) // 2
middle_area_width = HEIGHT // 10  # middle square area
divider_lines_width = 4
HEADER_HEIGHT = int((1/9) * HEIGHT)

pygame.init()


window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(background_color)
# arr = [[randint(0, 1) for _ in range(3)] for _ in range(3)]

arr = [randint(1, HEIGHT - HEADER_HEIGHT - 1) for _ in range(middle_area_width)]
# print(pygame.font.get_fonts())
print(pygame.font.match_font('hightowertext'))

def draw_background():
    window.fill(background_color)
    pygame.draw.rect(window, middle_area_color, (side_panels_width, HEADER_HEIGHT, HEIGHT, HEIGHT))
    pygame.draw.line(window, linecolor, (side_panels_width, HEADER_HEIGHT), (side_panels_width, HEIGHT), divider_lines_width)
    pygame.draw.line(window, linecolor, (side_panels_width + HEIGHT, HEADER_HEIGHT), (side_panels_width +HEIGHT, HEIGHT), divider_lines_width)
    pygame.draw.line(window, linecolor, (side_panels_width, HEADER_HEIGHT), (side_panels_width + HEIGHT, HEADER_HEIGHT), divider_lines_width)
    pygame.draw.line(window, linecolor, (side_panels_width, HEIGHT - 3), (side_panels_width + HEIGHT, HEIGHT -3), divider_lines_width)
    # font = pygame.font.Font("C:\Windows\Fonts\LSANSD.TTF", 40)
    font = pygame.font.SysFont("Comicsafasfas Sans", 46)
    x = pygame.font.Font.render(font, "Sorting Visualiser", 1, arr_secondary_color, arr_main_color)
    z = window.blit(x, (20, HEADER_HEIGHT//6))
    pygame.display.update()

def draw_array(window, arr, current={}):
    draw_background()
    for i in range(len(arr)):
        current_item = pygame.Rect(side_panels_width + (divider_lines_width+1) + (10*i), HEIGHT-arr[i] - divider_lines_width, 7, arr[i])
        if i not in current:
            pygame.draw.rect(window, arr_main_color, current_item, border_top_left_radius=6, border_top_right_radius= 6)
        else:
            pygame.draw.rect(window, arr_secondary_color, current_item, border_top_left_radius=6, border_top_right_radius= 6)

    pygame.display.update()


run = True
y=1
clock = pygame.time.Clock()
while run:
    clock.tick(3)
    current = {randint(0, 66), randint(0, 66)}
    draw_array(window,arr,current)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            current = {randint(0, middle_area_width-1), randint(0, middle_area_width-1)}
            if event.pos[0] in range(side_panels_width + HEIGHT + divider_lines_width, WIDTH):
                arr.sort()
                draw_array(window, arr, current)
                y *= -1
            elif event.pos[0] in range(0, side_panels_width):
                arr = [randint(1, HEIGHT - HEADER_HEIGHT - (2 * divider_lines_width)) for _ in range(middle_area_width)]
                draw_array(window, arr, current)
                y *= -1
            pygame.draw.line(window, (0, 0, 222), (0, 0), event.pos, 4)
            pygame.display.update()
            
    
    # pygame.draw.line(window, (111, 2, 220), (0, 0), (randint(0,1200), randint(0,HEIGHT)), 22)
    # pygame.draw.line(window, (222, 111, 0), (1200, 0), (randint(0,1200), randint(0,HEIGHT)), 22)
    # pygame.draw.line(window, (155, 111, 55), (0, HEIGHT), (randint(0,1200), randint(0,HEIGHT)), 22)
    # pygame.draw.line(window, (122, 111, 220), (1200, HEIGHT), (randint(0,1200), randint(0,HEIGHT)), 22)


    pygame.display.update()

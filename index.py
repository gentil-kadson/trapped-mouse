from colors import *
import sys
from classes import Mouse
import pygame
from pygame.locals import *
from functions import create_maze


pygame.init()

# initializing constants #
DISPLAY_SURFACE = pygame.display.set_mode((800, 600))
FPS = 10
FRAMES_PER_SECOND = pygame.time.Clock()

# creating maze and blitting it to display surface
mouse = Mouse()
maze = create_maze(mouse)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY_SURFACE.fill(BLUE)
    for row in maze:
        for column in row:
            DISPLAY_SURFACE.blit(column.image, column.rect.center)

    pygame.display.update()
    FRAMES_PER_SECOND.tick(FPS)

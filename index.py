from pygame.locals import *
import pygame
import sys
from colors import *
from classes import Mouse, Cheese, Path
from functions import create_maze, get_all_walls, can_it_move

# Initiating pygame module #
pygame.init()

# Setting up display surface, window name and FPS #
DISPLAY_SURFACE = pygame.display.set_mode((800, 600))
FPS = 1
FRAMES_PER_SECOND = pygame.time.Clock()
pygame.display.set_caption("El ratón")

# Instanciating mouse, cheese and maze #
mouse = Mouse()
cheese = Cheese()
maze = create_maze(mouse, cheese)
walls = get_all_walls(maze)

# Creation of walls, cheese, and all sprites groups #
walls_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
cheese_group = pygame.sprite.Group()
cheese_group.add(cheese)

for wall in walls:
    walls_group.add(wall)
    all_sprites.add(wall)

all_sprites.add(mouse)

# Plotting the display surface #
DISPLAY_SURFACE.fill(BLUE)
for row in maze:
    for column in row:
        DISPLAY_SURFACE.blit(column.image, column.rect.center)

# Game loop #
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FRAMES_PER_SECOND.tick(FPS)

    if not pygame.sprite.spritecollideany(mouse, cheese_group):
        if can_it_move(mouse, 'right', walls_group):
            DISPLAY_SURFACE.blit(Path().image, mouse.rect.center)
            mouse.move_right()
            DISPLAY_SURFACE.blit(mouse.image, mouse.rect.center)
        elif can_it_move(mouse, 'left', walls_group):
            DISPLAY_SURFACE.blit(Path().image, mouse.rect.center)
            mouse.move_left()
            DISPLAY_SURFACE.blit(mouse.image, mouse.rect.center)
        elif can_it_move(mouse, 'down', walls_group):
            DISPLAY_SURFACE.blit(Path().image, mouse.rect.center)
            mouse.move_down()
            DISPLAY_SURFACE.blit(mouse.image, mouse.rect.center)
        elif can_it_move(mouse, 'up', walls_group):
            DISPLAY_SURFACE.blit(Path().image, mouse.rect.center)
            mouse.move_up()
            DISPLAY_SURFACE.blit(mouse.image, mouse.rect.center)

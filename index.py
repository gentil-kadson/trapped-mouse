from pygame.locals import *
import pygame
import sys
from colors import *
from classes import Mouse, Path, Wall
from functions import create_maze, get_all_walls


pygame.init()

DISPLAY_SURFACE = pygame.display.set_mode((800, 600))
FPS = 1
FRAMES_PER_SECOND = pygame.time.Clock()
pygame.display.set_caption("El ratón")

mouse = Mouse()
maze = create_maze(mouse)
walls = get_all_walls(maze)

walls_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for wall in walls:
    walls_group.add(wall)
    all_sprites.add(wall)

all_sprites.add(mouse)

DISPLAY_SURFACE.fill(BLUE)
for row in maze:
    for column in row:
        DISPLAY_SURFACE.blit(column.image, column.rect.center)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FRAMES_PER_SECOND.tick(FPS)

    old_path = Path()
    old_path.set_center(mouse.rect.center)
    mouse.move_right()
    if not pygame.sprite.spritecollideany(mouse, walls_group):
        DISPLAY_SURFACE.blit(old_path.image, old_path.rect.center)
        DISPLAY_SURFACE.blit(mouse.image, mouse.rect.center)
    else:
        mouse.move_left()

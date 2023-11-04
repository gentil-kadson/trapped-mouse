import pygame
from classes import Mouse, Cheese
from functions import create_maze

pygame.init()

## constants ##
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
WHITE = (255, 255, 255)
BORDER = (10, 10, 10)
BLACK = (0, 0, 0)
MOUSE = (255, 193, 110)
CHEESE = (255, 255, 0)

## initial variables ##
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running: bool = True
mouse = Mouse()
cheese = Cheese()
visited: list[tuple] = []

## Creating maze cells (includes mouse and cheese starting cells) ##
maze_cells = create_maze(mouse, cheese)

## Inserting cells on pygame's main surface object ##
screen.fill("white")
screen_x_position: float = 0
screen_y_position: float = 0

for row in maze_cells:
    for cell in row:
        if isinstance(cell, Mouse):
            mouse.x = screen_x_position
            mouse.y = screen_y_position
        elif isinstance(cell, Cheese):
            cheese.x = screen_x_position
            cheese.y = screen_y_position
        else:
            cell.x = screen_x_position
            cell.y = screen_y_position

        screen.blit(cell.surface, (screen_x_position, screen_y_position))
        screen_x_position += 50

    screen_x_position = 0
    screen_y_position += 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(1)
    ## solving the maze ##


pygame.quit()

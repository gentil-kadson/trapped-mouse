import pygame
from classes import Mouse, Cheese, Cell
from functions import create_maze, can_go_down, can_go_left, can_go_right, can_go_up

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
visited: list[tuple] = []
mouse = Mouse()
cheese = Cheese()

## Creating maze cells (includes mouse and cheese starting cells) ##
maze_cells = create_maze()

## Inserting cells on pygame's main surface object, getting mouse and cheese surfaces ##
screen.fill("teal")
screen_x_position: float = 0
screen_y_position: float = 0

for row in maze_cells:
    for cell in row:
        if isinstance(cell, Mouse):
            mouse = cell

        if isinstance(cell, Cheese):
            cheese = cell

        screen.blit(cell.surface, (screen_x_position, screen_y_position))
        screen_x_position += 50

    screen_x_position = 0
    screen_y_position += 50

pygame.display.flip()
clock.tick(2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while mouse.position != cheese.position:
        pass
pygame.quit()

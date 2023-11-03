import pygame
from classes import Mouse, Cheese, Cell
from functions import create_maze, get_next_step

pygame.init()

## constants ##
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

## initial variables ##
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running: bool = True
mouse = Mouse()
cheese = Cheese()
steps: list[tuple] = []

## Creating maze cells (includes mouse and cheese starting cells) ##
maze_cells = create_maze(mouse, cheese)

## Inserting cells on pygame's main surface object ##
screen.fill("#181818")
screen_x_position: float = 0
screen_y_position: float = 0

for row in maze_cells:
    for cell in row:
        if isinstance(cell, Mouse):
            mouse.x = screen_x_position
            mouse.y = screen_y_position

        if isinstance(cell, Cheese):
            cheese.x = screen_x_position
            cheese.y = screen_y_position

        cell.x = screen_x_position
        cell.y = screen_y_position

        screen.blit(cell.surface, (screen_x_position, screen_y_position))
        screen_x_position += 50

    screen_x_position = 0
    screen_y_position += 50

steps.append((mouse.x, mouse.y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## solving the maze ##
    for row in maze_cells:
        for cell in row:
            data_tuple = get_next_step(mouse, cell)
            steps.append(data_tuple)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()

print(steps)

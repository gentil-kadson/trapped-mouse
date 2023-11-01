import pygame
from classes import Mouse, Cheese, Cell
from functions import create_maze, get_cheese, get_mouse

pygame.init()

## initializing variables ##
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running: bool = True

## Creating maze cells (includes mouse and cheese starting cells) ##
maze_cells = create_maze()
stack: list[Cell | Mouse | Cheese] = []

## Inserting cells on pygame's main surface object ##
screen.fill("#181818")
screen_x_position: float = 0
screen_y_position: float = 0

for row in maze_cells:
    for cell in row:
        screen.blit(cell.surface, (screen_x_position, screen_y_position))
        screen_x_position += 50

    screen_x_position = 0
    screen_y_position += 50

mouse = get_mouse(maze_cells)
cheese = get_cheese(maze_cells)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(10)

pygame.quit()

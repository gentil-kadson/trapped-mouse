import pygame
from classes import Mouse, Cheese, Cell
from functions import create_maze, get_cheese, get_mouse

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mouse: Mouse = Mouse()
cheese: Cheese = Cheese()


clock = pygame.time.Clock()
running: bool = True

## initializing variables ##
maze_cells = create_maze()
stack: list[Cell | Mouse | Cheese] = []


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## Creating surface with the maze's cells, wall, mouse, and cheese ##
    screen.fill("#181818")
    screen_x_position: float = 50
    screen_y_position: float = 50

    for row in maze_cells:
        for cell in row:
            screen.blit(cell.surface, (screen_x_position, screen_y_position))
            screen_x_position += 50

        screen_x_position = 50
        screen_y_position += 50

    screen_x_position = mouse.rectangle.x
    screen_y_position = mouse.rectangle.y

    mouse = get_mouse(maze_cells)
    cheese = get_cheese(maze_cells)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()

import pygame
from classes import Mouse, Cheese
from functions import create_maze, find_cheese, find_mouse

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mouse: Mouse = Mouse()
cheese: Cheese = Cheese()


clock = pygame.time.Clock()
running: bool = True

## initialize variables to both create and solve the maze ##
maze_surfaces = create_maze(mouse, cheese)
maze_mouse = find_mouse(maze_surfaces)
maze_cheese = find_cheese(maze_surfaces)
stack: list[pygame.Surface] = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## Creating surface with the maze's cells, wall, mouse, and cheese ##
    screen.fill("#181818")
    screen_x_position: float = 50
    screen_y_position: float = 50

    for row in maze_surfaces:
        for column in row:
            if isinstance(column, Mouse) or isinstance(column, Cheese):
                screen.blit(column.surface,
                            (screen_x_position, screen_y_position))
                screen_x_position += 50
            else:
                screen.blit(column, (screen_x_position, screen_y_position))
                screen_x_position += 50

        screen_x_position = 50
        screen_y_position += 50

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

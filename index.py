import pygame
from classes import Mouse, Cheese
from fuctions import create_maze

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mouse: Mouse = Mouse()
cheese: Cheese = Cheese()


clock = pygame.time.Clock()
running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## Creating surface with the labyrinth, mouse, and cheese ##
    labyrinth_surfaces = create_maze(mouse, cheese)
    screen.fill("#181818")
    screen_x_position: float = 50
    screen_y_position: float = 50
    for row in labyrinth_surfaces:
        for column in row:
            screen.blit(column, (screen_x_position, screen_y_position))
            screen_x_position += 50

        screen_x_position = 50
        screen_y_position += 50

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

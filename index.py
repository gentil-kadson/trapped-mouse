import pygame
from mouse import mouse
from labyrinth import labyrinth_surfaces

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#181818")
    screen_x_position = 50
    screen_y_position = 50
    for row in labyrinth_surfaces:
        for column in row:
            screen.blit(column, (screen_x_position, screen_y_position))
            screen_x_position += 50

        screen_x_position = 50
        screen_y_position += 50

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

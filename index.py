import pygame
from mouse import mouse

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
    screen.blit(mouse, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

import pygame

pygame.init()
screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#181818")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

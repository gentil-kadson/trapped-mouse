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
mouse = Mouse()
cheese = Cheese()
visited: list[tuple] = []

## Creating maze cells (includes mouse and cheese starting cells) ##
maze_cells = create_maze(mouse, cheese)

## Inserting cells on pygame's main surface object ##
screen.fill("teal")
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

pygame.display.flip()
clock.tick(2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## solving the maze ##
    while mouse.x != cheese.x and mouse.y != cheese.y:
        while can_go_right(mouse, maze_cells):
            cell_to_blit = Cell(WHITE, mouse.x, mouse.y)
            mouse.x += 50

            screen.blit(cell_to_blit.surface, (cell_to_blit.x, cell_to_blit.y))
            screen.blit(mouse.surface, (mouse.x, mouse.y))
            pygame.display.flip()

        while can_go_left(mouse, maze_cells):
            cell_to_blit = Cell(WHITE, mouse.x, mouse.y)
            mouse.x -= 50

            screen.blit(cell_to_blit.surface, (cell_to_blit.x, cell_to_blit.y))
            screen.blit(mouse.surface, (mouse.x, mouse.y))
            pygame.display.flip()

    print("POV!!!!")

pygame.quit()

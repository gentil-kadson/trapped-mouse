import pygame


def create_maze(mouse, cheese):
    maze_surfaces = []

    with open('test_text.txt') as file:
        lines = file.readlines()

        for line in lines:
            surfaces_aux = []
            for value in line:
                maze_surface = pygame.Surface((50, 50))
                if value == "0":
                    maze_surface.fill((255, 255, 255))
                    surfaces_aux.append(maze_surface)
                elif value == "1":
                    maze_surface.fill((0, 0, 0))
                    surfaces_aux.append(maze_surface)
                elif value == "m":
                    surfaces_aux.append(mouse.surface)
                elif value == "c":
                    surfaces_aux.append(cheese.surface)

            maze_surfaces.append(surfaces_aux)

    return maze_surfaces

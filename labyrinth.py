import pygame


def create_labyrinth(mouse, cheese):
    labyrinth_surfaces = []

    with open('test_text.txt') as file:
        lines = file.readlines()

        for line in lines:
            surfaces_aux = []
            for value in line:
                labyrinth_surface = pygame.Surface((50, 50))
                if value == "0":
                    labyrinth_surface.fill((255, 255, 255))
                    surfaces_aux.append(labyrinth_surface)
                elif value == "1":
                    labyrinth_surface.fill((0, 0, 0))
                    surfaces_aux.append(labyrinth_surface)
                elif value == "m":
                    surfaces_aux.append(mouse.surface)
                elif value == "c":
                    surfaces_aux.append(cheese.surface)

            labyrinth_surfaces.append(surfaces_aux)

    return labyrinth_surfaces

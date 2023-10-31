import pygame
from classes import Cheese, Mouse


def create_maze(mouse: Mouse, cheese: Cheese) -> list[list[pygame.Surface]]:
    maze_surfaces: list[pygame.Surface] = []
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


def find_rat(maze_surfaces):
    for row in maze_surfaces:
        for column in row:
            if column.get_color() == "rat":
                return column


def find_cheese(maze_surfaces):
    for row in maze_surfaces:
        for column in row:
            if column.get_color() == "cheese":
                return column


def solve_maze(maze_surfaces):
    rat = find_rat(maze_surfaces)
    cheese = find_cheese(maze_surfaces)

    for row in maze_surfaces:
        for column in row:
            pass

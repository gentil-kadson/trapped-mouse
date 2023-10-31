import pygame
from classes import Cheese, Mouse


def create_maze(mouse: Mouse, cheese: Cheese) -> list[list[pygame.Surface]]:
    maze_surfaces: list[list[pygame.Surface]] = []
    with open('test_text.txt') as file:
        lines = file.readlines()
        vertical_border_surfaces: list[pygame.Surface] = []

        for _ in range(len(lines)+2):
            vertical_border_surface = pygame.Surface((50, 50))
            vertical_border_surface.fill((10, 10, 10))
            vertical_border_surfaces.append(vertical_border_surface)

        maze_surfaces.append(vertical_border_surfaces)

        for line in lines:
            left_border_surface = pygame.Surface((50, 50))
            left_border_surface.fill((10, 10, 10))
            surfaces_aux: list[pygame.Surface] = [left_border_surface]
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

            right_border_surface = pygame.Surface((50, 50))
            right_border_surface.fill((10, 10, 10))
            surfaces_aux.append(right_border_surface)

            maze_surfaces.append(surfaces_aux)

        maze_surfaces.append(vertical_border_surfaces)

    return maze_surfaces


def find_mouse(maze_surfaces: list[list[pygame.Surface]]) -> Mouse:
    for row in maze_surfaces:
        for column in row:
            if isinstance(column, Mouse):
                return column


def find_cheese(maze_surfaces: list[list[pygame.Surface]]) -> Cheese:
    for row in maze_surfaces:
        for column in row:
            if isinstance(column, Cheese):
                return column


def solve_maze(maze_surfaces: list[list[pygame.Surface]]) -> bool:
    mouse_rect = find_mouse(maze_surfaces).rectangle
    cheese_rect = find_cheese(maze_surfaces).rectangle

    return True

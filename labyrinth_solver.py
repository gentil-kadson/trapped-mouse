import pygame


def solve_labyrinth(mouse, cheese, labyrinth):
    current_mouse_x = mouse.surface.get_width()
    current_mouse_y = mouse.surface.get_height()

    for row in labyrinth:
        for column in row:
            pass

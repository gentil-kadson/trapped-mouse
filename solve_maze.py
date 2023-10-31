from pygame import Surface
from classes import Mouse, Cheese


def solve_maze(mouse: Mouse, cheese: Cheese, maze_surfaces: list[Surface]):
    stack = []
    phantom_mouse = Mouse()
    phantom_mouse.rectangle.width = mouse.rectangle.width
    phantom_mouse.rectangle.height = mouse.rectangle.height

    while phantom_mouse.rectangle.width != cheese.rectangle.width and mouse.rectangle.height != cheese.rectangle.height:
        pass

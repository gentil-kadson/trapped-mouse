import pygame
from classes import Mouse, Path, Wall, Cheese


def create_maze(mouse: Mouse, cheese: Cheese) -> list[list[Mouse | Path | Wall]]:
    maze: list[list[Mouse | Path | Wall]] = []

    with open('test_text.txt') as file:
        lines = file.readlines()

        x_axis = 0
        y_axis = 0

        for row in lines:
            maze_columns = []
            for column in row:
                if column == '0':
                    free_path = Path()
                    free_path.set_center((x_axis, y_axis))
                    maze_columns.append(free_path)
                    x_axis += 70

                elif column == '1':
                    wall_block = Wall()
                    wall_block.set_center((x_axis, y_axis))
                    maze_columns.append(wall_block)
                    x_axis += 70

                elif column == 'm':
                    mouse.set_center((x_axis, y_axis))
                    maze_columns.append(mouse)
                    x_axis += 70

                elif column == 'e':
                    cheese.set_center((x_axis, y_axis))
                    maze_columns.append(cheese)
                    x_axis += 70

            maze.append(maze_columns)
            x_axis = 0
            y_axis += 70

    return maze


def get_all_walls(maze: list[list[Mouse | Path | Wall]]):
    walls: list[Wall] = []
    for row in maze:
        for column in row:
            if isinstance(column, Wall):
                walls.append(column)

    return walls


def get_neighbouring_cells(mouse: Mouse, neighbouring_cells: list, walls: pygame.sprite.Group, visited: list[tuple[int, int]]):
    pass

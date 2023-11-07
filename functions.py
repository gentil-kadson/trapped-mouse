import pygame
from colors import FOREST_GREEN
from classes import Mouse, Path, Wall, Cheese


def create_maze(mouse: Mouse, cheese: Cheese) -> list[list[Mouse | Path | Wall]]:
    maze: list[list[Mouse | Path | Wall]] = []

    with open('test_text.txt') as file:
        lines = file.readlines()

        x_axis = 0
        y_axis = 0

        top_border = []
        for _ in range(len(lines[0])+1):
            top_border_wall = Wall()
            top_border_wall.image.fill(FOREST_GREEN)
            top_border_wall.set_center((x_axis, y_axis))
            top_border.append(top_border_wall)
            x_axis += 70

        x_axis = 0
        maze.append(top_border)
        y_axis += 70

        for row in lines:
            maze_columns = []
            left_border_wall = Wall()
            left_border_wall.image.fill(FOREST_GREEN)
            left_border_wall.set_center((x_axis, y_axis))
            maze_columns.append(left_border_wall)
            x_axis += 70

            skip_border_creation = False
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
                    exit_cell = Path()
                    exit_cell.set_center((x_axis, y_axis))
                    maze_columns.append(exit_cell)
                    x_axis += 70
                    skip_border_creation = True

            if not skip_border_creation:
                right_border = Wall()
                right_border.image.fill(FOREST_GREEN)
                right_border.set_center((x_axis, y_axis))
                maze_columns.append(right_border)
            else:
                cheese.set_center((x_axis, y_axis))
                maze_columns.append(cheese)

            maze.append(maze_columns)
            x_axis = 0
            y_axis += 70

        x_axis = 0
        bottom_border = []
        for _ in range(len(lines[0])+1):
            bottom_border_wall = Wall()
            bottom_border_wall.image.fill(FOREST_GREEN)
            bottom_border_wall.set_center((x_axis, y_axis))
            bottom_border.append(bottom_border_wall)
            x_axis += 70

        maze.append(bottom_border)

    return maze


def get_all_walls(maze: list[list[Mouse | Path | Wall]]):
    walls: list[Wall] = []
    for row in maze:
        for column in row:
            if isinstance(column, Wall):
                walls.append(column)

    return walls


def can_it_move(mouse: Mouse, direction: str, walls: pygame.sprite.Group) -> bool:
    ghost_mouse = Mouse()
    ghost_mouse.set_center(mouse.rect.center)

    if direction == 'right':
        ghost_mouse.move_right()
        if not pygame.sprite.spritecollideany(ghost_mouse, walls):
            return True

    if direction == 'left':
        ghost_mouse.move_left()
        if not pygame.sprite.spritecollideany(ghost_mouse, walls):
            return True

    if direction == 'up':
        ghost_mouse.move_up()
        if not pygame.sprite.spritecollideany(ghost_mouse, walls):
            return True

    if direction == 'down':
        ghost_mouse.move_down()
        if not pygame.sprite.spritecollideany(ghost_mouse, walls):
            return True

    return False


def insert_non_visited_cells(current_mouse_cell: tuple[int, int], visited: list[tuple[int, int]], neighbouring_cells: dict):
    mouse_cell_x = current_mouse_cell[0]
    mouse_cell_y = current_mouse_cell[1]

    top = (mouse_cell_x, mouse_cell_y + 70)
    bottom = (mouse_cell_x, mouse_cell_y - 70)
    left = (mouse_cell_x - 70, mouse_cell_y)
    right = (mouse_cell_x + 70, mouse_cell_y)

    if right not in visited and not isinstance(right, Wall):
        neighbouring_cells["right"] = right

    if left not in visited and not isinstance(left, Wall):
        neighbouring_cells["left"] = left

    if top not in visited and not isinstance(top, Wall):
        neighbouring_cells["top"] = top

    if bottom not in visited and not isinstance(bottom, Wall):
        neighbouring_cells["bottom"] = bottom

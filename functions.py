import pygame
from classes import Mouse, Path, Wall, Cheese


def create_maze(mouse: Mouse, cheese: Cheese) -> list[list[Mouse | Path | Wall]]:
    maze: list[list[Mouse | Path | Wall]] = []
    maze_dimensions = ''

    with open('test_text.txt') as file:
        lines = file.readlines()
        maze_dimensions = lines[0].strip().split(" ")
        lines = lines[1:]
        lines = [line.strip() for line in lines]

        if len(lines) != int(maze_dimensions[0]) or len(lines[0]) != int(maze_dimensions[1]):
            print("As dimensões não coincidem com o labirinto.")
            raise SystemExit()

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


def get_neighbouring_cells(mouse: Mouse, neighbouring_cells: list, walls: pygame.sprite.Group, visited: list[tuple[int, int]], marked: list[tuple[int, int]]):
    mouse_copy = Mouse()
    mouse_copy.set_center(mouse.rect.center)

    # top #
    mouse_copy.set_center((mouse.rect.centerx, mouse.rect.centery - 70))
    if mouse_copy.rect.center not in visited and not pygame.sprite.spritecollideany(mouse_copy, walls) and mouse_copy.rect.center not in marked:
        neighbouring_cells.append(
            (mouse_copy.rect.centerx, mouse_copy.rect.centery))

    # bottom #
    mouse_copy.set_center(mouse.rect.center)
    mouse_copy.set_center((mouse.rect.centerx, mouse.rect.centery + 70))
    if mouse_copy.rect.center not in visited and not pygame.sprite.spritecollideany(mouse_copy, walls) and mouse_copy.rect.center not in marked:
        neighbouring_cells.append(
            (mouse_copy.rect.centerx, mouse_copy.rect.centery))

    # left #
    mouse_copy.set_center(mouse.rect.center)
    mouse_copy.set_center((mouse.rect.centerx - 70, mouse.rect.centery))
    if mouse_copy.rect.center not in visited and not pygame.sprite.spritecollideany(mouse_copy, walls) and mouse_copy.rect.center not in marked:
        neighbouring_cells.append(
            (mouse_copy.rect.centerx, mouse_copy.rect.centery))

    # right #
    mouse_copy.set_center(mouse.rect.center)
    mouse_copy.set_center((mouse.rect.centerx + 70, mouse.rect.centery))
    if mouse_copy.rect.center not in visited and not pygame.sprite.spritecollideany(mouse_copy, walls) and mouse_copy.rect.center not in marked:
        neighbouring_cells.append(
            (mouse_copy.rect.centerx, mouse_copy.rect.centery))

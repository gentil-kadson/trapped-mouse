from classes import Mouse, Path, Wall


def create_maze(mouse: Mouse) -> list[list[Mouse | Path | Wall]]:
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
                elif column == '1':
                    wall_block = Wall()
                    wall_block.set_center((x_axis, y_axis))
                    maze_columns.append(wall_block)
                elif column == 'm':
                    mouse.set_center((x_axis, y_axis))
                    maze_columns.append(mouse)
                elif column == 'e':
                    exit_cell = Path()
                    exit_cell.set_center((x_axis, y_axis))
                    maze_columns.append(exit_cell)

                x_axis += 70

            x_axis = 0
            y_axis += 70
            maze.append(maze_columns)

    return maze

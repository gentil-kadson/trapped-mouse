from classes import Mouse, Path, Wall


def create_maze(mouse: Mouse) -> list[list[Mouse | Path | Wall]]:
    maze: list[list[Mouse | Path | Wall]] = []

    with open('test_text.txt') as file:
        lines = file.readlines()

        x_axis = 0
        y_axis = 0

        top_border = []
        for _ in range(len(lines[0])):
            print("entrei")
            top_border_wall = Wall()
            top_border_wall.set_center((x_axis, y_axis))
            top_border.append(top_border_wall)
            x_axis += 70

        x_axis = 0
        maze.append(top_border)
        y_axis += 70

        for row in lines:
            maze_columns = []
            left_border_wall = Wall()
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
                right_border.set_center((x_axis, y_axis))
                maze_columns.append(right_border)

            maze.append(maze_columns)
            x_axis = 0
            y_axis += 70

    return maze

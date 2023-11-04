from classes import Cheese, Mouse, Cell

WHITE = (255, 255, 255)
BORDER = (10, 10, 10)
BLACK = (0, 0, 0)
MOUSE = (255, 193, 110)
CHEESE = (255, 255, 0)


def create_maze(mouse: Mouse, cheese: Cheese) -> list[list[Cheese | Mouse | Cell]]:
    maze_cells: list[list[Cheese | Mouse | Cell]] = []

    with open('test_text.txt') as file:
        lines = file.readlines()
        vertical_border_cells: list[Cell] = []

        for _ in range(len(lines)+2):
            vertical_border_cell = Cell(BORDER)
            vertical_border_cells.append(vertical_border_cell)

        maze_cells.append(vertical_border_cells)

        for line in lines:
            left_border_cell = Cell(BORDER)
            cells_aux: list[Cell] = [left_border_cell]

            for value in line:
                if value == "0":
                    white_cell = Cell(WHITE)
                    cells_aux.append(white_cell)

                elif value == "1":
                    dark_cell = Cell(BLACK)
                    cells_aux.append(dark_cell)

                elif value == "m":
                    cells_aux.append(mouse)

                elif value == "c":
                    cells_aux.append(cheese)

            if isinstance(cells_aux[-1], Cheese) is False:
                right_border_cell = Cell(BORDER)
                cells_aux.append(right_border_cell)

            maze_cells.append(cells_aux)

        maze_cells.append(vertical_border_cells)

    return maze_cells


def is_color_valid(cell: Cell) -> bool:
    if cell.color != BLACK and cell.color != BORDER and cell.color != MOUSE:
        return True

    return False


def get_next_step(mouse: Mouse, cell: Cell) -> tuple:
    if mouse.x+50 == cell.x and mouse.y == cell.y and is_color_valid(cell):
        return (cell.x, cell.y)

    if mouse.x-50 == cell.x and mouse.y == cell.y and is_color_valid(cell):
        return (cell.x, cell.y)

    if mouse.y+50 == cell.y and mouse.x == cell.x and is_color_valid(cell):
        return (cell.x, cell.y)

    if mouse.y-50 == cell.y and mouse.x == cell.x and is_color_valid(cell):
        return (cell.x, cell.y)

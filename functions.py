from classes import Cheese, Mouse, Cell

WHITE = (255, 255, 255)
BORDER = (238, 75, 43)
BLACK = (0, 0, 0)
MOUSE = (255, 193, 110)
CHEESE = (255, 255, 0)


def create_maze() -> list[list[Cheese | Mouse | Cell]]:
    mouse = Mouse()
    cheese = Cheese()
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


def can_move_to(cell: Cell) -> bool:
    return cell.color == WHITE or cell.color == CHEESE


def has_been_visited(x: float, y: float, visited: list[tuple]) -> bool:
    return (x, y) in visited


def can_go_right(mouse: Mouse, maze_cells: list[list[Cell | Mouse | Cheese]]) -> bool:
    pass


def can_go_left(mouse: Mouse, maze_cells: list[list[Cell | Mouse | Cheese]]) -> bool:
    pass


def can_go_down(mouse: Mouse, maze_cells: list[list[Cell | Mouse | Cheese]]) -> bool:
    pass


def can_go_up(mouse: Mouse, maze_cells: list[list[Cell | Mouse | Cheese]]) -> bool:
    pass

import pygame
from classes import Cheese, Mouse, Cell

white = (255, 255, 255)
border = (10, 10, 10)
black = (0, 0, 0)


def create_maze(mouse: Mouse, cheese: Cheese) -> list[list[Cheese | Mouse | Cell]]:
    maze_cells: list[list[Cheese | Mouse | Cell]] = []

    with open('test_text.txt') as file:
        lines = file.readlines()
        vertical_border_cells: list[Cell] = []

        for _ in range(len(lines)+2):
            vertical_border_cell = Cell(border)
            vertical_border_cells.append(vertical_border_cell)

        maze_cells.append(vertical_border_cells)

        for line in lines:
            left_border_cell = Cell(border)
            cells_aux: list[Cell] = [left_border_cell]

            for value in line:
                if value == "0":
                    white_cell = Cell(white)
                    cells_aux.append(white_cell)

                elif value == "1":
                    dark_cell = Cell(black)
                    cells_aux.append(dark_cell)

                elif value == "m":
                    cells_aux.append(mouse)

                elif value == "c":
                    cells_aux.append(cheese)

            right_border_cell = Cell(border)
            cells_aux.append(right_border_cell)

            maze_cells.append(cells_aux)

        maze_cells.append(vertical_border_cells)

    return maze_cells


def is_black(screen: pygame.Surface, cell: Cell) -> bool:
    black = (0, 0, 0)

    if (screen.get_at((cell.width, cell.height) != black)):
        return False

    return True

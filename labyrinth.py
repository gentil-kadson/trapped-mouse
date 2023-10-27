from pygame import Surface

labyrinth_surfaces = []

with open('test_text.txt') as file:
    lines = file.readlines()

    for line in lines:
        surfaces_aux = []
        for number in line:
            labyrinth_surface = Surface((50, 50))
            if number == "0":
                labyrinth_surface.fill((255, 255, 255))
                surfaces_aux.append(labyrinth_surface)
            elif number == "1":
                labyrinth_surface.fill((0, 0, 0))
                surfaces_aux.append(labyrinth_surface)

        labyrinth_surfaces.append(surfaces_aux)

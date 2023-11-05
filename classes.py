import pygame
MOUSE = (255, 193, 110)
CHEESE = (255, 255, 0)


class Cell():
    def __init__(self, color, x: float = 0, y: float = 0) -> None:
        self.color = color
        self.surface = pygame.Surface((50, 50))
        self.surface.fill(color)
        self.rectangle = self.surface.get_rect()
        self.position = self.rectangle.center
        self.width = self.rectangle.width
        self.height = self.rectangle.height


class Mouse(pygame.sprite.Sprite):
    def __init__(self, x: float = 0, y: float = 0) -> None:
        super(Mouse, self).__init__()
        self.surface = pygame.image.load("icons/jerry.png").convert()
        self.rectangle = self.surface.get_rect()
        self.width = self.rectangle.width
        self.height = self.rectangle.height
        self.position = self.rectangle.center
        self.color = MOUSE


class Cheese(pygame.sprite.Sprite):
    def __init__(self, x: float = 0, y: float = 0) -> None:
        super(Cheese, self).__init__()
        self.surface = pygame.image.load("icons/cheese.png").convert()
        self.rectangle = self.surface.get_rect()
        self.width = self.rectangle.width
        self.height = self.rectangle.height
        self.position = self.rectangle.center
        self.color = CHEESE

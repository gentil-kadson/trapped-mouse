import pygame


class Cell(pygame.surface.Surface):
    def __init__(self, color: str):
        self.fill(color)
        self.rectangle = self.get_rect()
        self.rectangle.width = 50
        self.rectangle.height = 50


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super(Mouse, self).__init__()
        self.surface = pygame.image.load("icons/jerry.png").convert()
        self.rectangle = self.surface.get_rect()


class Cheese(pygame.sprite.Sprite):
    def __init__(self):
        super(Cheese, self).__init__()
        self.surface = pygame.image.load("icons/cheese.png").convert()
        self.rectangle = self.surface.get_rect()

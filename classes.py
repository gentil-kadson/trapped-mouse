import pygame


class Cell():
    def __init__(self, color):
        self.surface = pygame.Surface((50, 50))
        self.surface.fill(color)
        self.rectangle = self.surface.get_rect()
        self.width = self.rectangle.width
        self.height = self.rectangle.height


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super(Mouse, self).__init__()
        self.surface = pygame.image.load("icons/jerry.png").convert()
        self.rectangle = self.surface.get_rect()
        self.width = self.rectangle.width
        self.height = self.rectangle.height


class Cheese(pygame.sprite.Sprite):
    def __init__(self):
        super(Cheese, self).__init__()
        self.surface = pygame.image.load("icons/cheese.png").convert()
        self.rectangle = self.surface.get_rect()
        self.width = self.rectangle.width
        self.height = self.rectangle.height

import pygame


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
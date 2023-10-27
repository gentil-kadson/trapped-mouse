import pygame


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super(Mouse, self).__init__()
        self.mouse_surface = pygame.image.load("/icons/rat.png").convert()
        self.rectangle = self.mouse_surface.get_rect()


class Cheese(pygame.sprite.Sprite):
    def __init__(self):
        super(Cheese, self).__init__()
        self.cheese_surface = pygame.image.load("/icons/cheese.png").convert()
        self.rectangle = self.cheese_surface.get_rect()

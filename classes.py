import pygame
from colors import *


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./icons/jerry.png")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_center(self, coordinates: tuple[int, int]):
        self.rect.center = coordinates


class Path(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((70, 70))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_center(self, coordinates: tuple[int, int]):
        self.rect.center = coordinates


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((70, 70))
        self.image.fill(CHARCOAL)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_center(self, coordinates: tuple[int, int]):
        self.rect.center = coordinates

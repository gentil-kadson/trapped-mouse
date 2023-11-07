import pygame
from colors import *


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./icons/mouse.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_center(self, coordinates: tuple[int, int]):
        self.rect.center = coordinates

    def move_right(self) -> None:
        self.rect.move_ip(70, 0)

    def move_left(self) -> None:
        self.rect.move_ip(-70, 0)

    def move_up(self) -> None:
        self.rect.move_ip(0, -7)

    def move_down(self) -> None:
        self.rect.move_ip(0, 7)


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

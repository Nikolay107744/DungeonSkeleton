import pygame
from core.settings import SCALED_TILE_SIZE

class Gemstone:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SCALED_TILE_SIZE, SCALED_TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x * SCALED_TILE_SIZE, y * SCALED_TILE_SIZE))

    def render(self, screen, camera):
        screen.blit(self.image, camera.apply(self))


class PinkGemstone(Gemstone):
    def __init__(self, x, y):
        super().__init__(x, y, "../assets/collectables/Gem_E_Pink.png")


class OrangeGemstone(Gemstone):
    def __init__(self, x, y):
        super().__init__(x, y, "../assets/collectables/Gem_E_Orange.png")
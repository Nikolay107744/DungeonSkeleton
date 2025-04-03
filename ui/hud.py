import pygame
from core.settings import SCALE_FACTOR

class UI:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.SysFont("Arial", 10 * SCALE_FACTOR)

    def render(self, screen):
        # Render collected gems
        gem_text = f"Gems: {self.player.collected_gems}"

        # Shadow for visibility
        shadow = self.font.render(gem_text, True, (0, 0, 0))
        text_surface = self.font.render(gem_text, True, (255, 255, 255))

        screen.blit(shadow, (12, 12))
        screen.blit(text_surface, (10, 10))
import pygame
from core.settings import SCALED_TILE_SIZE

class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_path):
        super().__init__()

        # Load and scale image
        original_image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(original_image, (SCALED_TILE_SIZE, SCALED_TILE_SIZE))

        # Create a rect that matches the scaled image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, dt):
        """Update logic for the entity."""
        pass  # To be overridden by subclasses

    def render(self, screen, camera):
        """Render the entity on screen with camera offset."""
        screen.blit(self.image, camera.apply(self))

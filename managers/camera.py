import pygame
from core.settings import WIDTH, HEIGHT, SCALE_FACTOR

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)

    def apply(self, entity):
        """Offset entity position based on camera position."""
        return entity.rect.move(-self.camera.x, -self.camera.y)

    def update(self, target):
        """Center the camera on the player."""
        self.camera.x = target.rect.x - (WIDTH // 2)
        self.camera.y = target.rect.y - (HEIGHT // 2)

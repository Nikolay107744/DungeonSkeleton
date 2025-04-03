import pygame
from core.settings import SCALED_TILE_SIZE, SCALE_FACTOR

class Tile:
    """Base Tile class with automatic scaling."""
    def __init__(self, x, y, sprite):
        original_image = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(original_image, (SCALED_TILE_SIZE, SCALED_TILE_SIZE))
        self.rect = pygame.Rect(x * SCALE_FACTOR, y * SCALE_FACTOR, SCALED_TILE_SIZE, SCALED_TILE_SIZE)

    def render(self, screen, camera):
        screen.blit(self.image, camera.apply(self))


class Floor(Tile):
    """Represents a floor tile."""
    def __init__(self, x, y, sprite="../assets/floor.png"):
        super().__init__(x, y, sprite)
        self.is_solid = False


class Wall(Tile):
    """Represents a wall tile with different variations."""
    def __init__(self, x, y, wall_type):
        # Choose the correct wall sprite based on type
        sprite_mapping = {
            "top": "../assets/wall_top.png",
            "bottom": "../assets/wall_bottom.png",
            "left": "../assets/wall_left.png",
            "right": "../assets/wall_right.png",
        }
        super().__init__(x, y, sprite_mapping[wall_type])
        self.is_solid = True

import pygame
from .base_entity import BaseEntity
from core.settings import PLAYER_SPEED, SCALED_TILE_SIZE

class Player(BaseEntity):
    def __init__(self, x, y, sprite_path, level):
        scaled_x = x * SCALED_TILE_SIZE
        scaled_y = y * SCALED_TILE_SIZE
        super().__init__(scaled_x, scaled_y, sprite_path)

        self.level = level
        self.gemstones = level.gemstones
        self.velocity_x = 0
        self.velocity_y = 0
        self.collected_gems = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                self.velocity_x = PLAYER_SPEED
            if event.key in (pygame.K_a, pygame.K_LEFT):
                self.velocity_x = -PLAYER_SPEED
            if event.key in (pygame.K_s, pygame.K_DOWN):
                self.velocity_y = PLAYER_SPEED
            if event.key in (pygame.K_w, pygame.K_UP):
                self.velocity_y = -PLAYER_SPEED

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_d, pygame.K_RIGHT, pygame.K_a, pygame.K_LEFT):
                self.velocity_x = 0
            if event.key in (pygame.K_s, pygame.K_DOWN, pygame.K_w, pygame.K_UP):
                self.velocity_y = 0

    def move(self):
        new_x = self.rect.x + self.velocity_x
        new_y = self.rect.y + self.velocity_y

        # Horizontal movement
        future_rect_x = self.rect.copy()
        future_rect_x.x = new_x
        if not self.collides_with_solid_tile(future_rect_x):
            self.rect.x = new_x

        # Vertical movement
        future_rect_y = self.rect.copy()
        future_rect_y.y = new_y
        if not self.collides_with_solid_tile(future_rect_y):
            self.rect.y = new_y

    def collides_with_solid_tile(self, rect):
        top_left = (rect.left // SCALED_TILE_SIZE, rect.top // SCALED_TILE_SIZE)
        top_right = ((rect.right - 1) // SCALED_TILE_SIZE, rect.top // SCALED_TILE_SIZE)
        bottom_left = (rect.left // SCALED_TILE_SIZE, (rect.bottom - 1) // SCALED_TILE_SIZE)
        bottom_right = ((rect.right - 1) // SCALED_TILE_SIZE, (rect.bottom - 1) // SCALED_TILE_SIZE)

        for (tx, ty) in [top_left, top_right, bottom_left, bottom_right]:
            if self.level.is_solid(tx, ty):
                return True

        return False

    def collect_gemstones(self):
        for gem in self.gemstones[:]:  # Copy to avoid modifying during iteration
            if self.rect.colliderect(gem.rect):
                self.gemstones.remove(gem)
                self.collected_gems += 1
                print(f"💎 Collected! Total gems: {self.collected_gems}")

    def update(self, dt):
        self.move()
        self.collect_gemstones()

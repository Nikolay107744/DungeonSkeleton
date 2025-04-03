import pygame
from core.settings import WIDTH, HEIGHT, FPS, SCALE_FACTOR
from managers.camera import Camera
from levels.level import Level
from entities.player import Player
from ui.hud import UI

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # Load assets
        player_sprite = "../assets/player.png"

        # Load Level
        self.level = Level()

        # Create player
        self.player = Player(3, 3, player_sprite, self.level)  # Start position in tiles

        self.ui = UI(self.player)

        # Initialize camera
        self.camera = Camera(WIDTH, HEIGHT)

    def run(self):
        """Main game loop."""
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            self.handle_events()
            self.update(dt)
            self.render()

    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.player.handle_input(event)

    def update(self, dt):
        """Update game objects."""
        self.player.update(dt)
        self.camera.update(self.player)

    def render(self):
        """Render the game scene."""
        self.screen.fill((0, 0, 0))
        self.level.render(self.screen, self.camera)
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        self.ui.render(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

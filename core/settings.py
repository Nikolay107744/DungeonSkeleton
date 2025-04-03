# General Settings
WIDTH, HEIGHT = 800, 600  # Screen resolution
FPS = 60

# Scaling Factor (Change this for bigger/smaller rendering)
SCALE_FACTOR = 8  # Try 2, 4, or 8

# Tile Settings
TILE_SIZE = 16  # Base tile size in pixels
SCALED_TILE_SIZE = TILE_SIZE * SCALE_FACTOR  # Scaled tile size for rendering

# Player Settings
PLAYER_SPEED = 2 * SCALE_FACTOR  # Adjusted for scale

# Tile Symbols
WALL_SYMBOL = "@"
FLOOR_SYMBOL = "#"
EMPTY_SYMBOL = " "

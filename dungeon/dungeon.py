from .tile import Wall, Floor
from core.settings import TILE_SIZE, WALL_SYMBOL, FLOOR_SYMBOL, EMPTY_SYMBOL, SCALE_FACTOR

class Dungeon:
    def __init__(self, level_data):
        """Initialize the dungeon based on level string layout."""
        self.tiles = []
        self.width = len(level_data[0])
        self.height = len(level_data)

        for row_idx, row in enumerate(level_data):
            row_tiles = []
            for col_idx, symbol in enumerate(row):
                x, y = col_idx * TILE_SIZE, row_idx * TILE_SIZE  # Logical position

                if symbol == WALL_SYMBOL:
                    wall_type = self.get_wall_type(level_data, row_idx, col_idx)
                    row_tiles.append(Wall(x, y, wall_type))
                elif symbol == FLOOR_SYMBOL:
                    row_tiles.append(Floor(x, y))
                else:
                    row_tiles.append(None)  # Empty space

            self.tiles.append(row_tiles)

    def get_wall_type(self, level_data, row, col):
        """Determine if the wall is top, bottom, left, or right."""
        if row > 0 and level_data[row - 1][col] != WALL_SYMBOL:
            return "top"
        if row < len(level_data) - 1 and level_data[row + 1][col] != WALL_SYMBOL:
            return "bottom"
        if col > 0 and level_data[row][col - 1] != WALL_SYMBOL:
            return "left"
        if col < len(level_data[row]) - 1 and level_data[row][col + 1] != WALL_SYMBOL:
            return "right"
        return "top"  # Default to top wall if surrounded

    def render(self, screen, camera):
        """Render only the visible tiles."""
        for row in self.tiles:
            for tile in row:
                if tile:
                    tile.render(screen, camera)

    def is_solid(self, col, row):
        """Check if tile at (col, row) is solid. Coordinates are in tile units."""
        if 0 <= row < self.height and 0 <= col < self.width:
            tile = self.tiles[row][col]
            return tile.is_solid if tile else True
        return True  # Treat empty or out-of-bounds as solid

from dungeon.dungeon import Dungeon
from entities.collectables.gemstone import PinkGemstone, OrangeGemstone
from dungeon.tile import Floor
from core.settings import TILE_SIZE

class Level:
    def __init__(self):
        """Define the level layout using a string format."""
        level_layout = [
            "@@@@@@@@@@@@@@@@@@@@@@@",
            "@@#####@@@@@@@@@@@@@@@@",
            "@@#@@@@@@@@@@@@@@@@@@@@",
            "@###M#############P###@",
            "@@@#@@@@@@@@#@@@@@@@@@@",
            "@M@#@#@P@#M###@@#@@@#@@",
            "@#@#@#@#@#####@######M@",
            "@#####################@",
            "@@@@@@@@@@@@@@@@@#@@@@@",
            "@@@@@@@@@@@@    @#@    ",
            "@M#########@@@@@@#@@@@@",
            "@###@@##P#####M###P###@",
            "@##########@@@@@@@@@@@@",
            "@@@@@@@@@@@@           "
        ]

        self.dungeon = Dungeon(level_layout)
        self.gemstones = []

        for row_idx, row in enumerate(level_layout):
            for col_idx, symbol in enumerate(row):
                if symbol == "P" or symbol == "M":
                    # Place a floor under the gemstone so player can walk there
                    self.dungeon.tiles[row_idx][col_idx] = Floor(col_idx * TILE_SIZE, row_idx * TILE_SIZE)

                if symbol == "P":
                    self.gemstones.append(PinkGemstone(col_idx, row_idx))
                elif symbol == "M":
                    self.gemstones.append(OrangeGemstone(col_idx, row_idx))

    def render(self, screen, camera):
        self.dungeon.render(screen, camera)

        # Render all gemstones
        for gem in self.gemstones:
            gem.render(screen, camera)

    def is_solid(self, x, y):
        return self.dungeon.is_solid(x, y)

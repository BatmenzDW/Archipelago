from typing import ClassVar

from test.bases import WorldTestBase

class BluePrinceTestBase(WorldTestBase):
    game = "Blue Prince"
    player: ClassVar[int] = 1

    def debug_print_regions_and_items(self) -> None:
        regions = self.multiworld.state.reachable_regions[self.player]
        print("Regions: [",", ".join([x.name for x in regions]), "]")
        print()
        items = self.multiworld.state.prog_items[self.player]        
        print("Items: [",", ".join(items), "]")
from typing import ClassVar

from test.bases import WorldTestBase

class BluePrinceTestBase(WorldTestBase):
    game = "Blue Prince"
    player: ClassVar[int] = 1

    def debug_print_regions_items_locations(self, do_print: bool = False):
        regions = self.multiworld.state.reachable_regions[self.player]
        items = self.multiworld.state.prog_items[self.player]
        locations = self.multiworld.get_reachable_locations(self.multiworld.state, self.player)
        if do_print:
            print("Regions: [",", ".join([x.name for x in regions]), "]")
            print()
            print("Items: [",", ".join([f"{item}: {items[item]}" if items[item] > 1 else item for item in items]), "]")
            print()
            print("Locations: [",", ".join([x.name for x in locations]), "]")
        else:
            return f"Regions: [{', '.join([x.name for x in regions])} ]\nItems: [{', '.join([f'{item}: {items[item]}' if items[item] > 1 else item for item in items])}]\nLocations: [{', '.join([x.name for x in locations])}]"
            
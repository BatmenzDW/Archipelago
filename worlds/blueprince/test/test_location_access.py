from BaseClasses import CollectionState, Location
from worlds.blueprince.options import GoalType
from worlds.blueprince.test import BluePrinceTestBase
from worlds.blueprince.data_rooms import rooms, core_rooms
from worlds.blueprince.constants import *

class TestLocationAccess(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_room46,
    }
    
    def test_can_reach_tunnel_floorplan_after_crates(self):
        self.collect_by_name(["Laboratory", "Boiler Room", "Parlor", "Clock Tower", "Observatory", "Attic", "Study", "Office", "MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3", "TORCH", "The Armory", "Garage", "Hovel", "Utility Closet", "Schoolhouse"])
        self.assertTrue(self.can_reach_region("Tunnel Area Past Crates"), "Tunnel Floorplan should be reachable after having the crates")

    def test_can_reach_compass(self):
        self.collect_by_name(["Closet", "COMPASS"])
        self.debug_print_regions_items_locations(True)
        self.assertTrue(self.can_reach_location("COMPASS First Pickup"), "COMPASS First Pickup should be reachable after having ")

    def test_can_craft_electromagnet(self):
        self.collect_by_name(["Electromagnet", "COMPASS", "BATTERY PACK", "Workshop", "Closet", "Bedroom"])
        self.assertTrue(self.can_reach_location("Electromagnet First Craft"), "Electromagnet should be reachable after having the required items")
from BaseClasses import CollectionState, Location
from ..options import GoalType
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *

class TestLocationAccess(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_room46,
    }
    
    def test_can_reach_tunnel_floorplan_after_crates(self):
        self.collect_by_name(["Laboratory", "Boiler Room", "Parlor", "MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3", "Garage", "Hovel", "Utility Closet", "Schoolhouse", "SHOVEL", "SLEDGE HAMMER", "Workshop", "MAGNIFYING GLASS", "METAL DETECTOR", "Library", "Burning Glass"])
        self.debug_print_regions_items_locations(True)
        self.assertTrue(self.can_reach_location("Raise Satellite"), "Raise Satellite should be reachable after having the microchips and burning glass")
        self.assertTrue(self.can_reach_region("Tunnel Area Past Crates"), "Tunnel Floorplan should be reachable after having crate experiment")

    def test_can_reach_compass(self):
        self.collect_by_name(["Closet", "COMPASS"])
        self.debug_print_regions_items_locations(True)
        self.assertTrue(self.can_reach_location("COMPASS First Pickup"), "COMPASS First Pickup should be reachable after having ")

    def test_can_craft_electromagnet(self):
        self.collect_by_name(["Electromagnet", "COMPASS", "BATTERY PACK", "Workshop", "Closet", "Bedroom"])
        self.assertTrue(self.can_reach_location("Electromagnet First Craft"), "Electromagnet should be reachable after having the required items")

    def test_can_craft_burning_glass(self):
        self.collect_by_name(["Burning Glass", "Workshop", "MAGNIFYING GLASS", "Library", "METAL DETECTOR"])
        self.assertTrue(self.can_reach_location("Burning Glass First Craft"), "Burning Glass should be reachable after having the required items")
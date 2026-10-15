from BaseClasses import CollectionState, Location
from ..rules import CanReachItemLocation
from ..options import GoalType
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *
from ..locations import LOCATION_NAME_TO_ID
from ..items import ITEM_NAME_TO_ID

class TestLocationAccess(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "goal_type": GoalType.option_room46,
        "dev_testing": True,
    }

    def test_all_location_ids_unique(self):
        mem = dict()
        for name, id in LOCATION_NAME_TO_ID.items():
            if id in mem:
                self.fail(f"Duplicate location ID {id} for {name} and {mem[id]}")
            mem[id] = name

    def test_can_reach_tunnel_after_crates(self):
        self.collect_all_but(["Laboratory", "MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3", "Burning Glass", "TORCH", "Satellite Dish"])
        self.assertFalse(self.can_reach_region("Tunnel Area Past Crates"), "Tunnel Area Past Crates should not be reachable without having crate experiment")
        self.collect_by_name(["Laboratory", "MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3", "TORCH", "Satellite Dish"])
        self.assertTrue(self.can_reach_region("Tunnel Area Past Crates"), "Tunnel Area Past Crates should be reachable after having crate experiment")

    def test_can_reach_compass(self):
        self.collect_by_name(["Closet", "COMPASS"])
        self.debug_print_regions_items_locations(True)
        self.assertTrue(self.can_reach_location("First Pickup - COMPASS"), "COMPASS First Pickup should be reachable after having ")

    def test_can_craft_electromagnet(self):
        self.collect_by_name(["Electromagnet", "COMPASS", "BATTERY PACK", "Workshop", "Closet", "Bedroom"])
        self.assertTrue(self.can_reach_location("First Pickup - Electromagnet"), "Electromagnet should be reachable after having the required items")

    def test_can_craft_burning_glass(self):
        self.collect_by_name(["Burning Glass", "Workshop", "MAGNIFYING GLASS", "Library", "METAL DETECTOR"])
        self.assertTrue(self.can_reach_location("First Pickup - Burning Glass"), "Burning Glass should be reachable after having the required items")

    def test_bunk_rooms_have_same_item(self):
        from Fill import distribute_items_restrictive
        distribute_items_restrictive(self.multiworld)
        loc1 = self.world.get_location("First Draft - Bunk Room").item
        loc2 = self.world.get_location("First Draft - Bunk Room 2").item
        self.assertIsNotNone(loc1, "First Draft - Bunk Room should have an item")
        self.assertIsNotNone(loc2, "First Draft - Bunk Room 2 should have an item")
        self.assertEqual(loc1.name, loc2.name, "First Draft - Bunk Room and First Draft - Bunk Room 2 should have the same item") # type: ignore
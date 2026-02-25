from worlds.blueprince.options import GoalType
from worlds.blueprince.test import BluePrinceTestBase
from worlds.blueprince.data_rooms import rooms, core_rooms
from worlds.blueprince.constants import *

class TestRegionAcess(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_room46,
    }

    def test_starting_from_campsite(self) -> None:
        self.assertTrue(self.can_reach_region("Campsite"))
        self.assertTrue(self.can_reach_region("Entrance Hall"))
        self.assertTrue(self.can_reach_region("Grounds"))
        self.assertTrue(self.can_reach_region("Private Drive"))
        self.assertTrue(self.can_reach_region("Apple Orchard"))
        self.assertTrue(self.can_reach_region("Tunnel Area Entrance"))

    def test_inner_rooms_requires_room_item(self) -> None:

        for room,v in rooms.items():
            if room in core_rooms or v[OUTER_ROOM_KEY]:
                continue

            self.assertFalse(self.can_reach_region(room), f"{room} should not be reachable without having the room as an item")
            self.collect_by_name(room)
            self.assertTrue(self.can_reach_region(room), f"{room} should be reachable after collecting the room as an item")
    
    def test_outer_room_requires_garage_utility_closet(self) -> None:
        self.assertFalse(self.can_reach_region("Outer Room"), f"Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Utility Closet")
        self.assertFalse(self.can_reach_region("Outer Room"), f"Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Garage")
        self.assertTrue(self.can_reach_region("Outer Room"), f"Outer Room should be reachable after collecting the Garage as an item")
    
    def test_outer_room_requires_garage_boiler_room(self) -> None:
        self.assertFalse(self.can_reach_region("Outer Room"), f"Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Garage")

        self.assertFalse(self.can_reach_region("Outer Room"), f"Outer Room should not be reachable without having the Garage as an item")

        self.collect_by_name("Boiler Room")
        self.assertTrue(self.can_reach_region("Outer Room"), f"Outer Room should be reachable after collecting the Garage as an item")

    def test_outer_rooms_require_room_item(self) -> None:
        self.assertFalse(self.can_reach_region("Outer Room"), f"Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Garage")
        self.collect_by_name("Utility Closet")
        self.assertTrue(self.can_reach_region("Outer Room"), f"Outer Room should be reachable after collecting the Garage as an item")

        for room,v in rooms.items():
            if not v[OUTER_ROOM_KEY]:
                continue

            self.assertFalse(self.can_reach_region(room), f"{room} should not be reachable without having the room as an item")
            self.collect_by_name(room)
            self.assertTrue(self.can_reach_region(room), f"{room} should be reachable after collecting the room as an item")
    
    def test_gemstone_cavern_requires_utility_closet(self) -> None:
        self.assertFalse(self.can_reach_region("Gemstone Cavern"), f"Gemstone Caverns should not be reachable without having the Utility Closet as an item")
        self.collect_by_name("Utility Closet")
        self.assertTrue(self.can_reach_region("Gemstone Cavern"), f"Gemstone Caverns should be reachable after collecting the Utility Closet as an item")
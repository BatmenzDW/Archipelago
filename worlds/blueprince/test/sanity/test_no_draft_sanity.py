
from ...constants import *

from ...options import GoalType
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms

class TestNoDraftSanity(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "room_draft_sanity": False,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "goal_type": GoalType.option_room46,
    }

    def test_all_starting_room_items(self) -> None:
        for room, data in rooms.items():
            if room in core_rooms or room in ["Secret Garden", "Room 8"]:
                continue
            
            if NONSANITY_LOCATION_KEY not in data or data[NONSANITY_LOCATION_KEY] == STARTING_INVENTORY:
                self.assertTrue(self.multiworld.state.has(room, self.player), f"Expected to have {room} in starting inventory for player {self.player}")
            else:
                self.assertFalse(self.multiworld.state.has(room, self.player), f"Expected not to have {room} in starting inventory for player {self.player}")
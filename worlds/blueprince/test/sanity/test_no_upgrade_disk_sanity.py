
from ...constants import *

from ...options import GoalType
from ...test import BluePrinceTestBase

class TestNoUpgradeDiskSanity(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "room_draft_sanity": True,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": False,
        "key_sanity": True,
        "special_shop_sanity": True,
        "item_logic_mode": "complex",
        "goal_type": GoalType.option_room46,
    }

    def test_battery_pack_from_car_requires_terminal(self):
        self.remove(self.multiworld.get_items())
        self.collect_by_name(["Garage", "Hallway", "West Wing Hall", "Pantry", "Parlor", "Bedroom", "CAR KEYS"])
        self.assertTrue(self.can_reach_region("Garage"), "Garage should be reached for this Battery Pack location")
        print(self.world.get_location("BATTERY PACK First Pickup").access_rule.explain_json())
        self.assertFalse(self.can_reach_location("BATTERY PACK First Pickup"), "Should not be able to reach Battery Pack without having a way to block the upgrade disk spawn.")
        self.collect_by_name("Office")
        self.assertTrue(self.can_reach_location("BATTERY PACK First Pickup"), "Should be able to reach Battery Pack once having a way to block the upgrade disk spawn.")
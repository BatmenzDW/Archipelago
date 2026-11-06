
import typing

from ....AutoWorld import call_all

from BaseClasses import Location, MultiWorld, CollectionState, Item

from ...options import GoalType
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms
from ... import data_rooms, data_other_locations

class TestItemLogicComplex(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "starting_room_amount": 3,
        "room_draft_sanity": True,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "item_logic_mode": "complex",
        "goal_type": GoalType.option_room46,
    }

    def test_trading_post_upgrade_disk(self):
        self.collect_by_name(["Garage", "Trading Post", "Utility Closet", "Showroom", "Vault", "Hallway", "Spare Room", "ORNATE COMPASS", "Casino"])
        self.assertTrue(self.can_reach_location("First Pickup - ORNATE COMPASS"), "Should be able to reach Ornate Compass First Pickup with Showroom and required coins")
        self.assertTrue(self.can_reach_location("Upgrade Disk - Trading Post Trade"), "Should be able to reach Trading Post Upgrade Disk with Trading Post and a valid trade")
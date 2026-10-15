
from ...rules import CanReachItemLocation

from ...constants import *

from ...options import GoalType
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms

class TestItemLogicDefault(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "room_draft_sanity": False,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "item_logic_mode": "default",
        "goal_type": GoalType.option_room46,
    }

    def test_commissary_upgrade_disk_requires_blocking(self):
        # self.collect_by_name(["Commissary", "Vault"])
        self.assertFalse(self.can_reach_location("Upgrade Disk - Commissary"), "Should not be able to reach Upgrade Disk - Commissary without items to block Commissary selections")
        self.collect_by_name(["SLEDGE HAMMER", "SHOVEL"])
        self.assertTrue(self.can_reach_location("Upgrade Disk - Commissary"), "Should be able to reach Upgrade Disk - Commissary with items to block Commissary selections")
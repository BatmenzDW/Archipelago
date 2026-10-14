
from ...constants import *

from ...options import GoalType
from ...test import BluePrinceTestBase

class TestItemLogicExtreme(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "room_draft_sanity": False,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "item_logic_mode": "extreme",
        "goal_type": GoalType.option_room46,
    }
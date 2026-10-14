
from ...constants import *

from ...options import GoalType
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms

class TestItemLogicRareComplex(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "room_draft_sanity": False,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "item_logic_mode": "rare_complex",
        "goal_type": GoalType.option_room46,
    }
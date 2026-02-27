from ..options import GoalType
from ..test import BluePrinceTestBase
from ..constants import *

class TestAscendVictory(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_ascend,
    }
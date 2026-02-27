from worlds.blueprince.options import GoalType
from worlds.blueprince.test import BluePrinceTestBase
from worlds.blueprince.constants import *

class TestAscendVictory(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_ascend,
    }
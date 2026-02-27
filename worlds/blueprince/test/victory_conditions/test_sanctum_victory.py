from BaseClasses import CollectionState, Location
from ..options import GoalType
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *

class TestSanctumVictory(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_sanctum,
        "goal_sanctum_solves": 8
    }
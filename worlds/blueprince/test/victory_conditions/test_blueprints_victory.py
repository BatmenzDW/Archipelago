from BaseClasses import CollectionState, Location
from ...options import GoalType, ItemLogicMode
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms
from ...constants import *

class TestBlueprintsVictory(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "trophy_sanity": True,
        "item_logic_mode": ItemLogicMode.option_complex,
        "goal_type": GoalType.option_blueprints,
    }
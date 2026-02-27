from BaseClasses import CollectionState, Location
from worlds.blueprince.options import GoalType
from worlds.blueprince.test import BluePrinceTestBase
from worlds.blueprince.data_rooms import rooms, core_rooms
from worlds.blueprince.constants import *

class TestAntechamberVictory(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_antechamber,
    }
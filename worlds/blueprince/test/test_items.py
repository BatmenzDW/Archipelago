from BaseClasses import CollectionState, Location
from ..options import GoalType
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *
from ..locations import LOCATION_NAME_TO_ID
from ..items import ITEM_NAME_TO_ID

class TestLocationAccess(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "goal_type": GoalType.option_room46,
    }

    def test_all_item_ids_unique(self):
        mem = dict()
        for name, id in ITEM_NAME_TO_ID.items():
            if id in mem:
                self.fail(f"Duplicate item ID {id} for {name} and {mem[id]}")
            mem[id] = name
    
    def test_item_groups(self):
        for name, group in self.world.item_name_groups.items():
            print(f"Group {name} contains: {group}\n")
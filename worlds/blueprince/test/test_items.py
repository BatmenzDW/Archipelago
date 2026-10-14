from BaseClasses import CollectionState, Location
from ..options import GoalType, ItemLogicMode, EnableObscureLocations
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *
from ..locations import LOCATION_NAME_TO_ID
from ..items import ITEM_NAME_TO_ID

class TestItems(BluePrinceTestBase):
    options = {
        "progression_balancing": 5,
        "accessibility": "full",
        "room_draft_sanity": False,
        "starting_room_amount": 8,
        "locked_trunks_common": 30,
        "locked_trunks_rare": 6,
        "locked_trunks_complex": 78,
        "trunks": {
            "Secret Passage": 71,
            "Her Ladyship's Chamber": 86,
            "Conservatory": 46,
            "Morning Room": 85,
            "Great Hall": 81,
            "Entrance Hall": 68,
            "Drawing Room": 64,
            "Storeroom": 16,
        },
        "item_logic_mode": ItemLogicMode.option_rare,
        "standard_item_sanity": False,
        "workshop_sanity": True,
        "upgrade_disk_sanity": False,
        "key_sanity": False,
        "enable_obscure_locations": EnableObscureLocations.option_enable,
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
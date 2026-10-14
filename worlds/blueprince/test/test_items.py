from BaseClasses import CollectionState, Location
from ..options import GoalType, ItemLogicMode, EnableObscureLocations
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *
from ..locations import LOCATION_NAME_TO_ID
from ..items import ITEM_NAME_TO_ID

class TestItems(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "starting_room_amount": 8,
        "locked_trunks_common": 38,
        "locked_trunks_rare": 78,
        "locked_trunks_complex": 41,
        "trunks": {
            "Hovel": 92,
            "Weight Room": 92,
            "Morning Room": 14,
            "Attic": 50,
            "Drawing Room": 26,
            "Entrance Hall": 29,
            "Mail Room": 29,
            "Foyer": 11,
            "Dormitory": 66,
            "Mechanarium": 11,
            "Gallery": 55,
            "Conservatory": 99,
            "Trophy Room": 17,
            "Office": 32,
            "Nook": 0,
            "Root Cellar": 70,
            "Planetarium": 31,
            "Her Ladyship's Chamber": 60,
            "Pump Room": 18,
            "Music Room": 67
        },
        "item_logic_mode": ItemLogicMode.option_complex,
        "standard_item_sanity": False,
        "workshop_sanity": False,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "enable_obscure_locations": EnableObscureLocations.option_exclude,
        "goal_type": GoalType.option_antechamber
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
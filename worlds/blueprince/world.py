from collections.abc import Mapping
from typing import Any, Set

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

from .data_items import ITEMS_BY_GROUPS
# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import (
    options as blue_prince_options,
)  # rename due to a name conflict with World.options


class BluePrinceWorld(World):
    """
    Blue Prince is a puzzle-adventure Roguelite where the player takes on the role of
    Simon P Jones as he explores the Mt. Holly estate, bequeathed to him in the will
    of his great uncle, Herbert S. Sinclair. The only stipulation is that Simon must
    discover a hidden 46th room within the mansion thereon to secure his inheritance.
    """

    game = "Blue Prince"

    # Set the Web World
    web = web_world.BluePrinceWebWorld()

    # Set the Options
    options_dataclass = blue_prince_options.BluePrinceOptions
    options: blue_prince_options.BluePrinceOptions

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    # Technically, Simon starts in the Entrance Hall, but for lore reasons, Starting at The Campsite is also acceptable, and is not a "room"
    origin_region_name = "Campsite"

    item_name_groups = ITEMS_BY_GROUPS

    dares : Set[str] = set()

    # # Our world class must have certain functions ("steps") that get called during generation.
    # # The main ones are: create_regions, set_rules, create_items.
    # # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BluePrinceItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "room_draft_sanity",
            "locked_trunks_common",
            "locked_trunks_rare",
            "locked_trunks_complex",
            "standard_item_sanity",
            "workshop_sanity",
            "upgrade_disk_sanity",
            "key_sanity",
            "special_shop_sanity",
            "item_logic_mode",
            "filler_item_distribution",
            "trap_type_distribution",
            "trap_percentage",
            "death_link_type",
            "death_link_grace",
            "death_link_monk_exception",
            "goal_type",
            "goal_sanctum_solves",
            "start_inventory",
        )

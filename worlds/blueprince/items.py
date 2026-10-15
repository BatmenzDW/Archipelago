from __future__ import annotations

from random import random
from typing import TYPE_CHECKING

from .room_min_pieces import ENTRANCE_HALL_DRAFTABLE

from .data_rooms import rooms, core_rooms, classrooms
from .data_items import *
from .constants import *
from . import data_rooms

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BluePrinceWorld

ITEM_NAME_TO_ID = (
    {
        # Special Items
        "Wind-up Key": 1024,
        #
        # Extra "Stuff" Items
        #
        "1 Allowance": 10101,
        "2 Allowance": 10102,
        #
        "1 Gold": 10201,
        "2 Gold": 10202,
        "5 Gold": 10203,
        #
        "1 Dice": 10301,
        "2 Dice": 10302,
        "4 Dice": 10303,
        #
        "1 Gems": 10501,
        "2 Gems": 10502,
        #
        "1 Keys": 10601,
        "2 Keys": 10602,
        "3 Keys": 10603,
        #
        "1 Steps": 10701,
        "2 Steps": 10702,
        "5 Steps": 10703,
        #
        "1 Permanent Dice": 10801,
        "2 Permanent Dice": 10802,
        #
        "1 Permanent Gems": 10901,
        "2 Permanent Gems": 10902,
        #
        "1 Permanent Keys": 11001,
        "2 Permanent Keys": 11002,
        #
        "1 Permanent Luck": 11101,
        "2 Permanent Luck": 11102,
        #
        "1 Permanent Steps": 11201,
        "2 Permanent Steps": 11202,
        "5 Permanent Steps": 11203,
        "10 Permanent Steps": 11204,
        #
        "1 Stars": 11301,
        "2 Stars": 11302,
        "5 Stars": 11303,
        #
        # Traps
        #
        "Trap Freeze Items": 40101,
        #
        "Trap Take Steps 1": 40201,
        "Trap Take Steps 2": 40202,
        "Trap Take Steps 5": 40203,
        #
        "Trap Set Steps 1": 41201,
        "Trap Set Steps 10": 41202,
        #
        "Trap Lose Item": 40301,
        #
        "Trap Lose Stars 1": 40401,
        "Trap Lose Stars 2": 40402,
        "Trap Lose Stars 5": 40405,
        #
        "Trap End Day": 40501,
        #
        # Trash Item from digging. Client may interpret this freely as any of the "trash" items
        #
        "Dug Up Nothing": 50000,
        #
        # Progressive Classroom
        #
        "Progressive Classroom": 60000,
    }
    | {k: v[ROOM_ITEM_ID_KEY] * 100_000 for k, v in rooms.items()}
    | {k: v[ITEM_ID_KEY] * 1_000_000 for k, v in all_items.items()}
)


DEFAULT_ITEM_CLASSIFICATIONS = (
    {
        # Special Items
        "Wind-up Key": ItemClassification.progression,
        #
        # Extra "Stuff" Items
        #
        "1 Allowance": ItemClassification.filler,
        "2 Allowance": ItemClassification.filler,
        #
        "1 Gold": ItemClassification.filler,
        "2 Gold": ItemClassification.filler,
        "5 Gold": ItemClassification.filler,
        #
        "1 Dice": ItemClassification.filler,
        "2 Dice": ItemClassification.filler,
        "4 Dice": ItemClassification.filler,
        #
        "1 Gems": ItemClassification.filler,
        "2 Gems": ItemClassification.filler,
        #
        "1 Keys": ItemClassification.filler,
        "2 Keys": ItemClassification.filler,
        "3 Keys": ItemClassification.filler,
        #
        "1 Steps": ItemClassification.filler,
        "2 Steps": ItemClassification.filler,
        "5 Steps": ItemClassification.filler,
        #
        "1 Permanent Dice": ItemClassification.filler,
        "2 Permanent Dice": ItemClassification.filler,
        #
        "1 Permanent Gems": ItemClassification.filler,
        "2 Permanent Gems": ItemClassification.filler,
        #
        "1 Permanent Keys": ItemClassification.filler,
        "2 Permanent Keys": ItemClassification.filler,
        #
        "1 Permanent Luck": ItemClassification.filler,
        "2 Permanent Luck": ItemClassification.filler,
        #
        "1 Permanent Steps": ItemClassification.filler,
        "2 Permanent Steps": ItemClassification.filler,
        "5 Permanent Steps": ItemClassification.filler,
        "10 Permanent Steps": ItemClassification.filler,
        #
        "1 Stars": ItemClassification.filler,
        "2 Stars": ItemClassification.filler,
        "5 Stars": ItemClassification.filler,
        #
        # Traps
        #
        "Trap Freeze Items": ItemClassification.trap,
        #
        "Trap Take Steps 1": ItemClassification.trap,
        "Trap Take Steps 2": ItemClassification.trap,
        "Trap Take Steps 5": ItemClassification.trap,
        #
        "Trap Set Steps 1": ItemClassification.trap,
        "Trap Set Steps 10": ItemClassification.trap,
        #
        "Trap Lose Item": ItemClassification.trap,
        #
        "Trap Lose Stars 1": ItemClassification.trap,
        "Trap Lose Stars 2": ItemClassification.trap,
        "Trap Lose Stars 5": ItemClassification.trap,
        #
        "Trap End Day": ItemClassification.trap,
        #
        # Trash Item from digging. Client may interpret this freely as any of the "trash" items
        #
        "Dug Up Nothing": ItemClassification.filler,
        #
        # Progressive Classroom
        #
        "Progressive Classroom": ItemClassification.progression,
    }
    | {k: v[ROOM_ITEM_CLASSIFICATION_KEY] for k, v in rooms.items()}
    | {k: v[ROOM_ITEM_CLASSIFICATION_KEY] for k, v in all_items.items()}
)


class BluePrinceItem(Item):
    game = "Blue Prince"


def get_random_filler_item_name(world: BluePrinceWorld) -> str:

    if world.random.randint(0, 99) < world.options.trap_percentage:

        choice = world.random.choices(
            list(world.options.trap_type_distribution.value.keys()),
            list(world.options.trap_type_distribution.value.values()),
        )[0]

        count = world.random.randint(0, 99)

        match choice:
            case "freeze_traps":
                return "Trap Freeze Items"

            case "step_traps_1":
                return "Trap Take Steps 1"
            case "step_traps_2":
                return "Trap Take Steps 2"
            case "step_traps_5":
                return "Trap Take Steps 5"

            case "step_traps_set_to_1":
                return "Trap Set Steps 1"
            case "step_traps_set_to_10":
                return "Trap Set Steps 10"

            case "star_traps_1":
                return "Trap Lose Stars 1"
            case "star_traps_2":
                return "Trap Lose Stars 2"
            case "star_traps_5":
                return "Trap Lose Stars 5"

            case "eod_traps":
                return "Trap End Day"

            case "step_traps":
                if count < 20:
                    return "Trap Take Steps 5"
                elif count < 60:
                    return "Trap Take Steps 2"
                else:
                    return "Trap Take Steps 1"
            case "star_traps":
                if count < 20:
                    return "Trap Lose Stars 5"
                elif count < 60:
                    return "Trap Lose Stars 2"
                else:
                    return "Trap Lose Stars 1"
    else:
        choice = world.random.choices(
            list(world.options.filler_item_distribution.value.keys()),
            list(world.options.filler_item_distribution.value.values())
        )[0]

        count = world.random.randint(0, 99)

        match choice:
            case "1_allowance":
                return "Allowance 1"
            case "2_allowance":
                return "Allowance 2"
            case "1_gold":
                return "1 Gold"
            case "2_gold":
                return "2 Gold"
            case "5_gold":
                return "5 Gold"
            case "1_dice":
                return "1 Dice"
            case "2_dice":
                return "2 Dice"
            case "4_dice":
                return "4 Dice"
            case "1_gems":
                return "1 Gems"
            case "2_gems":
                return "2 Gems"
            case "1_keys":
                return "1 Keys"
            case "2_keys":
                return "2 Keys"
            case "3_keys":
                return "3 Keys"
            case "1_stars":
                return "1 Stars"
            case "2_stars":
                return "2 Stars"
            case "5_stars":
                return "5 Stars"

            case "1_permanent_dice":
                return "1 Permanent Dice"
            case "2_permanent_dice":
                return "2 Permanent Dice"
            case "1_permanent_gems":
                return "1 Permanent Gems"
            case "2_permanent_gems":
                return "2 Permanent Gems"
            case "1_permanent_keys":
                return "1 Permanent Keys"
            case "2_permanent_keys":
                return "2 Permanent Keys"
            case "1_permanent_luck":
                return "1 Permanent Luck"
            case "2_permanent_luck":
                return "2 Permanent Luck"
            case "5_permanent_steps":
                return "5 Permanent Steps"
            case "10_permanent_steps":
                return "10 Permanent Steps"

            case "1_steps":
                return "1 Steps"
            case "2_steps":
                return "2 Steps"
            case "5_steps":
                return "5 Steps"
            case "nothing":
                return "Dug Up Nothing"

            case "allowance":
                if count < 20:
                    return "Allowance 2"
                else:
                    return "Allowance 1"

            case "gold":
                if count < 20:
                    return "5 Gold"
                elif count < 60:
                    return "2 Gold"
                else:
                    return "1 Gold"

            case "dice":
                if count < 10:
                    return "4 Dice"
                elif count < 40:
                    return "2 Dice"
                else:
                    return "1 Dice"

            case "gems":
                if count < 30:
                    return "2 Gems"
                else:
                    return "1 Gems"
            case "keys":

                if count < 10:
                    return "3 Keys"
                elif count < 30:
                    return "2 Keys"
                else:
                    return "1 Keys"

            case "stars":
                if count < 20:
                    return "5 Stars"
                elif count < 60:
                    return "2 Stars"
                else:
                    return "1 Stars"

            case "permanent_dice":
                if count < 20:
                    return "2 Permanent Dice"
                else:
                    return "1 Permanent Dice"

            case "permanent_gems":
                if count < 20:
                    return "2 Permanent Gems"
                else:
                    return "1 Permanent Gems"

            case "permanent_keys":
                if count < 20:
                    return "2 Permanent Keys"
                else:
                    return "1 Permanent Keys"

            case "permanent_luck":
                if count < 20:
                    return "2 Permanent Luck"
                else:
                    return "2 Permanent Luck"

            case "permanent_steps":
                if count < 20:
                    return "10 Permanent Steps"
                else:
                    return "5 Permanent Steps"

            case "steps":
                if count < 20:
                    return "5 Steps"
                elif count < 60:
                    return "2 Steps"
                else:
                    return "1 Steps"

    return "Dug Up Nothing"


def create_item_with_correct_classification(world: BluePrinceWorld, name: str) -> BluePrinceItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return BluePrinceItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

# Create the items For the world
def create_all_items(world: BluePrinceWorld) -> None:

    itempool: list[Item] = []
    to_precollect: list[Item] = []

    exclude = [item for item in world.multiworld.precollected_items[world.player]]

    standard_item_list = [world.create_item(k) for k in other_items if (k not in ["BASEMENT KEY"] or world.options.goal_type.value > 0)
                                                                    and (k not in ["LUNCH BOX", "CURSED EFFIGY"] or world.options.goal_type.value > 1) 
                                                                    and (k not in ["CROWN", "ROYAL SCEPTER"] or world.options.goal_type.value > 2)]
    if world.options.standard_item_sanity:
        itempool += standard_item_list
    else:
        to_precollect += standard_item_list

    workshop_item_list = [world.create_item(k) for k in workshop_items]
    if world.options.workshop_sanity:
        itempool += workshop_item_list
    else:
        to_precollect += workshop_item_list

    upgrade_disk_item_list = [world.create_item(k) for k in upgrade_disks]
    if world.options.upgrade_disk_sanity:
        itempool += upgrade_disk_item_list

    key_item_list = [world.create_item(k) for k in keys if (k not in ["BASEMENT KEY"] or world.options.goal_type.value > 0)
                                                            and (k not in sanctum_keys or world.options.goal_type.value > 1) 
                                                            and (k not in ["KEY of Aries"] or world.options.goal_type.value > 2)]
    if world.options.key_sanity:
        itempool += key_item_list
    else:
        to_precollect += [k for k in key_item_list if LOCATION_ITEM_KEY not in keys[k.name] or keys[k.name][LOCATION_ITEM_KEY] == STARTING_INVENTORY]

    special_shop_item_list = [world.create_item(k) for k in shop_items if k not in gift_shop_items]
    if world.options.special_shop_sanity:
        itempool += special_shop_item_list

    giftshop_item_list = [world.create_item(k) for k in gift_shop_items]
    if world.options.special_shop_sanity and world.options.goal_type.value > 1: # Only if Goal is past room 46
        itempool += giftshop_item_list
    elif world.options.goal_type.value > 1:
        to_precollect += giftshop_item_list

    data_rooms.progressive_classroom = [world.create_item("Progressive Classroom") for _ in range(9)]

    room_item_list = [world.create_item(room) for room in rooms if room not in core_rooms and room not in ["Secret Garden", "Room 8", "Bookshop"] and room not in classrooms]
    if world.options.room_draft_sanity:
        valid_rooms = [room for room in room_item_list 
                                                    if ROOM_PICK_POSITIONS_KEY in rooms[room.name] 
                                                    and (set(rooms[room.name][ROOM_PICK_POSITIONS_KEY]) & ENTRANCE_HALL_DRAFTABLE) 
                                                    and room.name not in ["Sauna", "Pump Room", "Closet"] 
                                                    and not (room.name in ["Treasure Trove", "Gift Shop"] and world.options.goal_type.value <= 1)
                                                    and not (world.options.trophy_sanity == False and world.options.goal_type.value <= 1 and room.name == "Trophy Room")]
        world.starting_rooms = world.random.sample(valid_rooms,
            k=world.options.starting_room_amount.value,
        )
        world.starting_rooms += [r for r in room_item_list if r.name == "Closet"]
        itempool += [room for room in room_item_list if room not in world.starting_rooms 
                     and not (room.name in ["Treasure Trove", "Gift Shop"] and world.options.goal_type.value <= 1)
                     and not (world.options.trophy_sanity == False and world.options.goal_type.value <= 1 and room.name == "Trophy Room")]
        to_precollect += world.starting_rooms
    else:
        # Precollects all room items, except for those that should be at their in-game locations, which are handled in locations.py
        to_precollect += [room for room in room_item_list if (NONSANITY_LOCATION_KEY not in rooms[room.name] 
                                                              or rooms[room.name][NONSANITY_LOCATION_KEY] == STARTING_INVENTORY) 
                                                              and not (room.name in ["Treasure Trove", "Gift Shop"] and world.options.goal_type.value <= 1)
                                                              and not (world.options.trophy_sanity == False and world.options.goal_type.value <=1  and room.name == "Trophy Room")]

    if world.options.room_draft_sanity:
        n = len([room for room in world.starting_rooms if room in data_rooms.progressive_classroom])
        itempool += data_rooms.progressive_classroom[n:]
    else:
        to_precollect += data_rooms.progressive_classroom

    permanent_additions = [world.create_item(k) for k in permanent_unlocks]
    itempool += permanent_additions

    # remove anything that isn't implemented yet
    for item in to_precollect.copy():
        if not is_implemented(item.name, world):
            to_precollect.remove(item)

    for item in itempool.copy():
        if not is_implemented(item.name, world):
            itempool.remove(item)

    # remove any items that are in starting inventory
    for item in to_precollect.copy():
        if item in exclude:
            exclude.remove(item)
        else:
            world.push_precollected(item)

    for item in itempool.copy():
        if item in exclude:
            exclude.remove(item)
            itempool.remove(item)

    #
    # Add Filler Stuff
    #

    # Get Number of Existing Items.
    number_of_items = len(itempool)

    # Get number of unfilled locations.
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Determine Number Of Filler Items To Create
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Append Filler Items To Item Pool
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Add Itempool to world itempool
    world.multiworld.itempool += itempool

def is_implemented(item_name: str, world: BluePrinceWorld) -> bool:
    if world.options.dev_testing:
        return True
    if item_name in all_items:
        if IMPLEMENTATION_STATUS not in all_items[item_name]:
            return True
        return all_items[item_name][IMPLEMENTATION_STATUS] == IMPLEMENTED
    
    elif item_name in rooms:
        if IMPLEMENTATION_STATUS not in rooms[item_name]:
            return True
        return rooms[item_name][IMPLEMENTATION_STATUS] == IMPLEMENTED
    
    return True
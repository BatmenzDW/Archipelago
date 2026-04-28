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
        "Extra Allowance 1": 10101,
        "Extra Allowance 2": 10102,
        #
        "Extra Gold 1": 10201,
        "Extra Gold 2": 10202,
        "Extra Gold 5": 10203,
        #
        "Extra Dice 1": 10301,
        "Extra Dice 2": 10302,
        "Extra Dice 4": 10303,
        #
        "Extra Gems 1": 10501,
        "Extra Gems 2": 10502,
        #
        "Extra Keys 1": 10601,
        "Extra Keys 2": 10602,
        "Extra Keys 3": 10603,
        #
        "Extra Steps 1": 10701,
        "Extra Steps 2": 10702,
        "Extra Steps 5": 10703,
        #
        "Extra Starting Dice 1": 10801,
        "Extra Starting Dice 2": 10802,
        #
        "Extra Starting Gems 1": 10901,
        "Extra Starting Gems 2": 10902,
        #
        "Extra Starting Keys 1": 11001,
        "Extra Starting Keys 2": 11002,
        #
        "Extra Starting Luck 1": 11101,
        "Extra Starting Luck 2": 11102,
        #
        "Extra Starting Steps 1": 11201,
        "Extra Starting Steps 2": 11202,
        "Extra Starting Steps 5": 11203,
        #
        "Extra Stars 1": 11301,
        "Extra Stars 2": 11302,
        "Extra Stars 5": 11303,
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
        "Extra Allowance 1": ItemClassification.filler,
        "Extra Allowance 2": ItemClassification.filler,
        #
        "Extra Gold 1": ItemClassification.filler,
        "Extra Gold 2": ItemClassification.filler,
        "Extra Gold 5": ItemClassification.filler,
        #
        "Extra Dice 1": ItemClassification.filler,
        "Extra Dice 2": ItemClassification.filler,
        "Extra Dice 4": ItemClassification.filler,
        #
        "Extra Gems 1": ItemClassification.filler,
        "Extra Gems 2": ItemClassification.filler,
        #
        "Extra Keys 1": ItemClassification.filler,
        "Extra Keys 2": ItemClassification.filler,
        "Extra Keys 3": ItemClassification.filler,
        #
        "Extra Steps 1": ItemClassification.filler,
        "Extra Steps 2": ItemClassification.filler,
        "Extra Steps 5": ItemClassification.filler,
        #
        "Extra Starting Dice 1": ItemClassification.filler,
        "Extra Starting Dice 2": ItemClassification.filler,
        #
        "Extra Starting Gems 1": ItemClassification.filler,
        "Extra Starting Gems 2": ItemClassification.filler,
        #
        "Extra Starting Keys 1": ItemClassification.filler,
        "Extra Starting Keys 2": ItemClassification.filler,
        #
        "Extra Starting Luck 1": ItemClassification.filler,
        "Extra Starting Luck 2": ItemClassification.filler,
        #
        "Extra Starting Steps 1": ItemClassification.filler,
        "Extra Starting Steps 2": ItemClassification.filler,
        "Extra Starting Steps 5": ItemClassification.filler,
        #
        "Extra Stars 1": ItemClassification.filler,
        "Extra Stars 2": ItemClassification.filler,
        "Extra Stars 5": ItemClassification.filler,
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
            list(world.options.trap_type_distribution.valid_keys),
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
            list(world.options.filler_item_distribution.valid_keys),
            list(world.options.filler_item_distribution.value.values()),
        )[0]

        count = world.random.randint(0, 99)

        match choice:
            case "extra_allowance_1":
                return "Extra Allowance 1"
            case "extra_allowance_2":
                return "Extra Allowance 2"
            case "extra_gold_1":
                return "Extra Gold 1"
            case "extra_gold_2":
                return "Extra Gold 2"
            case "extra_gold_5":
                return "Extra Gold 5"
            case "extra_dice_1":
                return "Extra Dice 1"
            case "extra_dice_2":
                return "Extra Dice 2"
            case "extra_dice_4":
                return "Extra Dice 4"
            case "extra_gems_1":
                return "Extra Gems 1"
            case "extra_gems_2":
                return "Extra Gems 2"
            case "extra_keys_1":
                return "Extra Keys 1"
            case "extra_keys_2":
                return "Extra Keys 2"
            case "extra_keys_3":
                return "Extra Keys 3"
            case "extra_stars_1":
                return "Extra Stars 1"
            case "extra_stars_2":
                return "Extra Stars 2"
            case "extra_stars_5":
                return "Extra Stars 5"

            case "extra_starting_dice_1":
                return "Extra Starting Dice 1"
            case "extra_starting_dice_2":
                return "Extra Starting Dice 2"
            case "extra_starting_gems_1":
                return "Extra Starting Gems 1"
            case "extra_starting_gems_2":
                return "Extra Starting Gems 2"
            case "extra_starting_key_1":
                return "Extra Starting Keys 1"
            case "extra_starting_key_2":
                return "Extra Starting Keys 2"
            case "extra_starting_luck_1":
                return "Extra Starting Luck 1"
            case "extra_starting_luck_2":
                return "Extra Starting Luck 2"
            case "extra_starting_steps_5":
                return "Extra Starting Steps 5"
            case "extra_starting_steps_10":
                return "Extra Starting Steps 10"

            case "extra_steps_1":
                return "Extra Steps 1"
            case "extra_steps_2":
                return "Extra Steps 2"
            case "extra_steps_5":
                return "Extra Steps 5"
            case "nothing":
                return "Dug Up Nothing"

            case "extra_allowance":
                if count < 20:
                    return "Extra Allowance 2"
                else:
                    return "Extra Allowance 1"

            case "extra_gold":
                if count < 20:
                    return "Extra Gold 5"
                elif count < 60:
                    return "Extra Gold 2"
                else:
                    return "Extra Gold 1"

            case "extra_dice":
                if count < 10:
                    return "Extra Dice 4"
                elif count < 40:
                    return "Extra Dice 2"
                else:
                    return "Extra Dice 1"

            case "extra_gems":
                if count < 30:
                    return "Extra Gems 2"
                else:
                    return "Extra Gems 1"
            case "extra_keys":

                if count < 10:
                    return "Extra Keys 3"
                elif count < 30:
                    return "Extra Keys 2"
                else:
                    return "Extra Keys 1"

            case "extra_stars":
                if count < 20:
                    return "Extra Stars 5"
                elif count < 60:
                    return "Extra Stars 2"
                else:
                    return "Extra Stars 1"

            case "extra_starting_dice":
                if count < 20:
                    return "Extra Starting Dice 2"
                else:
                    return "Extra Starting Dice 1"

            case "extra_starting_gems":
                if count < 20:
                    return "Extra Starting Gems 2"
                else:
                    return "Extra Starting Gems 1"

            case "extra_starting_key":
                if count < 20:
                    return "Extra Starting Keys 2"
                else:
                    return "Extra Starting Keys 1"

            case "extra_starting_luck":
                if count < 20:
                    return "Extra Starting Luck 2"
                else:
                    return "Extra Starting Luck 1"

            case "extra_starting_steps":
                if count < 20:
                    return "Extra Starting Steps 10"
                else:
                    return "Extra Starting Steps 5"

            case "extra_steps":
                if count < 20:
                    return "Extra Steps 5"
                elif count < 60:
                    return "Extra Steps 2"
                else:
                    return "Extra Steps 1"

    return "Dug Up Nothing"


def create_item_with_correct_classification(world: BluePrinceWorld, name: str) -> BluePrinceItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return BluePrinceItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

# Create the items For the world
def create_all_items(world: BluePrinceWorld) -> None:

    itempool: list[Item] = []
    to_precollect: list[Item] = []

    exclude = [item for item in world.multiworld.precollected_items[world.player]]

    standard_item_list = [world.create_item(k) for k in other_items]
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
    else:
        to_precollect += upgrade_disk_item_list

    key_item_list = [world.create_item(k) for k in keys]
    if world.options.key_sanity:
        itempool += key_item_list
    else:
        to_precollect += [k for k in key_item_list if LOCATION_ITEM_KEY not in keys[k.name] or keys[k.name][LOCATION_ITEM_KEY] == STARTING_INVENTORY]

    special_shop_item_list = [world.create_item(k) for k in shop_items if k not in gift_shop_items]
    if world.options.special_shop_sanity:
        itempool += special_shop_item_list
    else:
        to_precollect += special_shop_item_list


    giftshop_item_list = [world.create_item(k) for k in gift_shop_items]
    if world.options.special_shop_sanity and world.options.goal_type.value > 1: # Only if Goal is past room 46
        itempool += giftshop_item_list
    elif world.options.goal_type.value > 1:
        to_precollect += giftshop_item_list

    data_rooms.progressive_classroom = [world.create_item("Progressive Classroom") for _ in range(9)]

    room_item_list = [world.create_item(room) for room in rooms if room not in core_rooms and room not in ["Secret Garden", "Room 8"] and room not in classrooms]
    if world.options.room_draft_sanity:
        world.starting_rooms = world.random.choices(
            [room for room in room_item_list if ROOM_PICK_POSITIONS_KEY in rooms[room.name] and set(rooms[room.name][ROOM_PICK_POSITIONS_KEY]) & ENTRANCE_HALL_DRAFTABLE] + [data_rooms.progressive_classroom[0]],
            k=world.options.starting_room_amount.value,
        )
        itempool += [room for room in room_item_list if room not in world.starting_rooms]
        to_precollect += world.starting_rooms
    else:
        # Precollects all room items, except for those that should be at their in-game locations, which are handled in locations.py
        to_precollect += [room for room in room_item_list if NONSANITY_LOCATION_KEY not in rooms[room.name] or rooms[room.name][NONSANITY_LOCATION_KEY] == STARTING_INVENTORY]

    if world.options.room_draft_sanity:
        n = len([room for room in world.starting_rooms if room in data_rooms.progressive_classroom])
        itempool += data_rooms.progressive_classroom[n:]
    else:
        to_precollect += data_rooms.progressive_classroom

    # remove any items that are in starting inventory
    for item in to_precollect:
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
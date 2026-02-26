from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState, ItemClassification, Location

from .options import GoalType

from . import items
from .constants import *

from .data_rooms import rooms, room_layout_lists
from .data_items import showroom_items, armory_items, other_items
from .data_other_locations import other_locations

if TYPE_CHECKING:
    from .world import BluePrinceWorld

ROOM_MULTIPLIER = 100_000

LOCATION_NAME_TO_ID = (
    {
        k: v[LOCATION_ID_KEY]
        for k, v in other_locations.items()
    }
    | {
        # Create First Entering locations for each room.
        f"{k} First Entering": v[ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER
        for k, v in rooms.items()
    }
    | {
        # Create 100 locked trunk check locations for each room that has the ability to have locked trunks
        f"{k} Locked Trunk {idx}": v[ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 10_000 + idx
        for k, v in rooms.items()
        for idx in range(1, 101)
        if v[ROOM_CHEST_SPOT_COUNT_KEY] > 0
    }
    | {
        # Add First Pickup as locations for the standard "tools".
        f"{k} First Pickup": v[ITEM_ID_KEY] * ROOM_MULTIPLIER
        for k, v in (showroom_items | armory_items | other_items).items()
    }
)


class BluePrinceLocation(Location):
    game = "Blue Prince"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: BluePrinceWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: BluePrinceWorld) -> None:

    campsite = world.get_region("Campsite")  # For Sanctum Solves Victory.
    showroom = world.get_region("Showroom")
    armory = world.get_region("Armory")

    for k, v in showroom_items.items():
        location_key = f"{k} First Pickup"
        locations = get_location_names_with_ids([location_key])
        showroom.add_locations(locations, BluePrinceLocation)
    
    for k, v in armory_items.items():
        location_key = f"{k} First Pickup"
        locations = get_location_names_with_ids([location_key])
        armory.add_locations(locations, BluePrinceLocation)

    # Iterate through the campsite and add locations for all items.
    # for k, v in (other_items).items():
    #     # TODO-2 this could be a comprehension, but this works for now.
    #     location_key = f"{k} First Pickup"
    #     locations = get_location_names_with_ids([location_key])

    #     campsite.add_locations(locations, BluePrinceLocation)
            

    for room_key, v in rooms.items():
        room = world.get_region(room_key)

        # Add fist room entrance
        location_key = f"{room_key} First Entering"
        locations = get_location_names_with_ids([location_key])
        room.add_locations(locations, BluePrinceLocation)
        # Add Nth locked trunk open

        for idx in range(1, world.options.locked_trunks + 1):
            if v[ROOM_CHEST_SPOT_COUNT_KEY] > 0:
                # TODO-2 this could be a comprehension, but this works for now.
                location_key = f"{room_key} Locked Trunk {idx}"
                locations = get_location_names_with_ids([location_key])
                room.add_locations(locations, BluePrinceLocation)

    # Other locations
    for k, v in other_locations.items():
        location_key = k
        locations = get_location_names_with_ids([location_key])
        world.get_region(v[LOCATION_ROOM_KEY]).add_locations(locations, BluePrinceLocation)

        world.set_rule(world.get_location(location_key), lambda state, key=location_key: can_access_location_with_rule(key, world, state))
    
def can_access_location_with_rule(location_key: str, world: BluePrinceWorld, state: CollectionState) -> bool:
    location_data = other_locations[location_key]

    if LOCATION_RULE not in location_data:
        return True
    rule = location_data[LOCATION_RULE]

    return rule(state, world)

def create_events(world: BluePrinceWorld) -> None:

    campsite = world.get_region("Campsite")  # For Sanctum Solves Victory.
    antechamber = world.get_region("Antechamber")
    room_46 = world.get_region("Room 46")
    throne_room = world.get_region("Throne Room")
    atelier = world.get_region("The Atelier")

    # Set Victory as entering antechamber
    if world.options.goal_type.value == GoalType.option_antechamber:
        antechamber.add_event(
            "Antechamber First Entering Victory",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as reaching room 46
    if world.options.goal_type.value == GoalType.option_room46:
        room_46.add_event(
            "Room 46 First Entering Victory",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as opening X Sanctums.
    if world.options.goal_type.value == GoalType.option_sanctum:
        # Generate the necessary events for the solve count.
        for region in [
            "Orinda Aries Sanctum",
            "Fenn Aries Sanctum",
            "Arch Aries Sanctum",
            "Eraja Sanctum",
            "Corarica Sanctum",
            "Mora Jai Sanctum",
            "Verra Sanctum",
            "Nuance Sanctum",
        ]:
            world.get_region(region).add_event(
                f"Solved {region}",
                "Sanctum Solve",
                location_type=BluePrinceLocation,
                item_type=items.BluePrinceItem,
            )

        # Add solve count victory condition.
        campsite.add_event(
            "Solved Sanctums",
            "Victory",
            rule=lambda state: state.has("Sanctum Solve", world.player, world.options.goal_sanctum_solves.value),
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as ascending to the throne
    if world.options.goal_type.value == GoalType.option_ascend:
        throne_room.add_event(
            "Ascended The Throne",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as entering the atelier and reading the blue prints.
    if world.options.goal_type.value == GoalType.option_blueprints:

        atelier.add_event(
            "Read The Blue Prints",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set access events for the 4 blue flames.
    world.get_region("Apple Orchard").add_event(
        "Has Apple Orchard Access",
        "Apple Orchard Access",
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )
    world.get_region("Schoolhouse").add_event(
        "Has School House Access",
        "School House Access",
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )
    world.get_region("Hovel").add_event(
        "Has Hovel Access",
        "Hovel Access",
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )
    world.get_region("Gemstone Cavern").add_event(
        "Has Gemstone Cavern Access",
        "Gemstone Cavern Access",
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )

    # Set North Lever Access
    world.get_region("Inner Sanctum").add_event(
        "Inner Sanctum North Lever",
        "North Lever Access",
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )
    world.get_region("Throne Room").add_event(
        "Throne Room North Lever",
        "North Lever Access",
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )

    # Chess Piece Access Rules
    for k, v in rooms.items():
        if v[ROOM_CHESS_PIECE_KEY] == CHESS_PIECE_NONE:
            continue
        world.get_region(k).add_event(
            f"Has {k} Chess Piece",
            f"Chess Piece {v[ROOM_CHESS_PIECE_KEY]}",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )
        
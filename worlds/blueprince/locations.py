from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState, ItemClassification, Location

from .options import GoalType, ItemLogicMode

from . import items
from .constants import *

from .data_rooms import rooms, blue_rooms, core_rooms
from .data_items import armory_items
from .data_other_locations import can_reach_item_location, locations, keys
from .items import BluePrinceItem

if TYPE_CHECKING:
    from .world import BluePrinceWorld

LOCATION_NAME_TO_ID = (
    {
        k: v[LOCATION_ID_KEY]
        for k, v in locations.items()
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
        # Add First Pickup as locations for armory items.
        f"{k} First Pickup": v[ITEM_ID_KEY] * ROOM_MULTIPLIER
        for k, v in armory_items.items()
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

    armory = world.get_region("The Armory")
    LOCATIONS_BY_GROUPS["Armory Purchases"] = set()
    # Ignoring chance to get Knight's Shield by digging with Jack Hammer for now.
    for k, v in armory_items.items():
        location_key = f"{k} First Pickup"
        locs = get_location_names_with_ids([location_key])
        armory.add_locations(locs, BluePrinceLocation)
        LOCATIONS_BY_GROUPS["Armory Purchases"].add(location_key)

    LOCATIONS_BY_GROUPS["Room Entrances"] = set()
    LOCATIONS_BY_GROUPS["Trunks"] = set()
    for room_key, v in rooms.items():
        room = world.get_region(room_key)

        # Add fist room entrance
        location_key = f"{room_key} First Entering"
        locs = get_location_names_with_ids([location_key])
        room.add_locations(locs, BluePrinceLocation)
        LOCATIONS_BY_GROUPS["Room Entrances"].add(location_key)
        # Add Nth locked trunk open

        trunk_count = world.options.locked_trunks_common if ROOM_CHEST_SPOT_TYPE_KEY not in v or v[ROOM_CHEST_SPOT_TYPE_KEY] == ROOM_CHEST_SPOT_COMMON else world.options.locked_trunks_rare if v[ROOM_CHEST_SPOT_TYPE_KEY] == ROOM_CHEST_SPOT_RARE else world.options.locked_trunks_complex

        trunks = [f"{room_key} Locked Trunk {idx}" for idx in range(1, trunk_count + 1) if v[ROOM_CHEST_SPOT_COUNT_KEY] > 0]
        locs = get_location_names_with_ids(trunks)
        room.add_locations(locs, BluePrinceLocation)
        LOCATIONS_BY_GROUPS["Trunks"].update(trunks)

        # These trunks require extra logic
        if room_key == "Entrance Hall":
            for idx in range(1, trunk_count + 1):
                world.set_rule(world.get_location(f"Entrance Hall Locked Trunk {idx}"), lambda state: state.can_reach_region("Observatory", world.player) or state.can_reach_region("Laboratory", world.player))

        elif room_key == "The Pool":
            for idx in range(1, trunk_count + 1): 
                world.set_rule(world.get_location(f"The Pool Locked Trunk {idx}"), lambda state: state.can_reach_region("Gift Shop", world.player))
            
    for k, v in locations.items() if not world.options.key_sanity else [l for l in locations.items() if l not in keys]:
        if NONSANITY_LOCATION_KEY in v and world.options.room_draft_sanity == False:
            if v[NONSANITY_LOCATION_KEY] != STARTING_INVENTORY:
                # Place room items at their in-game locations when room draft sanity is off.
                reg = world.get_region(v[LOCATION_ROOM_KEY])
                loc = BluePrinceLocation(world.player, k, LOCATION_NAME_TO_ID[k], reg)
                loc.place_locked_item(BluePrinceItem(v[NONSANITY_LOCATION_KEY], ItemClassification.progression_skip_balancing, None, world.player))

                reg.locations.append(loc)

                world.set_rule(world.get_location(k), lambda state, key=k: can_access_location_with_rule(key, world, state))
                continue
        
        location_key = k
        locs = get_location_names_with_ids([location_key])
        world.get_region(v[LOCATION_ROOM_KEY]).add_locations(locs, BluePrinceLocation)

        world.set_rule(world.get_location(location_key), lambda state, key=location_key: can_access_location_with_rule(key, world, state))
    
def can_access_location_with_rule(location_key: str, world: BluePrinceWorld, state: CollectionState) -> bool:
    location_data = locations[location_key]
    
    # if LOCATION_ITEM_KEY in location_data:
    #     item_name = location_data[LOCATION_ITEM_KEY]
    #     if not state.has(item_name, world.player):
    #         return False
    
    if LOCATION_RULE_SIMPLE_COMMON not in location_data and LOCATION_RULE_SIMPLE_RARE not in location_data and LOCATION_RULE_COMPLEX not in location_data and LOCATION_RULE_EXTREME not in location_data:
        return True

    rules = []

    if LOCATION_RULE_SIMPLE_COMMON in location_data:
        rules.append(location_data[LOCATION_RULE_SIMPLE_COMMON])
    if LOCATION_RULE_SIMPLE_RARE in location_data and world.options.item_logic_mode.value is (ItemLogicMode.option_rare or ItemLogicMode.option_rare_complex or ItemLogicMode.option_extreme):
        rules.append(location_data[LOCATION_RULE_SIMPLE_RARE])
    if LOCATION_RULE_COMPLEX in location_data and world.options.item_logic_mode.value is (ItemLogicMode.option_complex or ItemLogicMode.option_rare_complex or ItemLogicMode.option_extreme):
        rules.append(location_data[LOCATION_RULE_COMPLEX])
    if LOCATION_RULE_EXTREME in location_data and world.options.item_logic_mode.value is ItemLogicMode.option_extreme:
        rules.append(location_data[LOCATION_RULE_EXTREME])

    if not rules:
        return False

    return any(rule(state, world) for rule in rules)

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

    throne_room.add_event(
        "Ascended The Throne",
        "Ascend The Throne",
        lambda state: can_reach_item_location("CROWN", state, world.player) and
        can_reach_item_location("ROYAL SCEPTER", state, world.player) and
        can_reach_item_location("CURSED EFFIGY", state, world.player),
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )

    # Set Victory as ascending to the throne
    if world.options.goal_type.value == GoalType.option_ascend:
        throne_room.add_event(
            "Ascend The Throne Victory",
            "Victory",
            lambda state: state.has("Ascend The Throne", world.player),
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    throne_room.add_event(
        "Unseal Blue Doors",
        "Blue Door Access",
        lambda state: len([x for x in blue_rooms if x not in core_rooms and state.can_reach_region(x, world.player)]) >= 8,
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

    world.get_region("Apple Orchard").add_event(
        "Raise Satellite",
        "Satellite Raised",
        lambda state: all(can_reach_item_location(x, state, world.player) for x in ["MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3"]) 
        and state.can_reach_location("Scorch Sundial", world.player),
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
        
    
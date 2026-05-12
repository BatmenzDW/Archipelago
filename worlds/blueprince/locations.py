from __future__ import annotations

from typing import TYPE_CHECKING
from rule_builder.rules import *

from BaseClasses import CollectionState, ItemClassification, Location
from .rules import *

from .options import GoalType, ItemLogicMode

from . import items
from .constants import *

from .data_rooms import rooms, blue_rooms, core_rooms
from .data_items import armory_items
from .data_other_locations import locations, keys, floorplans, shop_items, trophies, sanctum_keys, aries_court_mora_jai_boxes
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

    locations_to_setup : dict[str, Rule] = dict()

    armory = world.get_region("The Armory")
    # Ignoring chance to get Knight's Shield by digging with Jack Hammer for now.
    for k, v in armory_items.items():
        location_key = f"{k} First Pickup"
        locs = get_location_names_with_ids([location_key])
        armory.add_locations(locs, BluePrinceLocation)
    
    for room_key, v in rooms.items():
        if world.options.goal_type.value < 2 and room_key in ["Room 46", "Gift Shop", "Treasure Trove"]:
            continue # Skip Rooms that are past or at the goal

        if world.options.goal_type.value < 1 and room_key in ["Antechamber"]:
            continue # Skip Rooms that are at the goal

        if world.options.trophy_sanity == False and room_key in ["Trophy Room"] and world.options.goal_type.value < 2:
            continue # Skip Trophy Room when trophy sanity is off and goal is before it

        room = world.get_region(room_key)

        # Add fist room entrance
        location_key = f"{room_key} First Entering"
        locs = get_location_names_with_ids([location_key])
        room.add_locations(locs, BluePrinceLocation)
        # Add Nth locked trunk open

        trunk_count = world.options.locked_trunks_common if ROOM_CHEST_SPOT_TYPE_KEY not in v or v[ROOM_CHEST_SPOT_TYPE_KEY] == ROOM_CHEST_SPOT_COMMON else world.options.locked_trunks_rare if v[ROOM_CHEST_SPOT_TYPE_KEY] == ROOM_CHEST_SPOT_RARE else world.options.locked_trunks_complex

        trunks = [f"{room_key} Locked Trunk {idx}" for idx in range(1, trunk_count + 1) if v[ROOM_CHEST_SPOT_COUNT_KEY] > 0]
        locs = get_location_names_with_ids(trunks)
        room.add_locations(locs, BluePrinceLocation)

        # These trunks require extra logic
        if room_key == "Entrance Hall":
            for idx in range(1, trunk_count + 1):
                world.set_rule(world.get_location(f"Entrance Hall Locked Trunk {idx}"), lambda state: state.can_reach_region("Observatory", world.player) or state.can_reach_region("Laboratory", world.player))

        elif room_key == "The Pool":
            for idx in range(1, trunk_count + 1): 
                world.set_rule(world.get_location(f"The Pool Locked Trunk {idx}"), lambda state: state.can_reach_region("Gift Shop", world.player))

    for k, v in locations.items():

        if world.options.goal_type.value < 4 and k in ["Ascend The Throne", "Throne of the Blue Prince Mora Jai Box"]:
            continue

        if world.options.goal_type.value < 3 and (k in aries_court_mora_jai_boxes or k in ["KEY of Aries First Pickup", "ROYAL SCEPTER First Pickup"]):
            continue

        if world.options.goal_type.value < 2 and (k in sanctum_keys or 
            k in ["LUNCH BOX First Pickup", 
                  "CURSED EFFIGY First Pickup", 
                  "Cursed Coffers", 
                  "CROWN First Pickup", 
                  "Underpass Mora Jai Box", 
                  "Treasure Trove Floorplan",
                  "Gift Shop - Mt. Holly Tee", 
                  "Gift Shop - Lunch Box", 
                  "Gift Shop - Swim Trunks", 
                  "Gift Shop - Swim Bird Plushie", 
                  "Gift Shop - Blue Tents", 
                  "Gift Shop - Cursed Coffers"]
            or k in [f"Solved {s}" for s in [
            "Orinda Aries Sanctum",
            "Fenn Aries Sanctum",
            "Arch Aries Sanctum",
            "Eraja Sanctum",
            "Corarica Sanctum",
            "Mora Jai Sanctum",
            "Verra Sanctum",
            "Nuance Sanctum",
        ]] or k in [f"{s} Mora Jai Box" for s in [
            "Orinda Aries Sanctum",
            "Fenn Aries Sanctum",
            "Arch Aries Sanctum",
            "Eraja Sanctum",
            "Corarica Sanctum",
            "Mora Jai Sanctum",
            "Verra Sanctum",
            "Nuance Sanctum",
        ]]):
            continue # Skip locations that are past or at the goal

        if world.options.trophy_sanity == False and k in trophies:
            continue # Skip placing trophies when trophy sanity is off

        if k in shop_items and world.options.special_shop_sanity == False and NONSANITY_LOCATION_KEY in v:
            # Place special shop items at their in-game locations when special shop sanity is off.
            reg = world.get_region(v[LOCATION_ROOM_KEY])
            loc = BluePrinceLocation(world.player, k, None, reg)
            loc.place_locked_item(BluePrinceItem(v[NONSANITY_LOCATION_KEY], ItemClassification.progression_skip_balancing, None, world.player))

            reg.locations.append(loc)

            locations_to_setup[k] = get_location_rule(k)
            continue

        if NONSANITY_LOCATION_KEY in v and world.options.room_draft_sanity == False and k in floorplans.keys():
            if v[NONSANITY_LOCATION_KEY] != STARTING_INVENTORY:
                # Place room items at their in-game locations when room draft sanity is off.
                reg = world.get_region(v[LOCATION_ROOM_KEY])
                loc = BluePrinceLocation(world.player, k, None, reg)
                loc.place_locked_item(BluePrinceItem(v[NONSANITY_LOCATION_KEY], ItemClassification.progression_skip_balancing, None, world.player))

                reg.locations.append(loc)

                locations_to_setup[k] = get_location_rule(k)
                continue
        if LOCATION_ITEM_KEY in v and world.options.key_sanity == False and k in keys.keys():
            if v[LOCATION_ITEM_KEY] != STARTING_INVENTORY:
                # Place keys at their in-game locations when key sanity is off.
                reg = world.get_region(v[LOCATION_ROOM_KEY])
                loc = BluePrinceLocation(world.player, k, None, reg)
                loc.place_locked_item(BluePrinceItem(v[LOCATION_ITEM_KEY], ItemClassification.progression_skip_balancing, None, world.player))

                reg.locations.append(loc)

                locations_to_setup[k] = get_location_rule(k)
                continue

        location_key = k
        locs = get_location_names_with_ids([location_key])
        world.get_region(v[LOCATION_ROOM_KEY]).add_locations(locs, BluePrinceLocation)
        locations_to_setup[location_key] = get_location_rule(location_key)

    for location_key, rule in locations_to_setup.items():
        world.set_rule(world.get_location(location_key), rule)
    
def get_location_rule(location_key: str) -> Rule:
    location_data = locations[location_key]
    
    if LOCATION_RULE_SIMPLE_COMMON not in location_data:
        return True_()
    
    rule = location_data[LOCATION_RULE_SIMPLE_COMMON]

    if isinstance(rule, Rule): # Added this because pylance was showing an error
        return rule

    raise Exception(f"Invalid rule for location {location_key}: {rule}")

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
            "Ascend The Throne Victory",
            "Victory",
            lambda state: state.has("Ascend The Throne", world.player),
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )
        throne_room.add_event(
            "Ascended The Throne",
            "Ascend The Throne",
            (CanReachItemLocation("CROWN") &
                CanReachItemLocation("ROYAL SCEPTER") &
                CanReachItemLocation("CURSED EFFIGY")),
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )
    elif world.options.goal_type.value > GoalType.option_ascend:
        throne_room.add_event(
            "Ascended The Throne",
            "Ascend The Throne",
            (CanReachItemLocation("CROWN") &
                CanReachItemLocation("ROYAL SCEPTER") &
                CanReachItemLocation("CURSED EFFIGY")),
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )
        throne_room.add_event(
            "Unseal Blue Doors",
            "Blue Door Access",
            HasFromList(*[x for x in blue_rooms if x not in core_rooms], count = 8),
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
        And(
            *[CanReachItemLocation(x) for x in ["MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3"]],
            CanReachLocation("Scorch Sundial")
        ),
        location_type=BluePrinceLocation,
        item_type=items.BluePrinceItem,
    )

    # Chess Piece Access Rules
    for k, v in rooms.items():
        if v[ROOM_CHESS_PIECE_KEY] == CHESS_PIECE_NONE:
            continue
        if world.options.goal_type.value < 2 and k in ["Treasure Trove"]:
            continue # Skip Rooms that are past or at the goal

        world.get_region(k).add_event(
            f"Has {k} Chess Piece",
            f"Chess Piece {v[ROOM_CHESS_PIECE_KEY]}",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )
        
    
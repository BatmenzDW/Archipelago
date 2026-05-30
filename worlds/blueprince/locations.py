from __future__ import annotations

from logging import debug
from typing import TYPE_CHECKING, List, Optional
from rule_builder.rules import *

from BaseClasses import CollectionState, ItemClassification, Location, LocationProgressType, Region, Region
from worlds.blueprince import world
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
        "Bunk Room First Entering 2": rooms["Bunk Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1
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
        if not is_implemented(location_key, world):
            continue

        if room_key not in ["Entrance Hall", "Bunk Room"]:
            locs = get_location_names_with_ids([location_key])
            room.add_locations(locs, BluePrinceLocation)

        elif room_key == "Bunk Room":
            locs = get_location_names_with_ids(["Bunk Room First Entering", "Bunk Room First Entering 2"])
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
            continue 

        if world.options.goal_type.value < 1 and (k in ["BASEMENT KEY First Pickup", "Break Tunnel Wall"] or "Unlock Basement Door" in k):
            continue # Skip locations that are past or at the goal

        if world.options.trophy_sanity == False and (k in trophies or k in ["Gift Shop - Blue Tents"]):
            continue # Skip placing trophies when trophy sanity is off

        if not is_implemented(k, world):
            continue

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

def force_special_location_conditions(world: BluePrinceWorld,
                                    progitempool: List["Item"],
                                    usefulitempool: List["Item"],
                                    filleritempool: List["Item"],
                                    fill_locations: List["Location"]) -> None:
    
    item = world.random.choice(progitempool + usefulitempool + filleritempool)

    if item in progitempool:
        if attempt_to_fill_multiple_locations_with_same_item(world, progitempool, fill_locations):
            return
    if item in usefulitempool:
        if attempt_to_fill_multiple_locations_with_same_item(world, usefulitempool, fill_locations):
            return
    if item in filleritempool:
        if attempt_to_fill_multiple_locations_with_same_item(world, filleritempool, fill_locations):
            return

    if attempt_to_fill_multiple_locations_with_same_item(world, progitempool, fill_locations):
        return
    if attempt_to_fill_multiple_locations_with_same_item(world, usefulitempool, fill_locations):
        return
    if attempt_to_fill_multiple_locations_with_same_item(world, filleritempool, fill_locations):
        return
    raise Exception("Could not satisfy special location conditions. This should be impossible.")

# In theory, this should get a random item with multiple copies, but this world only has one that is progressive, so it will need to be tested if it works correctly
def attempt_to_fill_multiple_locations_with_same_item(world: BluePrinceWorld, pool: List["Item"], locations: List["Location"]) -> bool:
    multi : List[str] = []
    
    for item in pool:
        if item.name in multi:
            continue
        if len([x for x in pool if x.name == item.name]) > 1:
            multi.append(item.name)

    if len(multi) == 0:
        return False

    loc1 = world.get_location("Bunk Room First Entering")
    loc2 = world.get_location("Bunk Room First Entering 2")

    l1_item : Item | None = None

    order = list(range(len(pool)))
    world.random.shuffle(order)

    for i in order:
        item = pool[i]
        if item.name not in multi:
            continue

        if l1_item is None:
            if loc1.can_fill(world.multiworld.state, item, check_access=False):
                l1_item = item
                continue
        elif item.name == l1_item.name:
            if loc2.can_fill(world.multiworld.state, item, check_access=False):
                loc1.place_locked_item(l1_item)
                loc2.place_locked_item(item)

                locations.remove(loc1)
                locations.remove(loc2)
                pool.remove(l1_item)
                pool.remove(item)
                print(f"Placed {item} in both Bunk Room First Entering locations to satisfy the condition that they have the same item.")
                return True
            else:
                l1_item = None

    assert False, f"Could not find a way to fill the Bunk Room First Entering locations with the same item. This should be impossible."

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
        

def is_implemented(location_name: str, world: BluePrinceWorld) -> bool:
    if world.options.dev_testing:
        return True
    if location_name in locations:
        if IMPLEMENTATION_STATUS not in locations[location_name]:
            return True
        return locations[location_name][IMPLEMENTATION_STATUS] == IMPLEMENTED
    
    if location_name.endswith("First Entering"):
        room_name = location_name.replace(" First Entering", "")
        if room_name in rooms:
            if LOCATION_IMPLEMENTATION_STATUS not in rooms[room_name]:
                return True
            return rooms[room_name][LOCATION_IMPLEMENTATION_STATUS] == IMPLEMENTED

    return True
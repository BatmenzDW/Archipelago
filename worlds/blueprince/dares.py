from typing import Union

from .world import BluePrinceWorld
from .constants import *
from .data_rooms import blue_rooms, red_rooms, bedrooms, shops, black_rooms, hallways, green_rooms

from BaseClasses import CollectionState
from collections.abc import Callable

def dare_is_possible(dare_name: str, state: CollectionState, player: int, win_day: bool = False) -> bool:
    
    if dare_name not in dares:
        return False

    dare = dares[dare_name]

    if DARE_IS_POSSIBLE_RULE not in dare:
        return True
    
    return dare[DARE_IS_POSSIBLE_RULE](state, player, win_day)

def can_reach_with_dares(world: BluePrinceWorld, to_check: str, type_hint: str = "Region", win_day: bool = False) -> bool:
    for d in world.dares:
        if not can_reach_with_dare(d, to_check, type_hint, win_day):
            return False
    
    return True

def can_reach_with_dare(dare_name: str, to_check: str, type_hint: str = "Region", win_day: bool = False) -> bool:

    if dare_name not in dares:
        return False

    dare = dares[dare_name]

    if DARE_CAN_REACH_RULE not in dare:
        return True

    return dare[DARE_CAN_REACH_RULE](to_check, type_hint, win_day)

dares : dict[str, dict[str, Callable]] = {
    "Lavatory30s": {
        DARE_IS_POSSIBLE_RULE: lambda state, player, win_day: state.can_reach_region("Lavatory", player) or win_day
    }, # Can reach Lavatory or can win today
    "NoNorthEntranceHall": {
        # TODO: rework region logic so this can be implemented
    },
    "DraftFirstEntranceHall": {
        # TODO: check if conflicts with other dares
    },
    "ExcatlyOnePurchasePerShop": {
        DARE_CAN_REACH_RULE: lambda to_check, type_hint, win_day: not (to_check == "Aquarium" and type_hint == "Region") or win_day
    },
    "AlwaysAtLeast20Steps": {
        # Should always be possible
    },
    "NeverDraftFullRank": {
        # Should always be possible
    },
    "OpenEmptyBoxParlor": {
        # Should always be possible, unless we lock the windup key
    },
    "OnlyOneButtonUtilityCloset": {
        DARE_CAN_REACH_RULE: lambda to_check, type_hint, win_day: not ((to_check == "Gemstone Cavern" and type_hint == "Region") or to_check == "VAC Controls")
    },
    "LeaveBlueprint": {
        # Should always be possible
    },
    "NoBilliardFail": {
        # Should always be possible
    },
    "NeverStepThePool": {
        DARE_CAN_REACH_RULE: lambda to_check, type_hint, win_day: not (to_check == "The Pool" and type_hint == "Region")
    },
    "OpenEachLockedTrunk": {
        # Should always be possible
    },
    "NeverEnterMoreThan3x": {
        # Should always be possible
    },
    "NeverDraftDen": {
        DARE_CAN_REACH_RULE: lambda to_check, type_hint, win_day: not (to_check == "Den" and type_hint == "Region")
    },
    "AlwaysDraftMostExpensive": {
        # Should always be possible
    },
    "AlwaysDraftRed": {
        # Should always be possible
    },
    "NeverEatFruit": {
        # Should always be possible
    },
    "NeverRideElevator": {
        DARE_CAN_REACH_RULE: lambda to_check, type_hint, win_day: not ((to_check in ["The Foundation", "Blackbridge Grotto", "Tunnel Area Past Red Door", "Reservoir Bottom"] and type_hint == "Region") or (to_check in ["Underpass Gate", "Treasure Trove Floorplan"] and type_hint == "Location"))
    },
    "NeverDraftSouth": {
        DARE_CAN_REACH_RULE: lambda to_check, type_hint, win_day: not (to_check == "Her Ladyship's Chambers" and type_hint == "Region")
    },
    "EndDayAtLeast1Gem": {
        # Should always be possible
    },
    "Draft6DifferentColors": {
        DARE_IS_POSSIBLE_RULE: lambda state, player, win_day: win_day or state.can_reach_region("Aquarium", player)
    },
    "NeverExitEntranceHall": {
        # TODO: region logic would need to be fully rewritten to support this
    },
    "EndDay0Gem0Coin0Key": {
        # Should always be possible
    },
    "NeverHaveMoreThan2Items": {

    },
}
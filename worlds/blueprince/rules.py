from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING
from rule_builder.rules import *

if TYPE_CHECKING:
    from .world import BluePrinceWorld

from .data_rooms import rooms, core_rooms, room_layout_lists
from .constants import *
from .room_min_pieces import POSITION_MINIMUM_PIECES, POSITION_MINIMUM_TOTAL_PIECES
from .options import ItemLogicMode
from .data_items import *

default_logic_filter = [OptionFilter(ItemLogicMode, ItemLogicMode.option_default)]
rare_logic_filter = [OptionFilter(ItemLogicMode, [ItemLogicMode.option_rare, ItemLogicMode.option_rare_complex, ItemLogicMode.option_extreme], operator="contains")]
complex_logic_filter = [OptionFilter(ItemLogicMode, [ItemLogicMode.option_complex, ItemLogicMode.option_rare_complex, ItemLogicMode.option_extreme], operator="contains")]
extreme_logic_filter = [OptionFilter(ItemLogicMode, ItemLogicMode.option_extreme)]

def set_all_rules(world: BluePrinceWorld) -> None:

    set_completion_condition(world)

def set_completion_condition(world: BluePrinceWorld) -> None:

    world.set_completion_rule(Has("Victory"))


@dataclasses.dataclass()
class CanReachPickPosition(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Use pre-calculated tables to determine if a the pick position is reachable with the current inventory.
    """
    room : str
    always_have: bool = False
    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return self.Resolved(self.room, self.always_have, player=world.player)
    
    class Resolved(Rule.Resolved):
        room : str
        always_have: bool = False
        @override
        def _evaluate(self, state: CollectionState) -> bool:
            if not self.always_have and self.room not in core_rooms and not state.has(self.room, self.player):
                return False
            
            room_data = rooms[self.room]
            
            positions_types = room_data[ROOM_PICK_POSITIONS_KEY]

            inventory = {
                ROOM_LAYOUT_TYPE_X: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_X], self.player),
                ROOM_LAYOUT_TYPE_T: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_T], self.player),
                ROOM_LAYOUT_TYPE_I: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_I], self.player),
                ROOM_LAYOUT_TYPE_J: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_J], self.player),
            }

            total_inventory = sum(inventory.values())

            if (room_data[ROOM_LAYOUT_TYPE_KEY] in inventory and inventory[room_data[ROOM_LAYOUT_TYPE_KEY]] > 0):
                inventory[room_data[ROOM_LAYOUT_TYPE_KEY]] -= 1

            for pt in positions_types:
                if pt not in POSITION_MINIMUM_PIECES or total_inventory < POSITION_MINIMUM_TOTAL_PIECES[pt]:
                    continue
                if self.matches_minimum_inventory(POSITION_MINIMUM_PIECES[pt], inventory):
                    return True
                
            return False
        
        def matches_minimum_inventory(self, required: list[tuple[int, int, int, int]], inventory: dict[str, int]) -> bool:
            inv = tuple(inventory[k] for k in inventory)
            for req in required:
                if all(inv[i] >= req[i] for i in range(4)):
                    return True
                
            return False

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            return [
                {"type": "text", "text": "Use pre-calculated tables to determine if a the pick position for  "},
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": self.room},
                {"type": "text", "text": "is reachable with the current inventory."},
            ]

@dataclasses.dataclass()
class CanReachItemLocation(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Get the item rules for if the location is reachable with the current inventory.
    """
    location: str
    parent_region_name: str = ""
    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        from .data_other_locations import locations, armory_items, vault_keys, workshop_items
        loc_name = self.location + " First Pickup"
        if self.location in workshop_items:
            loc_name = self.location + " First Craft"
        elif self.location in vault_keys:
            loc_name = self.location

        if self.parent_region_name == "":
            self.parent_region_name = locations[loc_name][LOCATION_ROOM_KEY] if loc_name in locations else ""

        if loc_name in locations:
            return (Has(self.location) & CanReachLocation(loc_name, parent_region_name=self.parent_region_name)).resolve(world)

        if self.location in armory_items:
            return (Has(self.location) & CanReachRegion("The Armory")).resolve(world)
        
        for location, data in locations.items():
            if LOCATION_ITEM_KEY in data and data[LOCATION_ITEM_KEY] == self.location:
                return (Has(self.location) & CanReachLocation(location, parent_region_name=self.parent_region_name)).resolve(world)

        return False_().resolve(world)
    
@dataclasses.dataclass()
class MechanariumDoorRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Get the rules for if the mechanarium door can be opened with the current inventory.
    """
    door: int
    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return (CanReachRegion("Mechanarium") & 
            HasFromList("Utility Closet", "Boiler Room", "Pump Room", "Security", "Workshop", "Laboratory", "Mechanarium", # Might add electric eel aquarium when we add upgraded rooms
                        count=self.door + 1) # might make it require more, since its pretty hard to get a door with the minimum count
        ).resolve(world)
    
@dataclasses.dataclass()
class CanReachAllLocations(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can reach all locations in the list.
    """
    locations: tuple[str, ...]

    def __init__(self, *locations: str):
        self.locations = locations

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return And(*[CanReachLocation(location) for location in self.locations]).resolve(world)

@dataclasses.dataclass()
class TrunkRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can open a trunk with the current inventory.
    """
    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return (
            Or(*[CanReachRegion(room) for room in [
                "Attic",
                "Bedroom",
                "Courtyard",
                "Den",
                "Laboratory",
                "Library",
                "Mail Room",
                "Observatory",
                "Office",
                "Storeroom",
                "Study",
                "Terrace",
                "Vault",
                "Veranda",
                "Wine Cellar",
                "Morning Room",
                "Dormitory",
                "Tunnel",
                "Conservatory",
            ]], options=complex_logic_filter) |
            Or(
                *[CanReachRegion(room) for room in [
                    "Spare Room",
                    "Music Room",
                    "Drawing Room",
                    "Trophy Room",
                    "Gallery",
                    "Great Hall",
                ]], 
                CanReachRegion("The Pool") & Has("Gift Shop - Swim Trunks"),
                PlanetariumRule(),
                options=extreme_logic_filter
            )
        ).resolve(world)
    
@dataclasses.dataclass()
class DarkRoomRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can turn on dark room lights (and get the items within) with the current inventory.
    """

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return And(CanReachRegion("Darkroom"), (
            CanReachRegion("Utility Closet") |
            CanReachRegion("Shelter") |
            CanReachItemLocation("KNIGHTS SHIELD")
        ), options=complex_logic_filter).resolve(world)
    
@dataclasses.dataclass()
class LavatoryRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can spawn items in the lavatory with the current inventory.
    """

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return And(CanReachRegion("Lavatory"), (
            CanReachRegion("Shelter") |
            CanReachItemLocation("KNIGHTS SHIELD") |
            CanReachItemLocation("Dowsing Rod")
        ), options=complex_logic_filter).resolve(world)
    
@dataclasses.dataclass()
class PlanetariumRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can use the planetarium with the current inventory.
    """

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return And(CanReachRegion("Planetarium"), CanReachItemLocation("TELESCOPE"), options=complex_logic_filter).resolve(world)
    
@dataclasses.dataclass()
class AdvancedExperimentRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can do the advanced experiment with the current inventory.
    """

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return And(CanReachRegion("Laboratory"), Has("Satellite Raised"), options=extreme_logic_filter).resolve(world)
    
@dataclasses.dataclass()
class TradingPostRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can get an item from the trading post with the current inventory.
    """
    item_name: str

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return And(CanReachRegion("Trading Post"), 
                Or(
                    *[CanReachItemLocation(item) for item in self.get_trading_post_offers(self.item_name)]
                ),
                options=complex_logic_filter).resolve(world)
    
    # Trading can get any item of the same tier or lower
    def get_trading_post_offers(self, give: str) -> list[str]:
        if give in TRADING_POST_TIER1[TRADING_POST_GIVE]:
            return [x for x in TRADING_POST_TIER1[TRADING_POST_RECEIVE] if x != give]
        if give in TRADING_POST_TIER2[TRADING_POST_GIVE]:
            return [x for x in TRADING_POST_TIER2[TRADING_POST_RECEIVE] + TRADING_POST_TIER1[TRADING_POST_RECEIVE] if x != give]
        if give in TRADING_POST_TIER3[TRADING_POST_GIVE]:
            return [x for x in TRADING_POST_TIER3[TRADING_POST_RECEIVE] + TRADING_POST_TIER2[TRADING_POST_RECEIVE] + TRADING_POST_TIER1[TRADING_POST_RECEIVE] if x != give]
        if give in TRADING_POST_TIER4[TRADING_POST_GIVE]:
            return [x for x in TRADING_POST_TIER4[TRADING_POST_RECEIVE] + TRADING_POST_TIER3[TRADING_POST_RECEIVE] + TRADING_POST_TIER2[TRADING_POST_RECEIVE] + TRADING_POST_TIER1[TRADING_POST_RECEIVE] if x != give]
        return []
    
@dataclasses.dataclass()
class DigSpotRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can find a dig spot with the current inventory.
    """

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return (CanReachItemLocation("SHOVEL") &
            Or(
            *[CanReachRegion(room) for room in [
                "The Foundation",
                "Wine Cellar",
                "Aquarium",
                "Courtyard",
                "Greenhouse",
                "Morning Room",
                "Veranda",
                "Terrace",
                "Cloister",
                "Patio",
                "Storeroom",
                "Garage",
                "Pump Room",
                "Workshop",
                "Secret Garden",
                "Root Cellar",
                "Hovel",
                "Kennel",
                "Dovecote",
                "Solarium",
                "Tunnel",
                "Conservatory",
                "Boiler Room",
            ]], 
            PlanetariumRule())).resolve(world)

# TODO:
@dataclasses.dataclass()
class CloisterRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can reach a certain room with a certain Cloister upgrade
    """
    room: str
    cloister_upgrade: str

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return And(CanReachRegion(self.room), UpgradedRoomRule("Cloister", self.cloister_upgrade)).resolve(world)

# TODO:
@dataclasses.dataclass()
class UpgradedRoomRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can reach a certain upgraded room
    """
    room: str
    upgrade: str

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return False_().resolve(world)

@dataclasses.dataclass()
class CarTrunkRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can open the car trunk with the current inventory.
    """

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return (CanReachRegion("Garage") & Has("CAR KEYS")).resolve(world)
    
@dataclasses.dataclass()
class SpiralOfStarsRule(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can access the Spiral of Stars with the current inventory.
    """

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        return Filtered(CanReachRegion("Observatory"), options=extreme_logic_filter).resolve(world)

@dataclasses.dataclass()
class CanReachItemLocationsFromList(Rule["BluePrinceWorld"], game="Blue Prince"):
    """
    Check if the player can reach at least count item locations from the list
    """
    targets: tuple[str, ...]
    count : int = 1

    def __init__(self, *targets: str, count: int = 1):
        self.targets = tuple(sorted(set(targets)))
        self.count = count

    @override
    def _instantiate(self, world: "BluePrinceWorld") -> Rule.Resolved:
        if len(self.targets) == 0:
            return False_().resolve(world)
        if len(self.targets) == 1:
            return CanReachItemLocation(self.targets[0]).resolve(world)
        


        return self.Resolved(self.targets, self.count, player=world.player)
    
    class Resolved(Rule.Resolved):
        targets: tuple[str, ...]
        count : int = 1

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            from .data_other_locations import locations, armory_items
            reachable_count = 0
            for target in self.targets:
                loc_name = target + " First Pickup"
                if loc_name in locations:
                    if (state.has(target, self.player) and state.can_reach_location(loc_name, self.player)):
                        reachable_count += 1
                elif target in armory_items:
                    if (state.has(target, self.player) and state.can_reach_region("The Armory", self.player)):
                        reachable_count += 1
                else:
                    for location, data in locations.items():
                        if LOCATION_ITEM_KEY in data and data[LOCATION_ITEM_KEY] == target:
                            if (state.has(target, self.player) and state.can_reach_location(location, self.player)):
                                reachable_count += 1
                                break

                if reachable_count >= self.count:
                    return True

            return False
from BaseClasses import CollectionState, ItemClassification

from .constants import *
from .data_rooms import rooms, core_rooms, classrooms, room_layout_lists
from .data_items import *
from .locations import ROOM_MULTIPLIER

room_location_mem = {}

def get_room_location_id(room_name: str, n: int = 0) -> int:
    if room_name not in room_location_mem:
        room_location_mem[room_name] = []

    if n in room_location_mem[room_name]:
        raise Exception(f"Duplicate location ID for {room_name} {n}")
    
    if room_name in rooms:
        return rooms[room_name][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + n + 1000
    else:
        return (room_name.__hash__() % 10000000 + 1000) * ROOM_MULTIPLIER + n + 1000

def can_reach_item_location(item_name: str, state: CollectionState, player: int) -> bool:
    loc_name = item_name + " First Pickup"
    if state.has(loc_name, player):
        return True
    
    if loc_name in locations:
        return state.can_reach_location(loc_name, player)

    for location, data in locations.items():
        if LOCATION_ITEM_KEY in data and data[LOCATION_ITEM_KEY] == item_name:
            return state.can_reach_location(location, player)
        
    if item_name in armory_items:
        return state.can_reach_region("The Armory", player)
    
    return False

trophies = {
    "Full House Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 0),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.count_from_list([x for x in room_layout_lists[INNER_ROOM_KEY] if x not in core_rooms], world.player) >= 43
    },
    "Trophy of Invention": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 0),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in [
                "Burning Glass",
                "Detector Shovel",
                "Dowsing Rod",
                "Electromagnet",
                "Jack Hammer",
                "Lucky Purse",
                "Pick Sound Amplifier",
                "Power Hammer",
            ]
        )
    },
    "Trophy of Drafting": {
        LOCATION_ID_KEY: get_room_location_id("Mail Room", 0),
        LOCATION_ROOM_KEY: "Mail Room",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: len([x for x in rooms if rooms[x][ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_D and not rooms[x][OUTER_ROOM_KEY] and x not in core_rooms and state.can_reach_region(x, world.player)]) >= 20,
    },
    "Trophy of Wealth": {
        LOCATION_ID_KEY: get_room_location_id("Showroom", 0),
        LOCATION_ROOM_KEY: "Showroom",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in showroom_items),
    },
    "Inheritance Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Room 46", 0),
        LOCATION_ROOM_KEY: "Room 46",
    },
    "Bullseye Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Billiard Room", 0),
        LOCATION_ROOM_KEY: "Billiard Room",
    },
    "A Logical Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Parlor", 0),
        LOCATION_ROOM_KEY: "Parlor",
    },
    "Trophy 8": {
        LOCATION_ID_KEY: get_room_location_id("Room 8", 0),
        LOCATION_ROOM_KEY: "Room 8",
    },
    "Explorer's Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 1),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.has_all([x for x in rooms if x not in core_rooms and (x not in classrooms or x == "Classroom 1")], world.player) # Only count Classroom 1
    },
    "Trophy of Sigils": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 2),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(state.can_reach_region(sanctum, world.player) for sanctum in [
                "Orinda Aries Sanctum",
                "Fenn Aries Sanctum",
                "Arch Aries Sanctum",
                "Eraja Sanctum",
                "Corarica Sanctum",
                "Mora Jai Sanctum",
                "Verra Sanctum",
                "Nuance Sanctum",
            ]
        )
    },
    "Diploma Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 3),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(state.can_reach_region(region, world.player) for region in [
                "Schoolhouse",
                "Classroom 1",
                "Classroom 2",
                "Classroom 3",
                "Classroom 4",
                "Classroom 5",
                "Classroom 6",
                "Classroom 7",
                "Classroom 8",
                "Classroom Exam",
            ]
        )
    }

    # For if we add new game+ trophies, mostly here for completeness sake
    # "Dare Bird Trophy": {
    #     LOCATION_ID_KEY: get_room_location_id("Room 46") + 1,
    #     LOCATION_ROOM_KEY: "Room 46",
    # },
    # "Cursed Trophy": {
    #     LOCATION_ID_KEY: get_room_location_id("Room 46") + 2,
    #     LOCATION_ROOM_KEY: "Room 46",
    # },
    # "Day One Trophy": {
    #     LOCATION_ID_KEY: get_room_location_id("Room 46") + 3,
    #     LOCATION_ROOM_KEY: "Room 46",
    # },
    # "Trophy of Speed": {
    #     LOCATION_ID_KEY: get_room_location_id("Room 46") + 4,
    #     LOCATION_ROOM_KEY: "Room 46",
    # }
    # "Trophy of Trophies": {
    #     LOCATION_ID_KEY: get_room_location_id("Trophy Room") + 0,
    #     LOCATION_ROOM_KEY: "Trophy Room",
    #     LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(state.can_reach_location(trophy, world.player) for trophy in [
    #             "Full House Trophy",
    #             "Trophy of Invention",
    #             "Trophy of Drafting",
    #             "Trophy of Wealth",
    #             "Inheritance Trophy",
    #             "Bullseye Trophy",
    #             "A Logical Trophy",
    #             "Trophy 8",
    #             "Explorer's Trophy",
    #             "Trophy of Sigils",
    #             "Diploma Trophy",
    #             "Dare Bird Trophy",
    #             "Cursed Trophy",
    #             "Day One Trophy",
    #             "Trophy of Speed"
    #         ]
    #     )
    # }
}

safes_and_small_gates = {
    "Boudoir Safe": {
        LOCATION_ID_KEY: get_room_location_id("Boudoir", 0),
        LOCATION_ROOM_KEY: "Boudoir",
    },
    "Drafting Studio Safe": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 0),
        LOCATION_ROOM_KEY: "Drafting Studio",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("MAGNIFYING GLASS", state, world.player)
    },
    "Drawing Room Safe": {
        LOCATION_ID_KEY: get_room_location_id("Drawing Room", 0),
        LOCATION_ROOM_KEY: "Drawing Room",
    },
    "Office Safe": {
        LOCATION_ID_KEY: get_room_location_id("Office", 0),
        LOCATION_ROOM_KEY: "Office",
    },
    "Study Safe": {
        LOCATION_ID_KEY: get_room_location_id("Study", 0),
        LOCATION_ROOM_KEY: "Study",
    },
    "Underpass Gate": {
        LOCATION_ID_KEY: get_room_location_id("The Underpass", 0),
        LOCATION_ROOM_KEY: "The Underpass",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Boiler Room", world.player)
    },
    "Shelter Safe": {
        LOCATION_ID_KEY: get_room_location_id("Shelter", 0),
        LOCATION_ROOM_KEY: "Shelter",
    },
    "Orchard Gate": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 0),
        LOCATION_ROOM_KEY: "Campsite",
    }
}

aries_court_mora_jia_boxes = {
    f"Aries Court Mora Jia Box {n}": {
        LOCATION_ID_KEY: get_room_location_id("Aries Court", n),
        LOCATION_ROOM_KEY: "Aries Court",
    } for n in range(1, 9)
}

mora_jia_boxes = {
    "Master Bedroom Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Master Bedroom", 0),
        LOCATION_ROOM_KEY: "Master Bedroom",
    },
    "Closed Exhibit Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Closed Exhibit", 0),
        LOCATION_ROOM_KEY: "Closed Exhibit",
    },
    "Underpass Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("The Underpass", 1),
        LOCATION_ROOM_KEY: "The Underpass",
    },
    "Tomb Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Tomb", 0),
        LOCATION_ROOM_KEY: "Tomb",
    },
    "Trading Post Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post", 0),
        LOCATION_ROOM_KEY: "Trading Post",
    },
    "Tunnel Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Tunnel", 0),
        LOCATION_ROOM_KEY: "Tunnel",
    },
    "Solarium Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Solarium", 0),
        LOCATION_ROOM_KEY: "Solarium",
    },
    "Lost And Found Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Lost And Found", 1),
        LOCATION_ROOM_KEY: "Lost And Found",
    },
    "Throne of the Blue Prince Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Throne Room", 0),
        LOCATION_ROOM_KEY: "Throne Room",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.has("Ascend The Throne", world.player)
    },
    "Arch Aries Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Arch Aries Sanctum", 0),
        LOCATION_ROOM_KEY: "Arch Aries Sanctum",
    },
    "Corarica Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Corarica Sanctum", 0),
        LOCATION_ROOM_KEY: "Corarica Sanctum",
    },
    "Eraja Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Eraja Sanctum", 0),
        LOCATION_ROOM_KEY: "Eraja Sanctum",
    },
    "Fenn Aries Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Fenn Aries Sanctum", 0),
        LOCATION_ROOM_KEY: "Fenn Aries Sanctum",
    },
    "Mora Jai Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Mora Jai Sanctum", 0),
        LOCATION_ROOM_KEY: "Mora Jai Sanctum",
    },
    "Orinda Aries Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Orinda Aries Sanctum", 0),
        LOCATION_ROOM_KEY: "Orinda Aries Sanctum",
    },
    "Verra Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Verra Sanctum", 0),
        LOCATION_ROOM_KEY: "Verra Sanctum",
    },
    "Nuance Sanctum Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Nuance Sanctum", 0),
        LOCATION_ROOM_KEY: "Nuance Sanctum",
    }
} | aries_court_mora_jia_boxes
# not adding atelier boxes, since they are basically already at the latest goal

drafting_studio_additions = {
    "Dovecote Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 1),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Dovecote"
    },
    "The Kennel Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 2),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "The Kennel"
    },
    "Clock Tower Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 3),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Clock Tower"
    },
    "Classroom Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 4),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Classroom Exam"
    },
    "Solarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 5),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Solarium"
    },
    "Dormitory Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 6),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Dormitory"
    },
    "Vestibule Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 7),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Vestibule"
    },
    "Casino Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 8),
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Casino"
    },
}

found_floorplans = {
    "Planetarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Observatory", 0),
        LOCATION_ROOM_KEY: "Observatory",
        NONSANITY_LOCATION_KEY: "Planetarium"
    },
    "Mechanarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Rotating Gear", 0),
        LOCATION_ROOM_KEY: "Rotating Gear",
        NONSANITY_LOCATION_KEY: "Mechanarium"
    },
    "Treasure Trove Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("The Underpass", 2),
        LOCATION_ROOM_KEY: "The Underpass",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Boiler Room", world.player),
        NONSANITY_LOCATION_KEY: "Treasure Trove"
    },
    "Throne Room Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Orindian Ruins", 0),
        LOCATION_ROOM_KEY: "Orindian Ruins",
        NONSANITY_LOCATION_KEY: "Throne Room"
    },
    "Tunnel Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Tunnel Area Past Crates", 0),
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
        NONSANITY_LOCATION_KEY: "Tunnel"
    },
    "Conservatory Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 1),
        LOCATION_ROOM_KEY: "Campsite",
        NONSANITY_LOCATION_KEY: "Conservatory",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SHOVEL", state, world.player),
    },
    "Lost And Found Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Basement", 0),
        LOCATION_ROOM_KEY: "Basement",
        NONSANITY_LOCATION_KEY: "Lost And Found",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SHOVEL", state, world.player),
    },
    "Closed Exhibit Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Study", 1),
        LOCATION_ROOM_KEY: "Study",
        NONSANITY_LOCATION_KEY: "Closed Exhibit"
    }
}

floorplans = drafting_studio_additions | found_floorplans

gift_shop_items = {
    "Gift Shop - Mt. Holly Tee": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop", 0),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Lunch Box": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop", 1),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Swim Trunks": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop", 2),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Swim Bird Plushie": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop", 3),
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Blue Tents": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop", 4),
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: len([state.can_reach_location(loc, world.player) for loc in trophies.keys()]) >= 8
    },
    "Gift Shop - Cursed Coffers": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop", 5),
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in ["Library", "Shrine"]),
    }
}

bookshop_items = {
    "Bookshop - The History of Orindia (1st ed.) ": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop", 0),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - A New Clue": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop", 1),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - The Curse of Black Bridge": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop", 2),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Realm & Rune": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop", 3),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 4": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop", 4),
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 5": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop", 5),
        LOCATION_ROOM_KEY: "Bookshop",
    },
}

shop_items = gift_shop_items | bookshop_items

def get_trading_post_offers(give: str) -> list[str]:
    if give in TRADING_POST_TIER1[TRADING_POST_GIVE]:
        return [x for x in TRADING_POST_TIER1[TRADING_POST_RECEIVE] if x != give]
    if give in TRADING_POST_TIER2[TRADING_POST_GIVE]:
        return [x for x in TRADING_POST_TIER2[TRADING_POST_RECEIVE] if x != give]
    if give in TRADING_POST_TIER3[TRADING_POST_GIVE]:
        return [x for x in TRADING_POST_TIER3[TRADING_POST_RECEIVE] if x != give]
    if give in TRADING_POST_TIER4[TRADING_POST_GIVE]:
        return [x for x in TRADING_POST_TIER4[TRADING_POST_RECEIVE] if x != give]
    return []

# I ignored Cloister upgrades for now, but they should probably be checked eventually, since some of them would be a break in logic for item pickups

def trunk_rule(state: CollectionState, player: int) -> bool: 
    return any(state.can_reach_region(region, player) for region in [
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
    ])
    # Also several spare room upgrades, but we aren't adding upgraded rooms seperately atm.

def trunk_extreme_rule(state: CollectionState, player: int) -> bool: 
    return any(state.can_reach_region(region, player) for region in [
        "Spare Room",
        "Music Room",
        "Drawing Room",
        "Trophy Room",
        "Gallery",
        "Great Hall",
    ]) or (state.can_reach_region("The Pool", player) and state.can_reach_region("Gift Shop", player)) or (state.can_reach_region("Planetarium", player) and can_reach_item_location("TELESCOPE", state, player))

def darkroom_rule(state: CollectionState, player: int) -> bool:
    return state.can_reach_region("Darkroom", player) and (state.can_reach_region("Utility Closet", player) or state.can_reach_region("Shelter", player) or can_reach_item_location("KNIGHTS SHIELD", state, player))

def lavatory_rule(state: CollectionState, player: int) -> bool:
    return state.can_reach_region("Lavatory", player) and (state.can_reach_region("Shelter", player) or can_reach_item_location("KNIGHTS SHIELD", state, player) or can_reach_item_location("Dowsing Rod", state, player))

def advanced_experiment_rule(state: CollectionState, player: int) -> bool: 
    return state.has("Satellite Raised", player) and state.can_reach_region("Laboratory", player)

def trading_post_rule(item_name: str, state: CollectionState, player: int) -> bool:
    return state.can_reach_region("Trading Post", player) and any(can_reach_item_location(item, state, player) for item in get_trading_post_offers(item_name))

def dig_spot_rule(state: CollectionState, player: int) -> bool:
    return any(state.can_reach_region(region, player) for region in [
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
        "Boiler Room",
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
    ]) or (state.can_reach_region("Planetarium", player) and can_reach_item_location("TELESCOPE", state, player))

standard_item_pickup = {
    "BATTERY PACK First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 2), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BATTERY PACK",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Attic",
            "Archives",
            "Courtyard",
            "Laboratory",
            "Mail Room",
            "Patio",
            "Storeroom",
            "Wine Cellar",
            "Workshop",
            "Clock Tower",
            "Mechanarium",
            "Toolshed",
            "Hovel",
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Spare Room",
            "Garage",
            "Utility Closet",
            "Kitchen",
        ]),

        LOCATION_RULE_COMPLEX: lambda state, world: darkroom_rule(state, world.player)
        or (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world.player)),

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or trading_post_rule("BATTERY PACK", state, world.player),
        # Also spawns in Spare Patio, but we aren't adding upgraded rooms seperately atm.
    },
    "BROKEN LEVER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 3), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BROKEN LEVER",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Aquarium",
            "Attic",
            "Cloister",
            "Drafting Studio",
            "Laboratory",
            "Locker Room",
            "Observatory",
            "Patio",
            "Sauna",
            "Security",
            "Storeroom",
            "Weight Room",
            "Wine Cellar",
            "Workshop",
            "Secret Garden",
            "Conservatory",
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Spare Room",
            "Billiard Room",
            "Garage",
            "Utility Closet",
            "Kitchen",
        ]) or (can_reach_item_location("SHOVEL", state, world.player) and dig_spot_rule(state, world.player)),

        LOCATION_RULE_COMPLEX: darkroom_rule,

        LOCATION_RULE_EXTREME: advanced_experiment_rule
        # Also spawns in Spare Greenroom, but we aren't adding upgraded rooms seperately atm.
    },
    "COIN PURSE First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 4), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "COIN PURSE",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Walk-In Closet",
            "Parlor",
            "Attic",
            "Workshop",
            "Dining Room",
            "Bedroom",
            "Mail Room", # Packages
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Gallery",
            "Ballroom",
            "Drawing Room",
        ]),

        LOCATION_RULE_COMPLEX: lavatory_rule,

        LOCATION_RULE_EXTREME: advanced_experiment_rule
        # Also spawns in Her Ladyship's Spare Room and Spare Master Bedroom, but we aren't adding upgraded rooms seperately atm.
    },
    "COMPASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 5), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "COMPASS",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Aquarium",
            "Attic",
            "Cloister",
            "Closet",
            "Drafting Studio",
            "Observatory",
            "Terrace",
            "Walk-In Closet",
            "Workshop",
            "Throne Room",
            "Commissary",
            "Mail Room", # Packages
        ]),
        # Also spawns in Her Ladyship's Spare Room, Spare Master Bedroom, and Spare Terrace, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Den",
            "Trophy Room",
        ]),

        LOCATION_RULE_COMPLEX: trunk_rule,
        LOCATION_RULE_EXTREME: advanced_experiment_rule,
    },
    "COUPON BOOK First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 6), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Attic",
            "Conference Room",
            "Dining Room",
            "Library",
            "Mail Room",
            "Nook",
            "Office",
            "Vault",
            "Walk-In Closet",
            "Morning Room",
            "Mail Room", # Packages
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Den",
            "Pantry",
        ]),

        LOCATION_RULE_EXTREME: advanced_experiment_rule,
    },
    "GEAR WRENCH First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 7), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "GEAR WRENCH",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Toolshed",
            "Lost And Found",
        ]),

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "HALL PASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 8), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "HALL PASS",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Classroom 1",
            "Classroom 2",
            "Classroom 3",
            "Classroom 4",
            "Classroom 5",
            "Classroom 6",
            "Classroom 7",
            "Classroom 8",
            "Classroom Exam",
            "Dormitory",
            "Lost And Found",
        ]),

        LOCATION_RULE_EXTREME: lambda state, world: (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player)) or state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "LOCK PICK KIT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 9), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "LOCK PICK KIT",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Archives",
            "Attic",
            "Rumpus Room",
            "Security",
            "Vault",
            "Walk-In Closet",
            "Wine Cellar",
            "Workshop",
            "Closed Exhibit",
            "Locksmith",
            "Mail Room", # Packages
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player)),
        # Also spawns in Spare Bedroom (and its upgrades), but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: state.can_reach_region("Garage", world.player),

        LOCATION_RULE_COMPLEX: lambda state, world: trunk_rule(state, world) or (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world.player)) or (state.can_reach_region("Darkroom", world.player) 
            and (state.can_reach_region("Utility Closet", world.player) or state.can_reach_region("Shelter", world.player) 
                 or can_reach_item_location("KNIGHTS SHIELD", state, world.player))),

        LOCATION_RULE_EXTREME: lambda state, world: (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player)) or trunk_extreme_rule(state, world),
    },
    "LUCKY RABBIT'S FOOT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 10), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "LUCKY RABBIT'S FOOT",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Walk-In Closet",
            "Rumpus Room",
            "Nursery",
            "Morning Room",
            "Throne Room",
            "Lost And Found",
        ]),
        # Also spawns in Her Ladyship's Spare Room, Spare Servant's Quarters, and Spare Bedroom, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Gallery",
            "Den",
            "Ballroom",
        ]),

        LOCATION_RULE_COMPLEX: lambda state, world: (state.can_reach_region("Lavatory", world.player) and 
            (state.can_reach_region("Shelter", world.player) or can_reach_item_location("KNIGHTS SHIELD", state, world.player) 
             or can_reach_item_location("Dowsing Rod", state, world.player))),
        
        LOCATION_RULE_EXTREME: lambda state, world: (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player)),
    },
    "MAGNIFYING GLASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 11), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "MAGNIFYING GLASS",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Archives",
            "Attic",
            "Boudoir",
            "Chapel",
            "Courtyard",
            "Drafting Studio",
            "Guest Bedroom",
            "Her Ladyship's Chambers",
            "Laboratory",
            "Library",
            "Mail Room",
            "Nook",
            "Observatory",
            "Office",
            "Parlor",
            "Study",
            "Workshop",
            "Classroom 1",
            "Classroom 2",
            "Classroom 3",
            "Classroom 4",
            "Classroom 5",
            "Classroom 6",
            "Classroom 7",
            "Classroom 8",
            "Classroom Exam",
            "Conservatory",
            "Commissary",
        ]),
        # Also spawns in Spare Foyer, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Den",
            "Drawing Room",
        ]),

        LOCATION_RULE_COMPLEX: lambda state, world: (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world.player)),

        LOCATION_RULE_EXTREME: advanced_experiment_rule,
    },
    "METAL DETECTOR First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 12), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "METAL DETECTOR",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Archives",
            "Attic",
            "Closet",
            "Courtyard",
            "Greenhouse",
            "Maids Chamber",
            "Mail Room",
            "Patio",
            "Veranda",
            "Workshop",
            "Secret Garden",
            "Clock Tower",
            "Toolshed",
            "Commissary",
        ]),
        # Also spawns in Spare Patio and Spare Veranda, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Garage",
            "Boiler Room",
        ]),

        LOCATION_RULE_EXTREME: advanced_experiment_rule,
    },
    "REPELLENT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Lost And Found", 2),
        LOCATION_ROOM_KEY: "Lost And Found",
        LOCATION_ITEM_KEY: "REPELLENT",
    },
    "RUNNING SHOES First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 14), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "RUNNING SHOES",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Gymnasium",
            "Locker Room",
            "Rumpus Room",
            "Sauna",
            "The Pool",
            "Walk-In Closet",
            "Weight Room",
            "Dormitory",
            "Commissary",
            "Locker Room",
        ]),
        # Also spawns in Spare Servant's Quarters, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: state.can_reach_region("Garage", world.player),

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or state.can_reach_region("Mail Room", world.player),
    },
    "SALT SHAKER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 15), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SALT SHAKER",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Rumpus Room",
            "Walk-In Closet",
            "Billiard Room",
            "Dining Room",
            "Morning Room",
            "Commissary",
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Pantry",
            "Kitchen",
        ]),

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or trading_post_rule("SALT SHAKER", state, world.player) or state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "SHOVEL First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 16), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SHOVEL",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Aquarium",
            "Attic",
            "Cloister",
            "Closet",
            "Courtyard",
            "Furnace",
            "Greenhouse",
            "Patio",
            "Storeroom",
            "Terrace",
            "Veranda",
            "Wine Cellar",
            "Workshop",
            "Secret Garden",
            "Clock Tower",
            "Solarium",
            "Tunnel",
            "Toolshed",
            "Hovel",
            "Commissary",
        ]),
        # Also spawns in Spare Greenhouse, Spare Patio, Space Terrace, and Spare Veranda, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Spare Room",
            "Garage",
            "Trophy Room",
            "Utility Closet",
            "Boiler Room",
        ]),

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player)
        or trading_post_rule("SHOVEL", state, world.player) or state.can_reach_region("Mail Room", world.player) or state.can_reach_region("Observatory", world.player), # Spiral of Stars and Freight Mail
    },
    "SLEDGE HAMMER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 17), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SLEDGE HAMMER",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Attic",
            "Closet",
            "Courtyard",
            "Greenhouse",
            "Storeroom",
            "Veranda",
            "Workshop",
            "Wine Cellar",
            "Secret Garden",
            "Tunnel",
            "Toolshed",
            "Commissary",
        ]),
        # Also spawns in Spare Hall and Spare Foyer, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Spare Room",
            "Garage",
            "Music Room",
            "Trophy Room",
            "Utility Closet",
        ]),

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player)
        or trading_post_rule("SLEDGE HAMMER", state, world.player) or state.can_reach_region("Mail Room", world.player) or state.can_reach_region("Observatory", world.player), # Spiral of Stars and Freight Mail
    },
    "SLEEPING MASK First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 18), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SLEEPING MASK",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Bedroom",
            "Boudoir",
            "Closet",
            "Master Bedroom",
            "Sauna",
            "Walk-In Closet",
            "Commissary",
            "Mail Room", # Packages
        ]),
        # Also spawns in Her Ladyship's Spare Room, Spare Bedroom, Spare Master Bedroom, and Spare Servant's Quarters, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or state.state.can_reach_region("Observatory", world.player),
    },
    "STOPWATCH First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 19), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "STOPWATCH",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Clock Tower",
            "Lost And Found",
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: can_reach_item_location("JACK HAMMER", state, world.player) and dig_spot_rule(state, world.player),
    },
    "TELESCOPE First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 20), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "TELESCOPE",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Her Ladyship's Chambers",
            "Walk-In Closet",
            "Planetarium",
        ]),
        # Also spawns in Her Ladyship's Spare Room, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or trading_post_rule("TELESCOPE", state, world.player) or state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "TREASURE MAP First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 21), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "TREASURE MAP",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Attic",
            "Drafting Studio",
            "Library",
            "Mail Room",
            "Observatory",
            "Rumpus Room",
            "Study",
            "Wine Cellar",
            "Clock Tower",
            "Locker Room",
        ]),
        # Also spawns in Spare Foyer and Spare Secret Passage, but we aren't adding upgraded rooms seperately atm.
        # Also, ignoring chance to spawn in trunks for the moment

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Den",
            "Trophy Room",
        ]),

        LOCATION_RULE_COMPLEX: lambda state, world: trunk_rule(state, world.player) or (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world.player)) or lavatory_rule(state, world.player),

        LOCATION_RULE_EXTREME: trunk_extreme_rule
    },
    "WATERING CAN First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 22), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "WATERING CAN",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Greenhouse",
            "Toolshed",
            "Hovel",
            "Lost And Found",
        ]),
        # Also spawns in Spare Greenroom, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
}

special_key_pickup = {
    "BASEMENT KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 30), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BASEMENT KEY",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Antechamber", world.player),

        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "CAR KEYS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 31), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "CAR KEYS",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Bedroom",
            "Billiard Room",
            "Dining Room",
            "Gymnasium",
            "Locker Room",
            "Music Room",
            "Office",
            "Parlor",
            "Patio",
            "Rumpus Room",
            "Sauna",
            "Security",
            "The Pool",
            "Walk-In Closet",
            "Locker Room",
        ]),
        # Also spawns in Spare Bedroom, Spare Patio, and Spare Servant's Quarters, but we aren't adding upgraded rooms seperately atm.

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Gallery",
            "Den",
            "Locksmith",
        ]),

        LOCATION_RULE_COMPLEX: trunk_rule,

        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player) or advanced_experiment_rule(state, world.player) or trunk_extreme_rule(state, world.player), # Spiral of Stars
    },
    "KEY 8 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 32), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "KEY 8",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Gallery", world.player),

        LOCATION_RULE_COMPLEX: lambda state, world: state.can_reach_region("Lost And Found", world.player), # Day 365+
    },
    "KEYCARD First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 33), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "KEYCARD",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Archives",
            "Closet",
            "Conference Room",
            "Guest Bedroom",
            "Mail Room",
            "Music Room",
            "Laboratory",
            "Locker Room",
            "Office",
            "Rumpus Room",
            "Sauna",
            "Security",
            "Study",
            "The Pool",
            "Vault",
            "Walk-In Closet",
            "Dormitory",
            "Locker Room",
        ]),

        LOCATION_RULE_COMPLEX: lambda state, world: (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world.player)) or darkroom_rule(state, world.player) or trunk_rule(state, world.player),

        LOCATION_RULE_EXTREME: lambda state, world: advanced_experiment_rule(state, world.player) or trunk_extreme_rule(state, world.player),
    },
    "PRISM KEY_0 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 34), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "PRISM KEY_0",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Music Room",
            "Lost And Found",
            "Locksmith"
        ]),

        LOCATION_RULE_COMPLEX: lambda state, world: (state.can_reach_region("Freezer", world.player) and any(can_reach_item_location(item, state, world.player) for item in ["Burning Glass", "TORCH"]))
        or (state.can_reach_region("Planetarium", world.player) and can_reach_item_location("TELESCOPE", state, world.player)),
    },
    "SECRET GARDEN KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 35), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SECRET GARDEN KEY",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Attic",
            "Music Room",
            "Lost And Found",
            "Locksmith",
            "Billiard Room",
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: can_reach_item_location("SHOVEL", state, world.player) and dig_spot_rule(state, world.player),

        LOCATION_RULE_COMPLEX: lambda state, world: (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world.player)) or trunk_rule(state, world.player),

        LOCATION_RULE_EXTREME: trunk_extreme_rule,
    },
    "SILVER KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 36), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SILVER KEY",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Music Room",
            "Her Ladyship's Chambers",
            "Mechanarium",
            "Locksmith",
            "Billiard Room", # Dartboard puzzle
            "Mail Room", # Packages
        ]),
        # Also ignoring chance to spawn in trunks for the moment

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: can_reach_item_location("SHOVEL", state, world.player) and dig_spot_rule(state, world.player),

        LOCATION_RULE_COMPLEX: lambda state, world: (state.can_reach_region("Freezer", world.player) and any(can_reach_item_location(item, state, world.player) for item in ["Burning Glass", "TORCH"]) 
            and can_reach_item_location("PRISM KEY_0", state, world)) or trunk_rule(state, world.player),

        LOCATION_RULE_EXTREME:lambda state, world: advanced_experiment_rule(state, world.player) or trunk_extreme_rule(state, world.player) or state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    # "Wind-up Key First Pickup": {
    #     LOCATION_ID_KEY: get_room_location_id("Campsite", 37), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
    #     LOCATION_ROOM_KEY: "Campsite",
    #     LOCATION_ITEM_KEY: "Wind-up Key",
    #     LOCATION_RULE: lambda state, world: obf_can_reach_region("Parlor", state, world) 
    #     or state.can_reach_region("Observatory", world.player) # Spiral of Stars
    #     or can_reach_item_location("Jack Hammer", state, world.player)
    #     or state.can_reach_region("Tunnel Area Past Blue Door", world.player) # I would be very suprised if this is the only one a player has access to, but adding just in case
    # }
}

showroom_item_pickup = {
    "CHRONOGRAPH First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 40), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "CHRONOGRAPH",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Showroom", world.player),
        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "EMERALD BRACELET First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 41), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "EMERALD BRACELET",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Showroom", world.player),
        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "MASTER KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 42), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "MASTER KEY",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Showroom", world.player),
        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "MOON PENDANT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 43), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "MOON PENDANT",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Showroom", world.player),
        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "ORNATE COMPASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 44), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "ORNATE COMPASS",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Showroom", world.player),
        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
    "SILVER SPOON First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 45), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "SILVER SPOON",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Showroom", world.player),
        LOCATION_RULE_EXTREME: lambda state, world: state.can_reach_region("Observatory", world.player), # Spiral of Stars
    },
}

unique_item_pickup = {
    "CROWN First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Room 46", 6),
        LOCATION_ROOM_KEY: "Room 46",
        LOCATION_ITEM_KEY: "CROWN",
    },
    "CURSED EFFIGY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Shrine", 0),
        LOCATION_ROOM_KEY: "Shrine",
        LOCATION_ITEM_KEY: "CURSED EFFIGY",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: (can_reach_item_location("SLEDGE HAMMER", state, world.player) or can_reach_item_location("MORNING STAR", state, world.player)) 
        and state.can_reach_region("Gift Shop", world.player)
    },
    "DIARY KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Her Ladyship's Chambers", 0),
        LOCATION_ROOM_KEY: "Her Ladyship's Chambers",
        LOCATION_ITEM_KEY: "DIARY KEY",
    },
    "KEY of Aries First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Aries Court", 0),
        LOCATION_ROOM_KEY: "Aries Court",
        LOCATION_ITEM_KEY: "KEY of Aries",
    },
    "LUNCH BOX First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Dining Room", 0),
        LOCATION_ROOM_KEY: "Dining Room",
        LOCATION_ITEM_KEY: "LUNCH BOX",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Gift Shop", world.player)
    },
    "MICROCHIP 1 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("West Path", 0),
        LOCATION_ROOM_KEY: "West Path",
        LOCATION_ITEM_KEY: "MICROCHIP 1",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SHOVEL", state, world.player)
    },
    "MICROCHIP 2 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 10),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "MICROCHIP 2",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SLEDGE HAMMER", state, world.player) or can_reach_item_location("MORNING STAR", state, world.player)
    },
    "MICROCHIP 3 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Blackbridge Grotto", 0),
        LOCATION_ROOM_KEY: "Blackbridge Grotto",
        LOCATION_ITEM_KEY: "MICROCHIP 3",
    },
    "PAPER CROWN First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Closed Exhibit", 1),
        LOCATION_ROOM_KEY: "Closed Exhibit",
        LOCATION_ITEM_KEY: "PAPER CROWN",
    },
    "ROYAL SCEPTER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Treasure Trove", 0),
        LOCATION_ROOM_KEY: "Treasure Trove",
        LOCATION_ITEM_KEY: "ROYAL SCEPTER",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Shrine", world.player) and can_reach_item_location("KEY of Aries", state, world.player)
    }
}

item_pickups = standard_item_pickup | special_key_pickup | showroom_item_pickup | unique_item_pickup

workshop_contraptions = {
    "Burning Glass First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 1),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Burning Glass",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["MAGNIFYING GLASS", "METAL DETECTOR"])
    },
    "Detector Shovel First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 2),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Detector Shovel",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["SHOVEL", "METAL DETECTOR"])
    },
    "Dowsing Rod First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 3),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Dowsing Rod",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["SHOVEL", "COMPASS"])
    },
    "Power Hammer First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 4),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Power Hammer",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["SLEDGE HAMMER", "BROKEN LEVER", "BATTERY PACK"])
    },
    "Electromagnet First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 5),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Electromagnet",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["COMPASS", "BATTERY PACK"])
    },
    "Lucky Purse First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 6),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Lucky Purse",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["COIN PURSE", "LUCKY RABBIT'S FOOT"])
    },
    "Jack Hammer First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 7),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Jack Hammer",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["SHOVEL", "BATTERY PACK", "BROKEN LEVER"])
    },
    "Pick Sound Amplifier First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 8),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Pick Sound Amplifier",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: all(can_reach_item_location(item, state, world.player) for item in ["LOCK PICK KIT", "METAL DETECTOR"])
    },
}

upgrade_disks = {
    "Upgrade Disk - Offic": {
        LOCATION_ID_KEY: get_room_location_id("Office", 1),
        LOCATION_ROOM_KEY: "Office",
    },
    "Upgrade Disk - Morning Room": {
        LOCATION_ID_KEY: get_room_location_id("Morning Room", 0),
        LOCATION_ROOM_KEY: "Morning Room",
    },
    "Upgrade Disk - Her Ladyship's Chambers": {
        LOCATION_ID_KEY: get_room_location_id("Her Ladyship's Chambers", 1),
        LOCATION_ROOM_KEY: "Her Ladyship's Chambers",
    },
    "Upgrade Disk - Commissary": {
        LOCATION_ID_KEY: get_room_location_id("Commissary", 0),
        LOCATION_ROOM_KEY: "Commissary",
    },
    "Upgrade Disk - Garage": {
        LOCATION_ID_KEY: get_room_location_id("Garage", 0),
        LOCATION_ROOM_KEY: "Garage",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("CAR KEYS", state, world.player)
    },
    "Upgrade Disk - Great Hall": {
        LOCATION_ID_KEY: get_room_location_id("Great Hall", 0),
        LOCATION_ROOM_KEY: "Great Hall",
    },
    "Upgrade Disk - Vault": {
        LOCATION_ID_KEY: get_room_location_id("Vault", 0),
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("VAULT KEY 304", state, world.player)
    },
    "Upgrade Disk - Trading Post Dynamite": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post", 1),
        LOCATION_ROOM_KEY: "Trading Post",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(can_reach_item_location(item, state, world.player) for item in ["Burning Glass", "TORCH"]),
    },
    "Upgrade Disk - Freezer": {
        LOCATION_ID_KEY: get_room_location_id("Freezer", 0),
        LOCATION_ROOM_KEY: "Freezer",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(can_reach_item_location(item, state, world.player) for item in [
            "Burning Glass",
            "TORCH",
            "Power Hammer",
        ]) or state.can_reach_region("Furnace", world.player)
    },
    "Upgrade Disk - Tomb": {
        LOCATION_ID_KEY: get_room_location_id("Tomb", 1),
        LOCATION_ROOM_KEY: "Tomb",
    },
    "Upgrade Disk - The Foundation": {
        LOCATION_ID_KEY: get_room_location_id("The Foundation", 0),
        LOCATION_ROOM_KEY: "The Foundation",
    },
    "Upgrade Disk - Abandoned Mine": {
        LOCATION_ID_KEY: get_room_location_id("Abandoned Mine", 0),
        LOCATION_ROOM_KEY: "Abandoned Mine",
    },
    "Upgrade Disk - Lost And Found": {
        LOCATION_ID_KEY: get_room_location_id("Lost And Found", 0),
        LOCATION_ROOM_KEY: "Lost And Found",
    },
    "Upgrade Disk - Mechanarium": {
        LOCATION_ID_KEY: get_room_location_id("Mechanarium", 0),
        LOCATION_ROOM_KEY: "Mechanarium",
    },
    "Upgrade Disk - Archives": {
        LOCATION_ID_KEY: get_room_location_id("Archives", 0),
        LOCATION_ROOM_KEY: "Archives",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("CABINET KEY 1", state, world.player)
    },
    "Upgrade Disk - Trading Post Trade": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post", 2),
        LOCATION_ROOM_KEY: "Trading Post",
    },
}

vault_keys = {
    "Vault Key 149": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 4), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 149",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: any(state.can_reach_region(x, world.player) for x in [
            "Attic", 
            "Rumpus Room", 
            "Security", 
            "Locker Room",
            "Music Room",
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: (can_reach_item_location("SHOVEL", state, world.player) and dig_spot_rule(state, world.player)) or state.can_reach_region("Trophy Room", world.player),

        LOCATION_RULE_EXTREME: advanced_experiment_rule,
    },
    "Vault Key 233": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 5), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 233",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SHOVEL", state, world.player)
        or any(state.can_reach_region(x, world.player) for x in [
            "Office",
            "Sauna",
            "Wine Cellar",
            "Morning Room",
            "Locker Room",
            "Music Room",
        ]),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: (can_reach_item_location("SHOVEL", state, world.player) and dig_spot_rule(state, world.player)),
        LOCATION_RULE_COMPLEX: lavatory_rule,
        LOCATION_RULE_EXTREME: advanced_experiment_rule,
    },
    "Vault Key 304": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 6), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 304",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SHOVEL", state, world.player) 
        or any(state.can_reach_region(x, world.player) for x in [
            "Conference Room",
            "Her Ladyship's Chambers",
            "Walk-In Closet",
            "Hovel",
        ]),
        # Can also spawn in Spare Hall, but we aren't adding upgraded rooms seperately atm.
        LOCATION_RULE_SIMPLE_RARE: lambda state, world: (can_reach_item_location("SHOVEL", state, world.player) and dig_spot_rule(state, world.player)) or state.can_reach_region("Drawing Room", world.player),
    },
    "Vault Key 370": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 7), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 370",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Lost And Found", world.player),

        LOCATION_RULE_SIMPLE_RARE: lambda state, world: (can_reach_item_location("SHOVEL", state, world.player) and dig_spot_rule(state, world.player)),
    }
}

sanctum_keys = {
    "Sanctum Key - Room 46": {
        LOCATION_ID_KEY: get_room_location_id("Room 46", 5),
        LOCATION_ROOM_KEY: "Room 46",
        LOCATION_ITEM_KEY: "SANCTUM KEY ANTECHAMBER"
    },
    "Sanctum Key - Vault": {
        LOCATION_ID_KEY: get_room_location_id("Vault", 1),
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_ITEM_KEY: "SANCTUM KEY VAULT",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("VAULT KEY 370", state, world.player)
    },
    "Sanctum Key - Clock Tower": {
        LOCATION_ID_KEY: get_room_location_id("Clock Tower", 0),
        LOCATION_ROOM_KEY: "Clock Tower",
        LOCATION_ITEM_KEY: "SANCTUM KEY CLOCK TOWER"
    },
    "Sanctum Key - Reservoir Bottom": {
        LOCATION_ID_KEY: get_room_location_id("Reservoir Bottom", 0),
        LOCATION_ROOM_KEY: "Reservoir Bottom",
        LOCATION_ITEM_KEY: "SANCTUM KEY RESERVOIR"
    },
    "Sanctum Key - Throne Room": {
        LOCATION_ID_KEY: get_room_location_id("Throne Room", 1),
        LOCATION_ROOM_KEY: "Throne Room",
        LOCATION_ITEM_KEY: "SANCTUM KEY THRONE ROOM"
    },
    "Sanctum Key - Safehouse": {
        LOCATION_ID_KEY: get_room_location_id("Safehouse", 0),
        LOCATION_ROOM_KEY: "Safehouse",
        LOCATION_ITEM_KEY: "SANCTUM KEY SAFEHOUSE"
    },
    "Sanctum Key - Music Room": {
        LOCATION_ID_KEY: get_room_location_id("Music Room", 0),
        LOCATION_ROOM_KEY: "Music Room",
        LOCATION_ITEM_KEY: "SANCTUM KEY MUSIC ROOM"
    },
    "Sanctum Key - Mechanarium": {
        LOCATION_ID_KEY: get_room_location_id("Mechanarium", 1),
        LOCATION_ROOM_KEY: "Mechanarium",
        LOCATION_ITEM_KEY: "SANCTUM KEY MECHANARIUM"
    }
}

file_cabinet_keys = {
    "File Cabinet Key - Patio": {
        LOCATION_ID_KEY: get_room_location_id("Patio", 0),
        LOCATION_ROOM_KEY: "Patio",
        LOCATION_ITEM_KEY: "CABINET KEY 1",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SHOVEL", state, world.player)
    },
    "File Cabinet Key - Laundry Room": {
        LOCATION_ID_KEY: get_room_location_id("Laundry Room", 0),
        LOCATION_ROOM_KEY: "Laundry Room",
        LOCATION_ITEM_KEY: "CABINET KEY 2",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SHOVEL", state, world.player)
    },
    "File Cabinet Key - Tunnel Area Past Crates": {
        LOCATION_ID_KEY: get_room_location_id("Tunnel Area Past Crates", 1),
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
        LOCATION_ITEM_KEY: "CABINET KEY 3",
    },
}

keys = vault_keys | sanctum_keys | file_cabinet_keys

misc_locations = {
    "Entrance Hall East Vase": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 8),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SLEDGE HAMMER", state, world.player) or can_reach_item_location("MORNING STAR", state, world.player)
    },
    "Entrance Hall West Vase": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 9),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SLEDGE HAMMER", state, world.player) or can_reach_item_location("MORNING STAR", state, world.player)
    },
    "Cursed Coffers": {
        LOCATION_ID_KEY: get_room_location_id("Shrine", 1),
        LOCATION_ROOM_KEY: "Shrine",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("SLEDGE HAMMER", state, world.player) or can_reach_item_location("MORNING STAR", state, world.player)
    },
    "Gasline Valve - Orchard": {
        LOCATION_ID_KEY: get_room_location_id("Apple Orchard", 0),
        LOCATION_ROOM_KEY: "Apple Orchard",
    },
    "Gasline Valve - Schoolhouse": {
        LOCATION_ID_KEY: get_room_location_id("Schoolhouse", 0),
        LOCATION_ROOM_KEY: "Schoolhouse",
    },
    "Gasline Valve - Hovel": {
        LOCATION_ID_KEY: get_room_location_id("Hovel", 0),
        LOCATION_ROOM_KEY: "Hovel",
    },
    "Gasline Valve - Gemstone Cavern": {
        LOCATION_ID_KEY: get_room_location_id("Gemstone Cavern", 0),
        LOCATION_ROOM_KEY: "Gemstone Cavern",
    },
    "Scorch Sundial": {
        LOCATION_ID_KEY: get_room_location_id("Apple Orchard", 1),
        LOCATION_ROOM_KEY: "Apple Orchard",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: can_reach_item_location("Burning Glass", state, world.player) or can_reach_item_location("TORCH", state, world.player)
    },
    "VAC Controls": {
        LOCATION_ID_KEY: get_room_location_id("Utility Closet", 0),
        LOCATION_ROOM_KEY: "Utility Closet",
    },
    # Almost all of the other Allowance Tokens are directly behind/next to another location
    "Allowance Token - Cloister Statue": {
        LOCATION_ID_KEY: get_room_location_id("Cloister", 0),
        LOCATION_ROOM_KEY: "Cloister",
    },
    "Allowance Token - Outer Entrance Hall Vase": {
        LOCATION_ID_KEY: get_room_location_id("Outer Room", 0),
        LOCATION_ROOM_KEY: "Outer Room",
        LOCATION_RULE_SIMPLE_COMMON: lambda state, world: state.can_reach_region("Shrine", world.player) and (can_reach_item_location("SLEDGE HAMMER", state, world.player) or can_reach_item_location("MORNING STAR", state, world.player))
    },
    # Ignoring deposit box allowance tokens for now, since they are missable (don't respawn if not picked up)
}

# TODO-1: add locations for other stuff later.
# Chapel Keeper
# Alzara Prophecies

# Treasure Map Chests? (Might need to pre-calculate min piece counts for chest locations)
# Bedroom Treasure Map Chest

# Mirror Room Floorplan Duplicates?

# Deposit Box 053? (The one opened with Key 8)

locations = trophies | safes_and_small_gates | mora_jia_boxes | floorplans | shop_items | upgrade_disks | keys | misc_locations | item_pickups | workshop_contraptions
    
from BaseClasses import CollectionState, ItemClassification

from .constants import *
from .data_rooms import rooms, core_rooms, room_layout_lists
from .data_items import *
from .locations import ROOM_MULTIPLIER

room_location_mem = {}

def get_room_location_id(room_name: str, n: int = 0) -> int:
    if room_name not in room_location_mem:
        room_location_mem[room_name] = []

    if n in room_location_mem[room_name]:
        raise Exception(f"Duplicate location ID for {room_name} {n}")
    
    if room_name in rooms:
        return rooms[room_name][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + n
    else:
        return (room_name.__hash__() % 100 + 1000) * ROOM_MULTIPLIER + n

def can_reach_item_location(item_name: str, state: CollectionState, world) -> bool:
    loc_name = item_name + " First Pickup"
    if state.has(loc_name, world.player):
        return True
    
    if loc_name in locations:
        return state.can_reach_location(loc_name, world.player)

    for location, data in locations.items():
        if LOCATION_ITEM_KEY in data and data[LOCATION_ITEM_KEY] == item_name:
            return state.can_reach_location(location, world.player)
        
    if item_name in armory_items:
        return state.can_reach_region("The Armory", world.player)
    
    return False

trophies = {
    "Full House Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 0),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: state.count_from_list([x for x in room_layout_lists[INNER_ROOM_KEY] if x not in core_rooms], world.player) >= 43
    },
    "Trophy of Invention": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 0),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in [
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
        LOCATION_RULE: lambda state, world: len([x for x in rooms if rooms[x][ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_D and not rooms[x][OUTER_ROOM_KEY] and x not in core_rooms and state.can_reach_region(x, world.player)]) >= 20,
    },
    "Trophy of Wealth": {
        LOCATION_ID_KEY: get_room_location_id("Showroom", 0),
        LOCATION_ROOM_KEY: "Showroom",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in showroom_items),
    },
    "Inheritance Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Room 46", 0),
        LOCATION_ROOM_KEY: "Room 46",
    },
    "Bullesye Trophy": {
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
        LOCATION_RULE: lambda state, world: state.has_all([x for x in rooms if x not in core_rooms], world.player)
    },
    "Trophy of Sigils": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 2),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: all(state.can_reach_region(sanctum, world.player) for sanctum in [
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
        LOCATION_RULE: lambda state, world: all(state.can_reach_region(region, world.player) for region in [
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
    #     LOCATION_REQUIREMENTS: lambda state, world: all(state.can_reach_location(trophy, world.player) for trophy in [
    #             "Full House Trophy",
    #             "Trophy of Invention",
    #             "Trophy of Drafting",
    #             "Trophy of Wealth",
    #             "Inheritance Trophy",
    #             "Bullesye Trophy",
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
        LOCATION_RULE: lambda state, world: can_reach_item_location("MAGNIFYING GLASS", state, world)
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
        LOCATION_RULE: lambda state, world: state.can_reach_region("Boiler Room", world.player)
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
        LOCATION_ID_KEY: get_room_location_id("Aries Court", n - 1),
        LOCATION_ROOM_KEY: "Aries Court",
    } for n in range(1, 9)
}

mora_jia_boxes = {
    "Master Bedroom Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Master Bedroom", 0),
        LOCATION_ROOM_KEY: "Master Bedroom",
    },
    "Closed Exhbit Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Closed Exhibit", 0),
        LOCATION_ROOM_KEY: "Closed Exhibit",
    },
    "Underpass Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("The Underpass", 0),
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
    "Solaium Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Solarium", 0),
        LOCATION_ROOM_KEY: "Solarium",
    },
    "Lost And Found Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Lost And Found", 0),
        LOCATION_ROOM_KEY: "Lost And Found",
    },
    "Throne of the Blue Prince Mora Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Throne Room", 0),
        LOCATION_ROOM_KEY: "Throne Room",
        LOCATION_RULE: lambda state, world: state.has("Ascend The Throne", world.player) and
        all(can_reach_item_location(item, state, world) for item in [
            "CROWN",
            "ROYAL SCEPTER",
            "CURSED EFFIGY",
        ])
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
# not adding atelier boxes, since they are bascially already at the latest goal

drafting_studio_additions = {
    "Dovecote Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 1),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "The Kennel Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 2),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Clock Tower Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 3),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Classroom Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 4),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Solarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 5),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Dormitory Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 6),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Vestibule Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 7),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Casino Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio", 8),
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
}

found_floorplans = {
    "Planetarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Observatory", 0),
        LOCATION_ROOM_KEY: "Observatory",
    },
    "Mechanarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Rotating Gear", 0),
        LOCATION_ROOM_KEY: "Rotating Gear",
    },
    "Treasure Trove Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("The Underpass", 0),
        LOCATION_ROOM_KEY: "The Underpass",
        LOCATION_RULE: lambda state, world: state.can_reach_region("Boiler Room", world.player)
    },
    "Throne Room Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Orindian Ruins", 0),
        LOCATION_ROOM_KEY: "Orindian Ruins",
    },
    "Tunnel Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Tunnel Area Past Crates", 0),
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
    },
    "Conservatory Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 1),
        LOCATION_ROOM_KEY: "Campsite",
    },
    "Lost And Found Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Basement", 0),
        LOCATION_ROOM_KEY: "Basement",
    },
    "Closed Exhibit Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Study", 1),
        LOCATION_ROOM_KEY: "Study",
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
        LOCATION_RULE: lambda state, world: len([state.can_reach_location(loc, world.player) for loc in trophies.keys()]) >= 8
    },
    "Gift Shop - Cursed Coffers": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop", 5),
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in ["Library", "Shrine"]),
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

standard_item_pickup = {
    "BATTERY PACK First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 2), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BATTERY PACK",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Spare Room",
            "Garage",
            "Utility Closet",
            "Kitchen",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Trading Post", world.player) and any(can_reach_item_location(item, state, world) for item in get_trading_post_offers("BATTERY PACK")))
        or (state.can_reach_region("Darkroom", world.player) 
          and (state.can_reach_region("Utility Closet", world.player) or state.can_reach_region("Shelter", world.player) 
               or can_reach_item_location("KNIGHTS SHIELD", state, world)))
        # Also spawns in Spare Patio, but we aren't adding upgraded rooms seperately atm.
    },
    "BROKEN LEVER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 3), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BROKEN LEVER",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Spare Room",
            "Billiard Room",
            "Garage",
            "Utility Closet",
            "Kitchen",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or can_reach_item_location("SHOVEL", state, world)
        or (state.can_reach_region("Darkroom", world.player) 
          and (state.can_reach_region("Utility Closet", world.player) or state.can_reach_region("Shelter", world.player) 
               or can_reach_item_location("KNIGHTS SHIELD", state, world)))
        # Also spawns in Spare Greenroom, but we aren't adding upgraded rooms seperately atm.
    },
    "COIN PURSE First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 4), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "COIN PURSE",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Walk-In Closet",
            "Parlor",
            "Attic",
            "Workshop",
            "Dining Room",
            "Bedroom",
            "Gallery",
            "Ballroom",
            "Drawing Room",
            "Mail Room",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Lavatory", world.player) and 
            (state.can_reach_region("Shelter", world.player) or can_reach_item_location("KNIGHTS SHIELD", state, world) or can_reach_item_location("Dowsing Rod", state, world)))
        # Also spawns in Her Ladyship's Spare Room and Spare Master Bedroom, but we aren't adding upgraded rooms seperately atm.
    },
    "COMPASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 5), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "COMPASS",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Den",
            "Commissary",
            "Mail Room",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        # Also spawns in Her Ladyship's Spare Room, Spare Master Bedroom, and Spare Terrace, but we aren't adding upgraded rooms seperately atm.
        # Also, ignoring chance to spawn in trunks for the moment
    },
    "COUPON BOOK First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 6), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Den",
            "Pantry",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
    },
    "GEAR WRENCH First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 7), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "GEAR WRENCH",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Toolshed",
            "Lost And Found",
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
    },
    "HALL PASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 8), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "HALL PASS",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
    },
    "LOCK PICK KIT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 9), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "LOCK PICK KIT",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Archives",
            "Attic",
            "Rumpus Room",
            "Security",
            "Vault",
            "Walk-In Closet",
            "Wine Cellar",
            "Workshop",
            "Closed Exhibit",
            "Garage",
            "Locksmith",
            "Mail Room",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Darkroom", world.player) 
            and (state.can_reach_region("Utility Closet", world.player) or state.can_reach_region("Shelter", world.player) 
                 or can_reach_item_location("KNIGHTS SHIELD", state, world)))
        # Also spawns in Spare Bedroom (and its upgrades), but we aren't adding upgraded rooms seperately atm.
        # Also, ignoring chance to spawn in trunks for the moment
    },
    "LUCKY RABBIT'S FOOT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 10), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "LUCKY RABBIT'S FOOT",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Walk-In Closet",
            "Rumpus Room",
            "Nursery",
            "Morning Room",
            "Throne Room",
            "Lost And Found",
            "Gallery",
            "Den",
            "Ballroom",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Lavatory", world.player) and 
            (state.can_reach_region("Shelter", world.player) or can_reach_item_location("KNIGHTS SHIELD", state, world) 
             or can_reach_item_location("Dowsing Rod", state, world)))
        # Also spawns in Her Ladyship's Spare Room, Spare Servant's Quarters, and Spare Bedroom, but we aren't adding upgraded rooms seperately atm.
    },
    "MAGNIFYING GLASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 11), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "MAGNIFYING GLASS",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Den",
            "Drawing Room",
            "Commissary",
        ]) or (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world))
        # Also spawns in Spare Foyer, but we aren't adding upgraded rooms seperately atm.
    },
    "METAL DETECTOR First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 12), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "METAL DETECTOR",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Garage",
            "Boiler Room",
            "Commissary",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        # Also spawns in Spare Patio and Spare Veranda, but we aren't adding upgraded rooms seperately atm.
    },
    "REPELLENT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Lost And Found", 0),
        LOCATION_ROOM_KEY: "Lost And Found",
        LOCATION_ITEM_KEY: "REPELLENT",
    },
    "RUNNING SHOES First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 14), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "RUNNING SHOES",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Gymnasium",
            "Locker Room",
            "Rumpus Room",
            "Sauna",
            "The Pool",
            "Walk-In Closet",
            "Weight Room",
            "Dormitory",
            "Garage",
            "Commissary",
            "Locker Room",
            "Mail Room", # Frieght Mail
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        # Also spawns in Spare Servant's Quarters, but we aren't adding upgraded rooms seperately atm.
    },
    "SALT SHAKER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 15), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SALT SHAKER",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Rumpus Room",
            "Walk-In Closet",
            "Billiard Room",
            "Dining Room",
            "Morning Room",
            "Pantry",
            "Kitchen",
            "Commissary",
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Trading Post", world.player) and any(can_reach_item_location(item, state, world) for item in get_trading_post_offers("SALT SHAKER")))
    },
    "SHOVEL First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 16), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SHOVEL",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Spare Room",
            "Garage",
            "Trophy Room",
            "Utility Closet",
            "Boiler Room",
            "Commissary",
            "Observatory", # Spiral of Stars
            "Mail Room", # Frieght Mail
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Trading Post", world.player) and any(can_reach_item_location(item, state, world) for item in get_trading_post_offers("SHOVEL")))
        # Also spawns in Spare Greenhouse, Spare Patio, Space Terrace, and Spare Veranda, but we aren't adding upgraded rooms seperately atm.
    },
    "SLEDGE HAMMER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 17), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SLEDGE HAMMER",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Spare Room",
            "Garage",
            "Music Room",
            "Trophy Room",
            "Utility Closet",
            "Commissary",
            "Observatory", # Spiral of Stars
            "Mail Room", # Frieght Mail
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Trading Post", world.player) and any(can_reach_item_location(item, state, world) for item in get_trading_post_offers("SLEDGE HAMMER")))
        # Also spawns in Spare Hall and Spare Foyer, but we aren't adding upgraded rooms seperately atm.
    },
    "SLEEPING MASK First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 18), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SLEEPING MASK",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Bedroom",
            "Boudoir",
            "Closet",
            "Master Bedroom",
            "Sauna",
            "Walk-In Closet",
            "Commissary",
            "Mail Room",
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        # Also spawns in Her Ladyship's Spare Room, Spare Bedroom, Spare Master Bedroom, and Spare Servant's Quarters, but we aren't adding upgraded rooms seperately atm.
    },
    "STOPWATCH First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 19), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "STOPWATCH",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Clock Tower",
            "Lost And Found",
        ]) or can_reach_item_location("JACK HAMMER", state, world)
    },
    "TELESCOPE First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 20), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "TELESCOPE",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Her Ladyship's Chambers",
            "Walk-In Closet",
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Trading Post", world.player) and any(can_reach_item_location(item, state, world) for item in get_trading_post_offers("TELESCOPE")))
        # Also spawns in Her Ladyship's Spare Room, but we aren't adding upgraded rooms seperately atm.
    },
    "TREASURE MAP First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 21), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "TREASURE MAP",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Attic",
            "Drafting Studio",
            "Library",
            "Mail Room",
            "Observatory",
            "Rumpus Room",
            "Study",
            "Wine Cellar",
            "Clock Tower",
            "Den",
            "Trophy Room",
            "Locker Room",
        ]) or (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world))
        or (state.can_reach_region("Lavatory", world.player) 
            and (state.can_reach_region("Shelter", world.player) or can_reach_item_location("KNIGHTS SHIELD", state, world) or can_reach_item_location("Dowsing Rod", state, world)))
        # Also spawns in Spare Foyer and Spare Secret Passage, but we aren't adding upgraded rooms seperately atm.
        # Also, ignoring chance to spawn in trunks for the moment
    },
    "WATERING CAN First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 22), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "WATERING CAN",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Greenhouse",
            "Toolshed",
            "Hovel",
            "Lost And Found",
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        # Also spawns in Spare Greenroom, but we aren't adding upgraded rooms seperately atm.
    },
}

special_key_pickup = {
    "BASEMENT KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 30), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BASEMENT KEY",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Antechamber",
            "Observatory", # Spiral of Stars
        ]),
    },
    "CAR KEYS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 31), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "CAR KEYS",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
            "Gallery",
            "Den",
            "Locksmith",
            "Locker Room",
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        # Also spawns in Spare Bedroom, Spare Patio, and Spare Servant's Quarters, but we aren't adding upgraded rooms seperately atm.
        # Also, ignoring chance to spawn in trunks for the moment
    },
    "KEY 8 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 32), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "KEY 8",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Gallery",
            "Lost And Found", # Day 365+
        ]),
    },
    "KEYCARD First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 33), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "KEYCARD",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
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
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Darkroom", world.player) 
            and (state.can_reach_region("Utility Closet", world.player) or state.can_reach_region("Shelter", world.player) or can_reach_item_location("KNIGHTS SHIELD", state, world)))
        or (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world))
        # Also ignoring chance to spawn in trunks for the moment
    },
    "PRISM KEY_0 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 34), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "PRISM KEY_0",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Music Room",
            "Lost And Found",
            "Locksmith"
        ]) or (state.can_reach_region("Freezer", world.player) and any(can_reach_item_location(item, state, world) for item in ["Burning Glass", "TORCH"]))
        or (state.can_reach_region("Planetarium", world.player) and can_reach_item_location("TELESCOPE", state, world))
    },
    "SECRET GARDEN KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 35), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SECRET GARDEN KEY",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Attic",
            "Music Room",
            "Lost And Found",
            "Locksmith",
            "Billiard Room",
        ]) or (state.can_reach_region("Garage", world.player) and can_reach_item_location("CAR KEYS", state, world))
        or can_reach_item_location("SHOVEL", state, world)
        # Also ignoring chance to spawn in trunks for the moment
    },
    "SILVER KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 36), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SILVER KEY",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Music Room",
            "Her Ladyship's Chambers",
            "Mechanarium",
            "Locksmith",
            "Billiard Room",
            "Mail Room",
            "Observatory", # Spiral of Stars
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or can_reach_item_location("SHOVEL", state, world)
        or (state.can_reach_region("Freezer", world.player) and any(can_reach_item_location(item, state, world) for item in ["Burning Glass", "TORCH"]) 
            and can_reach_item_location("PRISM KEY_0", state, world))
        # Also ignoring chance to spawn in trunks for the moment
    },
    # "Wind-up Key First Pickup": {
    #     LOCATION_ID_KEY: get_room_location_id("Campsite", 37), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
    #     LOCATION_ROOM_KEY: "Campsite",
    #     LOCATION_ITEM_KEY: "Wind-up Key",
    #     LOCATION_RULE: lambda state, world: obf_can_reach_region("Parlor", state, world) 
    #     or state.can_reach_region("Observatory", world.player) # Spiral of Stars
    #     or can_reach_item_location("Jack Hammer", state, world)
    #     or state.can_reach_region("Tunnel Area Past Blue Door", world.player) # I would be very suprised if this is the only one a player has access to, but adding just in case
    # }
}

def obf_can_reach_region(region_name: str, state, world) -> bool:
    res = state.can_reach_region(region_name, world.player)
    return res

showroom_item_rule = lambda state, world: state.can_reach_region("Showroom", world.player) or state.can_reach_region("Observatory", world.player) # Spiral of Stars

showroom_item_pickup = {
    "CHRONOGRAPH First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 40), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "CHRONOGRAPH",
        LOCATION_RULE: showroom_item_rule
    },
    "EMERALD BRACELET First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 41), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "EMERALD BRACELET",
        LOCATION_RULE: showroom_item_rule
    },
    "MASTER KEY First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 42), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "MASTER KEY",
        LOCATION_RULE: showroom_item_rule
    },
    "MOON PENDANT First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 43), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "MOON PENDANT",
        LOCATION_RULE: showroom_item_rule
    },
    "ORNATE COMPASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 44), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "ORNATE COMPASS",
        LOCATION_RULE: showroom_item_rule
    },
    "SILVER SPOON First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite", 45), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "SILVER SPOON",
        LOCATION_RULE: showroom_item_rule
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
        LOCATION_RULE: lambda state, world: can_reach_item_location("SLEDGE HAMMER", state, world) and state.can_reach_region("Gift Shop", world.player)
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
        LOCATION_RULE: lambda state, world: state.can_reach_region("Gift Shop", world.player)
    },
    "MICROCHIP 1 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("West Path", 0),
        LOCATION_ROOM_KEY: "West Path",
        LOCATION_ITEM_KEY: "MICROCHIP 1",
        LOCATION_RULE: lambda state, world: can_reach_item_location("SHOVEL", state, world)
    },
    "MICROCHIP 2 First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 10),
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "MICROCHIP 2",
        LOCATION_RULE: lambda state, world: can_reach_item_location("SLEDGE HAMMER", state, world)
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
        LOCATION_RULE: lambda state, world: state.can_reach_region("Shrine", world.player) and can_reach_item_location("KEY of Aries", state, world)
    }
}

item_pickups = standard_item_pickup | special_key_pickup | showroom_item_pickup | unique_item_pickup

workshop_contraptions = {
    "Burning Glass First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 1),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Burning Glass",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["MAGNIFYING GLASS", "METAL DETECTOR"])
    },
    "Detector Shovel First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 2),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Detector Shovel",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["SHOVEL", "METAL DETECTOR"])
    },
    "Dowsing Rod First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 3),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Dowsing Rod",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["SHOVEL", "COMPASS"])
    },
    "Power Hammer First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 4),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Power Hammer",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["SLEDGE HAMMER", "BROKEN LEVER", "BATTERY PACK"])
    },
    "Electromagnet First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 5),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Electromagnet",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["COMPASS", "BATTERY PACK"])
    },
    "Lucky Purse First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 6),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Lucky Purse",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["COIN PURSE", "LUCKY RABBIT'S FOOT"])
    },
    "Jack Hammer First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 7),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Jack Hammer",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["SHOVEL", "BATTERY PACK", "BROKEN LEVER"])
    },
    "Pick Sound Amplifier First Craft": {
        LOCATION_ID_KEY: get_room_location_id("Workshop", 8),
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Pick Sound Amplifier",
        LOCATION_RULE: lambda state, world: all(can_reach_item_location(item, state, world) for item in ["LOCK PICK KIT", "METAL DETECTOR"])
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
        LOCATION_ID_KEY: get_room_location_id("Her Ladyship's Chambers", 0),
        LOCATION_ROOM_KEY: "Her Ladyship's Chambers",
    },
    "Upgrade Disk - Commissary": {
        LOCATION_ID_KEY: get_room_location_id("Commissary", 0),
        LOCATION_ROOM_KEY: "Commissary",
    },
    "Upgrade Disk - Garage": {
        LOCATION_ID_KEY: get_room_location_id("Garage", 0),
        LOCATION_ROOM_KEY: "Garage",
        LOCATION_RULE: lambda state, world: can_reach_item_location("CAR KEYS", state, world)
    },
    "Upgrade Disk - Great Hall": {
        LOCATION_ID_KEY: get_room_location_id("Great Hall", 0),
        LOCATION_ROOM_KEY: "Great Hall",
    },
    "Upgrade Disk - Vault": {
        LOCATION_ID_KEY: get_room_location_id("Vault", 0),
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_RULE: lambda state, world: can_reach_item_location("VAULT KEY 304", state, world)
    },
    "Upgrade Disk - Trading Post Dynamite": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post", 0),
        LOCATION_ROOM_KEY: "Trading Post",
        LOCATION_RULE: lambda state, world: any(can_reach_item_location(item, state, world) for item in ["Burning Glass", "TORCH"]),
    },
    "Upgrade Disk - Freezer": {
        LOCATION_ID_KEY: get_room_location_id("Freezer", 0),
        LOCATION_ROOM_KEY: "Freezer",
        LOCATION_RULE: lambda state, world: any(can_reach_item_location(item, state, world) for item in [
            "Burning Glass",
            "TORCH",
            "Power Hammer",
        ]) or state.can_reach_region("Furnace", world.player)
    },
    "Upgrade Disk - Tomb": {
        LOCATION_ID_KEY: get_room_location_id("Tomb", 0),
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
        LOCATION_RULE: lambda state, world: can_reach_item_location("CABINET KEY 1", state, world)
    },
    "Upgrade Disk - Trading Post Trade": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post", 1),
        LOCATION_ROOM_KEY: "Trading Post",
    },
}

vault_keys = {
    "Vault Key 149": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 4), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ID_KEY: "VAULT KEY 149",
        LOCATION_RULE: lambda state, world: can_reach_item_location("SHOVEL", state, world) 
        or any(state.can_reach_region(x, world.player) for x in [
            "Attic", 
            "Rumpus Room", 
            "Security", 
            "Trophy Room", 
            "Locker Room",
            "Music Room",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
    },
    "Vault Key 233": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 5), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 233",
        LOCATION_RULE: lambda state, world: can_reach_item_location("SHOVEL", state, world)
        or any(state.can_reach_region(x, world.player) for x in [
            "Office",
            "Sauna",
            "Wine Cellar",
            "Morning Room",
            "Locker Room",
            "Music Room",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
        or (state.can_reach_region("Lavatory", world.player) 
            and (state.can_reach_region("Shelter", world.player) or can_reach_item_location("KNIGHTS SHIELD", state, world) or can_reach_item_location("Dowsing Rod", state, world)))
    },
    "Vault Key 304": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 6), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 304",
        LOCATION_RULE: lambda state, world: can_reach_item_location("SHOVEL", state, world) 
        or any(state.can_reach_region(x, world.player) for x in [
            "Conference Room",
            "Her Ladyship's Chambers",
            "Walk-In Closet",
            "Hovel",
            "Drawing Room",
        ])
        # Can also spawn in Spare Hall, but we aren't adding upgraded rooms seperately atm.
    },
    "Vault Key 370": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 7), # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 370",
        LOCATION_RULE: lambda state, world: can_reach_item_location("SHOVEL", state, world) 
        or state.can_reach_region("Lost And Found", world.player)
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
        LOCATION_RULE: lambda state, world: can_reach_item_location("VAULT KEY 370", state, world)
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
        LOCATION_RULE: lambda state, world: can_reach_item_location("SHOVEL", state, world)
    },
    "File Cabinet Key - Laundry Room": {
        LOCATION_ID_KEY: get_room_location_id("Laundry Room", 0),
        LOCATION_ROOM_KEY: "Laundry Room",
        LOCATION_ITEM_KEY: "CABINET KEY 2",
        LOCATION_RULE: lambda state, world: can_reach_item_location("SHOVEL", state, world)
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
    },
    "Entrance Hall West Vase": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall", 9),
        LOCATION_ROOM_KEY: "Entrance Hall",
    },
    "Cursed Coffers": {
        LOCATION_ID_KEY: get_room_location_id("Shrine", 0),
        LOCATION_ROOM_KEY: "Shrine",
        # LOCATION_RULE: lambda state, world: state.has("Gift Shop - Cursed Coffers Purchased", world.player)
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
        LOCATION_RULE: lambda state, world: can_reach_item_location("Burning Glass", state, world) or can_reach_item_location("TORCH", state, world)
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
        LOCATION_RULE: lambda state, world: state.can_reach_region("Shrine", world.player) and can_reach_item_location("SLEDGE HAMMER", state, world)
    },
    # Ignoring deposit box allowance tokens for now, since they are missable (don't respawn if not picked up)
}

# TODO-1 add locations for other stuff later.
# Chapel Keeper
# Alzara Prophecies

# Treasure Map Chests? (Might need to pre-calculate min piece counts for chest locations)
# Bedroom Treasure Map Chest

# Mirror Room Floorplan Duplicates?

locations = trophies | safes_and_small_gates | mora_jia_boxes | floorplans | shop_items | upgrade_disks | keys | misc_locations | item_pickups | workshop_contraptions
    
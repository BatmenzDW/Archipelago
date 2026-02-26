from BaseClasses import ItemClassification

from .constants import *
from .data_rooms import rooms, core_rooms, room_layout_lists
from .locations import ROOM_MULTIPLIER

def get_room_location_id(room_name: str) -> int:
    return rooms[room_name][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER

trophies = {
    "Full House Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 0,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: state.count_from_list([x for x in room_layout_lists[INNER_ROOM_KEY] if x not in core_rooms], world.player) >= 43
    },
    "Trophy of Invention": {
        LOCATION_ID_KEY: get_room_location_id("Workshop") + 0,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_RULE: lambda state, world: state.has_all([
                "Burning Glass",
                "Detector Shovel",
                "Dowsing Rod",
                "Electromagnet",
                "Jack Hammer",
                "Lucky Purse",
                "Pick Sound Amplifier",
                "Power Hammer",
            ], world.player
        )
    },
    "Trophy of Drafting": {
        LOCATION_ID_KEY: get_room_location_id("Mail Room") + 0,
        LOCATION_ROOM_KEY: "Mail Room",
        LOCATION_RULE: lambda state, world: [x for x in rooms if rooms[x][ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_D and not rooms[x][OUTER_ROOM_KEY] and x not in core_rooms and state.can_reach_region(x, world.player)].count() >= 20,
    },
    "Trophy of Wealth": {
        LOCATION_ID_KEY: get_room_location_id("Showroom") + 0,
        LOCATION_ROOM_KEY: "Showroom",
    },
    "Inheritance Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Room 46") + 0,
        LOCATION_ROOM_KEY: "Room 46",
    },
    "Bullesye Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Billiard Room") + 0,
        LOCATION_ROOM_KEY: "Billiard Room",
    },
    "A Logical Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Parlor") + 0,
        LOCATION_ROOM_KEY: "Parlor",
    },
    "Trophy 8": {
        LOCATION_ID_KEY: get_room_location_id("Room 8") + 0,
        LOCATION_ROOM_KEY: "Room 8",
    },
    "Explorer's Trophy": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 1,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: state.has_all(rooms.keys(), world.player)
    },
    "Trophy of Sigils": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 2,
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
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 3,
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
        LOCATION_ID_KEY: get_room_location_id("Boudoir") + 0,
        LOCATION_ROOM_KEY: "Boudoir",
    },
    "Drafting Studio Safe": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 0,
        LOCATION_ROOM_KEY: "Drafting Studio",
        LOCATION_RULE: lambda state, world: state.has("MAGNIFYING GLASS")
    },
    "Drawing Room Safe": {
        LOCATION_ID_KEY: get_room_location_id("Drawing Room") + 0,
        LOCATION_ROOM_KEY: "Drawing Room",
    },
    "Office Safe": {
        LOCATION_ID_KEY: get_room_location_id("Office") + 0,
        LOCATION_ROOM_KEY: "Office",
    },
    "Study Safe": {
        LOCATION_ID_KEY: get_room_location_id("Study") + 0,
        LOCATION_ROOM_KEY: "Study",
    },
    "Underpass Gate": {
        LOCATION_ID_KEY: get_room_location_id("Underpass") + 0,
        LOCATION_ROOM_KEY: "Underpass",
        LOCATION_RULE: lambda state, world: state.can_reach_region("Boiler Room", world.player)
    },
    "Shelter Safe": {
        LOCATION_ID_KEY: get_room_location_id("Shelter") + 0,
        LOCATION_ROOM_KEY: "Shelter",
    },
    "Orchard Gate": {
        LOCATION_ID_KEY: get_room_location_id("Campsite") + 0,
        LOCATION_ROOM_KEY: "Campsite",
    }
}

aries_court_moria_jia_boxes = {
    f"Aries Court Moria Jia Box {n}": {
        LOCATION_ID_KEY: get_room_location_id("Aries Court") + n - 1,
        LOCATION_ROOM_KEY: "Aries Court",
    } for n in range(1, 9)
}

moria_jia_boxes = {
    "Master Bedroom Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Master Bedroom") + 0,
        LOCATION_ROOM_KEY: "Master Bedroom",
    },
    "Closed Exhbit Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Closed Exhibit") + 0,
        LOCATION_ROOM_KEY: "Closed Exhibit",
    },
    "Underpass Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Underpass") + 0,
        LOCATION_ROOM_KEY: "Underpass",
    },
    "Tomb Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Tomb") + 0,
        LOCATION_ROOM_KEY: "Tomb",
    },
    "Trading Post Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post") + 0,
        LOCATION_ROOM_KEY: "Trading Post",
    },
    "Tunnel Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Tunnel") + 0,
        LOCATION_ROOM_KEY: "Tunnel",
    },
    "Solaium Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Solarium") + 0,
        LOCATION_ROOM_KEY: "Solarium",
    },
    "Lost And Found Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Lost And Found") + 0,
        LOCATION_ROOM_KEY: "Lost And Found",
    },
    "Throne of the Blue Prince Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Throne Room") + 0,
        LOCATION_ROOM_KEY: "Throne Room",
        LOCATION_RULE: lambda state, world: state.has_all([
            "CROWN",
            "ROYAL SCEPTER",
            "CURSED EFFIGY",
        ], world.player),
    },
    "Arch Aries Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Arch Aries Sanctum") + 0,
        LOCATION_ROOM_KEY: "Arch Aries Sanctum",
    },
    "Corarica Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Corarica Sanctum") + 0,
        LOCATION_ROOM_KEY: "Corarica Sanctum",
    },
    "Eraja Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Eraja Sanctum") + 0,
        LOCATION_ROOM_KEY: "Eraja Sanctum",
    },
    "Fenn Aries Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Fenn Aries Sanctum") + 0,
        LOCATION_ROOM_KEY: "Fenn Aries Sanctum",
    },
    "Mora Jai Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Mora Jai Sanctum") + 0,
        LOCATION_ROOM_KEY: "Mora Jai Sanctum",
    },
    "Orinda Aries Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Orinda Aries Sanctum") + 0,
        LOCATION_ROOM_KEY: "Orinda Aries Sanctum",
    },
    "Verra Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Verra Sanctum") + 0,
        LOCATION_ROOM_KEY: "Verra Sanctum",
    },
    "Nuance Sanctum Moria Jia Box": {
        LOCATION_ID_KEY: get_room_location_id("Nuance Sanctum") + 0,
        LOCATION_ROOM_KEY: "Nuance Sanctum",
    }
} | aries_court_moria_jia_boxes
# not adding atelier boxes, since they are bascially already at the latest goal

drafting_studio_additions = {
    "Dovecote Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 1,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "The Kennel Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 2,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Clock Tower Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 3,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Classroom Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 4,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Solarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 5,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Dormitory Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 6,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Vestibule Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 7,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
    "Casino Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Drafting Studio") + 8,
        LOCATION_ROOM_KEY: "Drafting Studio",
    },
}

found_floorplans = {
    "Planetarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Observatory") + 0,
        LOCATION_ROOM_KEY: "Observatory",
    },
    "Mechanarium Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Rotating Gear") + 0,
        LOCATION_ROOM_KEY: "Rotating Gear",
    },
    "Treasure Trove Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Underpass") + 0,
        LOCATION_ROOM_KEY: "Underpass",
        LOCATION_RULE: lambda state, world: state.can_reach_region("Boiler Room", world.player)
    },
    "Throne Room Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Orindian Ruins") + 0,
        LOCATION_ROOM_KEY: "Orindian Ruins",
    },
    "Tunnel Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Tunnel Area Past Crates") + 0,
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
    },
    "Conservatory Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Campsite") + 1,
        LOCATION_ROOM_KEY: "Campsite",
    },
    "Lost And Found Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Basement") + 0,
        LOCATION_ROOM_KEY: "Basement",
    },
    "Closed Exhibit Floorplan": {
        LOCATION_ID_KEY: get_room_location_id("Study") + 1,
        LOCATION_ROOM_KEY: "Study",
    }
}

floorplans = drafting_studio_additions | found_floorplans

gift_shop_items = {
    "Gift Shop - Mt. Holly Tee": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop") + 0,
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Lunch Box": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop") + 1,
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Swim Trunks": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop") + 2,
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Swim Bird Plushie": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop") + 3,
        LOCATION_ROOM_KEY: "Gift Shop",
    },
    "Gift Shop - Blue Tents": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop") + 4,
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_RULE: lambda state, world: [state.can_reach_location(loc, world.player) for loc in trophies.keys()].count() >= 8
    },
    "Gift Shop - Cursed Coffers": {
        LOCATION_ID_KEY: get_room_location_id("Gift Shop") + 5,
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in ["Library", "Shrine"]),
    }
}

bookshop_items = {
    "Bookshop - The History of Orindia (1st ed.) ": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop") + 0,
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - A New Clue": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop") + 1,
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - The Curse of Black Bridge": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop") + 2,
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Realm & Rune": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop") + 3,
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 4": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop") + 4,
        LOCATION_ROOM_KEY: "Bookshop",
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 5": {
        LOCATION_ID_KEY: get_room_location_id("Bookshop") + 5,
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

other_item_pickup = {
    "BATTERY PACK First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite") + 2, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
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
        or (state.can_reach_region("Trading Post", world.player) and any(state.has(item, world.player) for item in TRADING_POST_TIER1[TRADING_POST_GIVE]))
        #
        # These check is redundant. Leaving them here to document all spawn locations. 
        #
        # or (state.has("CAR KEYS", world.player) and state.can_reach_region("Garage", world.player)) 
        # or (state.can_reach_region("Darkroom", world.player) and state.can_reach_region("Utility Closet", world.player))
        #
        # Also spawns in Spare Patio, but we aren't adding upgraded rooms seperately atm.
    },
    "BROKEN LEVER First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite") + 3, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
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
        or state.has("SHOVEL", world.player) or state.has("Detector Shovel", world.player) or state.has("Jack Hammer", world.player)
        #
        # This check is redundant. Leaving it here to document all spawn locations. 
        #
        # or (state.can_reach_region("Darkroom", world.player) and state.can_reach_region("Utility Closet", world.player))
        #
        # Also spawns in Spare Greenroom, but we aren't adding upgraded rooms seperately atm.
    },
    "COIN PURSE First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite") + 4, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Closet",
            "Walk-in Closet",
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
        or (state.can_reach_region("Lavatory", world.player) and state.can_reach_region("Shelter", world.player))
        # Also spawns in Her Ladyship's Spare Room and Spare Master Bedroom, but we aren't adding upgraded rooms seperately atm.
    },
    "COMPASS First Pickup": {
        LOCATION_ID_KEY: get_room_location_id("Campsite") + 5, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_RULE: lambda state, world: any(state.can_reach_region(region, world.player) for region in [
            "Aquarium",
            "Attic",
            "Cloister",
            "Closet",
            "Drafting Studio",
            "Observatory",
            "Terrace",
            "Walk-in Closet",
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
        LOCATION_ID_KEY: get_room_location_id("Campsite") + 6, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
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
            "Walk-in Closet",
            "Morning Room",
            "Den",
            "Pantry",
        ]) or (state.has("Satellite Raised", world.player) and state.can_reach_region("Laboratory", world.player))
    }
}

upgrade_disks = {
    "Upgrade Disk - Offic": {
        LOCATION_ID_KEY: get_room_location_id("Office") + 1,
        LOCATION_ROOM_KEY: "Office",
    },
    "Upgrade Disk - Morning Room": {
        LOCATION_ID_KEY: get_room_location_id("Morning Room") + 0,
        LOCATION_ROOM_KEY: "Morning Room",
    },
    "Upgrade Disk - Her Ladyship's Chambers": {
        LOCATION_ID_KEY: get_room_location_id("Her Ladyship's Chambers") + 0,
        LOCATION_ROOM_KEY: "Her Ladyship's Chambers",
    },
    "Upgrade Disk - Commissary": {
        LOCATION_ID_KEY: get_room_location_id("Commissary") + 0,
        LOCATION_ROOM_KEY: "Commissary",
    },
    "Upgrade Disk - Garage": {
        LOCATION_ID_KEY: get_room_location_id("Garage") + 0,
        LOCATION_ROOM_KEY: "Garage",
    },
    "Upgrade Disk - Great Hall": {
        LOCATION_ID_KEY: get_room_location_id("Great Hall") + 0,
        LOCATION_ROOM_KEY: "Great Hall",
    },
    "Upgrade Disk - Vault": {
        LOCATION_ID_KEY: get_room_location_id("Vault") + 0,
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_RULE: lambda state, world: state.has("VAULT KEY 304", world.player)
    },
    "Upgrade Disk - Trading Post Dynamite": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post") + 0,
        LOCATION_ROOM_KEY: "Trading Post",
        LOCATION_RULE: lambda state, world: state.has_any(["Burning Glass", "TORCH"], world.player),
    },
    "Upgrade Disk - Freezer": {
        LOCATION_ID_KEY: get_room_location_id("Freezer") + 0,
        LOCATION_ROOM_KEY: "Freezer",
        LOCATION_RULE: lambda state, world: state.has_any([
                "Burning Glass",
                "TORCH",
                "Power Hammer",
        ], world.player) or state.can_reach_region("Furnace", world.player)
    },
    "Upgrade Disk - Tomb": {
        LOCATION_ID_KEY: get_room_location_id("Tomb") + 0,
        LOCATION_ROOM_KEY: "Tomb",
    },
    "Upgrade Disk - The Foundation": {
        LOCATION_ID_KEY: get_room_location_id("The Foundation") + 0,
        LOCATION_ROOM_KEY: "The Foundation",
    },
    "Upgrade Disk - Abandoned Mine": {
        LOCATION_ID_KEY: get_room_location_id("Abandoned Mine") + 0,
        LOCATION_ROOM_KEY: "Abandoned Mine",
    },
    "Upgrade Disk - Lost And Found": {
        LOCATION_ID_KEY: get_room_location_id("Lost And Found") + 0,
        LOCATION_ROOM_KEY: "Lost And Found",
    },
    "Upgrade Disk - Mechanarium": {
        LOCATION_ID_KEY: get_room_location_id("Mechanarium") + 0,
        LOCATION_ROOM_KEY: "Mechanarium",
    },
    "Upgrade Disk - Archives": {
        LOCATION_ID_KEY: get_room_location_id("Archives") + 0,
        LOCATION_ROOM_KEY: "Archives",
        LOCATION_RULE: lambda state, world: state.has("CABINET KEY 1", world.player)
    },
    "Upgrade Disk - Trading Post Trade": {
        LOCATION_ID_KEY: get_room_location_id("Trading Post") + 1,
        LOCATION_ROOM_KEY: "Trading Post",
    },
}

vault_keys = {
    "Vault Key 149": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 4, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: state.has_any([
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Satellite Raised"
        ], world.player) or any(state.can_reach_region(x, world.player) for x in [
            "Attic", 
            "Rumpus Room", 
            "Security", 
            "Trophy Room", 
            "Locker Room",
        ])
    },
    "Vault Key 233": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 5, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: state.has_any([
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Locker Room", 
            "Satellite Raised"
        ], world.player) or any(x for x in [
            "Office",
            "Sauna",
            "Wine Cellar",
            "Lavatory",
            "Morning Room",
        ] if state.can_reach_region(x, world.player))
        or (state.can_reach_region("Lavatory", world.player) and state.can_reach_region("Shelter", world.player))
    },
    "Vault Key 304": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 6, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: state.has_any([
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Locker Room", 
            "Satellite Raised"
        ], world.player) or any(state.can_reach_region(x, world.player) for x in [
            "Conference Room",
            "Her Ladyship's Chambers",
            "Walk-in Closet",
            "Hovel",
            "Spare Room",
            "Drawing Room",
        ])
    },
    "Vault Key 370": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 7, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE: lambda state, world: state.has_any([
            "SHOVEL", 
            "Detector Shovel", 
            "Jack Hammer", 
            "Locker Room", 
            "Satellite Raised"
        ], world.player) or state.can_reach_region("Lost And Found", world.player)
    }
}

sanctum_keys = {
    "Sanctum Key - Room 46": {
        LOCATION_ID_KEY: get_room_location_id("Room 46") + 5,
        LOCATION_ROOM_KEY: "Room 46",
    },
    "Sanctum Key - Vault": {
        LOCATION_ID_KEY: get_room_location_id("Vault") + 1,
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_RULE: lambda state, world: state.has("VAULT KEY 370", world.player)
    },
    "Sanctum Key - Clock Tower": {
        LOCATION_ID_KEY: get_room_location_id("Clock Tower") + 0,
        LOCATION_ROOM_KEY: "Clock Tower",
    },
    "Sanctum Key - Reservoir Bottom": {
        LOCATION_ID_KEY: get_room_location_id("Reservoir Bottom") + 0,
        LOCATION_ROOM_KEY: "Reservoir Bottom",
    },
    "Sanctum Key - Throne Room": {
        LOCATION_ID_KEY: get_room_location_id("Throne Room") + 1,
        LOCATION_ROOM_KEY: "Throne Room",
    },
    "Sanctum Key - Safehouse": {
        LOCATION_ID_KEY: get_room_location_id("Safehouse") + 0,
        LOCATION_ROOM_KEY: "Safehouse",
    },
    "Sanctum Key - Music Room": {
        LOCATION_ID_KEY: get_room_location_id("Music Room") + 0,
        LOCATION_ROOM_KEY: "Music Room",
    },
    "Sanctum Key - Mechanarium": {
        LOCATION_ID_KEY: get_room_location_id("Mechanarium") + 1,
        LOCATION_ROOM_KEY: "Mechanarium",
    }
}

file_cabinet_keys = {
    "File Cabinet Key - Patio": {
        LOCATION_ID_KEY: get_room_location_id("Patio") + 0,
        LOCATION_ROOM_KEY: "Patio",
    },
    "File Cabinet Key - Laundry Room": {
        LOCATION_ID_KEY: get_room_location_id("Laundry Room") + 0,
        LOCATION_ROOM_KEY: "Laundry Room",
    },
    "File Cabinet Key - Tunnel Area Past Crates": {
        LOCATION_ID_KEY: get_room_location_id("Tunnel Area Past Crates") + 1,
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
    },
}

keys = vault_keys | sanctum_keys | file_cabinet_keys

misc_locations = {
    "Entrance Hall East Vase": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 8,
        LOCATION_ROOM_KEY: "Entrance Hall",
    },
    "Entrance Hall West Vase": {
        LOCATION_ID_KEY: get_room_location_id("Entrance Hall") + 9,
        LOCATION_ROOM_KEY: "Entrance Hall",
    },
    "Cursed Coffers": {
        LOCATION_ID_KEY: get_room_location_id("Shrine") + 0,
        LOCATION_ROOM_KEY: "Shrine",
        LOCATION_RULE: lambda state, world: state.has("Gift Shop - Cursed Coffers Purchased", world.player)
    },
    "Gasline Valve - Orchard": {
        LOCATION_ID_KEY: get_room_location_id("Apple Orchard") + 0,
        LOCATION_ROOM_KEY: "Apple Orchard",
    },
    "Gasline Valve - Schoolhouse": {
        LOCATION_ID_KEY: get_room_location_id("Schoolhouse") + 0,
        LOCATION_ROOM_KEY: "Schoolhouse",
    },
    "Gasline Valve - Hovel": {
        LOCATION_ID_KEY: get_room_location_id("Hovel") + 0,
        LOCATION_ROOM_KEY: "Hovel",
    },
    "Gasline Valve - Gemstone Cavern": {
        LOCATION_ID_KEY: get_room_location_id("Gemstone Cavern") + 0,
        LOCATION_ROOM_KEY: "Gemstone Cavern",
    },
    "Sundial": {
        LOCATION_ID_KEY: get_room_location_id("Apple Orchard") + 1,
        LOCATION_ROOM_KEY: "Apple Orchard",
        LOCATION_RULE: lambda state, world: state.has_any([
            "Burning Glass",
            "TORCH",
        ], world.player),
    },
    "VAC Controls": {
        LOCATION_ID_KEY: get_room_location_id("Utility Closet") + 0,
        LOCATION_ROOM_KEY: "Utility Closet",
    },
    # Almost all of the other Allowance Tokens are directly behind/next to another location
    "Allowance Token - Cloister Statue": {
        LOCATION_ID_KEY: get_room_location_id("Cloister") + 0,
        LOCATION_ROOM_KEY: "Cloister",
    },
}

# TODO-1 add locations for other stuff later.
# Chapel Keeper
# Alzara Prophecies

# Unique key locations
# Unique/Semi-Unique item locations

# Mirror Room Floorplan Duplicates?

other_locations = trophies | safes_and_small_gates | moria_jia_boxes | floorplans | shop_items | upgrade_disks | keys | misc_locations
    
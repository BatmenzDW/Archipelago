from BaseClasses import CollectionState, ItemClassification
from rule_builder.rules import *

from .constants import *
from .data_rooms import rooms, core_rooms, classrooms, room_layout_lists, all_areas
from .data_items import *
from .rules import *
from .options import GoalType

directory_rooms = [x for x in rooms if x not in core_rooms and x not in ["Secret Garden", "Room 8"] and x not in classrooms] + ["Progressive Classroom"]

# Not implemented, but all are controlled by trophy sanity
trophies = {
    "Full House Trophy": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: HasFromList(*(directory_rooms + ["SECRET GARDEN KEY", "KEY 8"]), count=43)
    },
    "Trophy of Invention": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("Burning Glass") & CanReachItemLocation("Detector Shovel") & CanReachItemLocation("Dowsing Rod") & CanReachItemLocation("Electromagnet") & CanReachItemLocation("Jack Hammer") & CanReachItemLocation("Lucky Purse") & CanReachItemLocation("Pick Sound Amplifier") & CanReachItemLocation("Power Hammer"),
    },
    "Trophy of Drafting": {
        LOCATION_ID_KEY: all_areas["Mail Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Mail Room",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegionsFromList(*[x for x in rooms if rooms[x][ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_D and not rooms[x][OUTER_ROOM_KEY] and x not in core_rooms and x not in ["Mechanarium"]], count=20), # Mechanarium is a dead end for pathing, but doesn't count for the trophy
    },
    "Trophy of Wealth": {
        LOCATION_ID_KEY: all_areas["Showroom"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Showroom",
    },
    "Inheritance Trophy": {
        LOCATION_ID_KEY: all_areas["Room 46"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Room 46",
    },
    "Bullseye Trophy": {
        LOCATION_ID_KEY: all_areas["Billiard Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Billiard Room",
    },
    "A Logical Trophy": {
        LOCATION_ID_KEY: all_areas["Parlor"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Parlor",
    },
    "Trophy 8": {
        LOCATION_ID_KEY: all_areas["Room 8"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Room 8",
    },
    "Explorer's Trophy": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON:  CanReachRegionsFromList(*[x for x in room_layout_lists[INNER_ROOM_KEY] if x not in core_rooms], count=(len(room_layout_lists[INNER_ROOM_KEY]) - len(core_rooms))),
    },
    "Trophy of Sigils": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Orinda Aries Sanctum") & CanReachRegion("Fenn Aries Sanctum") & CanReachRegion("Arch Aries Sanctum") & CanReachRegion("Eraja Sanctum") & CanReachRegion("Corarica Sanctum") & CanReachRegion("Mora Jai Sanctum") & CanReachRegion("Verra Sanctum") & CanReachRegion("Nuance Sanctum"),
    },
    "Diploma Trophy": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 3,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: Has("Progressive Classroom", count=9),
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
        LOCATION_ID_KEY: all_areas["Boudoir"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Boudoir",
    },
    "Drafting Studio Safe": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Drafting Studio",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("MAGNIFYING GLASS"),
    },
    "Drawing Room Safe": {
        LOCATION_ID_KEY: all_areas["Drawing Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Drawing Room",
    },
    "Office Safe": {
        LOCATION_ID_KEY: all_areas["Office"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Office",
    },
    "Study Safe": {
        LOCATION_ID_KEY: all_areas["Study"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Study",
    },
    "Underpass Gate": {
        LOCATION_ID_KEY: all_areas["The Underpass"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "The Underpass",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Boiler Room"),
        # lambda state, world: state.can_reach_region("Boiler Room", world.player) and can_reach_with_dares(world, "Boiler Room", "Region")
    },
    "Shelter Safe": {
        LOCATION_ID_KEY: all_areas["Shelter"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Shelter",
    },
    "Orchard Gate": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Campsite",
    }
}

aries_court_mora_jai_boxes = {
    f"Aries Court Mora Jai Box {n}": {
        LOCATION_ID_KEY: all_areas["Aries Court"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + n,
        LOCATION_ROOM_KEY: "Aries Court",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    } for n in range(1, 9)
}

mora_jai_boxes = {
    "Master Bedroom Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Master Bedroom"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Master Bedroom",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Closed Exhibit Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Closed Exhibit"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Closed Exhibit",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Underpass Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["The Underpass"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "The Underpass",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Tomb Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Tomb"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Tomb",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("Burning Glass"),
            CanReachItemLocation("TORCH")
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Trading Post Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Trading Post"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Trading Post",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Tunnel Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Tunnel"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Tunnel",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Solarium Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Solarium"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Solarium",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Lost & Found Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Lost & Found"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Lost & Found",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Throne of the Blue Prince Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Throne Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Throne Room",
        LOCATION_RULE_SIMPLE_COMMON: Has("Ascend The Throne", options=[OptionFilter(GoalType, GoalType.option_blueprints, "ge")]),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Arch Aries Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Arch Aries Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Arch Aries Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Corarica Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Corarica Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Corarica Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Eraja Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Eraja Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Eraja Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Fenn Aries Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Fenn Aries Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Fenn Aries Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Mora Jai Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Mora Jai Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Mora Jai Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Orinda Aries Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Orinda Aries Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Orinda Aries Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Verra Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Verra Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Verra Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Nuance Sanctum Mora Jai Box": {
        LOCATION_ID_KEY: all_areas["Nuance Sanctum"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Nuance Sanctum",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    }
} | aries_court_mora_jai_boxes
# not adding atelier boxes, since they are basically already at the latest goal

drafting_studio_additions = {
    "Dovecote Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Dovecote"
    },
    "Kennel Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "The Kennel"
    },
    "Clock Tower Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 3,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Clock Tower"
    },
    "Classroom Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 4,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Classroom Exam"
    },
    "Solarium Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 5,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Solarium"
    },
    "Dormitory Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 6,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Dormitory"
    },
    "Vestibule Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 7,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Vestibule"
    },
    "Casino Floorplan": {
        LOCATION_ID_KEY: all_areas["Drafting Studio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 8,
        LOCATION_ROOM_KEY: "Drafting Studio",
        NONSANITY_LOCATION_KEY: "Casino"
    },
}

found_floorplans = {
    "Planetarium Floorplan": {
        LOCATION_ID_KEY: all_areas["Observatory"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Observatory",
        NONSANITY_LOCATION_KEY: "Planetarium"
    },
    "Mechanarium Floorplan": {
        LOCATION_ID_KEY: all_areas["Rotating Gear"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Rotating Gear",
        NONSANITY_LOCATION_KEY: "Mechanarium"
    },
    "Treasure Trove Floorplan": {
        LOCATION_ID_KEY: all_areas["The Underpass"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "The Underpass",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Boiler Room"),
        # lambda state, world: state.can_reach_region("Boiler Room", world.player) and can_reach_with_dares(world, "Boiler Room", "Region"),
        NONSANITY_LOCATION_KEY: "Treasure Trove"
    },
    "Throne Room Floorplan": {
        LOCATION_ID_KEY: all_areas["Orindian Ruins"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Orindian Ruins",
        NONSANITY_LOCATION_KEY: "Throne Room"
    },
    "Tunnel Floorplan": {
        LOCATION_ID_KEY: all_areas["Tunnel Area Past Crates"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
        NONSANITY_LOCATION_KEY: "Tunnel"
    },
    "Conservatory Floorplan": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Campsite",
        NONSANITY_LOCATION_KEY: "Conservatory",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("SHOVEL"),
    },
    "Lost And Found Floorplan": {
        LOCATION_ID_KEY: all_areas["Basement"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Basement",
        NONSANITY_LOCATION_KEY: "Lost & Found",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("SHOVEL"),
    },
    "Closed Exhibit Floorplan": {
        LOCATION_ID_KEY: all_areas["Study"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Study",
        NONSANITY_LOCATION_KEY: "Closed Exhibit"
    }
}

floorplans = drafting_studio_additions | found_floorplans

gift_shop_items = {
    "Gift Shop - Mt. Holly Tee": {
        LOCATION_ID_KEY: all_areas["Gift Shop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Gift Shop",
        NONSANITY_LOCATION_KEY: "Mt. Holly Tee",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Gift Shop - Lunch Box": {
        LOCATION_ID_KEY: all_areas["Gift Shop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Gift Shop",
        NONSANITY_LOCATION_KEY: "Lunch Box",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Gift Shop - Swim Trunks": {
        LOCATION_ID_KEY: all_areas["Gift Shop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Gift Shop",
        NONSANITY_LOCATION_KEY: "Swim Trunks",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Gift Shop - Swim Bird Plushie": {
        LOCATION_ID_KEY: all_areas["Gift Shop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 3,
        LOCATION_ROOM_KEY: "Gift Shop",
        NONSANITY_LOCATION_KEY: "Swim Bird Plushie",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Gift Shop - Blue Tents": {
        LOCATION_ID_KEY: all_areas["Gift Shop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 4,
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_RULE_SIMPLE_COMMON: CanReachAllLocations(*[t for t in trophies]),
        NONSANITY_LOCATION_KEY: "Blue Tents",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Gift Shop - Cursed Coffers": {
        LOCATION_ID_KEY: all_areas["Gift Shop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 5,
        LOCATION_ROOM_KEY: "Gift Shop",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Shrine") | (Has("The Curse of Black Bridge") & CanReachRegion("Library")),
        NONSANITY_LOCATION_KEY: "Cursed Coffers",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    }
}

bookshop_items = {
    "Bookshop - The History of Orindia (1st ed.)": {
        LOCATION_ID_KEY: all_areas["Bookshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Bookshop",
        NONSANITY_LOCATION_KEY: "History of Orindia (1st ed.)",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Bookshop - A New Clue": {
        LOCATION_ID_KEY: all_areas["Bookshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Bookshop",
        NONSANITY_LOCATION_KEY: "A New Clue",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Bookshop - The Curse of Black Bridge": {
        LOCATION_ID_KEY: all_areas["Bookshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Bookshop",
        NONSANITY_LOCATION_KEY: "The Curse of Black Bridge",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Bookshop - Realm & Rune": {
        LOCATION_ID_KEY: all_areas["Bookshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 3,
        LOCATION_ROOM_KEY: "Bookshop",
        NONSANITY_LOCATION_KEY: "Realm & Rune",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 4": {
        LOCATION_ID_KEY: all_areas["Bookshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 4,
        LOCATION_ROOM_KEY: "Bookshop",
        NONSANITY_LOCATION_KEY: "Drafting Strategy: Architectural Digest Vol. 4",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Bookshop - Drafting Strategy: Architectural Digest Vol. 5": {
        LOCATION_ID_KEY: all_areas["Bookshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 5,
        LOCATION_ROOM_KEY: "Bookshop",
        NONSANITY_LOCATION_KEY: "Drafting Strategy: Architectural Digest Vol. 5",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
}

shop_items = gift_shop_items | bookshop_items

# I ignored Cloister upgrades for now, but they should probably be checked eventually, since some of them would be a break in logic for item pickups

standard_item_pickup = {
    "BATTERY PACK First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BATTERY PACK",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
                "Toolshed",
                "Hovel",
            ]], 
            MechanariumDoorRule(3)
        ) | Or(
            *[CanReachItemLocation(item) for item in [
                "Spare Room",
                "Garage",
                "Utility Closet",
                "Kitchen",
            ]],
            options=rare_logic_filter
        ) | Or(
            DarkRoomRule(),
            CarTrunkRule(),
            options=complex_logic_filter
        ) | Or(
            AdvancedExperimentRule(),
            TradingPostRule("BATTERY PACK"),
            UpgradedRoomRule("Patio", "Spare Patio"),
            options=extreme_logic_filter
        ),
        
    },
    "BROKEN LEVER First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 3, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BROKEN LEVER",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | Or(
            *[CanReachRegion(region) for region in [
                "Spare Room",
                "Billiard Room",
                "Garage",
                "Utility Closet",
                "Kitchen",
            ]],
            DigSpotRule(),
            options=rare_logic_filter
        ) | DarkRoomRule() | AdvancedExperimentRule() | UpgradedRoomRule("Spare Room", "Spare Greenroom"),
        
    },
    "COIN PURSE First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 4, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "COIN PURSE",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Closet",
                "Walk-In Closet",
                "Parlor",
                "Attic",
                "Workshop",
                "Dining Room",
                "Bedroom",
                "Mail Room", # Packages
            ]]
        ) | Or(
            *[CanReachRegion(region) for region in [
                "Gallery",
                "Ballroom",
                "Drawing Room",
            ]],
            options=rare_logic_filter
        ) | LavatoryRule() | AdvancedExperimentRule() | UpgradedRoomRule("Spare Room", "Her Ladyship's Spare Room") | UpgradedRoomRule("Spare Room", "Spare Master Bedroom"),
        
    },
    "COMPASS First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 5, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "COMPASS",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | Or(
            CanReachRegion("Den"), CanReachRegion("Trophy Room"),
            options=rare_logic_filter
        ) | TrunkRule() | AdvancedExperimentRule() | UpgradedRoomRule("Spare Room", "Her Ladyship's Spare Room") | UpgradedRoomRule("Spare Room", "Spare Master Bedroom") | UpgradedRoomRule("Spare Room", "Spare Terrace"),
        
    },
    "COUPON BOOK First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 6, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | Or(
            CanReachRegion("Den"), CanReachRegion("Pantry"),
            options=rare_logic_filter
        ) | AdvancedExperimentRule(),
        
    },
    "GEAR WRENCH First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 7, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "GEAR WRENCH",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachRegion("Toolshed"), CanReachRegion("Lost & Found"),
        ) | AdvancedExperimentRule() | SpiralOfStarsRule(),
        
    },
    "HALL PASS First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 8, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "HALL PASS",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
                "Lost & Found",
            ]]
        ) | AdvancedExperimentRule() | SpiralOfStarsRule(),
        
    },
    "LOCK PICK KIT First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 9, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "LOCK PICK KIT",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | CanReachRegion("Garage", options=rare_logic_filter) |
        TrunkRule() | CarTrunkRule() | DarkRoomRule() |
        AdvancedExperimentRule() | UpgradedRoomRule("Spare Room", "Servant's Spare Quarters") | UpgradedRoomRule("Spare Room", "Her Ladyship's Spare Room") | UpgradedRoomRule("Spare Room", "Spare Master Bedroom") | UpgradedRoomRule("Spare Room", "Spare Bedroom"),
        
    },
    "LUCKY RABBIT'S FOOT First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 10, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "LUCKY RABBIT'S FOOT",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Closet",
                "Walk-In Closet",
                "Rumpus Room",
                "Nursery",
                "Morning Room",
                "Throne Room",
                "Lost & Found",
            ]]
        ) | Or(
            CanReachRegion("Gallery"), CanReachRegion("Den"), CanReachRegion("Ballroom"),
            options=rare_logic_filter
        ) | LavatoryRule() | AdvancedExperimentRule() | UpgradedRoomRule("Spare Room", "Her Ladyship's Spare Room") | UpgradedRoomRule("Spare Room", "Spare Bedroom") | UpgradedRoomRule("Spare Room", "Spare Servant's Quarters"),
        
    },
    "MAGNIFYING GLASS First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 11, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "MAGNIFYING GLASS",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Archives",
                "Attic",
                "Boudoir",
                "Chapel",
                "Courtyard",
                "Drafting Studio",
                "Guest Bedroom",
                "Her Ladyship's Chamber",
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
            ]]
        ) | Or(
            CanReachRegion("Den"), CanReachRegion("Drawing Room"),
            options=rare_logic_filter
        ) | CarTrunkRule() | AdvancedExperimentRule() | UpgradedRoomRule("Spare Room", "Spare Foyer"),
        
    },
    "METAL DETECTOR First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 12, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "METAL DETECTOR",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Archives",
                "Attic",
                "Closet",
                "Courtyard",
                "Greenhouse",
                "Maid's Chamber",
                "Mail Room",
                "Patio",
                "Veranda",
                "Workshop",
                "Secret Garden",
                "Clock Tower",
                "Toolshed",
                "Commissary",
            ]]
        ) | Or(
            CanReachRegion("Garage"), CanReachRegion("Boiler Room"),
            options=rare_logic_filter
        ) | AdvancedExperimentRule() | UpgradedRoomRule("Spare Room", "Spare Patio") | UpgradedRoomRule("Spare Room", "Spare Veranda"),
        
    },
    "REPELLENT First Pickup": {
        LOCATION_ID_KEY: all_areas["Lost & Found"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Lost & Found",
        LOCATION_ITEM_KEY: "REPELLENT",
        
    },
    "RUNNING SHOES First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 14, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "RUNNING SHOES",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | CanReachRegion("Garage", options=rare_logic_filter) |
        AdvancedExperimentRule() | UpgradedRoomRule("Mail Room", "Freight Mail") | UpgradedRoomRule("Spare Room", "Spare Servant's Quarters"),
        
    },
    "SALT SHAKER First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 15, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SALT SHAKER",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Rumpus Room",
                "Walk-In Closet",
                "Billiard Room",
                "Dining Room",
                "Morning Room",
                "Commissary",
            ]]
        ) | Or(
            CanReachRegion("Pantry"), CanReachRegion("Kitchen"),
            options=rare_logic_filter
        ) | AdvancedExperimentRule() | TradingPostRule("SALT SHAKER") | SpiralOfStarsRule(),
        
    },
    "SHOVEL First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 16, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SHOVEL",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | Or(
            *[CanReachRegion(region) for region in [
                "Spare Room",
                "Garage",
                "Trophy Room",
                "Utility Closet",
                "Boiler Room",
            ]],
            options=rare_logic_filter
        ) | TradingPostRule("SHOVEL") | SpiralOfStarsRule() | # Also from AdvancedExperimentRule, but that requires SHOVEL
        UpgradedRoomRule("Mail Room", "Freight Mail") | UpgradedRoomRule("Spare Room", "Spare Greenroom") | UpgradedRoomRule("Spare Room", "Spare Patio") | UpgradedRoomRule("Spare Room", "Spare Veranda") | UpgradedRoomRule("Spare Room", "Spare Terrace"),
        
    },
    "SLEDGE HAMMER First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 17, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SLEDGE HAMMER",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | Or(
            *[CanReachRegion(region) for region in [
                "Spare Room",
                "Garage",
                "Music Room",
                "Trophy Room",
                "Utility Closet",
            ]],
            options=rare_logic_filter
        ) | AdvancedExperimentRule() | TradingPostRule("SLEDGE HAMMER") | SpiralOfStarsRule() | 
        UpgradedRoomRule("Mail Room", "Freight Mail") | UpgradedRoomRule("Spare Room", "Spare Foyer") | UpgradedRoomRule("Spare Room", "Spare Hall"),
        
    },
    "SLEEPING MASK First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 18, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SLEEPING MASK",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Bedroom",
                "Boudoir",
                "Closet",
                "Master Bedroom",
                "Sauna",
                "Walk-In Closet",
                "Commissary",
                "Mail Room", # Packages
            ]]
        ) | AdvancedExperimentRule() | SpiralOfStarsRule() | 
        UpgradedRoomRule("Spare Room", "Her Ladyship's Spare Room") | UpgradedRoomRule("Spare Room", "Spare Bedroom") | UpgradedRoomRule("Spare Room", "Spare Master Bedroom") | UpgradedRoomRule("Spare Room", "Spare Servant's Quarters"),
        
    },
    "STOPWATCH First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 19, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "STOPWATCH",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachRegion("Clock Tower"), CanReachRegion("Lost & Found")
        ) | And(
            CanReachItemLocation("Jack Hammer"), DigSpotRule(),
            options=rare_logic_filter
        ),
        
    },
    "TELESCOPE First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 20, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "TELESCOPE",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Her Ladyship's Chamber",
                "Walk-In Closet",
            ]]
        ) | AdvancedExperimentRule() | SpiralOfStarsRule() | 
        UpgradedRoomRule("Spare Room", "Her Ladyship's Spare Room"),
        
    },
    "TREASURE MAP First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 21, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "TREASURE MAP",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | Or(
            CanReachRegion("Den"), CanReachRegion("Trophy Room"),
            options=rare_logic_filter
        ) | TrunkRule() | CarTrunkRule() | LavatoryRule() |
        UpgradedRoomRule("Spare Room", "Spare Foyer") | UpgradedRoomRule("Spare Room", "Spare Secret Passage"),
        
    },
    "WATERING CAN First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 22, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "WATERING CAN",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachRegion("Greenhouse"), CanReachRegion("Toolshed"), CanReachRegion("Hovel"), CanReachRegion("Lost & Found")
        ) | AdvancedExperimentRule() | SpiralOfStarsRule() |
        UpgradedRoomRule("Spare Room", "Spare Greenroom") | UpgradedRoomRule("Spare Room", "Spare Patio") | UpgradedRoomRule("Spare Room", "Spare Veranda") | UpgradedRoomRule("Spare Room", "Spare Terrace"),
        
    },
}

special_key_pickup = {
    "BASEMENT KEY First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 30, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "BASEMENT KEY",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Antechamber") | SpiralOfStarsRule(),
        
    },
    "CAR KEYS First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 31, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "CAR KEYS",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
        ]]) | Or(
            CanReachRegion("Gallery"), CanReachRegion("Den"), CanReachRegion("Locksmith"),
            options=rare_logic_filter
        ) | TrunkRule() | AdvancedExperimentRule() | SpiralOfStarsRule() | 
        UpgradedRoomRule("Spare Room", "Spare Bedroom") | UpgradedRoomRule("Spare Room", "Spare Patio") | UpgradedRoomRule("Spare Room", "Spare Servant's Quarters"),
        
    },
    "KEY 8 First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 32, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "KEY 8",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachRegion("Gallery"), CanReachRegion("Lost & Found", options=complex_logic_filter), # Lost & Found: Day 365+
        ),
        
    },
    "KEYCARD First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 33, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "KEYCARD",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
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
            ]]
        ) | CarTrunkRule() | DarkRoomRule() | TrunkRule() | AdvancedExperimentRule(),
        
    },
    "PRISM KEY_0 First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 34, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "PRISM KEY_0",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachRegion("Music Room"), CanReachRegion("Lost & Found"), CanReachRegion("Locksmith")
        ) | And(
            CanReachRegion("Freezer"),
            Or(CanReachItemLocation("Burning Glass"), CanReachItemLocation("TORCH")),
            options=complex_logic_filter
        ) | PlanetariumRule(),
        
    },
    "SECRET GARDEN KEY First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 35, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SECRET GARDEN KEY",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachRegion("Attic"), CanReachRegion("Music Room"), CanReachRegion("Lost & Found"), CanReachRegion("Locksmith"), CanReachRegion("Billiard Room")
        ) | DigSpotRule() | CarTrunkRule() | TrunkRule(),
        
    },
    "SILVER KEY First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 36, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        LOCATION_ITEM_KEY: "SILVER KEY",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Closet",
                "Music Room",
                "Her Ladyship's Chamber",
                "Locksmith",
                "Billiard Room", # Dartboard puzzle
                "Mail Room", # Packages
            ]]
        ) | MechanariumDoorRule(2) | DigSpotRule() | 
        And(
            CanReachRegion("Freezer"),
            Or(CanReachItemLocation("Burning Glass"), CanReachItemLocation("TORCH")),
            CanReachItemLocation("PRISM KEY_0"),
            options=complex_logic_filter
        ) | TrunkRule() | AdvancedExperimentRule() | SpiralOfStarsRule(),
        
    },
    # Not included since it is only used in the room it spawn in in both cases
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
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 40, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "CHRONOGRAPH",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Showroom") | SpiralOfStarsRule(),
        
    },
    "EMERALD BRACELET First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 41, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "EMERALD BRACELET",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Showroom") | SpiralOfStarsRule(),
        
    },
    "MASTER KEY First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 42, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "MASTER KEY",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Showroom") | SpiralOfStarsRule(),
        
    },
    "MOON PENDANT First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 43, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "MOON PENDANT",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Showroom") | SpiralOfStarsRule(),
        
    },
    "ORNATE COMPASS First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 44, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "ORNATE COMPASS",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Showroom") | SpiralOfStarsRule(),
        
    },
    "SILVER SPOON First Pickup": {
        LOCATION_ID_KEY: all_areas["Campsite"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 45, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Campsite",
        # LOCATION_ITEM_KEY: "SILVER SPOON",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Showroom") | SpiralOfStarsRule(),
        
    },
}

unique_item_pickup = {
    "CROWN First Pickup": {
        LOCATION_ID_KEY: all_areas["Room 46"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 6,
        LOCATION_ROOM_KEY: "Room 46",
        LOCATION_ITEM_KEY: "CROWN",
        
    },
    "CURSED EFFIGY First Pickup": {
        LOCATION_ID_KEY: all_areas["Shrine"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Shrine",
        LOCATION_ITEM_KEY: "CURSED EFFIGY",
        LOCATION_RULE_SIMPLE_COMMON: And(
            Or(
                CanReachItemLocation("SLEDGE HAMMER"), CanReachItemLocation("MORNING STAR")
            ),
            CanReachRegion("Gift Shop")
        ),
        
    },
    "DIARY KEY First Pickup": {
        LOCATION_ID_KEY: all_areas["Her Ladyship's Chamber"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Her Ladyship's Chamber",
        LOCATION_ITEM_KEY: "DIARY KEY",
        
    },
    "KEY of Aries First Pickup": {
        LOCATION_ID_KEY: all_areas["Aries Court"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Aries Court",
        LOCATION_ITEM_KEY: "KEY of Aries",
        
    },
    "LUNCH BOX First Pickup": {
        LOCATION_ID_KEY: all_areas["Dining Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Dining Room",
        LOCATION_ITEM_KEY: "LUNCH BOX",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Gift Shop"),
        
    },
    "MICROCHIP 1 First Pickup": {
        LOCATION_ID_KEY: all_areas["West Path"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "West Path",
        LOCATION_ITEM_KEY: "MICROCHIP 1",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("SHOVEL"),
        
    },
    "MICROCHIP 2 First Pickup": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 10,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "MICROCHIP 2",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("SLEDGE HAMMER"), CanReachItemLocation("MORNING STAR")
        ),
        
    },
    "MICROCHIP 3 First Pickup": {
        LOCATION_ID_KEY: all_areas["Blackbridge Grotto"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Blackbridge Grotto",
        LOCATION_ITEM_KEY: "MICROCHIP 3",
        
    },
    "PAPER CROWN First Pickup": {
        LOCATION_ID_KEY: all_areas["Closed Exhibit"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Closed Exhibit",
        LOCATION_ITEM_KEY: "PAPER CROWN",
        
    },
    "ROYAL SCEPTER First Pickup": {
        LOCATION_ID_KEY: all_areas["Treasure Trove"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Treasure Trove",
        LOCATION_ITEM_KEY: "ROYAL SCEPTER",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachRegion("Shrine"), CanReachItemLocation("KEY of Aries")
        ),
        
    }
}

item_pickups = standard_item_pickup | special_key_pickup | showroom_item_pickup | unique_item_pickup

workshop_contraptions = {
    "Burning Glass First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Burning Glass",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("MAGNIFYING GLASS"), CanReachItemLocation("METAL DETECTOR")
        ),
        
    },
    "Detector Shovel First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Detector Shovel",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("SHOVEL"), CanReachItemLocation("METAL DETECTOR")
        ),
        
    },
    "Dowsing Rod First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 3,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Dowsing Rod",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("SHOVEL"), CanReachItemLocation("COMPASS")
        ),
        
    },
    "Power Hammer First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 4,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Power Hammer",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("SLEDGE HAMMER"), CanReachItemLocation("BROKEN LEVER"), CanReachItemLocation("BATTERY PACK")
        ),
        
    },
    "Electromagnet First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 5,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Electromagnet",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("COMPASS"), CanReachItemLocation("BATTERY PACK")
        ),
        
    },
    "Lucky Purse First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 6,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Lucky Purse",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("COIN PURSE"), CanReachItemLocation("LUCKY RABBIT'S FOOT")
        ),
        
    },
    "Jack Hammer First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 7,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Jack Hammer",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("SHOVEL"), CanReachItemLocation("BATTERY PACK"), CanReachItemLocation("BROKEN LEVER")
        ),
        
    },
    "Pick Sound Amplifier First Craft": {
        LOCATION_ID_KEY: all_areas["Workshop"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 8,
        LOCATION_ROOM_KEY: "Workshop",
        LOCATION_ITEM_KEY: "Pick Sound Amplifier",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("LOCK PICK KIT"), CanReachItemLocation("METAL DETECTOR")
        ),
        
    },
}

upgrade_disks = {
    "Upgrade Disk - Office": {
        LOCATION_ID_KEY: all_areas["Office"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Office",
    },
    "Upgrade Disk - Morning Room": {
        LOCATION_ID_KEY: all_areas["Morning Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Morning Room",
    },
    "Upgrade Disk - Her Ladyship's Chamber": {
        LOCATION_ID_KEY: all_areas["Her Ladyship's Chamber"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Her Ladyship's Chamber",
    },
    "Upgrade Disk - Commissary": {
        LOCATION_ID_KEY: all_areas["Commissary"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Commissary",
    },
    "Upgrade Disk - Garage": {
        LOCATION_ID_KEY: all_areas["Garage"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Garage",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("CAR KEYS"),
    },
    "Upgrade Disk - Great Hall": {
        LOCATION_ID_KEY: all_areas["Great Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Great Hall",
    },
    "Upgrade Disk - Vault": {
        LOCATION_ID_KEY: all_areas["Vault"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("VAULT KEY 304"),
    },
    "Upgrade Disk - Trading Post Dynamite": {
        LOCATION_ID_KEY: all_areas["Trading Post"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Trading Post",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("Burning Glass"), CanReachItemLocation("TORCH")
        ),
    },
    "Upgrade Disk - Freezer": {
        LOCATION_ID_KEY: all_areas["Freezer"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Freezer",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("Burning Glass"), CanReachItemLocation("TORCH"), CanReachItemLocation("Power Hammer"), CanReachRegion("Furnace")
        )
    },
    "Upgrade Disk - Tomb": {
        LOCATION_ID_KEY: all_areas["Tomb"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Tomb",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("Burning Glass"),
            CanReachItemLocation("TORCH")
        ),
    },
    "Upgrade Disk - The Foundation": {
        LOCATION_ID_KEY: all_areas["The Foundation"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "The Foundation",
    },
    "Upgrade Disk - Abandoned Mine": {
        LOCATION_ID_KEY: all_areas["Abandoned Mine"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Abandoned Mine",
    },
    "Upgrade Disk - Lost & Found": {
        LOCATION_ID_KEY: all_areas["Lost & Found"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Lost & Found",
    },
    "Upgrade Disk - Mechanarium": {
        LOCATION_ID_KEY: all_areas["Mechanarium"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Mechanarium",
        LOCATION_RULE_SIMPLE_COMMON: MechanariumDoorRule(3),
    },
    "Upgrade Disk - Archives": {
        LOCATION_ID_KEY: all_areas["Archives"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Archives",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("CABINET KEY 1"),
    },
    "Upgrade Disk - Trading Post Trade": {
        LOCATION_ID_KEY: all_areas["Trading Post"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Trading Post",
    },
}

vault_keys = {
    "Vault Key 149": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 4, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 149",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Attic", 
                "Rumpus Room", 
                "Security", 
                "Locker Room",
                "Music Room",
            ]]
        ) | DigSpotRule() | CanReachRegion("Trophy Room", options=rare_logic_filter) | AdvancedExperimentRule(),
        
    },
    "Vault Key 233": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 5, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 233",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Office",
                "Sauna",
                "Wine Cellar",
                "Morning Room",
                "Locker Room",
                "Music Room",
            ]]
        ) | DigSpotRule() | LavatoryRule() | AdvancedExperimentRule(),
        
    },
    "Vault Key 304": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 6, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 304",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            *[CanReachRegion(region) for region in [
                "Conference Room",
                "Her Ladyship's Chamber",
                "Walk-In Closet",
                "Hovel",
            ]
        ]) | DigSpotRule() | CanReachRegion("Drawing Room", options=rare_logic_filter) | UpgradedRoomRule("Spare Room", "Spare Hall"),
        
    },
    "Vault Key 370": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 7, # Doesn't spawn there, but putting it there and adding spawn locations as requirements
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_ITEM_KEY: "VAULT KEY 370",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Lost & Found") | DigSpotRule(),
        
    },
}

sanctum_keys = {
    "Sanctum Key - Room 46": {
        LOCATION_ID_KEY: all_areas["Room 46"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 5,
        LOCATION_ROOM_KEY: "Room 46",
        LOCATION_ITEM_KEY: "SANCTUM KEY ANTECHAMBER",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Sanctum Key - Vault": {
        LOCATION_ID_KEY: all_areas["Vault"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_ITEM_KEY: "SANCTUM KEY VAULT",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("VAULT KEY 370"),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Sanctum Key - Clock Tower": {
        LOCATION_ID_KEY: all_areas["Clock Tower"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Clock Tower",
        LOCATION_ITEM_KEY: "SANCTUM KEY CLOCK TOWER",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Sanctum Key - Reservoir Bottom": {
        LOCATION_ID_KEY: all_areas["Reservoir Bottom"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Reservoir Bottom",
        LOCATION_ITEM_KEY: "SANCTUM KEY RESERVOIR",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Sanctum Key - Throne Room": {
        LOCATION_ID_KEY: all_areas["Throne Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Throne Room",
        LOCATION_ITEM_KEY: "SANCTUM KEY THRONE ROOM",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Sanctum Key - Safehouse": {
        LOCATION_ID_KEY: all_areas["Safehouse"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Safehouse",
        LOCATION_ITEM_KEY: "SANCTUM KEY SAFEHOUSE",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Sanctum Key - Music Room": {
        LOCATION_ID_KEY: all_areas["Music Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Music Room",
        LOCATION_ITEM_KEY: "SANCTUM KEY MUSIC ROOM",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Sanctum Key - Mechanarium": {
        LOCATION_ID_KEY: all_areas["Mechanarium"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Mechanarium",
        LOCATION_ITEM_KEY: "SANCTUM KEY MECHANARIUM",
        LOCATION_RULE_SIMPLE_COMMON: MechanariumDoorRule(4),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    }
}

file_cabinet_keys = {
    "File Cabinet Key - Patio": {
        LOCATION_ID_KEY: all_areas["Patio"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Patio",
        LOCATION_ITEM_KEY: "CABINET KEY 1",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("SHOVEL"),
        
    },
    "File Cabinet Key - Laundry Room": {
        LOCATION_ID_KEY: all_areas["Laundry Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Laundry Room",
        LOCATION_ITEM_KEY: "CABINET KEY 2",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("SHOVEL"),
        
    },
    "File Cabinet Key - Tunnel Area Past Crates": {
        LOCATION_ID_KEY: all_areas["Tunnel Area Past Crates"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Tunnel Area Past Crates",
        LOCATION_ITEM_KEY: "CABINET KEY 3",
        
    },
}

keys = vault_keys | sanctum_keys | file_cabinet_keys

doors_walls_and_gates = {
    "West Gate": {
        LOCATION_ID_KEY: all_areas["West Path"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "West Path",
    },
    "Break Grounds to Sealed Entrance Wall": {
        LOCATION_ID_KEY: all_areas["Sealed Entrance"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Sealed Entrance",
    },
    "Break Basement to Sealed Entrance Wall": {
        LOCATION_ID_KEY: all_areas["Sealed Entrance"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Sealed Entrance",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED, # Only found a hook for one side of sealed entrance
    },
    "Break Weight Room Wall": {
        LOCATION_ID_KEY: all_areas["Weight Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Weight Room",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("Power Hammer")
    },
    "Break Greenhouse Wall": {
        LOCATION_ID_KEY: all_areas["Greenhouse"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Greenhouse",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("Power Hammer")
    },
    "Break Secret Garden Wall": {
        LOCATION_ID_KEY: all_areas["Secret Garden"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Secret Garden",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("Power Hammer")
    },
    "Break Freezer Wall": {
        LOCATION_ID_KEY: all_areas["Freezer"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Freezer",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("Power Hammer"),
            CanReachRegion("Furnace"),
            CanReachItemLocation("Burning Glass"),
            CanReachItemLocation("TORCH")
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED, # Not sure if this gets hooked anywhere since its not persistent
    },
    "Break Precipice Wall": {
        LOCATION_ID_KEY: all_areas["The Precipice"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "The Precipice",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("Power Hammer")
    },
    "Break Tunnel Wall": {
        LOCATION_ID_KEY: all_areas["Tunnel Area Past Sealed Door"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Tunnel Area Past Sealed Door",
    },
    "Unlock Basement Door The Foundation": {
        LOCATION_ID_KEY: all_areas["The Foundation"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "The Foundation",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("BASEMENT KEY")
    },
    "Unlock Basement Door The Well": {
        LOCATION_ID_KEY: all_areas["The Well"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "The Well",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("BASEMENT KEY")
    },
    "Unlock Basement Door Tunnel Area": {
        LOCATION_ID_KEY: all_areas["Tunnel Area Past Basement key Door"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Tunnel Area Past Basement key Door",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED, # Know how to hook it, but haven't gotten around to it since its so lategame
    },
    "Solve Tomb Puzzle 1": {
        LOCATION_ID_KEY: all_areas["Catacombs"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Catacombs",
    },
    "Solve Tomb Puzzle 2": {
        LOCATION_ID_KEY: all_areas["Catacombs"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Catacombs",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED, # Didn't see a hook for the second solution
    },
    "Open the Torch Chamber Shortcut": {
        LOCATION_ID_KEY: all_areas["Torch Chamber"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Torch Chamber",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("Burning Glass"),
            CanReachItemLocation("TORCH")
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Open Deposit Box 053": {
        LOCATION_ID_KEY: all_areas["Vault"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Vault",
        LOCATION_RULE_SIMPLE_COMMON: CanReachItemLocation("KEY 8"),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Open Basement to Reservoir Door": {
        LOCATION_ID_KEY: all_areas["Basement"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Basement",
    },
    "Lower The Foundation Elevator": {
        LOCATION_ID_KEY: all_areas["The Foundation"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "The Foundation",
    },
}

misc_locations = {
    "Entrance Hall East Vase": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 8,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("SLEDGE HAMMER"),
            CanReachItemLocation("MORNING STAR")
        )
    },
    "Entrance Hall West Vase": {
        LOCATION_ID_KEY: all_areas["Entrance Hall"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 9,
        LOCATION_ROOM_KEY: "Entrance Hall",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("SLEDGE HAMMER"),
            CanReachItemLocation("MORNING STAR")
        )
    },
    "Cursed Coffers": {
        LOCATION_ID_KEY: all_areas["Shrine"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Shrine",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("SLEDGE HAMMER"),
            CanReachItemLocation("MORNING STAR")
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Gasline Valve - Orchard": {
        LOCATION_ID_KEY: all_areas["Apple Orchard"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Apple Orchard",
        LOCATION_RULE_SIMPLE_COMMON: Has("Apple Orchard"),
    },
    "Gasline Valve - Schoolhouse": {
        LOCATION_ID_KEY: all_areas["Schoolhouse"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Schoolhouse",
    },
    "Gasline Valve - Hovel": {
        LOCATION_ID_KEY: all_areas["Hovel"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Hovel",
    },
    "Gasline Valve - Gemstone Cavern": {
        LOCATION_ID_KEY: all_areas["Gemstone Cavern"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Gemstone Cavern",
    },
    "Scorch Sundial": {
        LOCATION_ID_KEY: all_areas["Apple Orchard"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Apple Orchard",
        LOCATION_RULE_SIMPLE_COMMON: Or(
            CanReachItemLocation("Burning Glass"),
            CanReachItemLocation("TORCH")
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Raise Satellite": {
        LOCATION_ID_KEY: all_areas["Apple Orchard"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 2,
        LOCATION_ROOM_KEY: "Apple Orchard",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachLocation("Scorch Sundial"),
            CanReachItemLocation("MICROCHIP 1"),
            CanReachItemLocation("MICROCHIP 2"),
            CanReachItemLocation("MICROCHIP 3"),
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "VAC Controls": {
        LOCATION_ID_KEY: all_areas["Utility Closet"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Utility Closet",
    },
    "Allowance Token - Cloister Statue": {
        LOCATION_ID_KEY: all_areas["Cloister"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Cloister",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED, # this was working at one point, but something broke it
    },
    "Allowance Token - Outer Entrance Hall Vase": {
        LOCATION_ID_KEY: all_areas["Outer Room"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Outer Room",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachRegion("Shrine"),
            Or(
                CanReachItemLocation("SLEDGE HAMMER"),
                CanReachItemLocation("MORNING STAR")
            )
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Allowance Tokens - Reservoir Bottom": {
        LOCATION_ID_KEY: all_areas["Reservoir Bottom"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Reservoir Bottom",
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    # Ignoring deposit box allowance tokens for now, since they are missable (don't respawn if not picked up)
    "Baron Bafflers": {
        LOCATION_ID_KEY: all_areas["Bedroom"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 100,
        LOCATION_ROOM_KEY: "Bedroom",
        LOCATION_RULE_SIMPLE_COMMON: And(
            CanReachItemLocation("SHOVEL"),
            CanReachItemLocation("TREASURE MAP")
        ),
        IMPLEMENTATION_STATUS: NOT_IMPLEMENTED,
    },
    "Laboratory Puzzle": {
        LOCATION_ID_KEY: all_areas["Laboratory"][ROOM_ITEM_ID_KEY] * ROOM_MULTIPLIER + 1,
        LOCATION_ROOM_KEY: "Laboratory",
        LOCATION_RULE_SIMPLE_COMMON: CanReachRegion("Boiler Room"),
    }
}

# TODO-1: add locations for other stuff later.
# Chapel Keeper
# Alzara Prophecies

# Blueprint first pickup

# Treasure Map Chests? (Might need to pre-calculate min piece counts for chest locations)

# Mirror Room Floorplan Duplicates?

# Swansong/SwansongHSS + Blackbridge passwords

# Reservoir/Treasure Trove chests? (46 in Trove, 23 in Reservoir)

# Gallery painting puzzles
# Boiler solve
# Well Drained
# Pool Drained
# Room Upgrades

# Possible locations that are currently Events:
# Raise Satellite
# Sanctum Solves
# Ascend the Throne
# Unseal Blue Doors
# Levers

locations = trophies | safes_and_small_gates | mora_jai_boxes | floorplans | shop_items | upgrade_disks | keys | misc_locations | item_pickups | workshop_contraptions | doors_walls_and_gates

LOCATIONS_BY_GROUPS |= {
    "Trophies": {k for k in trophies},
    "Safes and Small Gates": {k for k in safes_and_small_gates},
    "Mora Jai Boxes": {k for k in mora_jai_boxes},
    "Floorplans": {k for k in floorplans},
    "Shop Items": {k for k in shop_items},
    "Upgrade Disks": {k for k in upgrade_disks},
    "Keys": {k for k in keys},
    "Miscellaneous": {k for k in misc_locations},
    "Item Pickups": {k for k in item_pickups},
    "Workshop Contraptions": {k for k in workshop_contraptions},
    "Doors, Walls, and Gates": {k for k in doors_walls_and_gates},
    "Gift Shop": {k for k in gift_shop_items},
    "Bookshop": {k for k in bookshop_items},
    "Armory Purchases": {f"{k} First Pickup" for k in armory_items},
}
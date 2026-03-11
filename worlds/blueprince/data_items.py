from typing import Dict, Set
from .constants import *

from BaseClasses import Item, ItemClassification

upgrade_disks = {
    "UPGRADE DISK COMMISSARY": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2801,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK OFFICE": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2802,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK GARAGE": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2803,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK FOUNDATION": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2804,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK GREAT HALL": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2805,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK MORNING ROOM": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2806,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK HER LADYSHIPS CHAMBER": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2807,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK VAULT": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2808,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK ARCHIVES": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2809,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK FREEZER": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2810,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK TOMB": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2811,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK LOST AND FOUND": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2812,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK MECHANARIUM": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2813,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK ABANDONED MINE": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2814,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK TRADING POST TRADE": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2815,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "UPGRADE DISK TRADING POST DYNAMITE": {
        ITEM_ELEMENT_INDEX_KEY: 28,
        ITEM_ID_KEY: 2816,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
}

sanctum_keys = {
    "SANCTUM KEY ANTECHAMBER": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SANCTUM KEY VAULT": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9002,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SANCTUM KEY CLOCK TOWER": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9003,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SANCTUM KEY RESERVOIR": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9004,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SANCTUM KEY THRONE ROOM": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9005,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SANCTUM KEY SAFEHOUSE": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9006,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SANCTUM KEY MUSIC ROOM": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9007,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SANCTUM KEY MECHANARIUM": {
        ITEM_ELEMENT_INDEX_KEY: 9,
        ITEM_ID_KEY: 9008,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
}

keys = {
    "CAR KEYS": {
        ITEM_ELEMENT_INDEX_KEY: 3,
        ITEM_ID_KEY: 10003,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "KEYCARD": {
        ITEM_ELEMENT_INDEX_KEY: 10,
        ITEM_ID_KEY: 10010,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "SILVER KEY": {
        ITEM_ELEMENT_INDEX_KEY: 19,
        ITEM_ID_KEY: 10019,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "KEY 8": {
        ITEM_ELEMENT_INDEX_KEY: 27,
        ITEM_ID_KEY: 10027,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "BASEMENT KEY": {
        ITEM_ELEMENT_INDEX_KEY: 0,
        ITEM_ID_KEY: 10000,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "VAULT KEY 149": {
        ITEM_ELEMENT_INDEX_KEY: 22,
        ITEM_ID_KEY: 10022,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "VAULT KEY 233": {
        ITEM_ELEMENT_INDEX_KEY: 23,
        ITEM_ID_KEY: 10023,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "VAULT KEY 304": {
        ITEM_ELEMENT_INDEX_KEY: 24,
        ITEM_ID_KEY: 10024,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "VAULT KEY 370": {
        ITEM_ELEMENT_INDEX_KEY: 25,
        ITEM_ID_KEY: 10025,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "DIARY KEY": {
        ITEM_ELEMENT_INDEX_KEY: 42,
        ITEM_ID_KEY: 10042,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "CABINET KEY 1": {
        ITEM_ELEMENT_INDEX_KEY: 45,
        ITEM_ID_KEY: 10045,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "CABINET KEY 2": {
        ITEM_ELEMENT_INDEX_KEY: 46,
        ITEM_ID_KEY: 10046,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "CABINET KEY 3": {
        ITEM_ELEMENT_INDEX_KEY: 46,
        ITEM_ID_KEY: 10047,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "PRISM KEY_0": {
        # Known exception to formatting. Keeping consistent with game format.
        ITEM_ELEMENT_INDEX_KEY: 50,
        ITEM_ID_KEY: 10050,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "KEY of Aries": {
        # Known exception to formatting. Keeping consistent with game format.
        ITEM_ELEMENT_INDEX_KEY: 51,
        ITEM_ID_KEY: 10051,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "SECRET GARDEN KEY": {
        ITEM_ELEMENT_INDEX_KEY: 17,
        ITEM_ID_KEY: 10017,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "MICROCHIP 1": {
        ITEM_ELEMENT_INDEX_KEY: 39,
        ITEM_ID_KEY: 10039,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "MICROCHIP 2": {
        ITEM_ELEMENT_INDEX_KEY: 40,
        ITEM_ID_KEY: 10040,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "MICROCHIP 3": {
        ITEM_ELEMENT_INDEX_KEY: 41,
        ITEM_ID_KEY: 10041,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
} | sanctum_keys

showroom_items = {
    "CHRONOGRAPH": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 2001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing,
    },
    "EMERALD BRACELET": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 2002,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing,
    },
    "MASTER KEY": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 2003,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "MOON PENDANT": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 2004,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing,
    },
    "ORNATE COMPASS": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 2005,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing,
    },
    "SILVER SPOON": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 2006,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing,
    },
}
armory_items = {
    "MORNING STAR": {
        ITEM_ELEMENT_INDEX_KEY: 35,
        ITEM_ID_KEY: 1035,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "THE AXE": {
        ITEM_ELEMENT_INDEX_KEY: 36,
        ITEM_ID_KEY: 1036,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "TORCH": {
        ITEM_ELEMENT_INDEX_KEY: 37,
        ITEM_ID_KEY: 1037,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "KNIGHTS SHIELD": {
        ITEM_ELEMENT_INDEX_KEY: 38,
        ITEM_ID_KEY: 1038,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
}

other_items = {
    "BATTERY PACK": {
        ITEM_ELEMENT_INDEX_KEY: 1,
        ITEM_ID_KEY: 1001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "BROKEN LEVER": {
        ITEM_ELEMENT_INDEX_KEY: 2,
        ITEM_ID_KEY: 1002,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "MAGNIFYING GLASS": {
        ITEM_ELEMENT_INDEX_KEY: 13,
        ITEM_ID_KEY: 1013,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "METAL DETECTOR": {
        ITEM_ELEMENT_INDEX_KEY: 14,
        ITEM_ID_KEY: 1014,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "SHOVEL": {
        ITEM_ELEMENT_INDEX_KEY: 18,
        ITEM_ID_KEY: 1018,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "SLEDGE HAMMER": {
        ITEM_ELEMENT_INDEX_KEY: 20,
        ITEM_ID_KEY: 1020,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "TELESCOPE": {
        ITEM_ELEMENT_INDEX_KEY: 34,
        ITEM_ID_KEY: 1034,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "RUNNING SHOES": {
        ITEM_ELEMENT_INDEX_KEY: 15,
        ITEM_ID_KEY: 1015,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "SALT SHAKER": {
        ITEM_ELEMENT_INDEX_KEY: 16,
        ITEM_ID_KEY: 1016,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "SLEEPING MASK": {
        ITEM_ELEMENT_INDEX_KEY: 21,
        ITEM_ID_KEY: 1021,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "COIN PURSE": {
        ITEM_ELEMENT_INDEX_KEY: 4,
        ITEM_ID_KEY: 1004,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "COUPON BOOK": {
        ITEM_ELEMENT_INDEX_KEY: 6,
        ITEM_ID_KEY: 1006,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "LOCK PICK KIT": {
        ITEM_ELEMENT_INDEX_KEY: 11,
        ITEM_ID_KEY: 1011,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "LUCKY RABBIT'S FOOT": {
        ITEM_ELEMENT_INDEX_KEY: 12,
        ITEM_ID_KEY: 1012,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "TREASURE MAP": {
        ITEM_ELEMENT_INDEX_KEY: 26,
        ITEM_ID_KEY: 1026,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "STOPWATCH": {
        ITEM_ELEMENT_INDEX_KEY: 29,
        ITEM_ID_KEY: 1029,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "REPELLENT": {
        ITEM_ELEMENT_INDEX_KEY: 30,
        ITEM_ID_KEY: 1030,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing,
    },
    "WATERING CAN": {
        ITEM_ELEMENT_INDEX_KEY: 31,
        ITEM_ID_KEY: 1031,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
    "HALL PASS": {
        ITEM_ELEMENT_INDEX_KEY: 32,
        ITEM_ID_KEY: 1032,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "LUNCH BOX": {
        ITEM_ELEMENT_INDEX_KEY: 43,
        ITEM_ID_KEY: 1043,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing,
    },
    "CURSED EFFIGY": {
        ITEM_ELEMENT_INDEX_KEY: 44,
        ITEM_ID_KEY: 1044,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "CROWN": {
        ITEM_ELEMENT_INDEX_KEY: 47,
        ITEM_ID_KEY: 1047,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "PAPER CROWN": {
        ITEM_ELEMENT_INDEX_KEY: 48,
        ITEM_ID_KEY: 1048,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "ROYAL SCEPTER": {
        ITEM_ELEMENT_INDEX_KEY: 49,
        ITEM_ID_KEY: 1049,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "GEAR WRENCH": {
        ITEM_ELEMENT_INDEX_KEY: 33,
        ITEM_ID_KEY: 1033,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "COMPASS": {
        ITEM_ELEMENT_INDEX_KEY: 5,
        ITEM_ID_KEY: 1005,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
}

workshop_items = {
    "Burning Glass": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression,
    },
    "Detector Shovel": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3002,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "Dowsing Rod": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3003,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "Electromagnet": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3004,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "Jack Hammer": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3005,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized | ItemClassification.useful,
    },
    "Lucky Purse": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3006,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized | ItemClassification.useful,
    },
    "Pick Sound Amplifier": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3007,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression_deprioritized_skip_balancing | ItemClassification.useful,
    },
    "Power Hammer": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 3008,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression | ItemClassification.useful,
    },
}

upgrade_items = {
    "IVORY DICE": {
        ITEM_ELEMENT_INDEX_KEY: 8,
        ITEM_ID_KEY: 1008,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "ALLOWANCE TOKENS": {
        ITEM_ELEMENT_INDEX_KEY: NO_ITEM_ELEMENT_INDEX,
        ITEM_ID_KEY: 7001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
    "CUPCAKE MESH": {
        ITEM_ELEMENT_INDEX_KEY: 7,
        ITEM_ID_KEY: 1007,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful,
    },
}

# 
# Items to add:
# 
# Gift Shop Items
# Bookshop Items
# 
# Orchard Gate?

all_items_excluding_upgrade_items = upgrade_disks | keys | showroom_items | armory_items | workshop_items | other_items
all_items = all_items_excluding_upgrade_items | upgrade_items

#############################
# TRADING POST TIER LOOKUPS #
#############################

TRADING_POST_TIER1 = {
    TRADING_POST_GIVE: [
        "BATTERY PACK",
        "MAGNIFYING GLASS",
        "SALT SHAKER",
        "SLEEPING MASK",
        "BROKEN LEVER",
    ],
    TRADING_POST_RECEIVE: [
        "BATTERY PACK",
        "MAGNIFYING GLASS",
        "SALT SHAKER",
        "SLEEPING MASK",
        "BROKEN LEVER",
    ],
}
TRADING_POST_TIER2 = {
    TRADING_POST_GIVE: [
        "CAR KEYS",
        "COIN PURSE",
        "COMPASS",
        "COUPON BOOK",
        "SHOVEL",
        "SLEDGE HAMMER",
    ],
    TRADING_POST_RECEIVE: [
        "CAR KEYS",
        "COIN PURSE",
        "COMPASS",
        "COUPON BOOK",
        "SHOVEL",
        "SLEDGE HAMMER",
        "MICROCHIP 1",
        "MICROCHIP 2",
        "MICROCHIP 3",
        "TREASURE MAP",
        "Wind-up Key",
    ],
}
TRADING_POST_TIER3 = {
    TRADING_POST_GIVE: [
        "KEYCARD",
        "LOCK PICK KIT",
        "LUCKY RABBIT'S FOOT",
        "METAL DETECTOR",
        "RUNNING SHOES",
        "SILVER KEY",
        "VAULT KEY 149",
        "VAULT KEY 233",
        "VAULT KEY 304",
        "VAULT KEY 370",
    ],
    TRADING_POST_RECEIVE: [
        "KEYCARD",
        "LOCK PICK KIT",
        "LUCKY RABBIT'S FOOT",
        "METAL DETECTOR",
        "RUNNING SHOES",
        "SILVER KEY",
        "VAULT KEY 149",
        "VAULT KEY 233",
        "VAULT KEY 304",
        "VAULT KEY 370",
        "THE AXE",
        "KNIGHTS SHIELD",
        "MORNING STAR",
        "TORCH",
        "MOON PENDANT",
        "SILVER SPOON",
    ],
}
TRADING_POST_TIER4 = {
    TRADING_POST_GIVE: [
        "GEAR WRENCH",
        "HALL PASS",
        "PRISM KEY_0",
        "SECRET GARDEN KEY",
        "TELESCOPE",
    ],
    TRADING_POST_RECEIVE: [
        "GEAR WRENCH",
        "HALL PASS",
        "PRISM KEY_0",
        "SECRET GARDEN KEY",
        "TELESCOPE",
        "Burning Glass",
        "Detector Shovel",
        "Dowsing Rod",
        "Electromagnet",
        "Jack Hammer",
        "Lucky Purse",
        "Pick Sound Amplifier",
        "Power Hammer",
        "BASEMENT KEY",
        "DIARY KEY",
        "KEY 8",
        "CHRONOGRAPH",
        "LUNCH BOX",
        "REPELLENT",
        "STOPWATCH",
        "WATERING CAN",
        "UPGRADE DISK COMMISSARY",
        "UPGRADE DISK OFFICE",
        "UPGRADE DISK GARAGE",
        "UPGRADE DISK FOUNDATION",
        "UPGRADE DISK GREAT HALL",
        "UPGRADE DISK MORNING ROOM",
        "UPGRADE DISK HER LADYSHIPS CHAMBER",
        "UPGRADE DISK VAULT",
        "UPGRADE DISK ARCHIVES",
        "UPGRADE DISK FREEZER",
        "UPGRADE DISK TOMB",
        "UPGRADE DISK LOST AND FOUND",
        "UPGRADE DISK MECHANARIUM",
        "UPGRADE DISK ABANDONED MINE",
        "UPGRADE DISK TRADING POST TRADE",
        "UPGRADE DISK TRADING POST DYNAMITE"
    ],
}

# None of the Tier 5 items can be received, so there's no point in defining it atm

ITEMS_BY_GROUPS : Dict[str, Set[str]] = {
    "Upgrade Disks": {disk for disk in upgrade_disks},
    "Sanctum Keys": {key for key in sanctum_keys},
    "Keys": {key for key in keys},
    "Showroom Items": {item for item in showroom_items},
    "Armory Items": {item for item in armory_items},
    "Workshop Items": {item for item in workshop_items},
    "Standard Items": {item for item in other_items}
}
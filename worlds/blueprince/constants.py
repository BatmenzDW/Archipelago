#####################
# OPTIONS CONSTANTS #
#####################

from typing import Dict, Set


ROOM_DRAFT_SANITY = "room_draft_sanity"
STANDARD_ITEM_SANITY = "standard_item_sanity"
WORKSHOP_SANITY = "workshop_sanity"
UPGRADE_DISK_SANITY = "upgrade_disk_sanity"
KEY_SANITY = "key_sanity"
SPECIAL_SHOP_SANITY = "special_shop_sanity"

SANITY_TYPE_KEY = "sanity_type"
NONSANITY_LOCATION_KEY = "nonsanity_location_item"

######################
# ITEM KEY CONSTANTS #
######################

# Defines the key for setting the data in a room's info-dict. Used specifically to define what item classification a room is.
ROOM_ITEM_CLASSIFICATION_KEY = "item_classification"
# Defines the key for setting the data in a room's info-dict. Used specifically to define what ID the room is as an item.
ROOM_ITEM_ID_KEY = "item_id"
# Defines the key for setting the data in a room's info-dict. Used specifically to define the key for the array of where the room can be selected.
ROOM_PICK_POSITIONS_KEY = "room_picker_positions"
# Defines the key for setting the data in a room's info-dict. Used specifically to define how many spots the room can place an item like a shovel.
ROOM_ITEM_SPOT_COUNT_KEY = "item_spot_count"
# Defines which trunk spawn setting a room should be affected by.
ROOM_CHEST_SPOT_TYPE_KEY = "chest_spot_type"
# Defines the key for setting the data in a room's info-dict. Used specifically to define how many chest spots the room can have.
ROOM_CHEST_SPOT_COUNT_KEY = "chest_spot_count"
# defines the key for setting the data in a room's info-dict. Used specifically to define which chess piece is in a room
ROOM_CHESS_PIECE_KEY = "chess_piece"
# Defines the key for setting the data in a room's info-dict. Used specifically to define the general shape of the room for path calculations.
ROOM_LAYOUT_TYPE_KEY = "room_layout"
# room location type key is a key used to set if a room is from the outer rooms
OUTER_ROOM_KEY = "is_outer_room"

INNER_ROOM_KEY = "is_inner_room"

##################
# ITEM CONSTANTS #
##################

ROOM_MULTIPLIER = 100_000

ROOM_CHEST_SPOT_COMMON = "common"
ROOM_CHEST_SPOT_RARE = "rare"
ROOM_CHEST_SPOT_COMPLEX = "complex"

# One of the room layout types. Specifically, for dead-end rooms
ROOM_LAYOUT_TYPE_D = "room_layout_type_d"
# One of the room layout types. Specifically, for rooms with 3 entrances
ROOM_LAYOUT_TYPE_T = "room_layout_type_t"
# One of the room layout types. Specifically, for rooms with 2 entrances inline
ROOM_LAYOUT_TYPE_I = "room_layout_type_i"
# One of the room layout types. Specifically, for rooms with 2 entrances NOT inline
ROOM_LAYOUT_TYPE_J = "room_layout_type_j"
# One of the room layout types. Specifically, for rooms with 4 entrances.
ROOM_LAYOUT_TYPE_X = "room_layout_type_x"


# Chess piece values for the room having each of the different chess pieces.
CHESS_PIECE_ROOK = "Rook"
CHESS_PIECE_QUEEN = "Queen"
CHESS_PIECE_KING = "King"
CHESS_PIECE_KNIGHT = "Knight"
CHESS_PIECE_BISHOP = "Bishop"
CHESS_PIECE_PAWN = "Pawn"
CHESS_PIECE_NONE = ""

STARTING_INVENTORY = "starting_inventory"

######################
# ITEM KEY CONSTANTS #
######################

# This corresponds to the index of the item in the item list in the game itself.
ITEM_ELEMENT_INDEX_KEY = "item_element_index"
# Key of the item ID in the item data table.
ITEM_ID_KEY = "item_id"
# Key of the item's classification in the item data table.
ITEM_ITEM_CLASSIFICATION_KEY = "item_classification"

##################
# ITEM CONSTANTS #
##################

# Used to denote that no index exists in the main item list.
NO_ITEM_ELEMENT_INDEX = -1

##########################
# LOCATION KEY CONSTANTS #
##########################

LOCATION_ID_KEY = "location_id"

LOCATION_RULE_SIMPLE_COMMON = "rule_simple_common"
LOCATION_RULE_SIMPLE_RARE = "rule_simple_rare"
LOCATION_RULE_COMPLEX = "rule_complex"
LOCATION_RULE_EXTREME = "rule_extreme"

LOCATION_ROOM_KEY = "location_room"
LOCATION_ITEM_KEY = "location_item"
LOCATION_SANITY_TYPE_KEY = "sanity_type"

#####################
# CONTROL CONSTANTS #
#####################

# Enable room logic, when set to true, allows the rooms to be loaded into the world as items to be found.
# When false, "all rooms" will be available to the player "at the start"
ENABLE_ROOM_LOGIC = True

########################
# ROOM LOGIC POSITIONS #
########################

# Advance means going up that associated edge.
# Retreat means going down that edge.
# Edge creep means going up OR down that edge.
# Edge Pierce means going INTO the edge from non-edge.
# STANDALONE ARRAY (Outer Room)
# Tier:  Center Tier 1 is ranks 2-3 Center Tier 2 is 4-6 Center Tier 3 is 7-8 (Tier does not matter for Corner or Front.)
# Front Is Rank 1
# Back Is Rank 9
# Gems is Requires Gems
# North Pierce - Rank 9 from rank 8
# South Pierce - Rank 1 from Rank 2
# Frontback - Rare Front
#


ROOM_PICK_POSITION_CENTER_TIER_1 = "CENTER - Tier 1"
ROOM_PICK_POSITION_CENTER_TIER_1_GEMS = "CENTER - Tier 1 G"
ROOM_PICK_POSITION_CENTER_TIER_1_FOUNDATION = "CENTER - Tier 1 Foundation"
ROOM_PICK_POSITION_CENTER_TIER_2 = "CENTER - Tier 2"
ROOM_PICK_POSITION_CENTER_TIER_2_GEMS = "CENTER - Tier 2 G"
ROOM_PICK_POSITION_CENTER_TIER_3 = "CENTER - Tier 3"
ROOM_PICK_POSITION_CENTER_TIER_3_GEMS = "CENTER - Tier 3 G"
ROOM_PICK_POSITION_CENTER_RARE = "Center Rare"
ROOM_PICK_POSITION_CENTER_RARE_GEMS = "Center Rare G"
ROOM_PICK_POSITION_CORNER_RARE = "CORNER - RARE"
ROOM_PICK_POSITION_CORNER_RARE_GEMS = "CORNER - RARE G"
ROOM_PICK_POSITION_CORNER = "CORNER - Tier 1"
ROOM_PICK_POSITION_CORNER_GEMS = "CORNER - Tier 1 G"
ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS = "EDGE ADVANCE EASTWING - G"
ROOM_PICK_POSITION_EDGE_ADVANCE_WEST_WING_GEMS = "EDGE ADVANCE WESTWING - G"
ROOM_PICK_POSITION_EDGE_RETREAT_EAST_WING_GEMS = "EDGE RETREAT EASTWING - G"
ROOM_PICK_POSITION_EDGE_RETREAT_WEST_WING_GEMS = "EDGE RETREAT WESTWING - G"
ROOM_PICK_POSITION_EDGE_CREEP_RARE = "EDGECREEP - RARE"
ROOM_PICK_POSITION_EDGE_CREEP_RARE_GEMS = "EDGECREEP - RARE G"
ROOM_PICK_POSITION_EDGE_CREEP_EAST = "EDGECREEP EAST"
ROOM_PICK_POSITION_EDGE_CREEP_WEST = "EDGECREEP WEST"
ROOM_PICK_POSITION_EDGE_PIERCE_EAST = "EDGEPIERCE EAST"
ROOM_PICK_POSITION_EDGE_PIERCE_WEST = "EDGEPIERCE WEST"
ROOM_PICK_POSITION_EDGE_PIERCE_GEMS = "EDGEPIERCE G"
ROOM_PICK_POSITION_EDGE_PIERCE_RARE = "EDGEPIERCE - RARE"
ROOM_PICK_POSITION_EDGE_PIERCE_RARE_GEMS = "EDGEPIERCE - RARE G"
ROOM_PICK_POSITION_FRONT = "FRONT - Tier 1"
ROOM_PICK_POSITION_FRONT_GEMS = "FRONT - Tier 1 G"
ROOM_PICK_POSITION_FRONT_BACK_RARE = "FRONTBACK - RARE"
ROOM_PICK_POSITION_FRONT_BACK_RARE_GEMS = "FRONTBACK G - RARE"
ROOM_PICK_POSITION_NORTH_PIERCE = "NORTH PIERCE"
ROOM_PICK_POSITION_NORTH_PIERCE_GEMS = "NORTH PIERCE G"
ROOM_PICK_POSITION_SOUTH_PIERCE = "SOUTH PIERCE"
ROOM_PICK_POSITION_STANDALONE = "STANDALONE ARRAY"
ROOM_PICK_POSITION_STANDALONE_FULL = "STANDALONE ARRAY FULL"
ROOM_PICK_POSITION_ANTECHAMBER = "ANTECHAMBER"
ROOM_PICK_POSITION_ROOM_8 = "ROOM 8"

#################################
# TRADING POST LOOKUP CONSTANTS #
#################################

TRADING_POST_GIVE = "GIVE"
TRADING_POST_RECEIVE = "RECEIVE"

##################
# DARE CONSTANTS #
##################

DARE_CAN_REACH_RULE = "Can Reach Rule"
DARE_IS_POSSIBLE_RULE = "Is Possible Rule"

########################
# Item/Location GROUPS #
########################

ITEMS_BY_GROUPS : Dict[str, Set[str]] = {}
LOCATIONS_BY_GROUPS : Dict[str, Set[str]] = {}

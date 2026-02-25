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
# Defines the key for setting the data in a room's info-dict. Used specifically to define how many chest spots the room can have.
ROOM_CHEST_SPOT_COUNT_KEY = "chest_spot_count"
# defines the key for setting the data in a room's info-dict. Used specifically to define which chess piece is in a room
ROOM_CHESS_PIECE_KEY = "chess_piece"
# Defines the key for setting the data in a room's info-dict. Used specifically to define the general shape of the room for path calculations.
ROOM_LAYOUT_TYPE_KEY = "room_layout"
# room location type key is a key used to set if a room is from the outer rooms
OUTER_ROOM_KEY = "is_outer_room"

INNER_ROOM_KEY = "is_inner_room"
LOCATION_COUNT_KEY = "location_count"


##################
# ITEM CONSTANTS #
##################

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
LOCATION_REQUIREMENTS = "requirements"
LOCATION_ROOM_KEY = "location_room"

##################################
# LOCATION REQUIREMENT CONSTANTS #
##################################

LOCATION_REQUIREMENT_TYPE_ROOM_COUNT = "room_count"
LOCATION_REQUIREMENT_TYPE_HAS_ALL_ROOMS = "has_all_rooms"
LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ALL = "has_items_all"
LOCATION_REQUIREMENT_TYPE_HAS_ITEMS_ANY = "has_items_any"
LOCATION_REQUIREMENT_TYPE_HAS_ITEM_COUNTS = "has_item_counts"
LOCATION_REQUIREMENT_TYPE_HAS_REGIONS_ACCESS = "has_regions_access"
LOCATION_REQUIREMENT_TYPE_HAS_LOCATIONS_ACCESS = "has_locations_access"
LOCATION_REQUIREMENT_TYPE_COUNT_LOCATIONS_ACCESS = "count_locations_access"

#####################
# CONTROL CONSTANTS #
#####################

# Enable room logic, when set to true, allows the rooms to be loaded into the world as items to be found.
# When false, "all rooms" will be available to the player "at the start"
ENABLE_ROOM_LOGIC = True

# Enable advanced logic for room access checks, when set to true, use dfs to ensure a room is reachable
# When false, only check if the pool has the required number of rooms to reach the room
ENABLE_ADVANCED_ROOM_ACCESS_LOGIC = True


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

N, E, S, W = 1, 2, 4, 8

DIRS = {
    N: (0, 1),
    E: (1, 0),
    S: (0, -1),
    W: (-1, 0),
}

OPPOSITE = {
    N: S,
    S: N,
    E: W,
    W: E,
}

POSITION_CHECKS = {
    ROOM_PICK_POSITION_CENTER_TIER_1: [((3, 2), [S], 0)], # Should always be true
    ROOM_PICK_POSITION_CENTER_TIER_1_GEMS: [((3, 2), [S], 0)], # Should always be true
    ROOM_PICK_POSITION_CENTER_TIER_1_FOUNDATION: [((3, 3), [S], 3), ((2, 3), [S]), ((4, 3), [S])],
    ROOM_PICK_POSITION_CENTER_TIER_2: [((3, 4), [S], 5), ((2, 4), [S]), ((4, 4), [S])],
    ROOM_PICK_POSITION_CENTER_TIER_2_GEMS: [((3, 4), [S], 5), ((2, 4), [S]), ((4, 4), [S])],
    ROOM_PICK_POSITION_CENTER_TIER_3: [((3, 7), [S], 8), ((2, 7), [S]), ((4, 7), [S])],
    ROOM_PICK_POSITION_CENTER_TIER_3_GEMS: [((3, 7), [S], 8), ((2, 7), [S]), ((4, 7), [S])],
    ROOM_PICK_POSITION_CORNER_RARE: [((1, 1), [N, E], 4)],
    ROOM_PICK_POSITION_CORNER_RARE_GEMS: [((1, 1), [N, E], 4)],
    ROOM_PICK_POSITION_CORNER: [((1, 1), [N, E], 4)],
    ROOM_PICK_POSITION_CORNER_GEMS: [((1, 1), [N, E], 4)],
    ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS: [((5, 2), [S], 7)],
    ROOM_PICK_POSITION_EDGE_ADVANCE_WEST_WING_GEMS: [((1, 2), [S], 7)],
    ROOM_PICK_POSITION_EDGE_RETREAT_EAST_WING_GEMS: [((5, 2), [N], 7)],
    ROOM_PICK_POSITION_EDGE_RETREAT_WEST_WING_GEMS: [((1, 2), [N], 7)],
    ROOM_PICK_POSITION_EDGE_CREEP_RARE: [((1, 2), [S], 5)],
    ROOM_PICK_POSITION_EDGE_CREEP_RARE_GEMS: [((1, 2), [S], 5)],
    ROOM_PICK_POSITION_EDGE_CREEP_EAST: [((5, 2), [S], 5)],
    ROOM_PICK_POSITION_EDGE_CREEP_WEST: [((1, 2), [S], 5)],
    ROOM_PICK_POSITION_EDGE_PIERCE_EAST: [((5, 2), [W], 4)],
    ROOM_PICK_POSITION_EDGE_PIERCE_WEST: [((1, 2), [E], 4)],
    ROOM_PICK_POSITION_EDGE_PIERCE_GEMS: [((1, 2), [E], 4)],
    ROOM_PICK_POSITION_EDGE_PIERCE_RARE: [((1, 2), [E], 4)],
    ROOM_PICK_POSITION_EDGE_PIERCE_RARE_GEMS: [((1, 2), [E], 4)],
    ROOM_PICK_POSITION_FRONT: [((2, 1), [E], 0)], # should always be true
    ROOM_PICK_POSITION_FRONT_GEMS: [((2, 1), [E], 0)], # should always be true
    ROOM_PICK_POSITION_FRONT_BACK_RARE: [((2, 1), [E], 0)], # should always be true
    ROOM_PICK_POSITION_FRONT_BACK_RARE_GEMS: [((2, 1), [E], 0)], # should always be true
    ROOM_PICK_POSITION_NORTH_PIERCE: [((2, 9), [S], 13)],
    ROOM_PICK_POSITION_NORTH_PIERCE_GEMS: [((2, 9), [S], 13)],
    ROOM_PICK_POSITION_SOUTH_PIERCE: [((2, 1), [N], 3)],
    ROOM_PICK_POSITION_ANTECHAMBER: [((3, 9), [S, E, W], 14)],
}
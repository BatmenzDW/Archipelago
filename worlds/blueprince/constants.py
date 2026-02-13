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


#####################
# CONTROL CONSTANTS #
#####################

# Enable room logic, when set to true, allows the rooms to be loaded into the world as items to be found.
# When false, "all rooms" will be available to the player "at the start"
ENABLE_ROOM_LOGIC = False


########################
# ROOM LOGIC POSITIONS #
########################

# Advance means going up that associated edge.
# Retreat means going down that edge.
# Edge creep means going up OR down that edge.
# Edge Pierce means going INTO the edge from non-edge.
# STANDALONE ARRAY (Outer Room)
# Still Unknown:
#
# Center (as in, specific requirements. may be non edge/first/last rows)
# Front
# Back
# North/South Pierce (assumed entering north/south from outside.)
# Rare
# Gems
# Tier


ROOM_PICK_POSITION_CENTER_TIER_1 = "CENTER - Tier 1"
ROOM_PICK_POSITION_CENTER_TIER_1_GEMS = "CENTER - Tier 1 G"
ROOM_PICK_POSITION_CENTER_TIER_2 = "CENTER - Tier 2"
ROOM_PICK_POSITION_CENTER_TIER_2_GEMS = "CENTER - Tier 2 G"
ROOM_PICK_POSITION_CENTER_TIER_3 = "CENTER - Tier 3"
ROOM_PICK_POSITION_CENTER_TIER_3_GEMS = "CENTER - Tier 3 G"
ROOM_PICK_POSITION_CENTER_RARE = "Center Rare"
ROOM_PICK_POSITION_CENTER_RARE_GEMS = "Center Rare G"
ROOM_PICK_POSITION_CORNER_RARE = "CORNER - RARE"
ROOM_PICK_POSITION_CORNER_RARE_GEMS = "CORNER - RARE G"
ROOM_PICK_POSITION_CORNER_TIER_1 = "CORNER - Tier 1"
ROOM_PICK_POSITION_CORNER_TIER_1_GEMS = "CORNER - Tier 1 G"
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
ROOM_PICK_POSITION_FRONT_TIER_1 = "FRONT - Tier 1"
ROOM_PICK_POSITION_FRONT_TIER_1_GEMS = "FRONT - Tier 1 G"
ROOM_PICK_POSITION_FRONT_BACK_RARE = "FRONTBACK - RARE"
ROOM_PICK_POSITION_FRONT_BACK_RARE_GEMS = "FRONTBACK G - RARE"
ROOM_PICK_POSITION_NORTH_PIERCE = "NORTH PIERCE"
ROOM_PICK_POSITION_NORTH_PIERCE_GEMS = "NORTH PIERCE G"
ROOM_PICK_POSITION_SOUTH_PIERCE = "SOUTH PIERCE"
ROOM_PICK_POSITION_STANDALONE = "STANDALONE ARRAY"
ROOM_PICK_POSITION_STANDALONE_FULL = "STANDALONE ARRAY FULL"

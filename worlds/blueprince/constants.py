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

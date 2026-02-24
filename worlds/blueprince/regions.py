from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Entrance, Region

from .data_rooms import rooms, room_layout_lists
from .data_items import sanctum_keys
from .constants import *

if TYPE_CHECKING:
    from .world import BluePrinceWorld

def create_and_connect_regions(world: BluePrinceWorld) -> None:

    ##################
    # CREATE REGIONS #
    ##################

    # (area off the 9'oclock of the gear on the underground map.)
    abandoned_mine = Region("Abandoned Mine", world.player, world.multiworld)

    # Area to the left of the reservoir not past minecart on map.
    excavation_tunnel = Region("Excavation Tunnel", world.player, world.multiworld)

    basement = Region("Basement", world.player, world.multiworld)
    catacombs = Region("Catacombs", world.player, world.multiworld)
    inner_sanctum = Region("Inner Sanctum", world.player, world.multiworld)
    orinda_aries_sanctum = Region("Orinda Aries Sanctum", world.player, world.multiworld)
    fenn_aries_sanctum = Region("Fenn Aries Sanctum", world.player, world.multiworld)
    arch_aries_sanctum = Region("Arch Aries Sanctum", world.player, world.multiworld)
    eraja_sanctum = Region("Eraja Sanctum", world.player, world.multiworld)
    corarica_sanctum = Region("Corarica Sanctum", world.player, world.multiworld)
    mora_jai_sanctum = Region("Mora Jai Sanctum", world.player, world.multiworld)
    verra_sanctum = Region("Verra Sanctum", world.player, world.multiworld)
    nuance_sanctum = Region("Nuance Sanctum", world.player, world.multiworld)

    the_precipice = Region("The Precipice", world.player, world.multiworld)
    reservoir_gear_side = Region("Reservoir Gear Side", world.player, world.multiworld)
    reservoir_fountain_side = Region("Reservoir Fountain Side", world.player, world.multiworld)
    reservoir_bottom = Region("Reservoir Bottom", world.player, world.multiworld)
    rotating_gear = Region("Rotating Gear", world.player, world.multiworld)
    safehouse = Region("Safehouse", world.player, world.multiworld)
    torch_chamber = Region("Torch Chamber", world.player, world.multiworld)
    the_underpass = Region("The Underpass", world.player, world.multiworld)
    aries_court = Region("Aries Court", world.player, world.multiworld)
    the_well = Region("The Well", world.player, world.multiworld)
    campsite = Region("Campsite", world.player, world.multiworld)
    grounds = Region("Grounds", world.player, world.multiworld)
    private_drive = Region("Private Drive", world.player, world.multiworld)
    apple_orchard = Region("Apple Orchard", world.player, world.multiworld)
    gemstone_cavern = Region("Gemstone Cavern", world.player, world.multiworld)
    sealed_entrance = Region("Sealed Entrance", world.player, world.multiworld)
    blakbridge_grotto = Region("Blackbridge Grotto", world.player, world.multiworld)
    orindian_ruins = Region("Orindian Ruins", world.player, world.multiworld)
    tunnel_area_entrance = Region("Tunnel Area Entrance", world.player, world.multiworld)
    west_path = Region("West Path", world.player, world.multiworld)
    outer_room = Region("Outer Room", world.player, world.multiworld)
    foundation_elevator = Region("Foundation Elevator", world.player, world.multiworld)
    tunnel_area_post_crates = Region("Tunnel Area Past Crates", world.player, world.multiworld)
    tunnel_area_post_normal_locked_door = Region("Tunnel Area Past Normal Locked Door", world.player, world.multiworld)
    tunnel_area_post_basement_key_door = Region("Tunnel Area Past Basement key Door", world.player, world.multiworld)
    tunnel_area_post_security_door = Region("Tunnel Area Past Security Door", world.player, world.multiworld)
    tunnel_area_post_weak_wall = Region("Tunnel Area Past Weak Wall", world.player, world.multiworld)
    tunnel_area_post_red_door = Region("Tunnel Area Past Red Door", world.player, world.multiworld)
    tunnel_area_post_candle_door = Region("Tunnel Area Past Candle Door", world.player, world.multiworld)
    tunnel_area_post_sealed_door = Region("Tunnel Area Past Sealed Door", world.player, world.multiworld)
    tunnel_area_post_blue_door = Region("Tunnel Area Past Blue Door", world.player, world.multiworld)
    atelier = Region("The Atelier", world.player, world.multiworld)

    regions = [
        abandoned_mine,
        excavation_tunnel,
        basement,
        catacombs,
        inner_sanctum,
        orinda_aries_sanctum,
        fenn_aries_sanctum,
        arch_aries_sanctum,
        eraja_sanctum,
        corarica_sanctum,
        mora_jai_sanctum,
        verra_sanctum,
        nuance_sanctum,
        the_precipice,
        reservoir_gear_side,
        reservoir_fountain_side,
        reservoir_bottom,
        rotating_gear,
        safehouse,
        torch_chamber,
        the_underpass,
        aries_court,
        the_well,
        campsite,
        grounds,
        private_drive,
        apple_orchard,
        gemstone_cavern,
        sealed_entrance,
        blakbridge_grotto,
        orindian_ruins,
        tunnel_area_entrance,
        west_path,
        outer_room,
        tunnel_area_post_crates,
        tunnel_area_post_normal_locked_door,
        tunnel_area_post_basement_key_door,
        tunnel_area_post_security_door,
        tunnel_area_post_weak_wall,
        tunnel_area_post_red_door,
        tunnel_area_post_candle_door,
        tunnel_area_post_sealed_door,
        tunnel_area_post_blue_door,
        atelier,
    ]

    for k, v in rooms.items():
        regions.append(Region(k, world.player, world.multiworld))

    world.multiworld.regions += regions

    ###################
    # CONNECT REGIONS #
    ###################

    # Get regions I am going to need later.
    tomb = world.get_region("Tomb")
    garage = world.get_region("Garage")
    library = world.get_region("Library")
    foundation = world.get_region("The Foundation")
    entrance_hall = world.get_region("Entrance Hall")
    antechamber = world.get_region("Antechamber")

    # Go through the rooms and connect them to the outer room/campsite (starting area)
    for k, v in rooms.items():
        room = world.get_region(k)

        if v[OUTER_ROOM_KEY]:

            # Connect outer room only rooms to outer room.
            outer_room.connect(
                room,
                f"Outer Room To {k}",
                lambda state, key=k: state.has(key, world.player),
            )
        else:

            # Connecting rooms to shrine'ed outer room is unnecessary
            # because the rooms will already be considered to have access via shrines very requirement.

            # Connect all other rooms to campsite (entrance hall?) if you have that room unlocked

            if k == "Antechamber":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Antechamber",
                    lambda state: (
                        state.has("Great Hall", world.player)
                        or (state.has("Greenhouse", world.player) and state.has("BROKEN LEVER", world.player))
                        or state.has("Mechanarium", world.player)
                        or (state.has("Weight Room", world.player) and state.has("Power Hammer", world.player))
                        or state.has("Secret Garden", world.player)
                        # This check is redundant
                        # or (state.has("Secret Garden", world.player) and state.has("Power Hammer", world.player))
                    ) and can_reach_pick_position("Antechamber", world, state),
                )
            elif k == "Room 46":
                antechamber.connect(
                    room,
                    "Antechamber To Room 46",
                    lambda state: state.has("North Lever Access", world.player),
                )
            elif k == "Bookshop":
                library.connect(
                    room,
                    "Library To Bookshop",
                    lambda state: state.has("Bookshop", world.player),
                )
            elif k == "The Armory":
                entrance_hall.connect(
                    room,
                    "Entrance Hall The Armory",
                    lambda state: state.has("The Armory", world.player) and 
                        state.can_reach_region("Aries Court", world.player) and 
                        can_reach_pick_position("The Armory", world, state),
                )
            # This is only necessary if we track the day count
            # elif k == "Gallery":
            #     entrance_hall.connect(
            #         room,
            #         f"Entrance Hall {k}",
            #         lambda state: state.has(k, world.player) and state.can_reach_region("Room 46", world.player),
            #     ) # Has reached Room 46 or Day Count is >= 46, but < 363; Very rarily possible without either with a Silver Key, but that seems to be a bug
            elif k == "Trophy Room":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Trophy Room",
                    lambda state: state.has("Trophy Room", world.player) and
                        (
                            state.can_reach_region("Room 46", world.player) or 
                            state.can_reach_location("Full House Trophy", world.player) or 
                            state.can_reach_location("Trophy of Invention", world.player) or 
                            state.can_reach_location("Trophy of Drafting", world.player) or 
                            state.can_reach_location("Trophy of Wealth", world.player)
                        ) and can_reach_pick_position("Trophy Room", world, state),
                ) # Has reached Room 46 or has one of the 4 listed Trophies
            elif k == "Gift Shop":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Gift Shop",
                    lambda state: state.has("Gift Shop", world.player) and 
                        state.can_reach_region("Room 46", world.player) and
                        can_reach_pick_position("Gift Shop", world, state),
                ) # Has reached Room 46
            elif k == "Room 8":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Room 8",
                    lambda state: state.has("Room 8", world.player) and 
                        (
                            state.has("Gallery", world.player) or 
                            state.has("Lost And Found", world.player)
                        ) and can_reach_pick_position("Room 8", world, state),
                ) # Can get Key 8
            # TODO: Add Her Ladyship's Chamber, it has weird requirements
            elif k == "Entrance Hall":
                continue
            else:

                entrance_hall.connect(
                    room,
                    f"Entrance Hall {k}",
                    lambda state, key=k: state.has(key, world.player) and
                        can_reach_pick_position(key, world, state),
                )

    foundation.connect(
        foundation_elevator,
        "Foundation To Foundation Elevator",
    )

    campsite.connect(
        private_drive,
        "Campsite To Private Drive",
    )
    campsite.connect(
        apple_orchard,
        "Campsite To Apple Orchard",
    )
    campsite.connect(
        gemstone_cavern,
        "Campsite To Gemstone Cavern",
        lambda state: state.has("Utility Closet", world.player),
    )  # Rules of are found in office emails. Solution is in office emails. May be able to adjust pattern?
    private_drive.connect(
        blakbridge_grotto,
        "Private Drive To Blackbridge Grotto",
        lambda state: state.has("Boiler Room", world.player) and state.has("Laboratory", world.player),
    )
    private_drive.connect(grounds, "Private Drive To Frounds")
    blakbridge_grotto.connect(
        orindian_ruins,
        "Blackbridge Grotto To Orindian Ruins",
        lambda state: state.has_all({"MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3"}, world.player),
    )
    grounds.connect(
        the_precipice,
        "Grounds To Precipice",
        lambda state: state.has_all(
            {
                "Apple Orchard Access",
                "School House Access",
                "Hovel Access",
                "Gemstone Cavern Access",
            },
            world.player,
        ),
    )
    grounds.connect(
        sealed_entrance,
        "Grounds To Sealed Entrance",
        lambda state: state.has("Power Hammer", world.player),
    )
    grounds.connect(entrance_hall, "Grounds To Entrance Hall")

    sealed_entrance.connect(
        grounds,
        "Sealed Entrance To Grounds",
        lambda state: state.has("Power Hammer", world.player),
    )
    the_precipice.connect(
        aries_court,
        "Precipice to Aries Court",
        lambda state: state.has_all(
            {
                "Chess Piece King",
                "Chess Piece Queen",
                "Chess Piece Rook",
                "Chess Piece Knight",
                "Chess Piece Bishop",
                "Chess Piece Pawn",
            },
            world.player,
        ),
    )
    sealed_entrance.connect(
        basement,
        "Sealed Entrance To Basement",
        lambda state: state.has("Power Hammer", world.player),
    )
    basement.connect(
        sealed_entrance,
        "Basement To Sealed Entrance",
        lambda state: state.has("Power Hammer", world.player),
    )
    basement.connect(
        reservoir_gear_side,
        "Basement To Reservoir Gear Side",
    )
    reservoir_gear_side.connect(
        basement,
        "Reservoir Gear Side To Basement",
    )
    reservoir_gear_side.connect(
        rotating_gear,
        "Reservoir Gear Side To Rotating Gear",
    )
    rotating_gear.connect(
        reservoir_gear_side,
        "Rotating Gear To Reservoir Gear Side",
    )
    the_underpass.connect(
        inner_sanctum,
        "The Underpass To Inner Sanctum",
    )

    sanctum_key_names = list(sanctum_keys.keys())

    inner_sanctum.connect(
        orinda_aries_sanctum,
        "Inner Sanctum To Orinda Aries Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 1),
    )
    inner_sanctum.connect(
        fenn_aries_sanctum,
        "Inner Sanctum To Fenn Aries Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 2),
    )
    inner_sanctum.connect(
        arch_aries_sanctum,
        "Inner Sanctum To Arch Aries Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 3),
    )
    inner_sanctum.connect(
        eraja_sanctum,
        "Inner Sanctum To Eraja Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 4),
    )
    inner_sanctum.connect(
        corarica_sanctum,
        "Inner Sanctum To Corarica Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 5),
    )
    inner_sanctum.connect(
        mora_jai_sanctum,
        "Inner Sanctum To Mora Jai Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 6),
    )
    inner_sanctum.connect(
        verra_sanctum,
        "Inner Sanctum To Verra Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 7),
    )
    inner_sanctum.connect(
        nuance_sanctum,
        "Inner Sanctum To Nuance Sanctum",
        lambda state: state.has_from_list_unique(sanctum_key_names, world.player, 8),
    )
    abandoned_mine.connect(
        excavation_tunnel,
        "Abandoned Mine To Excavation Tunnel",
    )
    excavation_tunnel.connect(
        abandoned_mine,
        "Excavation Tunnel To Abandoned Mine",
    )
    excavation_tunnel.connect(
        torch_chamber,
        "Excavation Tunnel To Torch Chamber",
    )
    excavation_tunnel.connect(
        reservoir_fountain_side,
        "Excavation Tunnel To Reservoir Fountain Side",
    )
    reservoir_fountain_side.connect(
        excavation_tunnel,
        "Reservoir Fountain Side To Excavation Tunnel",
    )
    the_well.connect(
        reservoir_fountain_side,
        "Well To Reservoir Fountain Side",
        lambda state: state.has("Pump Room", world.player) and state.has("BASEMENT KEY", world.player),
    )

    west_path.connect(
        grounds,
        "West Path To Grounds",
    )
    tomb.connect(
        catacombs,
        "Tomb to Catacombs",
    )
    catacombs.connect(
        excavation_tunnel,
        "Catacombs to Excavation Tunnel",
    )
    west_path.connect(
        outer_room,
        "West Path To Outer Room",
    )
    garage.connect(
        west_path,
        "Garage To West Path",
        lambda state: state.has("Garage", world.player)
        and (state.has("Utility Closet", world.player) or state.has("Boiler Room", world.player)),
    )
    foundation_elevator.connect(
        basement,
        "Foundation Elevator To Basement",
        lambda state: state.has("The Foundation", world.player) and state.has("BASEMENT KEY", world.player),
    )
    torch_chamber.connect(
        the_precipice,
        "Torch Chamber To Precipice",
        lambda state: state.has("Burning Glass Access", world.player) and state.has("TORCH", world.player),
    )

    grounds.connect(
        tunnel_area_entrance,
        "Grounds To Tunnel Area Entrance",
    )
    tunnel_area_entrance.connect(
        tunnel_area_post_crates,
        "Tunnel Area Entrance To Tunnel Area Post Crates",
        lambda state: state.has("Satellite Raised", world.player)
        and (state.has("Laboratory", world.player) or state.has("Blackbridge Grotto Access", world.player)),
    )
    tunnel_area_post_crates.connect(
        tunnel_area_post_normal_locked_door,
        "Tunnel Area Post Crates to Tunnel Area Post Normal Locked Door",
    )
    tunnel_area_post_normal_locked_door.connect(
        tunnel_area_post_basement_key_door,
        "Tunnel Area Post Normal Locked Door to Tunnel Area Post Basement Key",
        lambda state: state.has("BASEMENT KEY", world.player),
    )
    tunnel_area_post_basement_key_door.connect(
        tunnel_area_post_security_door,
        "Tunnel Area Post Basement Key to Tunnel Area Post Security Door",
        lambda state: state.has("KEYCARD", world.player),
    )
    tunnel_area_post_security_door.connect(
        tunnel_area_post_weak_wall,
        "Tunnel Area Post Security Door to Tunnel Area Post Weak Wall",
        lambda state: state.has("Power Hammer", world.player),
    )
    tunnel_area_post_weak_wall.connect(
        tunnel_area_post_red_door,
        "Tunnel Area Post Weak Wall to Tunnel Area Post Red Door",
        lambda state: state.has("Boiler Room", world.player),
    )
    tunnel_area_post_red_door.connect(
        tunnel_area_post_candle_door,
        "Tunnel Area Post Red Door to Tunnel Area Post Candle Door",
        lambda state: state.has("TORCH", world.player) or state.has("Burning Glass", world.player),
    )
    tunnel_area_post_candle_door.connect(
        tunnel_area_post_sealed_door,
        "Tunnel Area Post Candle Door to Tunnel Area Post Sealed Door",
        lambda state: state.has_all({"MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3"}, world.player),
    )
    tunnel_area_post_sealed_door.connect(
        tunnel_area_post_blue_door,
        "Tunnel Area Post Sealed Door to Tunnel Area Post Blue Door",
        lambda state: state.has("Blue Door Access", world.player),
        # No item called blue door access RN.
    )

    ###################################
    # COMPLEX REGION CONNECTION LOGIC #
    ###################################
    reservoir_gear_side.connect(
        safehouse,
        "Reservoir Gear Side To Safehouse",
        lambda state: state.has("Pump Room", world.player) and state.can_reach_region("Reservoir Fountain Side", world.player) and state.can_reach_region("Basement", world.player),
    )  # Pump Room & Fountain Side Access. (take fountain side to gear side, lower again, and make it back down on gear side.)
    reservoir_gear_side.connect(
        reservoir_bottom,
        "Reservoir Gear Side To Reservoir Bottom",
        lambda state: state.has("Pump Room", world.player) and state.has("Boiler Room", world.player) and state.can_reach_region("Basement", world.player),
    )  # Pump Room and boiler room (both this and safehouse require ability to get to gear side NOT through well side.)
    rotating_gear.connect(
        the_underpass,
        "Rotating Gear To Underpass",
        lambda state: state.can_reach_region("Reservoir Fountain Side", world.player) and state.can_reach_region("Reservoir Gear Side", world.player),
    )  # Require Dual side access
    rotating_gear.connect(
        abandoned_mine,
        "Rotating Gear To Abandoned Mine",
    )
    reservoir_fountain_side.connect(
        reservoir_gear_side,
        "Reservoir Fountain Side To Reservoir Gear Side",
        lambda state: state.has("Pump Room", world.player),
    )  # Pump Room

    outer_room.connect(
        atelier,
        "Outer Room To Atelier",
        lambda state: state.has("Secret Passage", world.player) and state.has("Watering Can", world.player),
    )

def simple_reachability_test(room: str, state: CollectionState, world: BluePrinceWorld) -> bool:
    """
    Uses a simple check of how many rooms are in the pool to determine if a pick position is reachable. Only used if ENABLE_ADVANCED_ROOM_ACCESS_LOGIC is False.
    """
    room_data = rooms[room]
    positions_types = room_data[ROOM_PICK_POSITIONS_KEY]

    for pt in positions_types:
        if state.has(pt, world.player):
            return True
        
    pool_count = state.count_from_list(room_layout_lists[INNER_ROOM_KEY], world.player)

    for pt in positions_types:
        targets = POSITION_CHECKS[pt]

        for target in targets:
            target_count = target[2] if len(target) > 2 else 100_000
            if pool_count >= target_count:
                state.collect(pt, world.player)
                return True


def can_reach_pick_position(room: str, world: BluePrinceWorld, state: CollectionState) -> bool:
    """
    Use depth first search to determine if a the pick position is reachable with the current inventory.
    """

    if not ENABLE_ADVANCED_ROOM_ACCESS_LOGIC:
        return simple_reachability_test(room, state, world)

    # TODO: figure out how to cache unreachable pick locations and clear cache when a new region logic pass starts

    room_data = rooms[room]
    
    positions_types = room_data[ROOM_PICK_POSITIONS_KEY]

    for pt in positions_types:
        if state.has(pt, world.player):
            return True

    inventory = {
        ROOM_LAYOUT_TYPE_X: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_X], world.player),
        ROOM_LAYOUT_TYPE_T: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_T], world.player),
        ROOM_LAYOUT_TYPE_I: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_I], world.player),
        ROOM_LAYOUT_TYPE_J: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_J], world.player),
        # ROOM_LAYOUT_TYPE_D: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_D], world.player),
    }

    # This check shouldn't be necessary in theory, but adding it in case we later want to check if a room not in the pool is reachable for some reason.
    if (state.has(room, world.player) and room_data[ROOM_LAYOUT_TYPE_KEY] in [ROOM_LAYOUT_TYPE_I, ROOM_LAYOUT_TYPE_J, ROOM_LAYOUT_TYPE_T, ROOM_LAYOUT_TYPE_X]):
        inventory[room_data[ROOM_LAYOUT_TYPE_KEY]] -= 1

    start = (3, 1)

    for pt in positions_types:
        targets = POSITION_CHECKS[pt]

        visited = set()
        memo = set()

        visited.add(start)

        for target in targets:
            target_cell = target[0]
            target_sides = [OPPOSITE[x] for x in target[1]]

            for d in [N, E, S, W]:
                if not 0b1111 & d:
                    continue
                new_x, new_y = start[0] + DIRS[d][0], start[1] + DIRS[d][1]
                remaining = inventory.copy()
                if depth_first_tile_search(new_x, new_y, d, remaining, visited):
                    state.collect(pt, world.player)
                    return True
    
    # TODO: add an additional pass for when Foundation is in pool

    def get_shape_for_tile_type(tile_type):
        if tile_type == ROOM_LAYOUT_TYPE_I:
            return [N | S, E | W]
        elif tile_type == ROOM_LAYOUT_TYPE_J:
            return [N | E, E | S, S | W, W | N]
        elif tile_type == ROOM_LAYOUT_TYPE_T:
            return [N | E | S, E | S | W, S | W | N, W | N | E]
        elif tile_type == ROOM_LAYOUT_TYPE_X:
            return [N | E | S | W]
        else:
            return []

    def inside(x, y):
        return 1 <= x <= 9 and 1 <= y <= 9

    def is_valid_move(x, y, shape):
        for d in DIRS:
            if shape & d:
                nx = x + DIRS[d][0]
                ny = y + DIRS[d][1]
                if not inside(nx, ny) and not ((x, y) in target_cell and d in target_sides):
                    return False
        return True
    
    # Deconstruct the shape mask, except for the incoming side
    def get_sides_for_shape(shape, side):
        result = []
        if shape == 0:
            return result
        
        if shape & N and side != N:
            result.append(N)
        if shape & E and side != E:
            result.append(E)
        if shape & S and side != S:
            result.append(S)
        if shape & W and side != W:
            result.append(W)

        return result
    
    def depth_first_tile_search(x, y, side, inventory, visited):
        state_key = (x, y, side,
                     inventory[ROOM_LAYOUT_TYPE_I],
                     inventory[ROOM_LAYOUT_TYPE_J],
                     inventory[ROOM_LAYOUT_TYPE_T],
                     inventory[ROOM_LAYOUT_TYPE_X])
        if state_key in memo:
            return False
        if (x, y) == target_cell:
            # print(f"Reached target cell {target_cell} with side {get_dir_name(side)}")
            if side in target_sides:
                return True
        
        visited.add((x, y))

        if not inside(x, y):
            visited.remove((x, y))
            memo.add(state_key)
            return False

        # print(f"At {(x, y)} coming from {get_dir_name(side)}, trying to move to {(new_x, new_y)}, inventory: {inventory}")
        
        for piece_type in inventory:
            if inventory[piece_type] > 0:
                for shape in get_shape_for_tile_type(piece_type):
                    if not shape & OPPOSITE[side]:
                        continue

                    inventory[piece_type] -= 1

                    for new_side in get_sides_for_shape(shape, OPPOSITE[side]):
                        new_x, new_y = x + DIRS[new_side][0], y + DIRS[new_side][1]
                        if (new_x, new_y) not in visited and is_valid_move(new_x, new_y, shape):

                            if depth_first_tile_search(new_x, new_y, new_side, inventory, visited):
                                return True
                    
                    inventory[piece_type] += 1
        
        visited.remove((x, y))
        memo.add(state_key)

        return False
    
    return False
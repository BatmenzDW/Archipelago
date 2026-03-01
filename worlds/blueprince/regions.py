from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Entrance, Region

from .data_rooms import rooms, core_rooms, classrooms, room_layout_lists
from .data_items import sanctum_keys
from .constants import *
from .room_min_pieces import *
from .data_other_locations import can_reach_item_location

if TYPE_CHECKING:
    from .world import BluePrinceWorld

def create_and_connect_regions(world: BluePrinceWorld) -> None:
    world.explicit_indirect_conditions = False
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
                        state.can_reach_region("Great Hall", world.player)
                        or (state.can_reach_region("Greenhouse", world.player) and can_reach_item_location("BROKEN LEVER", state, world))
                        or state.can_reach_region("Mechanarium", world.player)
                        or (state.can_reach_region("Weight Room", world.player) and can_reach_item_location("Power Hammer", state, world))
                        or state.can_reach_region("Secret Garden", world.player)
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
                ) # Can only be drafted from the library, so only requires having the bookshop as an item.
            elif k == "The Armory":
                entrance_hall.connect(
                    room,
                    "Entrance Hall The Armory",
                    lambda state: state.can_reach_region("Aries Court", world.player) and can_reach_pick_position("The Armory", world, state),
                )
            #
            # This is only necessary if we track the day count
            #
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
                    lambda state: (
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
                    lambda state: state.can_reach_region("Room 46", world.player) and can_reach_pick_position("Gift Shop", world, state),
                ) # Has reached Room 46
            elif k == "Room 8":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Room 8",
                    lambda state: can_reach_item_location("KEY 8", state, world) and can_reach_pick_position("Room 8", world, state),
                ) # Has Key 8
            elif k == "Secret Garden":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Secret Garden",
                    lambda state: can_reach_item_location("SECRET GARDEN KEY", state, world) and can_reach_pick_position("Secret Garden", world, state),
                )
            elif k in classrooms and k != "Classroom 1":
                if k == "Classroom Exam":
                    prev = "Classroom 8"
                else:
                    prev = f"Classroom {int(k[-1]) - 1}"
                world.get_region(prev).connect(
                    room,
                    f"{prev} {k}",
                    lambda state: state.has(k, world.player),
                )
            
            # TODO: Add Her Ladyship's Chamber, it has weird requirements
            elif k == "Entrance Hall":
                continue
            else:

                entrance_hall.connect(
                    room,
                    f"Entrance Hall {k}",
                    lambda state, key=k: can_reach_pick_position(key, world, state),
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
        lambda state: state.can_reach_region("Utility Closet", world.player),
    )  # Rules of are found in office emails. Solution is in office emails. May be able to adjust pattern?
    private_drive.connect(
        blakbridge_grotto,
        "Private Drive To Blackbridge Grotto",
        lambda state: state.can_reach_region("Boiler Room", world.player) and state.can_reach_region("Laboratory", world.player),
    )
    private_drive.connect(grounds, "Private Drive To Grounds")
    blakbridge_grotto.connect(
        orindian_ruins,
        "Blackbridge Grotto To Orindian Ruins",
        lambda state: all(can_reach_item_location(x, state, world) for x in ["MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3"]) 
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
        lambda state: can_reach_item_location("Power Hammer", state, world),
    )
    grounds.connect(entrance_hall, "Grounds To Entrance Hall")

    sealed_entrance.connect(
        grounds,
        "Sealed Entrance To Grounds",
        lambda state: can_reach_item_location("Power Hammer", state, world),
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
        lambda state: can_reach_item_location("Power Hammer", state, world),
    )
    basement.connect(
        sealed_entrance,
        "Basement To Sealed Entrance",
        lambda state: can_reach_item_location("Power Hammer", state, world),
    )
    basement.connect(
        reservoir_gear_side,
        "Basement To Reservoir Gear Side",
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
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 1,
    )
    inner_sanctum.connect(
        fenn_aries_sanctum,
        "Inner Sanctum To Fenn Aries Sanctum",
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 2,
    )
    inner_sanctum.connect(
        arch_aries_sanctum,
        "Inner Sanctum To Arch Aries Sanctum",
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 3,
    )
    inner_sanctum.connect(
        eraja_sanctum,
        "Inner Sanctum To Eraja Sanctum",
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 4,
    )
    inner_sanctum.connect(
        corarica_sanctum,
        "Inner Sanctum To Corarica Sanctum",
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 5,
    )
    inner_sanctum.connect(
        mora_jai_sanctum,
        "Inner Sanctum To Mora Jai Sanctum",
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 6,
    )
    inner_sanctum.connect(
        verra_sanctum,
        "Inner Sanctum To Verra Sanctum",
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 7,
    )
    inner_sanctum.connect(
        nuance_sanctum,
        "Inner Sanctum To Nuance Sanctum",
        lambda state: len([x for x in sanctum_key_names if can_reach_item_location(x, state, world)]) >= 8,
    )
    abandoned_mine.connect(
        excavation_tunnel,
        "Abandoned Mine To Excavation Tunnel",
        lambda state: state.can_reach_region("Reservoir Fountain Side", world.player)
    )
    excavation_tunnel.connect(
        abandoned_mine,
        "Excavation Tunnel To Abandoned Mine",
        lambda state: state.can_reach_region("Reservoir Fountain Side", world.player)
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
        lambda state: can_reach_item_location("BASEMENT KEY", state, world),
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
        lambda state: state.can_reach_region("Utility Closet", world.player) or state.can_reach_region("Boiler Room", world.player),
    )
    foundation_elevator.connect(
        basement,
        "Foundation Elevator To Basement",
        lambda state: state.can_reach_region("The Foundation", world.player) and can_reach_item_location("BASEMENT KEY", state, world),
    )
    torch_chamber.connect(
        the_precipice,
        "Torch Chamber To Precipice",
        lambda state: can_reach_item_location("Burning Glass", state, world) or can_reach_item_location("TORCH", state, world),
    )

    grounds.connect(
        tunnel_area_entrance,
        "Grounds To Tunnel Area Entrance",
    )
    tunnel_area_entrance.connect(
        tunnel_area_post_crates,
        "Tunnel Area Entrance To Tunnel Area Post Crates",
        lambda state: state.has("Satellite Raised", world.player)
        and (state.can_reach_region("Laboratory", world.player) or state.can_reach_region("Blackbridge Grotto", world.player)),
    )
    tunnel_area_post_crates.connect(
        tunnel_area_post_normal_locked_door,
        "Tunnel Area Post Crates to Tunnel Area Post Normal Locked Door",
    )
    tunnel_area_post_normal_locked_door.connect(
        tunnel_area_post_basement_key_door,
        "Tunnel Area Post Normal Locked Door to Tunnel Area Post Basement Key",
        lambda state: can_reach_item_location("BASEMENT KEY", state, world),
    )
    tunnel_area_post_basement_key_door.connect(
        tunnel_area_post_security_door,
        "Tunnel Area Post Basement Key to Tunnel Area Post Security Door",
        lambda state: can_reach_item_location("KEYCARD", state, world),
    )
    tunnel_area_post_security_door.connect(
        tunnel_area_post_weak_wall,
        "Tunnel Area Post Security Door to Tunnel Area Post Weak Wall",
        lambda state: can_reach_item_location("Power Hammer", state, world),
    )
    tunnel_area_post_weak_wall.connect(
        tunnel_area_post_red_door,
        "Tunnel Area Post Weak Wall to Tunnel Area Post Red Door",
        lambda state: state.can_reach_region("Boiler Room", world.player),
    )
    tunnel_area_post_red_door.connect(
        tunnel_area_post_candle_door,
        "Tunnel Area Post Red Door to Tunnel Area Post Candle Door",
        lambda state: can_reach_item_location("Burning Glass", state, world) or can_reach_item_location("TORCH", state, world),
    )
    tunnel_area_post_candle_door.connect(
        tunnel_area_post_sealed_door,
        "Tunnel Area Post Candle Door to Tunnel Area Post Sealed Door",
        lambda state: all(can_reach_item_location(x, state, world) for x in ["MICROCHIP 1", "MICROCHIP 2", "MICROCHIP 3"]),
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
        lambda state: can_reach_pick_position("Pump Room", world, state) 
        and state.can_reach_region("Reservoir Fountain Side", world.player) 
        and state.can_reach_region("Basement", world.player),
    )  # Pump Room & Fountain Side Access. (take fountain side to gear side, lower again, and make it back down on gear side.)
    reservoir_gear_side.connect(
        reservoir_bottom,
        "Reservoir Gear Side To Reservoir Bottom",
        lambda state: state.can_reach_region("Pump Room", world.player) 
        and state.can_reach_region("Boiler Room", world.player) 
        and state.can_reach_region("Basement", world.player),
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
        lambda state: state.can_reach_region("Pump Room", world.player),
    )  # Pump Room

    outer_room.connect(
        atelier,
        "Outer Room To Atelier",
        lambda state: state.can_reach_region("Secret Passage", world.player) 
        and state.can_reach_region("Shrine", world.player)
        and can_reach_item_location("WATERING CAN", state, world),
    )

    grounds.connect(
        the_well,
        "Grounds To The Well",
        lambda state: state.can_reach_region("Pump Room", world.player),
    )

def can_reach_pick_position(room: str, world: BluePrinceWorld, state: CollectionState) -> bool:
    """
    Use pre-calculated tables to determine if a the pick position is reachable with the current inventory.
    """

    if room not in core_rooms and not state.has(room, world.player):
        return False
    
    room_data = rooms[room]
    
    positions_types = room_data[ROOM_PICK_POSITIONS_KEY]

    inventory = {
        ROOM_LAYOUT_TYPE_X: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_X], world.player),
        ROOM_LAYOUT_TYPE_T: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_T], world.player),
        ROOM_LAYOUT_TYPE_I: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_I], world.player),
        ROOM_LAYOUT_TYPE_J: state.count_from_list(room_layout_lists[ROOM_LAYOUT_TYPE_J], world.player),
    }

    total_inventory = sum(inventory.values())

    if (room_data[ROOM_LAYOUT_TYPE_KEY] in inventory and inventory[room_data[ROOM_LAYOUT_TYPE_KEY]] > 0):
        inventory[room_data[ROOM_LAYOUT_TYPE_KEY]] -= 1

    for pt in positions_types:
        if pt not in POSITION_MINIMUM_PIECES or total_inventory < POSITION_MINIMUM_TOTAL_PIECES[pt]:
            continue
        if matches_minimum_inventory(POSITION_MINIMUM_PIECES[pt], inventory):
            return True
        
    return False

def matches_minimum_inventory(required: list[tuple[int]], inventory: dict[str, int]) -> bool:
    inv = tuple(inventory[k] for k in inventory)
    for req in required:
        if all(inv[i] >= req[i] for i in range(4)):
            return True
        
    return False
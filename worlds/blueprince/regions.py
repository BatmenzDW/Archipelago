from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Entrance, Region
from rule_builder.rules import *
from .options import TrophySanity

from .data_rooms import rooms, core_rooms, classrooms, room_layout_lists
from .data_items import sanctum_keys
from .constants import *
from .room_min_pieces import *
from .dares import can_reach_with_dares
from .rules import *

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
    pool = world.get_region("The Pool")

    # Go through the rooms and connect them to the outer room/campsite (starting area)
    for k, v in rooms.items():
        room = world.get_region(k)

        if v[OUTER_ROOM_KEY]:

            # Connect outer room only rooms to outer room.
            outer_room.connect(
                room,
                f"Outer Room To {k}",
                Has(k),
            )
        else:

            # Connecting rooms to shrine'ed outer room is unnecessary
            # because the rooms will already be considered to have access via shrines very requirement.

            # Connect all other rooms to campsite (entrance hall?) if you have that room unlocked

            if k == "Antechamber":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Antechamber",
                    (CanReachPickPosition("Antechamber") &
                    (
                        CanReachRegion("Great Hall") | 
                        (CanReachRegion("Greenhouse") & CanReachItemLocation("BROKEN LEVER", parent_region_name="Entrance Hall")) |
                        MechanariumDoorRule(1) |
                        (CanReachRegion("Weight Room") & CanReachItemLocation("Power Hammer", parent_region_name="Entrance Hall")) |
                        CanReachRegion("Secret Garden")
                        # This check is redundant
                        # (CanReachRegion("Secret Garden") & CanReachItemLocation("Power Hammer"))
                    )),
                )

            elif k == "Room 46":
                antechamber.connect(
                    room,
                    "Antechamber To Room 46",
                    Has("North Lever Access"),
                )
            elif k == "Bookshop":
                library.connect(
                    room,
                    "Library To Bookshop",
                    Has("Bookshop"),
                ) # Can only be drafted from the library, so only requires having the bookshop as an item.
            elif k == "The Armory":
                entrance_hall.connect(
                    room,
                    "Entrance Hall The Armory",
                    (CanReachRegion("Aries Court") & CanReachPickPosition("The Armory")),
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
                    ((CanReachRegion("Room 46") | Or(
                                CanReachLocation("Full House Trophy", parent_region_name="Entrance Hall"),
                                CanReachLocation("Trophy of Invention", parent_region_name="Workshop"),
                                CanReachLocation("Trophy of Drafting", parent_region_name="Mail Room"), 
                                CanReachLocation("Trophy of Wealth", parent_region_name="Showroom"),
                                options=[OptionFilter(TrophySanity, True)]
                            )
                        ) & CanReachPickPosition("Trophy Room")),
                ) # Has reached Room 46 or has one of the 4 listed Trophies
            elif k == "Gift Shop":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Gift Shop",
                    (CanReachRegion("Room 46") & CanReachPickPosition("Gift Shop")),
                ) # Has reached Room 46
            elif k == "Room 8":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Room 8",
                    (CanReachItemLocation("KEY 8", parent_region_name="Entrance Hall") & CanReachPickPosition("Room 8", always_have=True)),
                ) # Has Key 8
            elif k == "Secret Garden":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Secret Garden",
                    (CanReachItemLocation("SECRET GARDEN KEY", parent_region_name="Entrance Hall") & CanReachPickPosition("Secret Garden", always_have=True)),
                )
            elif k in classrooms and k != "Classroom 1":
                if k == "Classroom Exam":
                    prev = "Classroom 8"
                    cnum = 9
                else:
                    cnum = int(k[-1])
                    prev = f"Classroom {cnum - 1}"
                world.get_region(prev).connect(
                    room,
                    f"{prev} {k}",
                    Has("Progressive Classroom", count=cnum) & CanReachRegion("Schoolhouse"),
                )
            elif k == "Classroom 1":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Classroom 1",
                    Has("Progressive Classroom"),
                )

            elif k in ["Boiler Room", "Pump Room", "Sauna"]:
                pool.connect(
                    room,
                    f"The Pool To {k}",
                    Has(k)
                )
            
            elif k == "Morning Room":
                entrance_hall.connect(
                    room,
                    "Entrance Hall Morning Room",
                    CanReachPickPosition("Morning Room") & CanReachRegion("Kitchen"), # Requires Kitchen or Breakfast Nook, but we don't handle room upgrades yet.
                )

            # TODO: Add Her Ladyship's Chamber, it has weird requirements
            elif k == "Entrance Hall":
                continue
            else:

                entrance_hall.connect(
                    room,
                    f"Entrance Hall {k}",
                    CanReachPickPosition(k),
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
        (CanReachRegion("Utility Closet")),
    )  # Rules of are found in office emails. Solution is in office emails. May be able to adjust pattern?
    private_drive.connect(
        blakbridge_grotto,
        "Private Drive To Blackbridge Grotto",
        (CanReachRegion("Boiler Room") & CanReachRegion("Laboratory")),
    )
    private_drive.connect(grounds, "Private Drive To Grounds")
    blakbridge_grotto.connect(
        orindian_ruins,
        "Blackbridge Grotto To Orindian Ruins",
        (CanReachItemLocation("MICROCHIP 1", parent_region_name="West Path") & CanReachItemLocation("MICROCHIP 2", parent_region_name="Entrance Hall") & CanReachItemLocation("MICROCHIP 3", parent_region_name="Blackbridge Grotto")),
    )
    grounds.connect(
        the_precipice,
        "Grounds To Precipice",
        (CanReachRegion("Apple Orchard") & CanReachRegion("Schoolhouse") & CanReachRegion("Hovel") & CanReachRegion("Gemstone Cavern")),
    )
    grounds.connect(
        sealed_entrance,
        "Grounds To Sealed Entrance",
        (CanReachItemLocation("Power Hammer", parent_region_name="Workshop")),
    )
    grounds.connect(entrance_hall, "Grounds To Entrance Hall")

    sealed_entrance.connect(
        grounds,
        "Sealed Entrance To Grounds",
        (CanReachItemLocation("Power Hammer", parent_region_name="Workshop")),
    )
    the_precipice.connect(
        aries_court,
        "Precipice to Aries Court",
        And(
            *[Has(piece) for piece in [
                "Chess Piece King",
                "Chess Piece Queen",
                "Chess Piece Rook",
                "Chess Piece Knight",
                "Chess Piece Bishop",
                "Chess Piece Pawn",
            ]]
        ),
    )
    sealed_entrance.connect(
        basement,
        "Sealed Entrance To Basement",
        CanReachItemLocation("Power Hammer", parent_region_name="Workshop"),
    )
    basement.connect(
        sealed_entrance,
        "Basement To Sealed Entrance",
        CanReachItemLocation("Power Hammer", parent_region_name="Workshop"),
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

    inner_sanctum.connect(
        orinda_aries_sanctum,
        "Inner Sanctum To Orinda Aries Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=1),
    )
    inner_sanctum.connect(
        fenn_aries_sanctum,
        "Inner Sanctum To Fenn Aries Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=2),
    )
    inner_sanctum.connect(
        arch_aries_sanctum,
        "Inner Sanctum To Arch Aries Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=3),
    )
    inner_sanctum.connect(
        eraja_sanctum,
        "Inner Sanctum To Eraja Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=4),
    )
    inner_sanctum.connect(
        corarica_sanctum,
        "Inner Sanctum To Corarica Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=5),
    )
    inner_sanctum.connect(
        mora_jai_sanctum,
        "Inner Sanctum To Mora Jai Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=6),
    )
    inner_sanctum.connect(
        verra_sanctum,
        "Inner Sanctum To Verra Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=7),
    )
    inner_sanctum.connect(
        nuance_sanctum,
        "Inner Sanctum To Nuance Sanctum",
        CanReachItemLocationsFromList(*sanctum_keys, count=8),
    )
    abandoned_mine.connect(
        excavation_tunnel,
        "Abandoned Mine To Excavation Tunnel",
        CanReachRegion("Reservoir Fountain Side"),
    )
    excavation_tunnel.connect(
        abandoned_mine,
        "Excavation Tunnel To Abandoned Mine",
        CanReachRegion("Reservoir Fountain Side"),
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
        CanReachItemLocation("BASEMENT KEY", parent_region_name="Antechamber"),
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
        Or(CanReachRegion("Utility Closet"), CanReachRegion("Boiler Room")),
    )
    foundation_elevator.connect(
        basement,
        "Foundation Elevator To Basement",
        And(
            CanReachRegion("The Foundation"),
            CanReachItemLocation("BASEMENT KEY", parent_region_name="Antechamber"),
        ),
    )
    torch_chamber.connect(
        the_precipice,
        "Torch Chamber To Precipice",
        Or(
            CanReachItemLocation("Burning Glass", parent_region_name="Workshop"),
            CanReachItemLocation("TORCH", parent_region_name="The Armory"),
        ),
    )

    grounds.connect(
        tunnel_area_entrance,
        "Grounds To Tunnel Area Entrance",
    )
    tunnel_area_entrance.connect(
        tunnel_area_post_crates,
        "Tunnel Area Entrance To Tunnel Area Post Crates",
        And(
            Has("Satellite Raised"),
            Or(
                CanReachRegion("Laboratory"),
                CanReachRegion("Blackbridge Grotto"),
            ),
        ),
    )
    tunnel_area_post_crates.connect(
        tunnel_area_post_normal_locked_door,
        "Tunnel Area Post Crates to Tunnel Area Post Normal Locked Door",
    )
    tunnel_area_post_normal_locked_door.connect(
        tunnel_area_post_basement_key_door,
        "Tunnel Area Post Normal Locked Door to Tunnel Area Post Basement Key",
        CanReachItemLocation("BASEMENT KEY", parent_region_name="Antechamber"),
    )
    tunnel_area_post_basement_key_door.connect(
        tunnel_area_post_security_door,
        "Tunnel Area Post Basement Key to Tunnel Area Post Security Door",
        CanReachItemLocation("KEYCARD", parent_region_name="Entrance Hall"),
    )
    tunnel_area_post_security_door.connect(
        tunnel_area_post_weak_wall,
        "Tunnel Area Post Security Door to Tunnel Area Post Weak Wall",
        CanReachItemLocation("Power Hammer", parent_region_name="Workshop"),
    )
    tunnel_area_post_weak_wall.connect(
        tunnel_area_post_red_door,
        "Tunnel Area Post Weak Wall to Tunnel Area Post Red Door",
        CanReachRegion("Boiler Room"),
    )
    tunnel_area_post_red_door.connect(
        tunnel_area_post_candle_door,
        "Tunnel Area Post Red Door to Tunnel Area Post Candle Door",
        Or(
            CanReachItemLocation("Burning Glass", parent_region_name="Workshop"),
            CanReachItemLocation("TORCH", parent_region_name="The Armory"),
        ),
    )
    tunnel_area_post_candle_door.connect(
        tunnel_area_post_sealed_door,
        "Tunnel Area Post Candle Door to Tunnel Area Post Sealed Door",
        And(
            CanReachItemLocation("MICROCHIP 1", parent_region_name="West Path"),
            CanReachItemLocation("MICROCHIP 2", parent_region_name="Entrance Hall"),
            CanReachItemLocation("MICROCHIP 3", parent_region_name="Blackbridge Grotto"),
        ),
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
        And(
            CanReachPickPosition("Pump Room"),
            CanReachRegion("Reservoir Fountain Side"),
            CanReachRegion("Basement"),
        ),
    )  # Pump Room & Fountain Side Access. (take fountain side to gear side, lower again, and make it back down on gear side.)
    reservoir_gear_side.connect(
        reservoir_bottom,
        "Reservoir Gear Side To Reservoir Bottom",
        And(
            CanReachRegion("Pump Room"),
            CanReachRegion("Reservoir Fountain Side"),
            CanReachRegion("Basement"),
        ),
    )  # Pump Room and boiler room (both this and safehouse require ability to get to gear side NOT through well side.)
    rotating_gear.connect(
        the_underpass,
        "Rotating Gear To Underpass",
        And(
            CanReachRegion("Reservoir Fountain Side"),
            CanReachRegion("Reservoir Gear Side"),
        ),
    )  # Require Dual side access
    rotating_gear.connect(
        abandoned_mine,
        "Rotating Gear To Abandoned Mine",
    )
    reservoir_fountain_side.connect(
        reservoir_gear_side,
        "Reservoir Fountain Side To Reservoir Gear Side",
        CanReachRegion("Pump Room"),
    )  # Pump Room

    outer_room.connect(
        atelier,
        "Outer Room To Atelier",
        And(
            CanReachRegion("Secret Passage"),
            CanReachRegion("Shrine"),
            CanReachItemLocation("WATERING CAN", parent_region_name="Entrance Hall"),
        ),
    )

    grounds.connect(
        the_well,
        "Grounds To The Well",
        CanReachRegion("Pump Room"),
    )
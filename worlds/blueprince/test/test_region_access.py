from BaseClasses import CollectionState, Location
from ..options import GoalType
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *

class TestRegionAccess(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "goal_type": GoalType.option_room46,
    }

    def test_starting_from_campsite(self) -> None:
        self.assertTrue(self.can_reach_region("Campsite"))
        self.assertTrue(self.can_reach_region("Entrance Hall"))
        self.assertTrue(self.can_reach_region("Grounds"))
        self.assertTrue(self.can_reach_region("Private Drive"))
        self.assertTrue(self.can_reach_region("Apple Orchard"))
        self.assertTrue(self.can_reach_region("Tunnel Area Entrance"))

    # def test_inner_rooms_requires_room_item(self) -> None:

    #     for room,v in rooms.items():
    #         if room in core_rooms or v[OUTER_ROOM_KEY]:
    #             continue

    #         self.assertFalse(self.can_reach_region(room), f"{room} should not be reachable without having the room as an item")
    #         self.collect_by_name(room)
    #         self.assertTrue(self.can_reach_region(room), f"{room} should be reachable after collecting the room as an item")
    
    def test_build_path_to_garage(self) -> None:
        if not self.multiworld.state.has("Garage", self.player):
            self.assertFalse(self.can_reach_region("Garage"), "Garage should not be reachable without having the Garage as an item")
            self.collect_by_name("Garage")
        if not self.can_reach_region("Garage"):
            self.collect_by_name("Hallway")
            self.collect_by_name("Office")
        self.assertTrue(self.can_reach_region("Garage"), "Garage should be reachable after collecting at least 1 I piece and at least 1 J piece as items")

    def test_outer_room_requires_garage_utility_closet(self) -> None:
        self.collect_all_but(["Garage", "Utility Closet", "Boiler Room"])
        self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Utility Closet as an item")
        self.collect_by_name("Utility Closet")
        self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Garage")
        self.assertTrue(self.can_reach_region("Outer Room"), "Outer Room should be reachable after collecting the Garage as an item")
    
    def test_outer_room_requires_garage_boiler_room(self) -> None:
        self.collect_all_but(["Garage", "Boiler Room", "Utility Closet"])
        if not self.multiworld.state.has("Garage", self.player):
            self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Garage as an item")
            self.collect_by_name("Garage")
        if not self.multiworld.state.has("Boiler Room", self.player):
            self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Boiler Room as an item")
            self.collect_by_name("Boiler Room")
        self.assertTrue(self.can_reach_region("Outer Room"), "Outer Room should be reachable after collecting the Garage as an item")

    def test_outer_rooms_require_room_item(self) -> None:
        self.collect_by_name("Hallway")
        self.collect_by_name("Office")
        self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Garage")
        self.collect_by_name("Utility Closet")
        self.assertTrue(self.can_reach_region("Outer Room"), "Outer Room should be reachable after collecting the Garage as an item")

        for room,v in rooms.items():
            if not v[OUTER_ROOM_KEY]:
                continue

            self.assertFalse(self.can_reach_region(room), f"{room} should not be reachable without having the room as an item")
            self.collect_by_name(room)
            self.assertTrue(self.can_reach_region(room), f"{room} should be reachable after collecting the room as an item")
    
    def test_gemstone_cavern_requires_utility_closet(self) -> None:
        self.assertFalse(self.can_reach_region("Gemstone Cavern"), "Gemstone Caverns should not be reachable without having the Utility Closet as an item")
        self.collect_by_name("Utility Closet")
        self.assertTrue(self.can_reach_region("Gemstone Cavern"), "Gemstone Caverns should be reachable after collecting the Utility Closet as an item")

    def test_blackbridge_grotto_requires_boiler_room_and_laboratory(self) -> None:
        self.collect_by_name("Hallway")
        if not self.multiworld.state.has("Boiler Room", self.player):
            self.assertFalse(self.can_reach_region("Blackbridge Grotto"), "Blackbridge Grotto should not be reachable without having the Boiler Room as an item")
            self.collect_by_name("Boiler Room")
        if not self.multiworld.state.has("Laboratory", self.player):
            self.assertFalse(self.can_reach_region("Blackbridge Grotto"), "Blackbridge Grotto should not be reachable without having the Laboratory as an item")
            self.collect_by_name("Laboratory")
        self.debug_print_regions_items_locations()
        self.assertTrue(self.can_reach_region("Blackbridge Grotto"), "Blackbridge Grotto should be reachable after collecting the Boiler Room as an item")

    def test_the_precipice_requires_gas_valves(self) -> None:
        self.collect_by_name("Hallway")
        self.collect_by_name("Pantry")
        self.assertFalse(self.can_reach_region("The Precipice"), "The Precipice should not be reachable without having all Gas Valves")
        self.collect_by_name("Garage")
        self.collect_by_name("Utility Closet")
        self.assertFalse(self.can_reach_region("The Precipice"), "The Precipice should not be reachable without having all Gas Valves")
        self.collect_by_name("Schoolhouse")
        self.assertFalse(self.can_reach_region("The Precipice"), "The Precipice should not be reachable without having all Gas Valves")
        self.collect_by_name("Hovel")
        self.assertTrue(self.can_reach_region("The Precipice"), "The Precipice should be reachable after having all Gas Valves")
    
    def test_orindian_ruins_requires_microchips(self) -> None:
        self.collect_by_name(["Hallway", "Boiler Room", "Laboratory", "Garage", "SHOVEL", "SLEDGE HAMMER", "Attic"])
        self.assertFalse(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should not be reachable without having all Microchips")
        self.collect_by_name("MICROCHIP 1")
        self.assertFalse(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should not be reachable without having all Microchips")
        self.collect_by_name("MICROCHIP 2")
        self.assertFalse(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should not be reachable without having all Microchips")
        self.collect_by_name("MICROCHIP 3")
        self.assertTrue(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should be reachable after having all Microchips")
    
    def test_sealed_entrance_requires_power_hammer(self) -> None:
        self.collect_by_name(["Workshop", "SLEDGE HAMMER", "BATTERY PACK", "BROKEN LEVER"])
        self.assertFalse(self.can_reach_region("Sealed Entrance"), "Sealed Entrance should not be reachable without having the Power Hammer")
        self.collect_by_name("Power Hammer")
        self.assertTrue(self.can_reach_region("Sealed Entrance"), "Sealed Entrance should be reachable after having the Power Hammer")

    def test_the_underpass_requires_reservoir_both_sides(self) -> None:
        self.assertFalse(self.can_reach_region("The Underpass"), "The Underpass should not be reachable without having the Reservoir on both sides")
        self.collect_by_name(["Power Hammer", "BASEMENT KEY", "Hallway", "Spare Room", "Workshop", "Attic", "Courtyard", "Greenhouse", "SLEDGE HAMMER", "BROKEN LEVER", "BATTERY PACK", "Veranda", "The Pool", "Observatory"])
        self.assertFalse(self.can_reach_region("The Underpass"), "The Underpass should not be reachable without having the Reservoir on both sides")
        self.collect_by_name(["Pump Room"])
        self.assertTrue(self.can_reach_region("The Underpass"), "The Underpass should be reachable after having the Reservoir on both sides")
    
    def test_aries_court_requires_chess_pieces(self) -> None:
        self.collect_by_name("Garage")
        self.collect_by_name("Utility Closet")
        self.collect_by_name("Schoolhouse")
        self.collect_by_name("Hovel")
        # Precipice

        if not self.multiworld.state.has("Chess Piece King", self.player):
            self.assertFalse(self.can_reach_region("Aries Court"), "Aries Court should not be reachable without having all Chess Pieces")
            self.collect_by_name("Office")
        if not self.multiworld.state.has("Chess Piece Queen", self.player):
            self.assertFalse(self.can_reach_region("Aries Court"), "Aries Court should not be reachable without having all Chess Pieces")
            self.collect_by_name("Study")
        if not self.multiworld.state.has("Chess Piece Rook", self.player):
            self.assertFalse(self.can_reach_region("Aries Court"), "Aries Court should not be reachable without having all Chess Pieces")
            self.collect_by_name("Nook")
        if not self.multiworld.state.has("Chess Piece Knight", self.player):
            self.assertFalse(self.can_reach_region("Aries Court"), "Aries Court should not be reachable without having all Chess Pieces")
            self.collect_by_name("Security")
        if not self.multiworld.state.has("Chess Piece Bishop", self.player):
            self.assertFalse(self.can_reach_region("Aries Court"), "Aries Court should not be reachable without having all Chess Pieces")
            self.collect_by_name("Chapel")
        if not self.multiworld.state.has("Chess Piece Pawn", self.player):
            self.assertFalse(self.can_reach_region("Aries Court"), "Aries Court should not be reachable without having all Chess Pieces")
            self.collect_by_name("Den")
        self.assertTrue(self.can_reach_region("Aries Court"), "Aries Court should be reachable after having all Chess Pieces")
    
    def test_basement_requires_the_foundation_and_basement_key(self) -> None:
        self.collect_by_name(["Hallway", "Tunnel", "Great Hall", "Courtyard", "Foyer", "Spare Room", "Workshop"])
        self.assertFalse(self.can_reach_region("Basement"), "Basement should not be reachable without having the Foundation")
        self.collect_by_name("The Foundation")
        self.assertFalse(self.can_reach_region("Basement"), "Basement should not be reachable without having the Basement Key")
        self.collect_by_name("BASEMENT KEY")
        self.assertTrue(self.can_reach_region("Basement"), "Basement should be reachable after having the Foundation and Basement Key")
    
    def test_room_8_requires_key_8(self) -> None:
        self.collect_all_but(["KEY 8"])
        self.assertFalse(self.can_reach_region("Room 8"), "Room 8 should not be reachable without having Key 8")
        self.collect_by_name("KEY 8")
        self.assertTrue(self.can_reach_region("Room 8"), "Room 8 should be reachable after having Key 8")

    def test_can_reach_showroom_items(self):
        self.collect_by_name("Showroom")
        self.assertTrue(self.can_reach_region("Showroom"), "Showroom should be reachable after having the Showroom item")
        self.assertTrue(self.can_reach_location("CHRONOGRAPH First Pickup"), "CHRONOGRAPH First Pickup should be reachable after having the Showroom item")
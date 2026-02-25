from worlds.blueprince.options import GoalType
from worlds.blueprince.test import BluePrinceTestBase
from worlds.blueprince.data_rooms import rooms, core_rooms
from worlds.blueprince.constants import *

class TestRegionAcess(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "item_sanity": True,
        "goal_type": GoalType.option_room46,
    }

    def test_starting_from_campsite(self) -> None:
        self.assertTrue(self.can_reach_region("Campsite"))
        self.assertTrue(self.can_reach_region("Entrance Hall"))
        self.assertTrue(self.can_reach_region("Grounds"))
        self.assertTrue(self.can_reach_region("Private Drive"))
        self.assertTrue(self.can_reach_region("Apple Orchard"))
        self.assertTrue(self.can_reach_region("Tunnel Area Entrance"))

    def test_inner_rooms_requires_room_item(self) -> None:

        for room,v in rooms.items():
            if room in core_rooms or v[OUTER_ROOM_KEY]:
                continue

            self.assertFalse(self.can_reach_region(room), f"{room} should not be reachable without having the room as an item")
            self.collect_by_name(room)
            self.assertTrue(self.can_reach_region(room), f"{room} should be reachable after collecting the room as an item")
    
    def test_outer_room_requires_garage_utility_closet(self) -> None:
        self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Utility Closet as an item")
        self.collect_by_name("Utility Closet")
        self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Garage")
        self.assertTrue(self.can_reach_region("Outer Room"), "Outer Room should be reachable after collecting the Garage as an item")
    
    def test_outer_room_requires_garage_boiler_room(self) -> None:
        self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Garage as an item")
        self.collect_by_name("Garage")

        self.assertFalse(self.can_reach_region("Outer Room"), "Outer Room should not be reachable without having the Boiler Room as an item")

        self.collect_by_name("Boiler Room")
        self.assertTrue(self.can_reach_region("Outer Room"), "Outer Room should be reachable after collecting the Garage as an item")

    def test_outer_rooms_require_room_item(self) -> None:
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
        self.assertFalse(self.can_reach_region("Blackbridge Grotto"), "Blackbridge Grotto should not be reachable without having the Boiler Room as an item")
        self.collect_by_name("Boiler Room")
        self.assertFalse(self.can_reach_region("Blackbridge Grotto"), "Blackbridge Grotto should not be reachable without having the Laboratory as an item")
        self.collect_by_name("Laboratory")
        self.assertTrue(self.can_reach_region("Blackbridge Grotto"), "Blackbridge Grotto should be reachable after collecting the Boiler Room as an item")

    def test_the_precipice_requires_gas_valves(self) -> None:
        self.assertFalse(self.can_reach_region("The Precipice"), "The Precipice should not be reachable without having all Gas Valves")
        self.collect_by_name("Garage")
        self.collect_by_name("Utility Closet")
        self.assertFalse(self.can_reach_region("The Precipice"), "The Precipice should not be reachable without having all Gas Valves")
        self.collect_by_name("Schoolhouse")
        self.assertFalse(self.can_reach_region("The Precipice"), "The Precipice should not be reachable without having all Gas Valves")
        self.collect_by_name("Hovel")
        self.assertTrue(self.can_reach_region("The Precipice"), "The Precipice should be reachable after having all Gas Valves")
    
    def test_orindian_ruins_requires_microchips(self) -> None:
        self.collect_by_name("Boiler Room")
        self.collect_by_name("Laboratory")
        self.assertFalse(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should not be reachable without having all Microchips")
        self.collect_by_name("MICROCHIP 1")
        self.assertFalse(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should not be reachable without having all Microchips")
        self.collect_by_name("MICROCHIP 2")
        self.assertFalse(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should not be reachable without having all Microchips")
        self.collect_by_name("MICROCHIP 3")
        self.assertTrue(self.can_reach_region("Orindian Ruins"), "Orindian Ruins should be reachable after having all Microchips")
    
    def test_sealed_entrance_requires_power_hammer(self) -> None:
        self.assertFalse(self.can_reach_region("Sealed Entrance"), "Sealed Entrance should not be reachable without having the Power Hammer")
        self.collect_by_name("Power Hammer")
        self.assertTrue(self.can_reach_region("Sealed Entrance"), "Sealed Entrance should be reachable after having the Power Hammer")

    def test_the_underpass_requires_reservoir_both_sides(self) -> None:
        self.assertFalse(self.can_reach_region("The Underpass"), "The Underpass should not be reachable without having the Reservoir on both sides")
        self.collect_by_name("Power Hammer")
        self.debug_print_regions_and_items()
        self.assertFalse(self.can_reach_region("The Underpass"), "The Underpass should not be reachable without having the Reservoir on both sides")
        self.collect_by_name("Pump Room")
        self.collect_by_name("BASEMENT KEY")
        self.assertTrue(self.can_reach_region("The Underpass"), "The Underpass should be reachable after having the Reservoir on both sides")
        
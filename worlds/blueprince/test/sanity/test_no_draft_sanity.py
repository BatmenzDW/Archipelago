
import typing

from ...constants import *

from BaseClasses import CollectionState, Location
from ....AutoWorld import call_all

from ...options import GoalType
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms

class TestNoDraftSanity(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "room_draft_sanity": False,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "trophy_sanity": True,
        "goal_type": GoalType.option_blueprints,
    }

    def test_all_starting_room_items(self) -> None:
        for room, data in rooms.items():
            if room in core_rooms or room in ["Secret Garden", "Room 8"] or room in ["Classroom 1", "Classroom 2", "Classroom 3", "Classroom 4", "Classroom 5", "Classroom 6", "Classroom 7", "Classroom 8", "Classroom Exam"]:
                continue
            
            if NONSANITY_LOCATION_KEY not in data or data[NONSANITY_LOCATION_KEY] == STARTING_INVENTORY:
                self.assertTrue(self.multiworld.state.has(room, self.player), f"Expected to have {room} in starting inventory for player {self.player}")
            else:
                self.assertFalse(self.multiworld.state.has(room, self.player), f"Expected not to have {room} in starting inventory for player {self.player}")

    #  Copied here for debugging. This is run by the base class, but its easier to debug with it here
    def test_fill(self):
        """Generates a multiworld and validates placements with the defined options"""
        if not (self.run_default_tests and self.constructed):
            return
        from Fill import distribute_items_restrictive

        # basically a shortened reimplementation of this method from core, in order to force the check is done
        def fulfills_accessibility() -> bool:
            locations = list(self.multiworld.get_locations(1))
            state = CollectionState(self.multiworld)
            spheres : list[list[str]] = []
            while locations:
                sphere: typing.List[Location] = []
                for n in range(len(locations) - 1, -1, -1):
                    if locations[n].can_reach(state):
                        sphere.append(locations.pop(n))

                spheres.append([])
                if not sphere:
                    break
                for location in sphere:
                    if location.item:
                        state.collect(location.item, True, location)
                        spheres[-1].append(str(location) + ": " + str(location.item))

            spheres_text = "\n".join([f"Sphere {i}: {', '.join(sphere)}" for i, sphere in enumerate(spheres)])
            print(spheres_text)

            return self.multiworld.has_beaten_game(state, self.player)

        with self.subTest("Game", game=self.game, seed=self.multiworld.seed):
            distribute_items_restrictive(self.multiworld)
            call_all(self.multiworld, "post_fill")
            self.assertTrue(fulfills_accessibility(), "Collected all locations, but can't beat the game.")
            placed_items = [loc.item for loc in self.multiworld.get_locations() if loc.item and loc.item.code]
            self.assertLessEqual(len(self.multiworld.itempool), len(placed_items),
                                 "Unplaced Items remaining in itempool")

    def test_fill2(self):
        """Generates a multiworld and validates placements with the defined options"""
        if not (self.run_default_tests and self.constructed):
            return
        from Fill import distribute_items_restrictive

        # basically a shortened reimplementation of this method from core, in order to force the check is done
        def fulfills_accessibility() -> bool:
            locations = list(self.multiworld.get_locations(1))
            state = CollectionState(self.multiworld)
            while locations:
                sphere: typing.List[Location] = []
                for n in range(len(locations) - 1, -1, -1):
                    if locations[n].can_reach(state):
                        sphere.append(locations.pop(n))
                self.assertTrue(sphere or self.multiworld.worlds[1].options.accessibility == "minimal",
                                f"Unreachable locations: {locations}")
                if not sphere:
                    break
                for location in sphere:
                    if location.item:
                        state.collect(location.item, True, location)
            return self.multiworld.has_beaten_game(state, self.player)

        with self.subTest("Game", game=self.game, seed=self.multiworld.seed):
            distribute_items_restrictive(self.multiworld)
            call_all(self.multiworld, "post_fill")
            call_all(self.multiworld, "finalize_multiworld")
            self.assertTrue(fulfills_accessibility(), "Collected all locations, but can't beat the game.")
            placed_items = [loc.item for loc in self.multiworld.get_locations() if loc.item and loc.item.code]
            self.assertLessEqual(len(self.multiworld.itempool), len(placed_items),
                                 "Unplaced Items remaining in itempool")
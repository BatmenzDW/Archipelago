
import typing

from ....AutoWorld import call_all

from BaseClasses import Location, MultiWorld, CollectionState, Item

from ...options import GoalType
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms
from ... import data_rooms, data_other_locations

class TestDraftSanity(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "goal_type": GoalType.option_room46,
    }

    def test_no_starting_room_items(self) -> None:
        for room in rooms:
            if room in core_rooms:
                continue
            self.assertFalse(self.multiworld.state.has(room, self.player))
        self.assertFalse(self.multiworld.state.has("Progressive Classroom", self.player))

    def test_progressive_classroom(self) -> None:
        for cnum in range(1, 10):
            current = f"Classroom {cnum}" if cnum < 9 else "Classroom Exam"

            self.assertFalse(self.can_reach_region(current))
            self.collect(data_rooms.progressive_classroom[cnum - 1])
            self.debug_print_regions_items_locations(True)
            self.assertTrue(self.can_reach_region(current), f"Should be able to reach {current} after collecting {cnum} Progressive Classrooms")

    def test_fill(self):
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
                
                print(f"{[str(loc) for loc in sphere]}")
                if not sphere:
                    self.assertTrue(state.can_reach_region("Secret Garden", 1))
                    self.assertTrue(state.can_reach_region("Room 8", 1))
                    for room in data_other_locations.directory_rooms:
                        self.assertTrue(state.has(room, self.player), f"Expected to have {room} in inventory for player {self.player}")
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
            self.assertTrue(fulfills_accessibility(), "Collected all locations, but can't beat the game.")
            placed_items = [loc.item for loc in self.multiworld.get_locations() if loc.item and loc.item.code]
            self.assertLessEqual(len(self.multiworld.itempool), len(placed_items),
                                 "Unplaced Items remaining in itempool")
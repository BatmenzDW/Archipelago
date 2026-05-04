import typing

from BaseClasses import CollectionState, Location
from ....AutoWorld import call_all
from ... import data_other_locations

from ...options import GoalType
from ...test import BluePrinceTestBase
from ...constants import *

class TestAscendVictory(BluePrinceTestBase):
    options = {
        "room_draft_sanity": True,
        "trophy_sanity": True,
        "special_shop_sanity": True,
        "goal_type": GoalType.option_ascend,
    }

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
            # spheres : list[list[str]] = []
            while locations:
                sphere: typing.List[Location] = []
                for n in range(len(locations) - 1, -1, -1):
                    if locations[n].can_reach(state):
                        sphere.append(locations.pop(n))

                # spheres.append([])
                if not sphere:
                    break
                for location in sphere:
                    if location.item:
                        state.collect(location.item, True, location)
                        # spheres[-1].append(str(location) + ": " + str(location.item))

            # spheres_text = "\n".join([f"Sphere {i}: {', '.join(sphere)}" for i, sphere in enumerate(spheres)])
            # print(spheres_text)

            return self.multiworld.has_beaten_game(state, self.player)

        with self.subTest("Game", game=self.game, seed=self.multiworld.seed):
            distribute_items_restrictive(self.multiworld)
            call_all(self.multiworld, "post_fill")
            self.assertTrue(fulfills_accessibility(), "Collected all locations, but can't beat the game.")
            placed_items = [loc.item for loc in self.multiworld.get_locations() if loc.item and loc.item.code]
            self.assertLessEqual(len(self.multiworld.itempool), len(placed_items),
                                 "Unplaced Items remaining in itempool")
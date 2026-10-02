import unittest
from unittest.mock import patch

from BaseClasses import CollectionState, Item, ItemClassification, Location, MultiWorld, Region
from ..locations import attempt_to_fill_multiple_locations_with_same_item
from ..world import BluePrinceWorld


class TestBunkRoomFill(unittest.TestCase):
    def setUp(self) -> None:
        self.multiworld = MultiWorld(3)
        self.worlds = []
        self.locations = []
        for player in (1, 2):
            world = BluePrinceWorld(self.multiworld, player)
            self.multiworld.worlds[player] = world
            self.worlds.append(world)
            region = Region("Bunk Room", player, self.multiworld)
            self.multiworld.regions.append(region)
            for address, name in enumerate(("Bunk Room First Entering", "Bunk Room First Entering 2"), 1):
                location = Location(player, name, address, region)
                region.locations.append(location)
                self.locations.append(location)
        self.multiworld.state = CollectionState(self.multiworld)

    def test_removes_placed_objects_in_each_pool(self) -> None:
        for pool_index, classification in enumerate((
            ItemClassification.progression, ItemClassification.useful, ItemClassification.filler
        )):
            with self.subTest(classification=classification):
                for location in self.locations:
                    location.item = None
                    location.locked = False
                copies = [Item("Lum", classification, 1, 3) for _ in range(4)]
                unrelated = Item("Other item", classification, 2, 3)
                pool = [copies[0], unrelated, *copies[1:]]
                pools = [[], [], []]
                pools[pool_index] = pool
                locations = list(self.locations)
                world = self.worlds[0]

                # Select the last two copies: equality-based removal would remove the first two.
                with patch.object(world.random, "shuffle", side_effect=lambda order: order.reverse()):
                    world.fill_hook(*pools, locations)

                self.assertIs(self.locations[0].item, copies[3])
                self.assertIs(self.locations[1].item, copies[2])
                self.assertEqual([id(item) for item in pool], [id(copies[0]), id(unrelated), id(copies[1])])
                self.assertTrue(all(item.location is None for item in pool))
                self.assertEqual(locations, self.locations[2:])
                self.assertTrue(all(location.locked for location in self.locations[:2]))

    def test_two_blue_prince_slots_preserve_foreign_item_pool(self) -> None:
        pool = [Item("Lum", ItemClassification.filler, 1, 3) for _ in range(6)]
        original_ids = {id(item) for item in pool}
        locations = list(self.locations)
        for world in self.worlds:
            with patch.object(world.random, "shuffle", side_effect=lambda order: order.reverse()):
                world.fill_hook([], [], pool, locations)

        self.assertEqual(len(pool), 2)
        self.assertTrue(all(item.location is None for item in pool))
        self.assertEqual(locations, [])
        placed_ids = {id(location.item) for location in self.locations}
        remaining_ids = {id(item) for item in pool}
        self.assertEqual(len(placed_ids), 4)
        self.assertTrue(placed_ids.isdisjoint(remaining_ids))
        self.assertEqual(original_ids, placed_ids | remaining_ids)

    def test_no_duplicates_leaves_pool_and_locations_unchanged(self) -> None:
        item = Item("Lum", ItemClassification.filler, 1, 3)
        pool = [item]
        locations = list(self.locations)
        self.assertFalse(attempt_to_fill_multiple_locations_with_same_item(self.worlds[0], pool, locations))
        self.assertIs(pool[0], item)
        self.assertIsNone(item.location)
        self.assertEqual(locations, self.locations)


if __name__ == "__main__":
    unittest.main()

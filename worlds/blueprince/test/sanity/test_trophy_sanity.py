

from ...rules import CanReachItemLocation

from ...options import GoalType
from ...data_other_locations import directory_rooms

from .. import BluePrinceTestBase


class TrophySanity(BluePrinceTestBase):
    options = {
        "progression_balancing": 50,
        "room_draft_sanity": True,
        "standard_item_sanity": True,
        "workshop_sanity": True,
        "upgrade_disk_sanity": True,
        "key_sanity": True,
        "special_shop_sanity": True,
        "trophy_sanity": True,
        "goal_type": GoalType.option_blueprints,
    }

    def test_full_house_requires_43_rooms(self):
        self.assertFalse(self.can_reach_location("Full House Trophy"), "Expected not to be able to reach Full House Trophy without at least 43 rooms")
        self.collect_by_name(["SECRET GARDEN KEY", "KEY 8"])
        self.collect_by_name(["Progressive Classroom"] * 9)
        i = 2
        for room in directory_rooms:
            if self.multiworld.state.has(room, self.player):
                i += self.count(room)

        for room in directory_rooms:
            if self.multiworld.state.has(room, self.player):
                continue
            i += 1
            self.collect_by_name(room)
            if i < 43:
                self.assertFalse(self.can_reach_location("Full House Trophy"), f"Expected not to be able to reach Full House Trophy with only {i} rooms")
            else:
                self.assertTrue(self.can_reach_location("Full House Trophy"), f"Expected to be able to reach Full House Trophy with {i} rooms")
                break

    # def test_invention_requires_workshop_and_materials(self):
    #     # Not implemented yet
    #     self.collect_all_but(["Workshop", "SLEDGE HAMMER", "BROKEN LEVER", "BATTERY PACK", "SHOVEL", "METAL DETECTOR", "MAGNIFYING GLASS", "COMPASS", "COIN PURSE", "LUCKY RABBIT'S FOOT", "LOCK PICK KIT"])
    #     self.assertFalse(self.can_reach_location("Trophy of Invention"), "Expected not to be able to reach Trophy of Invention without Workshop and materials")
    #     self.collect_by_name("Workshop")
    #     self.assertFalse(self.can_reach_location("Trophy of Invention"), "Expected not to be able to reach Trophy of Invention without materials")
    #     self.collect_by_name(["SLEDGE HAMMER", "BROKEN LEVER", "BATTERY PACK", "SHOVEL", "METAL DETECTOR", "MAGNIFYING GLASS", "COMPASS", "COIN PURSE", "LUCKY RABBIT'S FOOT", "LOCK PICK KIT"])

    #     # self.assertTrue(self.can_reach_location("Power Hammer First Craft"), "Expected to be able to reach Power Hammer First Craft with Workshop and materials")
    #     self.assertRuleTrue(CanReachItemLocation("Power Hammer"), "Expected to be able to reach Power Hammer with Workshop and materials") # type: ignore
    #     self.assertRuleTrue(CanReachItemLocation("Burning Glass"), "Expected to be able to reach Burning Glass First Craft with Workshop and materials") # type: ignore
    #     self.assertRuleTrue(CanReachItemLocation("Detector Shovel"), "Expected to be able to reach Detector Shovel First Craft with Workshop and materials;") # type: ignore
    #     self.assertRuleTrue(CanReachItemLocation("Dowsing Rod"), "Expected to be able to reach Dowsing Rod First Craft with Workshop and materials") # type: ignore
    #     self.assertRuleTrue(CanReachItemLocation("Electromagnet"), "Expected to be able to reach Electromagnet First Craft with Workshop and materials") # type: ignore
    #     self.assertRuleTrue(CanReachItemLocation("Jack Hammer"), "Expected to be able to reach Jack Hammer First Craft with Workshop and materials") # type: ignore
    #     self.assertRuleTrue(CanReachItemLocation("Lucky Purse"), "Expected to be able to reach Lucky Purse First Craft with Workshop and materials") # type: ignore
    #     self.assertRuleTrue(CanReachItemLocation("Pick Sound Amplifier"), "Expected to be able to reach Pick Sound Amplifier First Craft with Workshop and materials") # type: ignore
    
    #     self.assertTrue(self.can_reach_location("Trophy of Invention"), "Expected to be able to reach Trophy of Invention with Workshop and materials")

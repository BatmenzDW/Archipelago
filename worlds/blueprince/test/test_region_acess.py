from worlds.blueprince.options import GoalType
from worlds.blueprince.test import BluePrinceTestBase

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
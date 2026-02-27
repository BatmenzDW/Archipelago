
from ...options import GoalType
from ...test import BluePrinceTestBase
from ...data_rooms import rooms, core_rooms

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
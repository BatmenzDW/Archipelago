from ...options import GoalType
from ...data_rooms import rooms

from .. import BluePrinceTestBase


class TrunkSanity(BluePrinceTestBase):
    options = {
        "trunks": 
        {room: 100 for room in rooms if "chest_spot_count" in rooms[room] and rooms[room]["chest_spot_count"] > 0},
    }
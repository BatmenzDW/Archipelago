from collections import deque
from ..room_min_pieces import *
from ..test import BluePrinceTestBase
from ..data_rooms import rooms, core_rooms
from ..constants import *

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

PIECES = {
    ROOM_LAYOUT_TYPE_X: [{0,1,2,3}],
    ROOM_LAYOUT_TYPE_T: [
        {0,1,2},
        {1,2,3},
        {0,2,3},
        {0,1,3}
    ],
    ROOM_LAYOUT_TYPE_I: [
        {0,2}, # vertical
        {1,3}  # horizontal
    ],
    ROOM_LAYOUT_TYPE_J: [
        {0,1},
        {1,2},
        {2,3},
        {0,3}
    ]
}

ROOM_LAYOUTS = [ROOM_LAYOUT_TYPE_X, ROOM_LAYOUT_TYPE_T, ROOM_LAYOUT_TYPE_I, ROOM_LAYOUT_TYPE_J]

class TestCanReachPickPosition(BluePrinceTestBase):
    options = {}

    def in_bounds(self, r, c):
        return 0 <= r <= 8 and 0 <= c <= 4

    def opposite(self, d):
        return (d + 2) % 4

    def build_path(self, inventory: tuple[int, int, int, int], target: tuple[int, int]) -> tuple[bool, tuple[int, int, int, int] | None]:
        start = (0, 2)
        total_pieces = sum(inventory)

        q = deque()
        start_state = (start, None, inventory)
        q.append(start_state)

        visited = set()
        visited.add(start_state)

        while q:
            pos, incoming, inv = q.popleft()
            r, c = pos

            used = total_pieces - sum(inv)

            if pos == target:
                if used == total_pieces:
                    return True, None
                else:
                    return True, inv
            
            for i, count in enumerate(inv):
                if count == 0:
                    continue

                for shape in PIECES[ROOM_LAYOUTS[i]]:
                    for d in shape:
                        if incoming is not None and d == self.opposite(incoming):
                            continue

                        new_r = r + DIRS[d][0]
                        new_c = c + DIRS[d][1]
                        if not self.in_bounds(new_r, new_c):
                            continue

                        new_pos = (new_r, new_c)

                        new_inv = list(inv)
                        new_inv[i] -= 1

                        new_state = (new_pos, d, tuple(new_inv))
                        if new_state in visited:
                            continue

                        q.append(new_state)
            
        return False, None
                    

    def check_min_pieces(self, room: str, target: tuple[int, int]):
        room_data = rooms[room]
        position_types = room_data[ROOM_PICK_POSITIONS_KEY]

        for pt in position_types:
            with self.subTest(room):
                min_total = POSITION_MINIMUM_TOTAL_PIECES[pt]
                if room_data[ROOM_LAYOUT_TYPE_KEY] != ROOM_LAYOUT_TYPE_D:
                    min_total += 1
                
                min_layouts = POSITION_MINIMUM_PIECES[pt]
                for layout in min_layouts:
                    inventory = (
                        layout[0] + room_data[ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_X, 
                        layout[1] + room_data[ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_T,
                        layout[2] + room_data[ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_I,
                        layout[3] + room_data[ROOM_LAYOUT_TYPE_KEY] == ROOM_LAYOUT_TYPE_J
                    )
                    assert sum(inventory) >= min_total, f"{pt}:{layout} has fewer pieces than min total expects: {POSITION_MINIMUM_TOTAL_PIECES[pt]}"
                    result, rem = self.build_path(inventory, target)

                    assert result, f"{room} should be reachable with inventory: {layout}"
                    assert rem in None, f"Had leftover inventory after reaching {room}: {rem}"
        

    def test_foundation_requires_min_pieces(self):
        self.check_min_pieces("The Foundation", (2, 2))


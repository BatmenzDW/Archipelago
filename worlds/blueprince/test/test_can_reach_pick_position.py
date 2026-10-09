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

    def at_target(self, pos, incoming, targets) -> bool:
        for r, c, ds in targets:
            if (r, c) == pos and (len(ds) == 0 or incoming in ds):
                return True
        
        return False

    def in_target(self, pos, targets) -> bool:
        for r, c, _ in targets:
            if (r, c) == pos:
                return True
        
        return False

    def build_path(self, inventory: tuple[int, int, int, int], targets: tuple[int, int, set|dict]) -> tuple[bool, tuple[int, int, int, int] | None, list[tuple[tuple[int, int], set[int], int]]]:
        start = (-1, 2)
        total_pieces = sum(inventory)

        q = deque()
        start_state = (start, 2, inventory, [])
        q.append(start_state)

        visited = set()

        visited.add((start, None, inventory))

        while q:
            pos, incoming, inv, path = q.popleft()
            r, c = pos

            used = total_pieces - sum(inv)

            if self.at_target(pos, incoming, targets):
                if used == total_pieces:
                    return True, None, path
                else:
                    return True, inv, path
            
            for i, count in enumerate(inv):
                if count < 0:
                    if i != 1 or pos != start:
                        continue

                for shape in PIECES[ROOM_LAYOUTS[i]]:
                    if pos == start and shape != {0, 1, 2, 3}:
                        continue

                    if path and len(path[-1][1].intersection({self.opposite(x) for x in shape})) == 0:
                        continue

                    for d in shape:
                        if d == 1:
                            pass
                        if incoming is not None and d == self.opposite(incoming):
                            continue

                        new_r = r + DIRS[d][0]
                        new_c = c + DIRS[d][1]
                        if not self.in_bounds(new_r, new_c):
                            continue

                        new_pos = (new_r, new_c)

                        new_inv = list(inv)
                        if not self.in_target(new_pos, targets) and pos != start:
                            if count == 0:
                                continue

                            new_inv[i] -= 1
                        elif self.in_target(new_pos, targets):
                            if not self.at_target(new_pos, self.opposite(d), targets):
                                continue

                        new_state = (new_pos, d, tuple(new_inv))
                        if new_state in visited:
                            continue

                        visited.add(new_state)
                        new_path = path + [(new_pos, shape, d)]
                        q.append((new_pos, d, tuple(new_inv), new_path))

            print(path)
            
        return False, None, []

    def check_min_pieces_layout(self, name: str, layout: list[tuple[int, int, int, int]], min_total: int):
        with self.subTest(f"{name}: {layout}"):
            self.assertTrue(sum(layout) >= min_total, f"{name}: {layout} has fewer pieces than min total expects: {min_total}")

            solved = False
            targets = POSITION_MINIMUM_LOCATIONS[name]

            result, rem, path = self.build_path(layout, targets)
            self.assertTrue(result, f"{name} should be reachable with inventory: {layout}")
            self.assertTrue(rem is None, f"Had leftover inventory after reaching {name}: {rem}/{layout}: \n{path}")
            

    def check_min_pieces_position(self, position_type: str):   
        min_total = POSITION_MINIMUM_TOTAL_PIECES[position_type]

        min_layouts = POSITION_MINIMUM_PIECES[position_type]
        for layout in min_layouts:
            self.check_min_pieces_layout(position_type, layout, min_total)
            
    def test_foundation_requires_min_pieces(self):
        self.check_min_pieces_position(ROOM_PICK_POSITION_CENTER_FOUNDATION)

    def test_center_requires_nothing(self):
        self.check_min_pieces_position(ROOM_PICK_POSITION_CENTER_TIER_1)
        self.check_min_pieces_position(ROOM_PICK_POSITION_CENTER_TIER_2)
        self.check_min_pieces_position(ROOM_PICK_POSITION_CENTER_TIER_3)

    def test_corner_requires_min_pieces(self):
        self.check_min_pieces_position(ROOM_PICK_POSITION_CORNER)

        # self.check_min_pieces_layout(ROOM_PICK_POSITION_CORNER, (0, 0, 1, 0), (0, 0), 1, 1) # (0, 0, 1, 0), (0, 1, 0, 0),
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_CORNER, (0, 1, 0, 0), (0, 0), 1, 1)
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_CORNER, (0, 0, 0, 3), (0, 0), 2, 1) # (0, 0, 0, 3), (1, 0, 0, 2), (2, 0, 0, 1)
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_CORNER, (1, 0, 0, 2), (0, 0), 2, 1)
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_CORNER, (2, 0, 0, 1), (0, 0), 2, 1)

    def test_edge_advance_requires_min_pieces(self):
        self.check_min_pieces_position(ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS)
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS, (0, 0, 0, 3), (2, 0), 0, 2) # (0, 0, 0, 4), (1, 0, 0, 3),
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS, (1, 0, 0, 2), (2, 0), 0, 2)
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS, (0, 0, 1, 1), (1, 0), 0, 2) # (0, 0, 1, 1), (0, 1, 0, 1),
        # self.check_min_pieces_layout(ROOM_PICK_POSITION_EDGE_ADVANCE_EAST_WING_GEMS, (0, 1, 0, 1), (1, 0), 0, 2)
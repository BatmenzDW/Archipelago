from collections import defaultdict, deque
from enum import Enum
from typing import Callable

from .world import BluePrinceWorld

class ColorAction:
    def __init__(self, action: Callable[[list[str], int, str], None] | None) -> None:
        self.action = action

    def apply(self, board: list[str], i: int, color: str) -> None:
        if self.action:
            self.action(board, i, color)

def rotateRow(board: list[str], i: int, _: str) -> None:
    r = (i // 3) * 3
    board[r], board[r+1], board[r+2] = board[r+2], board[r], board[r+1]

def applyRed(board: list[str], _: int, color: str) -> None:
    for i in range(len(board)):
        if board[i] == "0":
            board[i] = color
        elif board[i] == "8":
            board[i] = "0"

def swap(board: list[str], a: int, b: int) -> None:
    board[a], board[b] = board[b], board[a]

def swapAcross(board: list[str], i: int, _: str) -> None:
    swap(board, i, 8 - i)

def applyBlue(board: list[str], i: int, _: str) -> None:
    if board[4] == "3":
        return

    colorActions[board[4]].apply(board, i, '3')

def shiftUp(board: list[str], i: int, _: str) -> None:
    if i <= 2:
        return

    swap(board, i, i - 3)

def shiftDown(board: list[str], i: int, _: str) -> None:
    if i >= 6:
        return

    swap(board, i, i + 3)

def rotateAround(board: list[str], i: int, _: str) -> None:
    indicies = aroundIndicies[i]
    last = board[indicies[-1]]
    for j in range(len(indicies) - 1, 0, -1): # if need to rotate the other way, reverse the iteration and replace j - 1 with j + 1
        board[indicies[j]] = board[indicies[j - 1]]
    board[indicies[0]] = last

crossIndicies = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [2, 4, 8],
    [3, 7],
    [6, 4, 8],
    [5, 7]
]

aroundIndicies = [
    [1, 4, 3],
    [2, 5, 4, 3, 0],
    [5, 4, 1],
    [0, 1, 4, 7, 6],
    [0, 1, 2, 5, 8, 7, 6, 3],
    [8, 7, 4, 1, 2],
    [3, 4, 7],
    [6, 3, 4, 5, 8],
    [7, 4, 5]
]

def applyOrange(board: list[str], i: int, _: str) -> None:
    counts : dict[str, int] = defaultdict(int)

    for j in crossIndicies[i]:
        counts[board[j]] += 1
    
    max_color = None
    max_count = 0
    tie = False
    for k,v in counts.items():
        if v > max_count:
            max_color, max_count = k, v
            tie = False
        elif v == max_count:
            tie = True

    if not tie and max_color is not None:
        board[i] = max_color

def invertColors(board: list[str], i: int, color: str, color2: str = "9") -> None:

    for j in crossIndicies[i]:
        if board[j] == color:
            board[j] = color2
        elif board[j] == color2:
            board[j] = color

    if board[i] == color:
        board[i] = color2
    elif board[i] == color2:
        board[i] = color


def is_unsolvable_state(board: tuple[str, ...] | list[str], expected: list[str]) -> bool:
    for c in "12345678":
        if c in expected and c not in board:
            return True

    return False

# 2 3 1 0
def is_solved(board: tuple[str, ...] | list[str], expected: list[str]) -> bool:
    return expected[2] == board[0] and expected[3] == board[2] and expected[1] == board[6] and expected[0] == board[8]

def is_nonop(board: tuple[str, ...], i: int, color: str, hist: tuple[int, ...]) -> bool:
    match color:
        case "0":
            r = (i//3) * 3
            if len(hist) >= 2 and hist[-1] % 10 == 0 and hist[-2] % 10 == 0: # check if prev two ops were the same color operation
                row = [r, r+1, r+2]
                if hist[-1]//10 in row and hist[-2]//10 in row: # cyclic repeat
                    return True
            return board[r] == board[r+1] and board[r+1] == board[r+2]
        case "1":
            return "0" not in board and "8" not in board
        case "2":
            return board[i] == board[8 - i]
        case "3":
            if i == 4 or board[4] == "3": return True # recursion is only an issue if board[4] is also "3", otherwise it will only ever recurse 1 deep

            return is_nonop(board, i, board[4], hist)
        case "4":
            return i <= 2 or board[i] == board[i - 3]
        case "5":
            return False
        case "6":
            return i >= 6 or board[i] == board[i + 3]
        case "7":
            return False
        case "8":
            return False
        case _:
            return True


def print_bfs_progress(depth: int, max_depth: int, breadth: int):
    filled = min(depth, max_depth)
    print("\rBFS Depth: [" 
          + "#" * filled 
          + "." * (max_depth - filled) 
          + f"] {depth} "
          + f"   Breadth: {breadth}", end="", flush=True)

def bfs_is_solvable(board: list[str], expected: list[str], max_depth: int = -1) -> tuple[bool, int, str]:
    que : deque[tuple[tuple[str, ...], tuple[int, ...], int]] = deque()
    seen = {tuple(board)}

    actioncache = {}

    depth, breadth = 1, 1

    que.append((tuple(board), (), 0))

    while que:
        current, hist, moves = que.popleft()
        breadth -= 1
        if max_depth > 0 and moves > max_depth: continue
        if moves > depth:
            depth += 1
            # print_bfs_progress(depth, max_depth, breadth)

        for i in range(9):

            if is_nonop(current, i, current[i], hist): continue

            color = current[i]

            key = (current, i)
            if key in actioncache:
                new = list(actioncache[key])
            else:
                new = list(current)
                colorActions[color].apply(new, i, color)
                actioncache[key] = tuple(new)

            new_t = tuple(new)

            if new_t in seen: continue

            if is_solved(new_t, expected): 
                print()
                return True, moves, "".join(str(h) for h in hist) + str(i) + color
            if is_unsolvable_state(new_t, expected): continue

            seen.add(new_t)

            breadth += 1
            que.append((new_t, hist + ((i * 10 + ord(color) - 48),), moves + 1))

    # print()
    return False, -1, ""

colorChars : dict[str, str] = {
    "0": "B",
    "1": "R",
    "2": "G",
    "3": "U",
    "4": "Y",
    "5": "O",
    "6": "P",
    "7": "K",
    "8": "W",
    "9": "#"
}

colorActions : dict[str, ColorAction] = {
    "0": ColorAction(rotateRow),
    "1": ColorAction(applyRed),
    "2": ColorAction(swapAcross),
    "3": ColorAction(applyBlue),
    "4": ColorAction(shiftUp),
    "5": ColorAction(applyOrange),
    "6": ColorAction(shiftDown),
    "7": ColorAction(rotateAround),
    "8": ColorAction(invertColors),
    "9": ColorAction(None)
}

backgroundColor : dict[str, str] = {
    "B": "1;37;40",
    "R": "1;37;41",
    "G": "1;37;42",
    "U": "1;37;44",
    "Y": "1;37;43",
    "O": "1;33;41",
    "P": "1;37;45",
    "K": "1;35;47",
    "W": "0;30;47",
    "#": "1;30;40"
}

def random_colorcode(colors: str, world: BluePrinceWorld, mono_color: bool = True) -> list[str]:
    corners = colors.replace("9", "")
    if mono_color:
        return [world.random.choice(corners)] * 4 + [world.random.choice(colors) for _ in range(9)]
    return [world.random.choice(corners) for _ in range(4)] + [world.random.choice(colors) for _ in range(9)]

# 2 3 1 0
vanillaPuzzles : dict[str, str] = {
    "Trading Post":     "4444799944944",
    "Tunnel":           "5555057555755",
    "Throne Room":      "3333023333699",
    "Lost & Found":     "7777777797999",
    "Closed Exhibit":   "1111505515505",
    "Tomb":             "6666969979666",
    "Solarium":         "2222294242492",
    "Master Bedroom":   "8888898899998",
    "Underpass":        "0000000909494",

}

def get_random_vanilla_puzzle(world: BluePrinceWorld) -> list[str]:
    fallback = world.random.choice(list(vanillaPuzzles.keys()))
    # print(f"Unable to find valid puzzle, falling back to {fallback}")
    return list(vanillaPuzzles[fallback])

def gen_solvable_puzzle(colors: str, min_complexity: int, max_complexity: int, world: BluePrinceWorld, max_attempts: int) -> tuple[list[str], int, str]:
    current = random_colorcode(colors, world)
    # print("Attempt 1")
    attempts = 1
    while True:
        if is_unsolvable_state(current[4:], current[:4]) or is_solved(current[4:], current[:4]):
            current = random_colorcode(colors, world)
            continue

        solvable, complexity, moves = bfs_is_solvable(current[4:], current[:4], max_complexity)
        if not solvable or complexity < min_complexity:
            current = random_colorcode(colors, world)
            attempts += 1
            # print(f"Attempt {attempts}")
            if attempts >= max_attempts:
                break
        else:
            break

    if attempts >= max_attempts:
        current = get_random_vanilla_puzzle(world)
        _, complexity, moves = bfs_is_solvable(current[4:], current[:4])

    return current, complexity, moves

def pretty_format_mj(colorcode: list[str] | tuple[str, ...]) -> str:
    # 2 3 1 0
    msg = \
    colorcode[2] + " --------- " + colorcode[3] + "\n" + \
    " |  " + "".join(colorcode[4:7]) + "  |" + "\n" + \
    " |  " + "".join(colorcode[7:10]) + "  |" + "\n" + \
    " |  " + "".join(colorcode[10:]) + "  |" + "\n" + \
    colorcode[1] + " --------- " + colorcode[0]

    for k, v in colorChars.items():
        msg = msg.replace(k, v)

    for k, v in backgroundColor.items():
        msg = msg.replace(k, f"\033[{v}m_{k}_\033[0m")
    return msg

def pretty_format_moves(moves: str) -> str:
    msg = ""
    for i in range(0, len(moves), 2):
        msg += moves[i]
        msg += f" \033[{backgroundColor[moves[i+1]]}m_{moves[i+1]}_\033[0m   "
    return msg

def gen_multiple_puzzles(colors: str, amount: int, min_complexity: int, max_complexity: int, max_attempts: int, world: BluePrinceWorld) -> list[tuple[str]]:
    res = []

    i = 0
    while i < amount:
        colorcode, _, _ = gen_solvable_puzzle(colors, min_complexity, max_complexity, world, max_attempts)
        hashed = tuple(colorcode)
        if hashed in res:
            continue

        res.append(hashed)
        i += 1

    return res
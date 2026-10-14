import heapq
<<<<<<< HEAD
from collections.abc import Generator

Point = tuple[int, int]


def heuristic(a: Point, b: Point) -> int:
    # Manhattan distance (good for 4-directional grids)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(came_from: dict[Point, Point], current: Point) -> list[Point]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def find_path_or_closest(
    grid: tuple[tuple[bool, ...], ...], source_x: int, source_y: int, target_x: int, target_y: int
) -> list[Point]:
    start = source_x, source_y
    goal = target_x, target_y

    rows, cols = len(grid), len(grid[0])

    def in_bounds(p: Point) -> bool:
        return 0 <= p[0] < rows and 0 <= p[1] < cols

    def passable(p: Point) -> bool:
        return grid[p[1]][p[0]]

    def neighbors(p: Point) -> Generator[Point, None, None]:
        x, y = p
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            np = (x + dx, y + dy)
            if in_bounds(np) and passable(np):
                yield np

    open_heap: list[tuple[int, tuple[int, int]]] = []
    heapq.heappush(open_heap, (0, start))

    came_from: dict[Point, Point] = {}
    g_score = {start: 0}

    # Track best fallback node
    best_node = start
    best_dist = heuristic(start, goal)

    visited = set()

    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current in visited:
            continue
        visited.add(current)

        # Check if we reached the goal
        if current == goal:
            return reconstruct_path(came_from, current)

        # Update "closest node" fallback
        dist = heuristic(current, goal)
        if dist < best_dist or (dist == best_dist and g_score[current] < g_score.get(best_node, float("inf"))):
            best_node = current
            best_dist = dist

        for neighbor in neighbors(current):
            tentative_g = g_score[current] + 1  # cost is 1 per move

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_heap, (f_score, neighbor))

    # Goal not reachable → return path to closest node
    if best_node is not None:
        return reconstruct_path(came_from, best_node)

    return []
=======
from dataclasses import dataclass

MAX_DISTANCE = 1000000000


@dataclass
class Vertex:
    x: int
    y: int
    euclidean_distance_to_target: float
    distance: int = MAX_DISTANCE
    prev: "Vertex | None" = None

    def __lt__(self, other: "Vertex") -> bool:
        return self.distance < other.distance


def find_path_or_closest(
    traversibility_grid: tuple[tuple[bool, ...], ...], source_x: int, source_y: int, target_x: int, target_y: int
) -> list[tuple[int, int]]:
    vertex_grid = [
        [Vertex(x, y, (x - target_x) ** 2 + (y - target_y) ** 2) for x in range(len(traversibility_grid[0]))]
        for y in range(len(traversibility_grid))
    ]
    vertex_grid[source_y][source_x].distance = 0

    vertices = [vertex for row in vertex_grid for vertex in row]

    heapq.heapify(vertices)

    while vertices:
        vertex = heapq.heappop(vertices)

        if vertex.distance == MAX_DISTANCE:
            break

        for neighbor_x, neighbor_y in (
            (vertex.x + 1, vertex.y),
            (vertex.x - 1, vertex.y),
            (vertex.x, vertex.y + 1),
            (vertex.x, vertex.y - 1),
        ):
            if neighbor_x < 0:
                continue
            if neighbor_y < 0:
                continue
            if neighbor_x >= len(traversibility_grid[0]):
                continue
            if neighbor_y >= len(traversibility_grid):
                continue

            if not traversibility_grid[neighbor_y][neighbor_x]:
                continue

            other_vertex = vertex_grid[neighbor_y][neighbor_x]

            new_distance = vertex.distance + 1

            if new_distance < other_vertex.distance:
                other_vertex.distance = new_distance
                other_vertex.prev = vertex

            heapq.heapify(vertices)

    closest_vertex = min(
        (vertex for row in vertex_grid for vertex in row if vertex.distance < MAX_DISTANCE),
        key=lambda vertex: (vertex.euclidean_distance_to_target, vertex.distance),
    )

    path: list[tuple[int, int]] = []

    while closest_vertex.prev is not None:
        path.append((closest_vertex.x, closest_vertex.y))

        closest_vertex = closest_vertex.prev

    path.append((source_x, source_y))
    path.reverse()

    return path
>>>>>>> 5efa6aa29b12482b3ba39fe96967751d649bfb5d

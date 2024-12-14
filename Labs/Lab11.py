import unittest
import heapq

#1
def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter

# Unit Test
class TestIslandPerimeter(unittest.TestCase):
    def test_example(self):
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(island_perimeter(grid), 16)

if __name__ == "__main__":
    unittest.main()


#2
def prims_mst(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))

    visited = set()
    min_heap = [(0, 1)]
    mst_cost = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_cost += weight
            for edge in graph[node]:
                if edge[1] not in visited:
                    heapq.heappush(min_heap, edge)

    return mst_cost
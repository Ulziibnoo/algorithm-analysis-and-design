#include <vector>
#include <catch2/catch_test_macros.hpp>

int islandPerimeter(const std::vector<std::vector<int>>& grid) {
    int rows = grid.size(), cols = grid[0].size();
    int perimeter = 0;

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (grid[r][c] == 1) {
                perimeter += 4;
                if (r > 0 && grid[r - 1][c] == 1) perimeter -= 2;
                if (c > 0 && grid[r][c - 1] == 1) perimeter -= 2;
            }
        }
    }

    return perimeter;
}

TEST_CASE("Island Perimeter") {
    std::vector<std::vector<int>> grid = {
        {0, 1, 0, 0},
        {1, 1, 1, 0},
        {0, 1, 0, 0},
        {1, 1, 0, 0}
    };
    REQUIRE(islandPerimeter(grid) == 16);
}


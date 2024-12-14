#include <iostream>
#include <vector>
#include <cassert>

int optimalBSTCost(const std::vector<int>& keys, const std::vector<int>& freq) {
    int n = keys.size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

    for (int i = 0; i < n; ++i) {
        dp[i][i] = freq[i];
    }

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i <= n - len; ++i) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            int totalFreq = 0;

            for (int k = i; k <= j; ++k) {
                totalFreq += freq[k];
            }

            for (int r = i; r <= j; ++r) {
                int cost = (r > i ? dp[i][r - 1] : 0) + (r < j ? dp[r + 1][j] : 0) + totalFreq;
                dp[i][j] = std::min(dp[i][j], cost);
            }
        }
    }

    return dp[0][n - 1];
}

// Catch2 Unit Test
#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

TEST_CASE("Optimal BST Cost") {
    REQUIRE(optimalBSTCost({5, 6}, {17, 25}) == 59);
    REQUIRE(optimalBSTCost({10}, {5}) == 5);
    REQUIRE(optimalBSTCost({1, 2, 3}, {10, 20, 30}) == 110);
}

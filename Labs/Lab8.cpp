#include <vector>
#include <algorithm>
#include <limits.h>
#include <catch2/catch_test_macros.hpp>
#include <tuple>
#include <unordered_set>

//1
int coinChange(const std::vector<int>& coins, int amount) {
    std::vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0;

    for (const int& coin : coins) {
        for (int x = coin; x <= amount; ++x) {
            if (dp[x - coin] != INT_MAX) {
                dp[x] = std::min(dp[x], dp[x - coin] + 1);
            }
        }
    }

    return dp[amount] == INT_MAX ? -1 : dp[amount];
}

// Unit Test
TEST_CASE("Coin Change") {
    REQUIRE(coinChange({1, 2, 5}, 11) == 3);  
    REQUIRE(coinChange({2}, 3) == -1);       
    REQUIRE(coinChange({1}, 0) == 0);        
    REQUIRE(coinChange({1, 2, 5}, 100) == 20);
}

//2
int countPrimes(int n) {
    if (n < 2) return 0;

    std::vector<bool> is_prime(n, true);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i * i < n; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j < n; j += i) {
                is_prime[j] = false;
            }
        }
    }

    return std::count(is_prime.begin(), is_prime.end(), true);
}

// Unit Test
TEST_CASE("Count Primes") {
    REQUIRE(countPrimes(18) == 7);  // Primes: 2, 3, 5, 7, 11, 13, 17
    REQUIRE(countPrimes(1) == 0);  // No primes below 2
    REQUIRE(countPrimes(10) == 4);  // Primes: 2, 3, 5, 7
}

//3
std::vector<int> assignBikes(const std::vector<std::pair<int, int>>& students,
                             const std::vector<std::pair<int, int>>& bikes) {
    std::vector<std::tuple<int, int, int>> distances;

    for (int i = 0; i < students.size(); ++i) {
        for (int j = 0; j < bikes.size(); ++j) {
            int dist = abs(students[i].first - bikes[j].first) +
                       abs(students[i].second - bikes[j].second);
            distances.push_back({dist, i, j});
        }
    }

    std::sort(distances.begin(), distances.end());
    std::vector<int> result(students.size(), -1);
    std::unordered_set<int> assignedBikes;

    for (const auto& [dist, student, bike] : distances) {
        if (result[student] == -1 && assignedBikes.find(bike) == assignedBikes.end()) {
            result[student] = bike;
            assignedBikes.insert(bike);
        }
    }

    return result;
}

// Unit Test
TEST_CASE("Assign Bikes") {
    REQUIRE(assignBikes({{0, 0}, {1, 1}}, {{0, 1}, {4, 3}, {2, 1}}) == std::vector<int>{0, 2});
    REQUIRE(assignBikes({{0, 0}}, {{1, 1}}) == std::vector<int>{0});
}
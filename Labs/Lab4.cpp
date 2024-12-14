#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>

int knapsack(int W, std::vector<int>& weights, std::vector<int>& values, int n) {
   std::vector<std::vector<int>> dp(n + 1, std::vector<int>(W + 1, 0));
   
   for (int i = 1; i <= n; i++) {
      for (int w = 1; w <= W; w++) {
         if (weights[i - 1] <= w) {
               dp[i][w] = std::max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
         } else {
               dp[i][w] = dp[i - 1][w];
         }
      }
   }
   
   return dp[n][W];
}

void test_knapsack() {
    std::vector<int> values = {60, 100, 120};
    std::vector<int> weights = {10, 20, 30};
    int W = 50;
    int n = values.size();
    assert(knapsack(W, weights, values, n) == 220);

    std::vector<int> values2 = {1, 2, 3};
    std::vector<int> weights2 = {4, 5, 1};
    int W2 = 4;
    assert(knapsack(W2, weights2, values2, values2.size()) == 3);
    
    std::cout << "All tests passed!\n";
}

int main() {
    test_knapsack();
    return 0;
}
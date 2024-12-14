#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<int, int> memo;

//5.1 Fibonacci
int fibonacci(int n) {
   if (memo.count(n)) {
      return memo[n];
   }
   if (n <= 1) {
      return n;
   }
   return memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
}

//5.2 Knapsack
int knapsack(const vector<int>& weights, const vector<int>& values, int capacity) {
   int n = values.size();

   int dp[n + 1][capacity + 1];

   for (int i = 0; i <= n; i++) {
      for (int w = 0; w <= capacity; w++) {
         dp[i][w] = 0;
      }
   }

   for (int i = 1; i <= n; i++) {
      for (int w = 1; w <= capacity; w++) {
         if (weights[i - 1] <= w) {
            dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
         } else {
            dp[i][w] = dp[i - 1][w];
         }
      }
   }
   return dp[n][capacity];
}


int main() {
   //5.1 Fibonacci
   int n = 10;
   cout << "Fibonacci of " << n << " is " << fibonacci(n) << endl;

   //5.2 Knapsack
   vector<int> values = {60, 100, 120};
   vector<int> weights = {10, 20, 30};
   int capacity = 50;
   cout << "Maximum value in Knapsack: " << knapsack(weights, values, capacity) << endl;
   


   return 0;
}
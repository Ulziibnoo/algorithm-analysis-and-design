#5.1
def fibonacci(n, memo={}):
   if n in memo:
      return memo[n]
   if n <= 1:
      return n
   memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
   return memo[n]

n = 10
print(f"Fibonacci of {n} is {fibonacci(n)}")

#5.2
def knapsack(weights, values, capacity):
   n = len(values)
   dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

   for i in range(1, n + 1):
      for w in range(1, capacity + 1):
         if weights[i - 1] <= w:
               dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
         else:
               dp[i][w] = dp[i - 1][w]

   return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(f"Maximum value in Knapsack: {knapsack(weights, values, capacity)}")
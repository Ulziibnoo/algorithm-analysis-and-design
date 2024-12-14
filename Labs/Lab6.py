import unittest

def optimal_bst_cost(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = freq[i]  
    
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            sum_freq = sum(freq[i:j + 1])
            
            for r in range(i, j + 1):
                cost = (dp[i][r - 1] if r > i else 0) + \
                (dp[r + 1][j] if r < j else 0) + sum_freq
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

class TestOptimalBSTCost(unittest.TestCase):
    def test_example(self):
        keys = [5, 6]
        freq = [17, 25]
        self.assertEqual(optimal_bst_cost(keys, freq), 59)

    def test_single_key(self):
        keys = [10]
        freq = [5]
        self.assertEqual(optimal_bst_cost(keys, freq), 5)

if __name__ == "__main__":
    unittest.main()
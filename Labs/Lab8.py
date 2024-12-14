import unittest

#1
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Unit Test
class TestCoinChange(unittest.TestCase):
    def test_example(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)  
        self.assertEqual(coin_change([2], 3), -1)
        self.assertEqual(coin_change([1], 0), 0) 
        self.assertEqual(coin_change([1, 2, 5], 100), 20)

if __name__ == "__main__":
    unittest.main()
    
#2
def count_primes(n):
    if n < 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)

# Unit Test
class TestCountPrimes(unittest.TestCase):
    def test_example(self):
        self.assertEqual(count_primes(18), 7)
        self.assertEqual(count_primes(1), 0) 
        self.assertEqual(count_primes(10), 4)

if __name__ == "__main__":
    unittest.main()

#3
def assign_bikes(students, bikes):
    distances = []
    for i, (sx, sy) in enumerate(students):
        for j, (bx, by) in enumerate(bikes):
            dist = abs(sx - bx) + abs(sy - by)
            distances.append((dist, i, j))
    distances.sort()

    assigned_bikes = set()
    result = [-1] * len(students)

    for _, student, bike in distances:
        if result[student] == -1 and bike not in assigned_bikes:
            result[student] = bike
            assigned_bikes.add(bike)

    return result

# Unit Test
class TestAssignBikes(unittest.TestCase):
    def test_example(self):
        students = [(0, 0), (1, 1)]
        bikes = [(0, 1), (4, 3), (2, 1)]
        self.assertEqual(assign_bikes(students, bikes), [0, 2])

    def test_single_student_bike(self):
        students = [(0, 0)]
        bikes = [(1, 1)]
        self.assertEqual(assign_bikes(students, bikes), [0])

if __name__ == "__main__":
    unittest.main()
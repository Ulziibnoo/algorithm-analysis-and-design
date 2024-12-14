import unittest

def fibonacci(n, cache={}):
   if n in cache:
      return cache[n]
   if n <= 1:
      return n
   cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
   return cache[n]

class TestFibonacci(unittest.TestCase):
   def test_fibonacci(self):
      self.assertEqual(fibonacci(0), 0)
      self.assertEqual(fibonacci(1), 1)
      self.assertEqual(fibonacci(5), 5)
      self.assertEqual(fibonacci(10), 55)
      self.assertEqual(fibonacci(20), 6765)

if __name__ == "__main__":
   unittest.main()




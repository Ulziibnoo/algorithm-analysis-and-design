import unittest

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    total_value = 0

    for item in items:
        if capacity >= item.weight:
            total_value += item.value
            capacity -= item.weight
        else:
            total_value += item.value * (capacity / item.weight)
            break

    return total_value

# Unit Test
class TestFractionalKnapsack(unittest.TestCase):
    def test_example(self):
        items = [Item(10, 60), Item(20, 100), Item(30, 120)]
        self.assertAlmostEqual(fractional_knapsack(items, 50), 240.0, places=2)

    def test_no_capacity(self):
        items = [Item(10, 60), Item(20, 100)]
        self.assertAlmostEqual(fractional_knapsack(items, 0), 0.0)

if __name__ == "__main__":
    unittest.main()

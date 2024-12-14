import unittest

#1
def aggregate_analysis(n):
    total_cost = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:  
            total_cost += i
        else:
            total_cost += 1
    return total_cost

# Unit Test
class TestAggregateAnalysis(unittest.TestCase):
    def test_example(self):
        self.assertEqual(aggregate_analysis(16), 31)  # Cost calculation example
        self.assertEqual(aggregate_analysis(1), 1)   # Only one operation
        self.assertEqual(aggregate_analysis(4), 7)   # Sum of costs: 1, 1, 1, 4

if __name__ == "__main__":
    unittest.main()

class BackupStack:
    def __init__(self, k):
        self.stack = []
        self.backup = []
        self.k = k
        self.operation_count = 0

    def push(self, value):
        self.stack.append(value)
        self.operation_count += 1
        if self.operation_count % self.k == 0:
            self.backup = self.stack.copy()

    def pop(self):
        if self.stack:
            self.operation_count += 1
            if self.operation_count % self.k == 0:
                self.backup = self.stack.copy()
            return self.stack.pop()
        return None

# Unit Test
class TestBackupStack(unittest.TestCase):
    def test_backup(self):
        stack = BackupStack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)  # Backup occurs here
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.backup, [1, 2])

if __name__ == "__main__":
    unittest.main()

#2
class DynamicArray:
    def __init__(self):
        self.array = []
        self.capacity = 1 

    def insert(self, value):
        if len(self.array) == self.capacity:
            self.capacity *= 2 
            self.array.extend([None] * (self.capacity - len(self.array)))  
        self.array.append(value)

    def size(self):
        return len(self.array)

class TestDynamicArray(unittest.TestCase):
    def test_insert(self):
        dyn_array = DynamicArray()

        for i in range(1, 11):
            dyn_array.insert(i)
            self.assertEqual(dyn_array.size(), i)
        
        self.assertEqual(dyn_array.capacity, 16)

if __name__ == "__main__":
    unittest.main()

import unittest
from collections import deque

#1
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x: int):
        self.in_stack.append(x)
    
    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

# Unit Test
class TestMyQueue(unittest.TestCase):
    def test_queue(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.pop(), 1)
        self.assertFalse(queue.empty())

if __name__ == "__main__":
    unittest.main()


#2
class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

# Unit Test
class TestMyStack(unittest.TestCase):
    def test_stack(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.empty())

if __name__ == "__main__":
    unittest.main()

#3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Unit Test
class TestHasCycle(unittest.TestCase):
    def test_cycle(self):
        head = ListNode(3)
        node2 = ListNode(2)
        node0 = ListNode(0)
        node4 = ListNode(-4)
        head.next = node2
        node2.next = node0
        node0.next = node4
        node4.next = node2  # Creates a cycle
        self.assertTrue(hasCycle(head))

        no_cycle_head = ListNode(1)
        no_cycle_head.next = ListNode(2)
        self.assertFalse(hasCycle(no_cycle_head))

if __name__ == "__main__":
    unittest.main()
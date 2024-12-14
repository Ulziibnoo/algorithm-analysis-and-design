#include <stack>
#include <catch2/catch_test_macros.hpp>
#include <queue>

//1
class MyQueue {
    std::stack<int> in_stack, out_stack;

public:
    void push(int x) {
        in_stack.push(x);
    }

    int pop() {
        if (out_stack.empty()) {
            while (!in_stack.empty()) {
                out_stack.push(in_stack.top());
                in_stack.pop();
            }
        }
        int top = out_stack.top();
        out_stack.pop();
        return top;
    }

    int peek() {
        if (out_stack.empty()) {
            while (!in_stack.empty()) {
                out_stack.push(in_stack.top());
                in_stack.pop();
            }
        }
        return out_stack.top();
    }

    bool empty() {
        return in_stack.empty() && out_stack.empty();
    }
};

TEST_CASE("Queue Using Stacks") {
    MyQueue queue;
    queue.push(1);
    queue.push(2);
    REQUIRE(queue.peek() == 1);
    REQUIRE(queue.pop() == 1);
    REQUIRE(!queue.empty());
}


//2
class MyStack {
    std::queue<int> queue;

public:
    void push(int x) {
        queue.push(x);
        for (int i = 0; i < queue.size() - 1; ++i) {
            queue.push(queue.front());
            queue.pop();
        }
    }

    int pop() {
        int top = queue.front();
        queue.pop();
        return top;
    }

    int top() {
        return queue.front();
    }

    bool empty() {
        return queue.empty();
    }
};

TEST_CASE("Stack Using Queues") {
    MyStack stack;
    stack.push(1);
    stack.push(2);
    REQUIRE(stack.top() == 2);
    REQUIRE(stack.pop() == 2);
    REQUIRE(!stack.empty());
}

//3
#include <unordered_set>
#include <catch2/catch_test_macros.hpp>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true;
        }
    }

    return false;
}

TEST_CASE("Detect Linked List Cycle") {
    ListNode* head = new ListNode(3);
    ListNode* node2 = new ListNode(2);
    ListNode* node0 = new ListNode(0);
    ListNode* node4 = new ListNode(-4);
    head->next = node2;
    node2->next = node0;
    node0->next = node4;
    node4->next = node2;  // Creates a cycle

    REQUIRE(hasCycle(head) == true);

    ListNode* no_cycle_head = new ListNode(1);
    no_cycle_head->next = new ListNode(2);
    REQUIRE(hasCycle(no_cycle_head) == false);
}
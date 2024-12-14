#include <catch2/catch_test_macros.hpp>
#include <cmath>
#include <vector>

//1
int aggregateAnalysis(int n) {
    int total_cost = 0;
    for (int i = 1; i <= n; ++i) {
        if ((i & (i - 1)) == 0) {  // Check if i is a power of 2
            total_cost += i;
        } else {
            total_cost += 1;
        }
    }
    return total_cost;
}

TEST_CASE("Aggregate Analysis") {
    REQUIRE(aggregateAnalysis(16) == 31);
    REQUIRE(aggregateAnalysis(1) == 1);
    REQUIRE(aggregateAnalysis(4) == 7);
}

//2
class BackupStack {
    std::vector<int> stack;
    std::vector<int> backup;
    int k;
    int operation_count;

public:
    BackupStack(int interval) : k(interval), operation_count(0) {}

    void push(int value) {
        stack.push_back(value);
        operation_count++;
        if (operation_count % k == 0) {
            backup = stack;
        }
    }

    int pop() {
        if (!stack.empty()) {
            int value = stack.back();
            stack.pop_back();
            operation_count++;
            if (operation_count % k == 0) {
                backup = stack;
            }
            return value;
        }
        return -1;  // Indicates stack is empty
    }

    std::vector<int> getBackup() const {
        return backup;
    }
};

TEST_CASE("Backup Stack") {
    BackupStack stack(3);
    stack.push(1);
    stack.push(2);
    stack.push(3);  // Backup occurs here
    REQUIRE(stack.pop() == 3);
    REQUIRE(stack.getBackup() == std::vector<int>{1, 2});
}
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>

struct Item {
    int weight;
    int value;
};

bool compare(Item a, Item b) {
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2;
}

double fractionalKnapsack(std::vector<Item> items, int capacity) {
    std::sort(items.begin(), items.end(), compare);
    double totalValue = 0.0;

    for (const auto& item : items) {
        if (capacity >= item.weight) {
            totalValue += item.value;
            capacity -= item.weight;
        } else {
            totalValue += item.value * ((double)capacity / item.weight);
            break;
        }
    }

    return totalValue;
}

void testFractionalKnapsack() {
    std::vector<Item> items = {{10, 60}, {20, 100}, {30, 120}};
    assert(abs(fractionalKnapsack(items, 50) - 240.0) < 1e-6);
    std::cout << "All fractionalKnapsack tests passed!" << std::endl;
}

int main() {
    testFractionalKnapsack();
    return 0;
}

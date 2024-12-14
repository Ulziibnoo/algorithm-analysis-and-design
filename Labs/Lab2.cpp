#include <iostream>
#include <vector>
#include <cassert>

using std::vector;

//Insertion sort
void insertion_sort(vector<int>& arr) {
   for (int i = 0; i < arr.size(); i++) {
      int key = arr[i];
      int j = i - 1;

      while (j >= 0 && arr[j] > key) {
         arr[j + 1] = arr[j];
         j--;
      }
      arr[j + 1] = key;
   }
}

//Merge sort
void merge(vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int i = 0; i < n2; i++)
        R[i] = arr[m + 1 + i];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        merge_sort(arr, l, m);
        merge_sort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

//Binary search
int binary_search(vector<int>& arr, int target) {
    merge_sort(arr, 0, arr.size() - 1);

    int left = 0, right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target)
            return target;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1;  
}


//Find max (divide and conquer)
int find_max(const vector<int>& arr, int low, int high) {
    if (low == high)
        return arr[low];

    int mid = (low + high) / 2;
    int left_max = find_max(arr, low, mid);
    int right_max = find_max(arr, mid + 1, high);

    return std::max(left_max, right_max);
}



int main() {
    //Insertion sort test
    vector<int> arr = {12, 11, 13, 5, 6, 3, 1, 8};
    
    insertion_sort(arr);
    for(int i: arr){
        std::cout << i << " ";
    }
    std::cout << "\n";

    //Merge sort test
    vector<int> arr1 = {5, 11, 9, 3, 6, 1, 4, 8};

    merge_sort(arr1, 0, arr1.size() - 1);
    for(int i: arr1){
        std::cout << i << " ";
    }
    std::cout << "\n";
    

    //Binary search test
    vector<int> arr2 = {5, 11, 9, 3, 6, 1, 4, 8};
    int result = binary_search(arr2, 11);
    std::cout << result;

    //Find max test
    vector<int> arr3 = {12, 11, 13, 5, 6};
    int result2 = find_max(arr3, 0, arr3.size() - 1);
    assert(result2 == 13 && "Test failed");
    std::cout << "\nFind max passed\n";
    
    return 0;
}
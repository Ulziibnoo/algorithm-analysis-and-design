#Insertion Sort
def insertion_sort(array):
   arr = array
   for i in range(1, len(arr)):
      cur_val = arr[i]
      pre_idx = i - 1

      while pre_idx >= 0 and cur_val < arr[pre_idx]:
         arr[pre_idx + 1] = arr[pre_idx]
         pre_idx -= 1

      arr[pre_idx + 1] = cur_val

   return arr

arr = [12, 11, 13, 5, 6, 1, 3]
print(arr)

#Merge Sort
def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index = right_index = merged_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                array[merged_index] = left_half[left_index]
                left_index += 1
            else:
                array[merged_index] = right_half[right_index]
                right_index += 1
            merged_index += 1

        while left_index < len(left_half):
            array[merged_index] = left_half[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_half):
            array[merged_index] = right_half[right_index]
            right_index += 1
            merged_index += 1

    return array

arr = [12, 11, 13, 5, 6]
print(merge_sort(arr))

#Recursive Binary Search
def binary_search(arr, left, right, target): # 2, 3, 4, 10, 40 /2 /40 /10 
    arr.sort()
    if right >= left: #40 > 2 
        middle = left + (right - left) // 2 #  =

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            return binary_search(arr, left, middle - 1, target)
        else:
            return binary_search(arr, middle + 1, right, target)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
print("At index: ", binary_search(arr, 0, len(arr) - 1, 10))

#Divide and Conquer
def find_max(arr, low, high):
   if low == high:
      return arr[low]

   mid = (low + high) // 2
   left_max = find_max(arr, low, mid)
   right_max = find_max(arr, mid + 1, high)

   return max(left_max, right_max)

arr = [12, 11, 13, 5, 6]
print("Max number: ", find_max(arr, 0, len(arr) - 1))

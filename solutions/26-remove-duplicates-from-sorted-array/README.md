# [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
Easy, Python3
## Approach
The key insight here is to take advantage of the fact that the input array is already sorted in non-decreasing order. This allows us to compare adjacent elements to identify duplicates. A naive approach would be to create a new array and append unique elements to it, but this would require extra space. Instead, we can modify the input array in-place by maintaining a pointer `k` that keeps track of the position where the next unique element should be placed. Here's a short walkthrough of the logic:
1. Initialize `k` to 1, assuming the first element is always unique.
2. Iterate through the array starting from the second element.
3. If the current element is different from the previous one, place it at the `k`-th position and increment `k`.
## Complexity
The time complexity is O(n), because we are scanning the array once, where n is the number of elements in the array. The space complexity is O(1), because we are modifying the input array in-place and using a constant amount of extra space to store the `k` pointer.
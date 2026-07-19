# [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
Medium, Python3
## Approach
The key insight here is to use a modified binary search algorithm to find the target in the rotated array. This approach was chosen over a naive brute-force linear search because it allows us to achieve the required O(log n) runtime complexity. Here's a short walkthrough of the logic:
1. Initialize two pointers, left and right, to the start and end of the array respectively.
2. Calculate the mid index and compare the value at this index with the target.
3. If the left half of the array is sorted, determine which half the target is likely to be in and adjust the pointers accordingly.
4. If the left half is not sorted, the right half must be sorted, so again determine which half the target is likely to be in and adjust the pointers.
## Complexity
Time complexity: O(log n), because with each iteration of the while loop, we are effectively halving the size of the search space.
Space complexity: O(1), because we are only using a constant amount of space to store the pointers and the mid index.
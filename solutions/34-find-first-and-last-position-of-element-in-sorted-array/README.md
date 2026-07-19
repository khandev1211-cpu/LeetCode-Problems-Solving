# [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
Medium, Python3
## Approach
The key insight here is to use a modified binary search algorithm to find both the first and last occurrence of the target element in the sorted array. This approach is chosen over a naive linear search because it allows us to achieve the required O(log n) runtime complexity. Here's a short walkthrough of the logic:
1. Define two helper functions, `find_first` and `find_last`, each using a binary search approach to find the first and last occurrence of the target element, respectively.
2. In `find_first`, if the middle element is less than the target, move the left pointer to the right of the middle element. Otherwise, move the right pointer to the left of the middle element.
3. In `find_last`, if the middle element is less than or equal to the target, move the left pointer to the right of the middle element. Otherwise, move the right pointer to the left of the middle element.
4. Use these helper functions to find the first and last occurrence of the target element, and return the result as a list.
## Complexity
The time complexity is O(log n) because we are using a binary search approach to find both the first and last occurrence of the target element, which reduces the search space by half at each step.
The space complexity is O(1) because we are only using a constant amount of space to store the pointers and the result, and not any data structures that scale with the input size.
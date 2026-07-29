# [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
Medium, Python3
## Approach
The key insight here is to recognize that a simple `in` check in Python can solve this problem efficiently because it leverages optimized C code under the hood for searching in lists. This approach was chosen over a naive brute-force approach (like manually iterating through the list) because it is more efficient and Pythonic. Here's a brief walkthrough:
1. The function checks if the target is present in the list `nums` using the `in` operator.
2. If the target is found, the function immediately returns `True`.
3. If the target is not found after checking all elements, the function returns `False`.
## Complexity
The time complexity is O(n) because in the worst-case scenario, Python's `in` operator has to iterate through all elements in the list to confirm the presence or absence of the target. The space complexity is O(1) because this solution does not use any additional space that scales with input size.
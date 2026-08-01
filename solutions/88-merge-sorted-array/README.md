# Merge Sorted Array
[https://leetcode.com/problems/merge-sorted-array/](https://leetcode.com/problems/merge-sorted-array/)
Easy, python3
## Approach
The key insight here is to utilize the existing space in `nums1` and then sort it. A naive approach would be to create a new array and then sort it, but this would require extra space. Instead, we can directly assign the elements of `nums2` to the end of `nums1` and then sort `nums1` in-place. Here's a short walkthrough:
1. Assign the elements of `nums2` to the end of `nums1` using slice assignment.
2. Sort `nums1` in-place using the built-in `sort` method.
## Complexity
Time complexity: The time complexity is O((m + n) log(m + n)) because the `sort` method in Python uses Timsort, which has a worst-case time complexity of O(n log n).
Space complexity: The space complexity is O(1) because we are sorting `nums1` in-place and not using any extra space that scales with the input size.
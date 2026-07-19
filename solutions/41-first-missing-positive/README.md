# [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
Hard, Python3
## Approach
The key insight here is to utilize the given array itself as extra space, thus adhering to the O(1) auxiliary space constraint. This approach is chosen over a naive sorting or hash set approach because it allows us to achieve the required O(n) time complexity without using additional space that scales with input size. The steps are:
1. Iterate through the array and for each positive number, attempt to place it in its corresponding index (i.e., the number `x` should be placed at index `x-1` if possible).
2. After rearranging the numbers, scan the array to find the first index that does not match its expected value (i.e., `nums[i] != i + 1`).
## Complexity
The time complexity is O(n) because each element is visited at most twice: once in the rearrangement step and once in the scanning step. The space complexity is O(1) because, aside from a constant amount of space for variables, no additional space that scales with input size is used.
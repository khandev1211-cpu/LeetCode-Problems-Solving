# [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
Medium, Python3
## Approach
The key insight here is to treat the 2D matrix as a 1D sorted array, given that each row is sorted in non-decreasing order and the first integer of each row is greater than the last integer of the previous row. This allows us to apply a binary search approach, which is more efficient than a brute-force linear search. Here's a short walkthrough of the logic:
1. Calculate the total number of elements in the matrix (m * n).
2. Initialize two pointers, left and right, to the start and end of the virtual 1D array, respectively.
3. Perform a binary search, calculating the mid index and mapping it to the corresponding element in the 2D matrix.
4. Compare the mid element to the target and adjust the left and right pointers accordingly.
## Complexity
Time complexity is O(log(m * n)) because we are performing a binary search on the virtual 1D array, which has m * n elements. Space complexity is O(1) because we are only using a constant amount of space to store the pointers and the mid element, regardless of the size of the input matrix.
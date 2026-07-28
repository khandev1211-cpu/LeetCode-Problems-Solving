# [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
Medium, Python3
## Approach
The key insight here is to utilize the first row and column of the matrix as flags to mark which rows and columns need to be zeroed out. This approach was chosen over a naive one that would use additional space (like separate arrays or sets) to keep track of rows and columns to zero, because it allows for an in-place solution that minimizes extra space usage. Here's a short walkthrough of the logic:
1. First, we initialize flags to track if the first column needs to be zeroed.
2. Then, we iterate through the matrix (excluding the first row and column), and whenever we encounter a zero, we mark the corresponding row and column in the first row and column.
3. After that, we iterate through the matrix again (excluding the first row and column), and zero out any row or column that was marked in the previous step.
4. Finally, we handle the first row and column separately, zeroing them out if necessary.
## Complexity
Time complexity: The solution has a time complexity of O(m*n) because we're doing a constant amount of work for each cell in the matrix, where m is the number of rows and n is the number of columns. This is justified because we make two passes through the matrix.
Space complexity: The space complexity is O(1) because we're only using a constant amount of space to store our flags and variables, and we're modifying the input matrix in-place.
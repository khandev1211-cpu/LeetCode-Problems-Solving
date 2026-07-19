# [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
Medium, Python3
## Approach
The key insight here is to use sets to keep track of the values we've seen so far in each row, column, and 3x3 sub-box. This approach is chosen over a naive one, such as sorting each row, column, and sub-box, because it allows us to check for duplicates in constant time. Here's a short walkthrough of the logic:
1. Initialize sets for each row, column, and sub-box.
2. Iterate over the Sudoku board, and for each cell, check if the value is already in the corresponding row, column, or sub-box set.
3. If it is, return False, as this means the Sudoku board is invalid.
4. If not, add the value to the corresponding sets and continue.
## Complexity
Time complexity: The time complexity is O(1) because we're doing a constant amount of work for each cell in the Sudoku board, and the size of the board is fixed at 9x9. 
Space complexity: The space complexity is O(1) because we're using a constant amount of space to store the sets for each row, column, and sub-box.
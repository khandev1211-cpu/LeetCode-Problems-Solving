# [Number of Paths with Max Score](https://leetcode.com/problems/number-of-paths-with-max-score/)
Difficulty: Hard, Language: python3
## Approach
The key insight here is to use dynamic programming to track the maximum sum and the number of paths to achieve that sum at each cell. A naive approach would be to try all possible paths and keep track of the maximum sum and the number of paths, but this would be inefficient due to the large number of possible paths. Instead, we use a bottom-up dynamic programming approach, starting from the 'S' cell and working our way up to the 'E' cell. Here's a short walkthrough of the logic:
1. Initialize the dp table with -1 for unreachable cells and (0, 1) for the 'S' cell.
2. Iterate over the cells in reverse order, and for each cell, check the cells below, to the right, and diagonally below-right.
3. If a cell is reachable, update the maximum sum and the number of paths to reach that sum.
## Complexity
The time complexity is O(n^2) because we are iterating over the cells in the grid once, where n is the number of rows (or columns) in the grid. This is justified because we are doing a constant amount of work for each cell. The space complexity is O(n^2) because we are storing the dp table, which has the same number of cells as the input grid. This is justified because we need to store the maximum sum and the number of paths for each cell.
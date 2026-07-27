# [Unique Paths](https://leetcode.com/problems/unique-paths/)
Medium, Python3
## Approach
The key insight here is to recognize that this problem can be solved using dynamic programming, specifically by storing the number of unique paths to each cell in the grid. A naive approach would be to try all possible paths and count them, but this would be inefficient due to the large number of possible paths. The dynamic programming approach was chosen because it allows us to avoid redundant calculations and solve the problem more efficiently. Here's a short walkthrough of the logic:
1. Initialize a 2D array `dp` with dimensions `m x n`, where `dp[i][j]` represents the number of unique paths to cell `(i, j)`.
2. Fill in the base cases, where `dp[i][0] = 1` for all `i` and `dp[0][j] = 1` for all `j`, since there is only one way to reach cells in the first row or column.
3. For each cell `(i, j)` in the grid, calculate `dp[i][j]` as the sum of `dp[i-1][j]` and `dp[i][j-1]`, which represents the number of unique paths to cell `(i, j)`.
## Complexity
The time complexity is O(m*n), because we need to fill in the `dp` array, which has `m*n` cells. The space complexity is O(m*n), because we need to store the `dp` array, which has `m*n` cells.
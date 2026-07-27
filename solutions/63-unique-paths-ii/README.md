# [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
Medium, Python3
## Approach
The key insight here is to use dynamic programming to solve this problem. A naive approach would be to try all possible paths and count the ones that do not include obstacles. However, this approach would be inefficient due to the large number of possible paths. Instead, we use a dynamic programming table `dp` where `dp[i][j]` represents the number of unique paths from the top-left corner to the cell at `(i, j)`. We fill this table row by row, using the fact that the number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left, if the current cell is not an obstacle. Here is a short walkthrough of the logic:
1. Initialize the starting point `dp[0][0]` to 1 if it is not an obstacle, and 0 otherwise.
2. Fill the first column and the first row of the `dp` table, based on whether the cells are obstacles or not.
3. Fill the rest of the `dp` table, using the fact that the number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left, if the current cell is not an obstacle.
## Complexity
The time complexity is O(m*n), because we need to fill the `dp` table of size m*n. The space complexity is O(m*n), because we need to store the `dp` table of size m*n.
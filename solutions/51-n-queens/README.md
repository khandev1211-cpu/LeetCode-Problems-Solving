# [N-Queens](https://leetcode.com/problems/n-queens/)
Hard, Python3
## Approach
The key insight here is to use a backtracking approach to solve the n-queens puzzle. This approach was chosen over a brute-force one, such as trying all possible board configurations, because it allows us to prune branches that will not lead to a solution. Here's a short walkthrough of the logic:
1. Start with an empty board and try to place a queen in each column of the first row.
2. For each placement, check if the queen is under attack by any previously placed queens.
3. If the queen is not under attack, recursively try to place queens in the next row.
## Complexity
The time complexity is O(N!) because in the worst case, we have to try all possible placements of queens. The space complexity is O(N) because we need to store the current board configuration and the sets of occupied columns and diagonals.
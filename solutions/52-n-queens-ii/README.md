# [N-Queens II](https://leetcode.com/problems/n-queens-ii/)
Hard, Python3
## Approach
The key insight is to use a backtracking approach to efficiently explore all possible configurations of the board. This approach was chosen over a brute-force one, which would involve checking all possible permutations of queen placements, because it allows us to prune branches of the search tree that are guaranteed to not lead to a solution. Here's a short walkthrough of the logic:
1. Start with an empty board and a set of available columns, diagonals, and anti-diagonals.
2. For each row, try placing a queen in each available column.
3. If a placement is valid (i.e., does not attack any existing queens), recursively explore the next row.
4. If a placement is not valid, backtrack and try the next column.
## Complexity
The time complexity is O(N!) because in the worst case, we have to try all possible permutations of queen placements. The space complexity is O(N) because we need to store the sets of available columns, diagonals, and anti-diagonals.
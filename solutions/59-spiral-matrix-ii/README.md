# [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)
Medium, python3
## Approach
The key insight here is to use a direction array to keep track of the current direction of movement in the matrix. This approach was chosen over a naive brute-force approach, such as trying all possible directions at each step, because it allows for efficient and systematic traversal of the matrix. Here's a short walkthrough of the logic:
1. Initialize the matrix with zeros and set the initial direction to right.
2. Iterate over the numbers from 1 to n^2, placing each number in the current position in the matrix.
3. Check if the next position in the current direction is within the matrix and empty. If it is, move to that position. Otherwise, turn right and move to the next position.
## Complexity
Time complexity: O(n^2), because we need to fill in all n^2 positions in the matrix.
Space complexity: O(n^2), because we need to store the entire n x n matrix.
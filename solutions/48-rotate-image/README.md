# [Rotate Image](https://leetcode.com/problems/rotate-image/)
Medium, python3
## Approach
The key insight here is to break down the rotation into two simpler operations: transposing the matrix and then reversing each row. This approach was chosen over a brute-force one (e.g., creating a new matrix and manually filling it with the rotated elements) because it minimizes the number of operations and avoids allocating additional space. Here's a short walkthrough of the logic:
1. Transpose the matrix: Swap the elements across the main diagonal to turn rows into columns and vice versa.
2. Reverse each row: After transposing, reversing each row achieves the desired 90-degree clockwise rotation.
## Complexity
Time complexity: The time complexity is O(n^2) because in the worst case, we are iterating over the entire matrix twice: once for transposing and once for reversing.
Space complexity: The space complexity is O(1) because we are modifying the input matrix in-place and not using any additional space that scales with the input size.
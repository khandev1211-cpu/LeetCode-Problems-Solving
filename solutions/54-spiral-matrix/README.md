# [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
Medium, Python3
## Approach
The key insight here is to iteratively traverse the matrix in a spiral order by maintaining four pointers (top, bottom, left, right) that define the current boundaries of the matrix. This approach was chosen over a naive brute-force one, such as attempting to directly calculate the next element in the spiral order, because it allows for a more efficient and straightforward implementation. Here's a short walkthrough of the logic:
1. Initialize the result list and the four pointers.
2. Traverse the top row from left to right, appending each element to the result list and incrementing the top pointer.
3. Traverse the right column from top to bottom, appending each element to the result list and decrementing the right pointer.
4. If the top pointer is still less than or equal to the bottom pointer, traverse the bottom row from right to left, appending each element to the result list and decrementing the bottom pointer.
5. If the left pointer is still less than or equal to the right pointer, traverse the left column from bottom to top, appending each element to the result list and incrementing the left pointer.
## Complexity
Time complexity: The algorithm has a time complexity of O(m*n) because it visits each element in the matrix exactly once, where m is the number of rows and n is the number of columns. 
Space complexity: The algorithm has a space complexity of O(m*n) because in the worst case, the result list will contain all elements from the matrix.
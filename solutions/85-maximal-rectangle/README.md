# [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
Hard, Python3
## Approach
The key insight here is to treat each row in the matrix as the bottom of a histogram and calculate the maximum area of the rectangle that can be formed using the heights of the histogram bars. This approach was chosen over a naive brute-force one, which would involve checking all possible rectangles in the matrix, because it reduces the time complexity significantly. Here's a short walkthrough of the logic:
1. Initialize an array `heights` to store the heights of the histogram bars for each column.
2. Iterate over each row in the matrix, updating the `heights` array based on whether the current cell is '1' or '0'.
3. Use a stack to calculate the maximum area of the rectangle that can be formed using the current `heights` array.
## Complexity
The time complexity is O(rows * cols) because we are iterating over each cell in the matrix once, and the space complexity is O(cols) because we are using an array of size `cols` to store the heights of the histogram bars.
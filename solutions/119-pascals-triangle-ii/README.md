# [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)
Easy, Python3
## Approach
The key insight here is to iteratively build up the rows of Pascal's triangle, starting from the first row which is just [1]. This approach is chosen over the naive approach of calculating each element from scratch using combinatorial formulas because it avoids redundant calculations and takes advantage of the fact that each row can be generated from the previous one. Here's a short walkthrough of the logic:
1. Initialize the first row as [1].
2. For each subsequent row up to the target row index, generate the new row by summing adjacent pairs of elements from the previous row, effectively implementing the rule that each number in Pascal's triangle is the sum of the two numbers directly above it.
## Complexity
The time complexity is O(rowIndex^2) because in the worst case, we are generating each row up to the target row index, and generating each row takes linear time proportional to the row index. The space complexity is O(rowIndex) because we only need to store the current row being generated, which has a length of rowIndex + 1.
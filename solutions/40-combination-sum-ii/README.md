# [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to find all unique combinations of candidate numbers that sum to the target. This approach was chosen over a naive brute-force one, such as generating all possible combinations and then filtering, because it allows us to prune branches early when the remaining sum becomes negative. Here's a short walkthrough of the logic:
1. Sort the candidate numbers to facilitate duplicate detection and early pruning.
2. Define a recursive backtrack function that takes the remaining sum, the current combination, and the starting index.
3. Within the backtrack function, iterate over the candidate numbers, skipping duplicates and adding each number to the current combination.
4. Recursively call the backtrack function with the updated remaining sum and combination.
## Complexity
Time complexity: The time complexity is O(2^n) because in the worst case, we might have to explore all possible combinations of the candidate numbers, where n is the number of candidates. This is justified because the backtracking approach still needs to consider all possible branches, even though it prunes some early.
Space complexity: The space complexity is O(n) because the maximum depth of the recursion call stack is equal to the number of candidates, which is used to store the recursive call stack and the current combination.
# [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to generate all combinations of well-formed parentheses. This approach was chosen over a naive brute-force one, such as generating all possible combinations of parentheses and then filtering out the well-formed ones, because it avoids generating invalid combinations in the first place. Here's a short walkthrough of the logic:
1. Start with an empty path and keep track of the number of open and close parentheses.
2. If the length of the path is equal to 2n, add it to the result list.
3. If the number of open parentheses is less than n, add an open parenthesis to the path and recurse.
4. If the number of close parentheses is less than the number of open parentheses, add a close parenthesis to the path and recurse.
## Complexity
The time complexity is O(4^n / n^(3/2)) because in the worst case, we generate all possible combinations of well-formed parentheses, and the number of these combinations is given by the Catalan number formula. The space complexity is O(4^n / n^(3/2)) because we need to store all generated combinations in the result list.
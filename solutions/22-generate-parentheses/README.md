# [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to generate all combinations of well-formed parentheses. This is chosen over a naive brute-force approach of generating all possible combinations of parentheses and then filtering out the well-formed ones, as it would be highly inefficient. The backtracking approach ensures that we only generate well-formed combinations. Here's a short walkthrough of the logic:
1. Start with an empty string and keep track of the number of open and close parentheses.
2. If the length of the current string is equal to 2n, it means we have a well-formed combination, so add it to the result.
3. If the number of open parentheses is less than n, we can add an open parenthesis to the current string and recurse.
4. If the number of close parentheses is less than the number of open parentheses, we can add a close parenthesis to the current string and recurse.
## Complexity
The time complexity is O(4^n / n^(3/2)) because in the worst case, we generate all possible combinations of well-formed parentheses, and the number of such combinations is given by the Catalan number, which has this time complexity. The space complexity is O(4^n / n^(3/2)) as well, because in the worst case, we need to store all the generated combinations in the result list.
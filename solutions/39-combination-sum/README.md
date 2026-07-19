# [Combination Sum](https://leetcode.com/problems/combination-sum/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to generate all unique combinations of candidates that sum up to the target. This approach was chosen over a naive brute-force one, such as generating all possible combinations and then filtering out those that do not sum to the target, because it allows us to prune branches of the search tree early, reducing the number of combinations that need to be generated. Here is a short walkthrough of the logic:
1. Start with an empty combination and the full target value.
2. For each candidate, add it to the current combination and recursively generate all combinations that sum to the remaining target value.
3. If the remaining target value reaches 0, add the current combination to the result list.
4. If the remaining target value becomes negative, stop exploring this branch of the search tree.
## Complexity
The time complexity is O(N^(T/M) + 1), where N is the number of candidates, T is the target value, and M is the minimum value among the candidates, because in the worst case, we need to generate all combinations of candidates that sum to the target value. The space complexity is O(T/M), because in the worst case, the maximum depth of the recursion call stack is T/M, where T is the target value and M is the minimum value among the candidates.
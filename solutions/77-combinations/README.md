# Combinations
[https://leetcode.com/problems/combinations/](https://leetcode.com/problems/combinations/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to generate all combinations of k numbers chosen from the range [1, n]. This approach was chosen over a naive brute-force one, such as generating all permutations and then filtering out the ones that are not combinations, because it avoids unnecessary computation. Here's a short walkthrough of the logic:
1. Start with an empty current combination and a start index of 1.
2. If the length of the current combination is equal to k, add it to the result list.
3. Otherwise, iterate over the range from the start index to n, adding each number to the current combination and recursively calling the backtrack function with the next start index.
4. After each recursive call, remove the last added number from the current combination to backtrack and explore other branches.
## Complexity
The time complexity is O(C(n, k)) because we generate all possible combinations of k numbers chosen from the range [1, n], where C(n, k) is the number of combinations. The space complexity is O(k) because we need to store the current combination, which can have up to k elements.
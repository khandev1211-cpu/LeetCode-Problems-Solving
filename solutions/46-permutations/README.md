# [Permutations](https://leetcode.com/problems/permutations/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to use a backtracking approach to generate all permutations. This is more efficient than a naive brute-force approach, which would involve generating all possible permutations and then filtering out duplicates. The backtracking approach works by swapping each element in the array with the current position, and then recursively generating all permutations of the remaining elements. Here's a short walkthrough of the logic:
1. Start with the first position and swap it with each of the remaining positions.
2. For each swap, recursively generate all permutations of the remaining positions.
3. After generating all permutations for a given swap, backtrack by swapping the elements back to their original positions.
## Complexity
Time complexity: The time complexity is O(N!), where N is the length of the input array, because there are N! possible permutations. This is justified because the backtracking approach generates all possible permutations, and there are N! possible permutations of an array of length N.
Space complexity: The space complexity is O(N), where N is the length of the input array, because the maximum depth of the recursion tree is N. This is justified because the recursion tree has a maximum depth of N, where N is the length of the input array.
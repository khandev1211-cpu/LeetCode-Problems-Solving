# [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/)
Easy, python3
## Approach
The key insight here is to recognize that we can solve this problem by iterating through the string and counting the consecutive occurrences of 0's and 1's. A naive approach would be to generate all possible substrings and check each one, but this would be inefficient due to its O(n^2) time complexity. Instead, we can use a two-pointer approach to keep track of the current and previous counts of consecutive 0's or 1's. Here's a short walkthrough:
1. Initialize two pointers, `prev` and `curr`, to keep track of the previous and current counts of consecutive 0's or 1's.
2. Iterate through the string, and whenever we encounter a different character, update `res` with the minimum of `prev` and `curr`, and reset `prev` and `curr` accordingly.
3. Finally, update `res` one last time with the minimum of `prev` and `curr` after the loop ends.
## Complexity
The time complexity is O(n), where n is the length of the string, because we only need to iterate through the string once. The space complexity is O(1), because we only use a constant amount of space to store the `prev`, `curr`, and `res` variables.
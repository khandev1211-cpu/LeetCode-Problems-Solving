# [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
Easy, Python3
## Approach
The key insight here is to recognize that this problem can be solved using dynamic programming, avoiding the naive brute-force approach of trying all possible combinations of steps. This approach was chosen because it allows us to break down the problem into smaller sub-problems and store the solutions to these sub-problems to avoid redundant computation. Here's a short walkthrough of the logic:
1. Initialize the base cases where `n` equals 1 or 2.
2. Create a dynamic programming array `dp` of size `n + 1` to store the number of ways to climb `i` steps.
3. For each step `i` from 3 to `n`, calculate the number of ways to climb `i` steps by summing the number of ways to climb `i - 1` and `i - 2` steps.
## Complexity
The time complexity is O(n) because we are doing a constant amount of work for each step from 3 to n. The space complexity is O(n) because we need to store the number of ways to climb each step in the dynamic programming array.
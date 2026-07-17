# [Sorted GCD Pair Queries](https://leetcode.com/problems/sorted-gcd-pair-queries/)

**Difficulty:** Hard
**Language:** Python3

## Approach
1. **Frequency Counting:** Count occurrences of each number and multiples of each number in the input array.
2. **Exact GCD Calculation:** Compute the exact number of pairs with GCD equal to each value by subtracting overcounted pairs from higher multiples.
3. **Prefix Sum Array:** Build a prefix sum array to quickly determine the number of pairs with GCD ≤ a given value.
4. **Binary Search:** Answer each query by performing a binary search on the prefix sum array to find the smallest GCD value that satisfies the query.

## Complexity
- **Time:** O(max(nums) * log(max(nums)) + Q log(max(nums))), where Q is the number of queries.
- **Space:** O(max(nums)) for storing frequency, exact GCD, and prefix arrays.
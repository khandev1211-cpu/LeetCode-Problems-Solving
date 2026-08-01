# Unique Binary Search Trees
[https://leetcode.com/problems/unique-binary-search-trees/](https://leetcode.com/problems/unique-binary-search-trees/)
Medium, Python3
## Approach
The key insight to solving this problem is recognizing that the number of unique binary search trees for a given number of nodes can be calculated using dynamic programming, specifically by considering each node as a potential root and counting the combinations of left and right subtrees. This approach is chosen over a naive brute-force method of generating all possible trees because it avoids redundant calculations and has a much lower time complexity. Here's a short walkthrough of the logic:
1. Initialize a dynamic programming array `dp` where `dp[i]` represents the number of unique BST's with `i` nodes.
2. Set the base cases `dp[0]` and `dp[1]` to 1, as there is exactly one way to arrange 0 or 1 nodes into a BST.
3. For each number of nodes `i` from 2 to `n`, calculate `dp[i]` by summing the product of `dp[j]` and `dp[i - j - 1]` for all `j` from 0 to `i - 1`, representing the number of ways to arrange the left and right subtrees given `j` nodes on the left.
## Complexity
The time complexity is O(n^2) because for each node from 2 to n, we perform a constant amount of work for each possible split of the tree, resulting in a quadratic number of operations. The space complexity is O(n) because we need to store the dynamic programming array of size n + 1 to keep track of the number of unique BST's for each number of nodes.
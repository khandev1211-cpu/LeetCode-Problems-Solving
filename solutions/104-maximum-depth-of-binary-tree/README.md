# [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
Difficulty: Easy, Language: Python3
## Approach
The key insight here is to recognize that the maximum depth of a binary tree can be found by recursively calculating the maximum depth of its left and right subtrees and adding 1 for the current node. A naive approach would involve manually traversing the tree and keeping track of the maximum depth encountered, but this recursive approach is more efficient as it breaks down the problem into smaller sub-problems. Here's a short walkthrough:
1. If the tree is empty (i.e., the root is None), return 0 as there are no nodes.
2. Otherwise, recursively calculate the maximum depth of the left and right subtrees.
3. Return the maximum of these two depths plus 1, accounting for the current node.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because each node is visited once. The space complexity is O(h), where h is the height of the tree, due to the recursive call stack, which in the worst case (a skewed tree) can be n.
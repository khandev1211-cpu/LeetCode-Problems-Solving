# [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
Easy, Python3
## Approach
The key insight here is to calculate the height of each subtree while checking if it's balanced, avoiding the naive approach of separately calculating the height of each subtree and then checking for balance. This is done by returning -1 as soon as an unbalanced subtree is found, indicating that the current subtree is not balanced, and returning the height of the subtree otherwise. Here's a short walkthrough:
1. Define a helper function `check(node)` that returns the height of the subtree rooted at `node` if it's balanced, and -1 otherwise.
2. In `check(node)`, recursively calculate the heights of the left and right subtrees.
3. If either subtree is unbalanced or their heights differ by more than 1, return -1.
4. Otherwise, return the height of the current subtree as 1 plus the maximum height of its subtrees.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because each node is visited once. The space complexity is O(h), where h is the height of the tree, because that's the maximum depth of the recursive call stack.
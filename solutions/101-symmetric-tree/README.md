# [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
Easy, Python3
## Approach
The key insight here is to compare the left subtree with the mirrored version of the right subtree. A naive approach would be to first flatten the tree into a list and then compare the list with its reverse, but this would be inefficient due to the extra space required. Instead, we use a recursive approach to directly compare the left and right subtrees. Here's a walkthrough of the logic:
1. If the tree is empty, it is symmetric by definition.
2. We define a helper function `isMirror` to check if two subtrees are mirror images of each other.
3. In `isMirror`, we check if both subtrees are empty (in which case they are mirror images) or if one is empty and the other is not (in which case they are not mirror images).
4. If both subtrees are non-empty, we check if their values are equal and if their left and right children are mirror images of each other.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because we visit each node once. The space complexity is O(h), where h is the height of the tree, because that's the maximum depth of the recursive call stack.
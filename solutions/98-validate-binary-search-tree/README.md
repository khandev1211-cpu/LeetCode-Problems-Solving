# [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
Medium, python3
## Approach
The key insight here is to validate the binary search tree property by ensuring each node's value falls within a valid range defined by its ancestors. This approach avoids the naive method of checking every possible pair of nodes, which would be inefficient. Instead, we use a recursive helper function that checks the following:
1. If a node is `None`, it is a valid BST by default.
2. If a node's value does not fall within the specified range (`lower` and `upper`), it is not a valid BST.
3. Recursively check the left and right subtrees with updated ranges.
## Complexity
The time complexity is O(N), where N is the number of nodes, because we visit each node once. The space complexity is O(H), where H is the height of the tree, due to the recursive call stack, which in the worst case (an unbalanced tree) can be N.
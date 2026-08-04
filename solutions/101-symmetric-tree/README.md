# [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
Difficulty: Easy, Language: python3
## Approach
The key insight here is to compare the left subtree with the mirrored right subtree. A naive approach would be to traverse the entire tree and then compare the left and right subtrees, but this would be inefficient. Instead, we can use a recursive or iterative approach to compare the two subtrees simultaneously. Here's a short walkthrough:
1. Start by checking if the tree is empty (i.e., the root is None).
2. If the tree is not empty, compare the left and right subtrees by checking if they are mirror images of each other.
3. To check if two trees are mirror images, compare the values of the nodes and recursively check the left child of the first tree with the right child of the second tree, and vice versa.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because we visit each node once. The space complexity is O(h), where h is the height of the tree, because that's the maximum depth of the recursive call stack.
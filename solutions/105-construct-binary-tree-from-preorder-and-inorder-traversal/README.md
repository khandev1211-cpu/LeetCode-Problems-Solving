# [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
Medium, python3
## Approach
The key insight here is to recognize that the first element in the preorder traversal is the root of the tree, and then find its position in the inorder traversal to determine the left and right subtrees. This approach is chosen over a naive brute-force one, such as trying all possible tree constructions, because it takes advantage of the given traversal orders to efficiently construct the tree. Here's a short walkthrough of the logic:
1. Identify the root node from the preorder traversal.
2. Find the index of the root node in the inorder traversal to split the tree into left and right subtrees.
3. Recursively construct the left and right subtrees using the corresponding elements from the preorder and inorder traversals.
## Complexity
The time complexity is O(n) because each node is visited once, where n is the number of nodes in the tree. The space complexity is O(n) because in the worst case, the recursive call stack can go as high as the height of the tree, which is n for an unbalanced tree.
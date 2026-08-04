# Construct Binary Tree from Inorder and Postorder Traversal
[https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to recognize that the last element in the postorder traversal is the root of the tree. This is because in a postorder traversal, we visit the left subtree, then the right subtree, and finally the root. Given this, we can find the index of the root in the inorder traversal, which allows us to split both the inorder and postorder traversals into their respective left and right subtrees. A naive approach would be to try all possible combinations of subtrees, but this is inefficient. Instead, we use recursion to build the left and right subtrees based on the splits determined by the root's index in the inorder traversal. Here's a short walkthrough:
1. Identify the root from the last element of the postorder traversal.
2. Find the index of the root in the inorder traversal.
3. Recursively build the left subtree using the elements before the root's index in the inorder traversal and the corresponding elements in the postorder traversal.
4. Recursively build the right subtree using the elements after the root's index in the inorder traversal and the corresponding elements in the postorder traversal.
## Complexity
The time complexity is O(n) because each node is visited once, where n is the number of nodes in the tree. The space complexity is O(n) because in the worst case, the recursion call stack can go as high as the height of the tree, which for an unbalanced tree could be n.
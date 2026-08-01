# [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
Easy, python3
## Approach
The key insight here is to utilize a stack to mimic the recursive call stack, allowing us to traverse the tree iteratively. This approach was chosen over a naive recursive solution to avoid potential stack overflow issues for very deep trees. Here's a short walkthrough of the logic:
1. We start by initializing an empty result list and an empty stack.
2. We then enter a loop that continues as long as there are nodes to visit (i.e., `root` is not `None` or the stack is not empty).
3. Inside the loop, we first traverse as far left as possible, pushing each node onto the stack and updating `root` to its left child.
4. Once we've reached a leaf node (i.e., `root` is `None`), we pop a node from the stack, append its value to the result list, and move to its right subtree.
## Complexity
The time complexity is O(n) because each node is visited exactly once, where n is the number of nodes in the tree. The space complexity is O(n) because in the worst case, the stack can grow up to the height of the tree, which for an unbalanced tree could be n.
# [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
Medium, Python3
## Approach
The key insight here is to perform a pre-order traversal of the binary tree and rearrange the nodes to form a linked list. A naive approach would be to first perform a pre-order traversal and store the node values in a list, then recreate the linked list. However, this approach would require extra space. To achieve an in-place solution, we can iterate through the tree and rearrange the nodes on the fly. Here's a short walkthrough:
1. Start at the root node and check if it has a left child.
2. If it does, find the rightmost node in the left subtree and append the right child of the current node to it.
3. Then, move the left child to the right child of the current node and set the left child to null.
4. Repeat this process until all nodes have been visited.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because each node is visited once. The space complexity is O(1), because only a constant amount of extra space is used to store the current node and the rightmost node in the left subtree.
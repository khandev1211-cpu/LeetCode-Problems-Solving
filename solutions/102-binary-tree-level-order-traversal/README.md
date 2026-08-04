# [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
Medium, python3
## Approach
The key insight here is to use a queue to perform a breadth-first search (BFS) of the binary tree. This approach was chosen over a naive recursive depth-first search (DFS) because DFS would not naturally traverse the tree level by level. Here's a short walkthrough of the logic:
1. Initialize a queue with the root node and an empty result list.
2. While the queue is not empty, process each node at the current level, adding its value to the current level's list and its children to the queue.
3. After processing all nodes at the current level, add the current level's list to the result list.
## Complexity
The time complexity is O(N), where N is the number of nodes in the tree, because each node is visited once. The space complexity is O(N), because in the worst case, the queue will store all nodes at the last level of the tree.
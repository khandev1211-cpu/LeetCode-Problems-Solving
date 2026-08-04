# [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
Medium, python3
## Approach
The key insight here is to use a queue for level order traversal and then insert each level's nodes at the beginning of the result list to achieve the bottom-up order. A naive approach would be to first perform a level order traversal and store all levels, then reverse the result list. However, this approach is more efficient as it avoids the extra step of reversing. Here's a short walkthrough:
1. Initialize the result list and a queue with the root node.
2. While the queue is not empty, process each level by removing all nodes at the current level from the queue, adding their values to a level list, and adding their children to the queue.
3. Insert the level list at the beginning of the result list.
## Complexity
The time complexity is O(N), where N is the number of nodes in the tree, because each node is visited once. The space complexity is O(N), where N is the number of nodes in the tree, because in the worst case, the queue will store all nodes at the last level.
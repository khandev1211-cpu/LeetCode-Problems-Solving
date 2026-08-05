# [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
Medium, python3
## Approach
The key insight here is to utilize a queue to perform a level-order traversal of the binary tree, allowing us to easily access and set the next pointer for each node. This approach is chosen over a naive recursive approach that would require additional space for the recursive call stack. Here's a short walkthrough:
1. Initialize a queue with the root node.
2. For each level, iterate through the nodes in the queue and set the next pointer for each node to the next node in the queue.
3. Add the left and right children of each node to the queue for the next level.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because we visit each node once. The space complexity is O(n), where n is the number of nodes in the tree, because in the worst case, the queue will contain all nodes at the last level.
# [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
Medium, python3
## Approach
The key insight here is to use a queue for level order traversal and a flag to track the direction of traversal at each level. A naive approach would be to traverse the tree level by level and then reverse every other level, but this would require extra space to store the reversed levels. Instead, we can use the `insert` method to add elements at the beginning of the level list when traversing from right to left, avoiding the need for extra space. Here's a short walkthrough:
1. Initialize a queue with the root node and a flag to track the direction of traversal.
2. While the queue is not empty, pop all nodes at the current level and add their children to the queue.
3. When adding node values to the level list, use the flag to determine whether to append or insert at the beginning.
4. After each level, toggle the direction flag.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because we visit each node exactly once. The space complexity is O(n) because in the worst case, the queue will contain all nodes at the last level, which can be at most n/2 nodes.
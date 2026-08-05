# [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
Medium, Python3
## Approach
The key insight here is to utilize a level-order traversal (Breadth-First Search, BFS) to populate the next pointers of each node. This approach is chosen over a naive recursive depth-first search (DFS) because DFS would not naturally lend itself to easily accessing the next node on the same level. Here's a short walkthrough of the logic:
1. Initialize a queue with the root node if it exists.
2. For each level, iterate through all nodes in the current level, setting the next pointer of each node to the next node in the queue (or None if it's the last node in the level).
3. Add the left and right children of each node to the queue to process in the next level.
4. Repeat steps 2-3 until all levels have been processed.
## Complexity
The time complexity is O(N), where N is the number of nodes in the tree, because each node is visited exactly once. The space complexity is O(N), where N is the number of nodes in the tree, because in the worst case, the queue will store all nodes at the last level.
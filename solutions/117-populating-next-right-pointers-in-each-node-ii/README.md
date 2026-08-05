# [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
Medium, Python3
## Approach
The key insight here is to use a level-order traversal (BFS) to populate the next pointers, as this allows us to easily access the next node at each level. A naive approach would be to use a recursive DFS, but this would not provide the same level of access to the next node. Here's a short walkthrough:
1. Initialize a queue with the root node.
2. For each level, iterate over the nodes in the queue and set the next pointer of each node to the next node in the queue.
3. Add the children of each node to the queue for the next level.
## Complexity
Time complexity: The time complexity is O(n), where n is the number of nodes in the tree, because we visit each node once. 
Space complexity: The space complexity is O(n), where n is the number of nodes in the tree, because in the worst case, the queue will contain all nodes at the last level.
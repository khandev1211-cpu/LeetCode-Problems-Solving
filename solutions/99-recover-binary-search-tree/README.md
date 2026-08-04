# [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)
Medium, Python3
## Approach
The key insight here is to identify the two nodes that were swapped by mistake. A naive approach would involve checking every pair of nodes, but this would be inefficient. Instead, we can use an in-order traversal of the binary search tree to find the two nodes. The in-order traversal visits nodes in ascending order, so if two nodes were swapped, they will be the ones that are out of order in the traversal. We can keep track of the previous node and the first and second nodes that are out of order.
Here is a short walkthrough of the logic:
1. Initialize variables to keep track of the first and second nodes that are out of order, as well as the previous node in the traversal.
2. Perform an in-order traversal of the tree, checking if the current node is out of order with the previous node.
3. If the current node is out of order, update the first and second nodes accordingly.
4. After the traversal, swap the values of the first and second nodes to recover the tree.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because we visit each node once during the in-order traversal. The space complexity is O(h), where h is the height of the tree, because that is the maximum depth of the recursion stack, but since we are not storing any additional data structures that scale with input size, we can consider it as O(1) for the iterative solution.
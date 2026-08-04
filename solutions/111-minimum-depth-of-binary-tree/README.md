# Minimum Depth of Binary Tree
[https://leetcode.com/problems/minimum-depth-of-binary-tree/](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
Easy, Python3
## Approach
The key insight here is to use recursion to traverse the binary tree, checking for the existence of left and right child nodes. A naive approach would be to perform a level-order traversal (BFS), but this recursive approach is more efficient for this problem since it prunes branches as soon as it finds a leaf node. Here's a short walkthrough:
1. If the root is None, return 0 since there are no nodes.
2. If the root has no left child, recursively find the minimum depth of the right subtree and add 1.
3. If the root has no right child, recursively find the minimum depth of the left subtree and add 1.
4. If the root has both left and right children, recursively find the minimum depth of both subtrees and return the minimum of the two plus 1.
## Complexity
The time complexity is O(n), where n is the number of nodes in the tree, because in the worst case, the function visits each node once. The space complexity is O(h), where h is the height of the tree, because that's the maximum depth of the recursive call stack.
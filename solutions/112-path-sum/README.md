# [Path Sum](https://leetcode.com/problems/path-sum/)
Easy, Python3
## Approach
The key insight here is to use a recursive depth-first search (DFS) approach to traverse the binary tree, subtracting the current node's value from the target sum at each step. This approach was chosen over a naive brute-force one (which would involve generating all possible paths and checking their sums) because it allows us to prune branches early when the target sum becomes negative, reducing unnecessary computation. Here's a short walkthrough of the logic:
1. If the current node is None, return False because there's no path to consider.
2. If the current node is a leaf node, return whether its value equals the current target sum.
3. Otherwise, subtract the current node's value from the target sum and recursively check the left and right subtrees.
## Complexity
The time complexity is O(N), where N is the number of nodes in the tree, because in the worst case we might need to visit every node. The space complexity is O(H), where H is the height of the tree, because that's the maximum depth of the recursive call stack.
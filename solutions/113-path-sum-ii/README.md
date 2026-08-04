# [Path Sum II](https://leetcode.com/problems/path-sum-ii/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to use a depth-first search (DFS) approach to traverse the binary tree, keeping track of the current path and its sum. This approach was chosen over a naive brute-force one, which would involve checking all possible paths, because DFS allows us to efficiently explore all root-to-leaf paths while avoiding unnecessary computations. Here's a short walkthrough of the logic:
1. Start at the root node and initialize an empty path and a path sum of 0.
2. Recursively traverse the tree, appending each node's value to the current path and adding it to the path sum.
3. If a leaf node is reached and the path sum equals the target sum, append a copy of the current path to the result list.
4. Backtrack by removing the last node from the path and exploring other branches.
## Complexity
The time complexity is O(N), where N is the number of nodes in the tree, because in the worst case, we visit each node once. The space complexity is O(H), where H is the height of the tree, because that's the maximum depth of the recursion call stack.
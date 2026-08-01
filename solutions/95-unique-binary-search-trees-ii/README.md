# [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)
Medium, Python3
## Approach
The key insight here is to use a recursive approach to generate all possible unique binary search trees. This approach was chosen over a naive brute-force one, such as trying all permutations of the numbers from 1 to n and checking if they form a valid binary search tree, because it avoids unnecessary computation and ensures that each generated tree is unique. Here's a short walkthrough of the logic:
1. Define a recursive function `generate_trees` that takes a start and end value, representing the range of values that can be used to construct the trees.
2. If the start value is greater than the end value, return a list containing `None`, representing an empty tree.
3. Otherwise, iterate over the range of values from start to end, and for each value, recursively generate all possible left and right subtrees.
4. Combine each left subtree with each right subtree, and add the resulting tree to the list of trees.
## Complexity
The time complexity is O(4^n / n^(3/2)) because the number of unique binary search trees with n nodes is given by the n-th Catalan number, which has this asymptotic growth rate. The space complexity is O(4^n / n^(3/2)) because in the worst case, we need to store all the unique binary search trees with n nodes.
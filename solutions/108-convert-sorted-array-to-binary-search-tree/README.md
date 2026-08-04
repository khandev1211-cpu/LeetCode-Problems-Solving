# [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
Difficulty: Easy, Language: python3
## Approach
The key insight here is to utilize the middle element of the sorted array as the root of the binary search tree to ensure the tree remains height-balanced. This approach is chosen over a naive one, such as selecting the first or last element, because it guarantees a balanced tree. Here's a short walkthrough of the logic:
1. If the input array is empty, return None as there are no elements to construct the tree.
2. Find the middle element of the array and create a new TreeNode with this element as its value.
3. Recursively construct the left subtree with the elements before the middle element and the right subtree with the elements after the middle element.
## Complexity
The time complexity is O(n) because each element in the input array is visited once, where n is the number of elements in the array. The space complexity is O(log n) due to the recursive call stack, which in the worst case (a completely unbalanced tree) could be n, but since we're constructing a balanced BST, it remains log n.
# [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
Easy, Python3
## Approach
The key insight here is to avoid a brute-force approach that involves sorting the combined list, which would result in a time complexity of O(n log n). Instead, we leverage the fact that both input lists are already sorted. We create a dummy node to simplify the merging process and then iterate through both lists, comparing node values and appending the smaller one to our merged list. Here's a short walkthrough:
1. Create a dummy node to serve as the starting point for our merged list.
2. Compare the current nodes of both lists and append the smaller value to our merged list.
3. Repeat step 2 until one of the lists is exhausted.
4. Append the remaining nodes from the non-exhausted list, if any.
## Complexity
Time complexity: The time complexity is O(n + m) because we are potentially traversing every node in both lists once, where n and m are the lengths of the input lists.
Space complexity: The space complexity is O(n + m) because in the worst case, we are creating a new list that contains all nodes from both input lists.
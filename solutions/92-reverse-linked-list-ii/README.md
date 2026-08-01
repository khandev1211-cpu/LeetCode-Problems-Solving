# [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
Medium, python3
## Approach
The key insight here is to use a dummy node to simplify the handling of edge cases such as when the list needs to be reversed from the head. A naive approach would be to reverse the entire list and then reverse the parts outside the specified range, but this would be inefficient. Instead, we use a two-pointer approach, where `pre` points to the node before the start of the reversal range and `cur` points to the start of the reversal range. We then perform the reversal in-place by iterating through the range and swapping the `next` pointers of the nodes. Here's a short walkthrough:
1. Initialize a dummy node and set its `next` pointer to the head of the list.
2. Move the `pre` pointer to the node before the start of the reversal range.
3. Initialize the `cur` pointer to the start of the reversal range.
4. Perform the reversal by iterating through the range and swapping the `next` pointers of the nodes.
## Complexity
The time complexity is O(n) because we only traverse the list once, where n is the number of nodes in the list. The space complexity is O(1) because we only use a constant amount of space to store the dummy node and the pointers.
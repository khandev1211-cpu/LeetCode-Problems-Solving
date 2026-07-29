# [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)
Medium, python3
## Approach
The key insight here is to recognize that we can solve this problem efficiently by iterating through the list and checking for duplicate values. A naive approach would be to remove duplicates one by one, but this would be inefficient. Instead, we use a dummy node to simplify the edge cases and then traverse the list, skipping over any nodes that have duplicate values. Here's a short walkthrough:
1. Initialize a dummy node that points to the head of the list.
2. Traverse the list, checking if the current node and the next node have the same value.
3. If they do, remove all nodes with that value by updating the `next` pointer of the current node.
4. If they don't, move to the next node.
## Complexity
The time complexity is O(n) because we're doing a constant amount of work for each node in the list. The space complexity is O(1) because we're only using a constant amount of space to store the dummy node and other variables.
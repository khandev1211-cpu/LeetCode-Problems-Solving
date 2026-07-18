# [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
Hard, Python3
## Approach
The key insight here is to utilize a min-heap data structure to efficiently merge the sorted linked lists. This approach was chosen over a naive brute-force one, such as concatenating all lists and then sorting, because it avoids the unnecessary overhead of sorting the entire list. Here's a short walkthrough of the logic:
1. Initialize a min-heap with the head of each linked list, along with a tie-breaker index to avoid comparing ListNode objects when values are equal.
2. Extract the smallest node from the heap and append it to the result list.
3. If the extracted node has a next node, push it back into the heap.
## Complexity
Time complexity: The time complexity is O(N log k), where N is the total number of nodes across all linked lists, because each node is pushed and popped from the heap exactly once, and heap operations take O(log k) time.
Space complexity: The space complexity is O(k), where k is the number of linked lists, because we need to store the head of each linked list in the heap.
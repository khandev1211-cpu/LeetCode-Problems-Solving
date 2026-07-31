# [Partition List](https://leetcode.com/problems/partition-list/)
Medium, python3
## Approach
The key insight here is to use two separate linked lists to store nodes less than `x` and nodes greater than or equal to `x`, thus avoiding the need for a brute-force approach like sorting the entire list. Here's a short walkthrough of the logic:
1. Initialize two dummy nodes, `before_head` and `after_head`, to serve as the starting points for the two separate lists.
2. Traverse the original linked list, and for each node, check if its value is less than `x`.
3. If the value is less than `x`, append the node to the `before` list; otherwise, append it to the `after` list.
4. After traversing the entire list, connect the `before` list to the `after` list and return the next node of `before_head` as the new head of the partitioned list.
## Complexity
The time complexity is O(n), where n is the number of nodes in the list, because we are doing a constant amount of work for each node. The space complexity is O(1), because we are using a constant amount of space to store the dummy nodes and pointers, regardless of the size of the input list.
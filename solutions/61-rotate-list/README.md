# [Rotate List](https://leetcode.com/problems/rotate-list/)
Medium, Python3
## Approach
The key insight here is to first find the length of the linked list and the tail node. Then, we calculate the effective rotation count by taking the modulus of k with the length of the list. This is because after length rotations, the list will be the same as the original. We then find the new tail node, which is length - k - 1 steps from the head, and perform the rotation by updating the next pointers of the new tail, new head, and the original tail. The approach avoids the naive brute-force method of actually rotating the list k times, which would be inefficient for large k.
Here is a short walkthrough of the logic:
1. Calculate the length of the list and find the tail node.
2. Determine the effective rotation count by taking k modulus length.
3. Find the new tail node by moving length - k - 1 steps from the head.
4. Perform the rotation by updating the next pointers.
## Complexity
The time complexity is O(n), where n is the number of nodes in the list, because we are traversing the list to find its length and the new tail node. The space complexity is O(1), because we are only using a constant amount of space to store the new tail, new head, and the original tail.
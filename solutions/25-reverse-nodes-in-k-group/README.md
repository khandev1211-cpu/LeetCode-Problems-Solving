# [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
Difficulty: Hard, Language: python3
## Approach
The key insight here is to reverse the nodes in place, k at a time, without using extra memory space. A naive approach would be to store all the nodes in an array and then reverse them, but this would require O(n) extra space. Instead, we choose to reverse the nodes in place by keeping track of the previous group's tail and the current group's start and end. Here's a short walkthrough:
1. Check if k nodes remain starting after the previous group's tail.
2. If not, return the modified list as it is.
3. Reverse the nodes in the current group in place.
4. Update the previous group's tail and the current group's start.
## Complexity
Time complexity: The time complexity is O(n), where n is the number of nodes in the list, because we are traversing the list once and reversing the nodes in place.
Space complexity: The space complexity is O(1), because we are only using a constant amount of space to store the previous group's tail and the current group's start and end.
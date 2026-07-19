# [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
Medium, python3
## Approach
The key insight here is to use recursion to swap every two adjacent nodes in the linked list. This approach was chosen over a naive brute-force one, such as iterating through the list and swapping nodes manually, because it allows for a more elegant and efficient solution. Here's a short walkthrough of the logic:
1. Check if the list is empty or only contains one node. If so, return the head as it is.
2. Identify the first two nodes to be swapped and store the second node as the new head.
3. Recursively call the function on the rest of the list, starting from the third node.
4. Swap the first two nodes by updating their next pointers.
## Complexity
The time complexity is O(n), where n is the number of nodes in the list, because each node is visited once. The space complexity is O(n), because in the worst case, the recursive call stack can go as high as the number of nodes in the list.
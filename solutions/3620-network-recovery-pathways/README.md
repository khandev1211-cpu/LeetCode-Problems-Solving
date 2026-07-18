# [Network Recovery Pathways](https://leetcode.com/problems/network-recovery-pathways/)
Difficulty: Hard, Language: python3
## Approach
This problem involves finding the maximum path score in a directed acyclic graph (DAG) with recovery costs and online/offline nodes. The key insight is to use a binary search approach to find the maximum minimum edge cost that satisfies the total recovery cost constraint. We start by building the graph and calculating the topological order. Then, we sort the unique edge costs and perform a binary search to find the maximum threshold that allows a valid path from node 0 to node n-1. We use a helper function `feasible` to check if a given threshold allows a valid path. The function uses dynamic programming to calculate the minimum distance from node 0 to each node, considering only online nodes and edges with costs less than the threshold.
Here's a short walkthrough of the logic:
1. Build the graph and calculate the topological order.
2. Sort the unique edge costs and initialize the binary search range.
3. Perform the binary search: for each mid threshold, check if a valid path exists using the `feasible` function.
4. If a valid path exists, update the answer and move the search range to the upper half; otherwise, move the search range to the lower half.
## Complexity
The time complexity is O(m log c), where m is the number of edges and c is the number of unique edge costs, because we perform a binary search over the sorted edge costs and for each threshold, we calculate the minimum distance from node 0 to each node in O(m) time. The space complexity is O(n + m), where n is the number of nodes, because we store the graph and the topological order.
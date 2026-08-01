# [Subsets II](https://leetcode.com/problems/subsets-ii/)
Medium, Python3
## Approach
The key insight here is to use a backtracking approach to generate all subsets while avoiding duplicates by skipping over duplicate elements in the sorted array. This approach was chosen over a naive brute-force one, such as generating all possible subsets and then removing duplicates, because it is more efficient. Here's a short walkthrough of the logic:
1. Sort the input array to group duplicate elements together.
2. Define a recursive backtracking function that takes a starting index and the current subset as parameters.
3. In the backtracking function, append the current subset to the result list and then iterate over the remaining elements in the array, skipping over any duplicates.
4. For each non-duplicate element, recursively call the backtracking function with the current element added to the subset.
## Complexity
The time complexity is O(2^n) because in the worst case, we generate all possible subsets of the input array. The space complexity is O(2^n) because we store all generated subsets in the result list.
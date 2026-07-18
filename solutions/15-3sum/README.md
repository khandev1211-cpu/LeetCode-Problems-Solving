# [3Sum](https://leetcode.com/problems/3sum/)
Medium, Python3
## Approach
The key insight here is to use a two-pointer technique after sorting the array, avoiding the brute-force approach of checking all possible triplets. This approach was chosen because it significantly reduces the number of operations needed. Here's a short walkthrough:
1. Sort the input array to enable the two-pointer technique.
2. Iterate over the array, skipping duplicates to avoid duplicate triplets in the result.
3. For each element, use two pointers starting from the next element and the end of the array to find a pair that sums up to the negation of the current element.
## Complexity
Time complexity is O(n^2) because after sorting the array, for each element, we potentially scan the rest of the array once, where n is the number of elements in the array. This is justified because the sorting operation takes O(n log n) time and the subsequent nested loop structure takes O(n^2) time in the worst case, but since n log n dominates n^2 for large n, the overall time complexity simplifies to O(n^2) due to the dominance of the nested loop over the sorting for large inputs.
Space complexity is O(n) because in the worst case, we might store all triplets in the result, where n is the number of elements in the input array. This is justified because we need additional space to store the result, which in the worst case can be as large as the input itself.
# [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to sort the intervals by their start values and then iterate through them, merging any overlapping intervals. This approach was chosen over a naive brute-force one, such as checking every interval against every other interval, because it allows us to take advantage of the fact that we only need to consider the current interval and the last merged interval. Here's a short walkthrough of the logic:
1. Sort the intervals by their start values.
2. Initialize the merged list with the first interval.
3. Iterate through the remaining intervals, checking if the current interval overlaps with the last merged interval.
4. If they overlap, merge them by updating the last merged interval. If not, append the current interval to the merged list.
## Complexity
Time complexity: The time complexity is O(n log n) because we sort the intervals, where n is the number of intervals. This is justified because the sorting operation dominates the subsequent for loop.
Space complexity: The space complexity is O(n) because in the worst case, we might need to store all intervals in the merged list, where n is the number of intervals. This is justified because we are storing the merged intervals in a separate list.
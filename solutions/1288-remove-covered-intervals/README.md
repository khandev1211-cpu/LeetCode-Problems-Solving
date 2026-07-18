# [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)
Medium, Python3
## Approach
The key insight here is to sort the intervals based on their start value and then by the end value in descending order. This ensures that if two intervals have the same start value, the one with the larger end value comes first. We then iterate through the sorted intervals, counting the ones that are not covered by any previous interval. The brute-force approach of checking every interval against every other interval would be inefficient, so we choose this sorted approach for efficiency. Here's a short walkthrough:
1. Sort the intervals based on the start value and then the end value in descending order.
2. Initialize a count of remaining intervals and a variable to track the end of the last uncovered interval.
3. Iterate through the sorted intervals, and for each interval, check if its end value is greater than the end of the last uncovered interval.
4. If it is, increment the count and update the end of the last uncovered interval.
## Complexity
Time complexity is O(n log n) because we are sorting the intervals, where n is the number of intervals, and the sorting operation dominates the subsequent for loop. Space complexity is O(n) because the sorting operation in Python creates additional space, and in the worst case, it can be as large as the input.
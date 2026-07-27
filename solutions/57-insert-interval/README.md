# [Insert Interval](https://leetcode.com/problems/insert-interval/)
Medium, python3
## Approach
The key insight here is to iterate through the given intervals and insert the new interval at the correct position while merging any overlapping intervals. This approach was chosen over a naive brute-force one, such as checking every interval against every other interval, because it takes advantage of the fact that the input intervals are already sorted. Here's a short walkthrough of the logic:
1. Add all intervals that come before the new interval.
2. Merge all overlapping intervals with the new interval by updating its start and end values.
3. Add the updated new interval.
4. Add all remaining intervals.
## Complexity
The time complexity is O(n) because we make a single pass through the input intervals, where n is the number of intervals. The space complexity is also O(n) because in the worst case, we might need to store all intervals in the result list.
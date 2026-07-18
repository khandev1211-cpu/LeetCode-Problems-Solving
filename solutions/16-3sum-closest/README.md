# [3Sum Closest](https://leetcode.com/problems/3sum-closest/)
Medium, Python3
## Approach
The key insight here is to use a two-pointer technique to find the closest sum to the target. A naive approach would be to use three nested loops to check all possible combinations of three numbers, but this would be inefficient due to its O(n^3) time complexity. Instead, we sort the array and fix one number at a time, then use two pointers to find a pair of numbers that sum up to the remaining target. Here's a short walkthrough of the logic:
1. Sort the input array to enable the two-pointer technique.
2. Iterate over the array, fixing one number at a time.
3. Initialize two pointers, one at the next number and one at the end of the array.
4. Calculate the current sum and update the closest sum if necessary.
5. Move the pointers based on whether the current sum is less than or greater than the target.
## Complexity
The time complexity is O(n^2) because we have a nested loop structure, where the outer loop iterates over the array and the inner loop uses the two-pointer technique to find a pair of numbers. The space complexity is O(1) because we only use a constant amount of space to store the closest sum and the pointers, assuming the input array is allowed to be modified in-place.
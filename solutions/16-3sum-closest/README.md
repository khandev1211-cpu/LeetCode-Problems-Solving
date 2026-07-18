# [3Sum Closest](https://leetcode.com/problems/3sum-closest/)
Medium, Python3
## Approach
The key insight here is to use a two-pointer technique after sorting the array, which allows us to efficiently find the closest sum to the target. This approach was chosen over a brute-force approach (which would involve checking all possible combinations of three numbers) because it significantly reduces the number of operations needed. Here's a short walkthrough of the logic:
1. Sort the input array to enable the two-pointer technique.
2. Initialize the closest sum to infinity and iterate over the array, fixing one number at a time.
3. For each fixed number, use two pointers (one starting from the next number and one from the end) to find a pair of numbers that, when added to the fixed number, gives a sum closest to the target.
4. Update the closest sum whenever a closer sum is found.
## Complexity
Time complexity: The time complexity is O(n^2) because we are iterating over the array and for each iteration, we are using a two-pointer technique that also iterates over the remaining part of the array, where n is the length of the input array.
Space complexity: The space complexity is O(1) because we are not using any additional data structures that scale with the input size, aside from a constant amount of space to store the closest sum and other variables.
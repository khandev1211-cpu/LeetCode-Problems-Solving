# Maximum Subarray
[https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
Medium, python3
## Approach
The key insight here is to use Kadane's algorithm, which iteratively builds up a solution by considering the maximum sum of subarrays ending at each position. This approach was chosen over a naive brute-force approach (checking all possible subarrays) because it avoids redundant computation and has a much better time complexity. Here's a short walkthrough of the logic:
1. Initialize `max_sum` to negative infinity and `current_sum` to 0.
2. For each number in the input array, update `current_sum` to be the maximum of the current number and the sum of `current_sum` and the current number.
3. Update `max_sum` to be the maximum of `max_sum` and `current_sum`.
## Complexity
The time complexity is O(n) because we only need to make a single pass through the input array, where n is the number of elements in the array. The space complexity is O(1) because we only use a constant amount of space to store the `max_sum` and `current_sum` variables.
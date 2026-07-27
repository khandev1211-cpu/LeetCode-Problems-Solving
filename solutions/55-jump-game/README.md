# [Jump Game](https://leetcode.com/problems/jump-game/)
Medium, Python3
## Approach
The key insight here is to use a greedy approach, starting from the end of the array and moving backwards. This approach was chosen over a naive brute-force one, such as trying all possible jump combinations, because it allows us to avoid unnecessary computations and reduce the time complexity. Here's a short walkthrough of the logic:
1. Initialize the last position as the last index of the array.
2. Iterate over the array from the end to the start.
3. If the current index plus its jump value is greater than or equal to the last position, update the last position to the current index.
## Complexity
The time complexity is O(n), where n is the length of the array, because we are doing a single pass through the array. The space complexity is O(1), because we are using a constant amount of space to store the last position.
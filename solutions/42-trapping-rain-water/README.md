# [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
Hard, Python3
## Approach
The key insight here is to use a two-pointer approach, starting from both ends of the elevation map. This approach was chosen over a naive brute-force one, such as checking every possible pair of bars to see if water can be trapped between them, because it allows us to keep track of the maximum height of the bars to the left and right of the current position. Here's a short walkthrough of the logic:
1. Initialize two pointers, one at the start and one at the end of the elevation map, along with the maximum height of the bars to the left and right of the current position.
2. Move the pointer that is pointing to the shorter bar towards the other end, updating the maximum height as we go.
3. At each step, add the difference between the maximum height and the current height to the total amount of water trapped.
## Complexity
The time complexity is O(n), where n is the number of bars in the elevation map, because we are scanning the elevation map once. The space complexity is O(1), because we are using a constant amount of space to store the pointers and the maximum heights.
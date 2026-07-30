# [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
Hard, Python3
## Approach
The key insight here is to use a stack-based approach to efficiently find the largest rectangle area. A naive approach would involve checking every possible rectangle, resulting in a time complexity of O(n^3). Instead, we use a stack to keep track of the indices of the bars. We start by pushing the index of the first bar onto the stack. Then, we iterate over the rest of the bars. If the current bar is higher than the bar at the top of the stack, we push its index onto the stack. If the current bar is lower, we start popping bars from the stack and calculate the area of the rectangle with the popped bar as the smallest bar. The width of the rectangle is the difference between the current index and the index of the previous bar in the stack minus one. We repeat this process until the stack is empty or the current bar is higher than the bar at the top of the stack. Here's a short walkthrough:
1. Initialize an empty stack and an array to store the indices of the bars.
2. Push the index of the first bar onto the stack.
3. Iterate over the rest of the bars, pushing or popping bars from the stack as necessary.
4. Calculate the area of the rectangle with the popped bar as the smallest bar and update the maximum area.
## Complexity
The time complexity is O(n) because we are doing a constant amount of work for each bar in the histogram. The space complexity is O(n) because in the worst case, we might need to push all the indices onto the stack.
# [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
Difficulty: Hard, Language: python3
## Approach
The key insight here is to use a stack-based approach to keep track of the indices of the histogram bars. This approach was chosen over a naive brute-force one, such as checking every possible rectangle, because it allows us to efficiently calculate the area of the largest rectangle that can be formed with each bar as the smallest bar. Here's a short walkthrough of the logic:
1. Initialize an empty stack and a variable to keep track of the maximum area found so far.
2. Iterate over the histogram bars, and for each bar, check if the stack is not empty and the current bar is smaller than the bar at the top of the stack.
3. If the current bar is smaller, pop the top of the stack, calculate the area of the rectangle that can be formed with the popped bar as the smallest bar, and update the maximum area if necessary.
4. Push the current index onto the stack and repeat the process until all bars have been processed.
## Complexity
The time complexity is O(n), where n is the number of histogram bars, because each bar is pushed and popped from the stack exactly once. The space complexity is O(n), because in the worst case, the stack can contain n indices.
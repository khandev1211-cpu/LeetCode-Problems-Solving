# [Pow(x, n)](https://leetcode.com/problems/powx-n/)
Medium, Python3
## Approach
The key insight here is to use exponentiation by squaring to efficiently calculate x raised to the power n. This approach was chosen over the naive brute-force approach of repeated multiplication because it significantly reduces the number of operations required. Here's a short walkthrough of the logic:
1. If n is negative, we convert the problem to a positive n by taking the reciprocal of x and negating n.
2. We initialize a result variable res to 1.
3. We then enter a loop where we repeatedly square x and halve n, effectively reducing the problem size by half in each iteration.
4. If n is odd in any iteration, we multiply res by the current x to account for the extra factor.
## Complexity
Time complexity: O(log n), because we divide the problem size roughly in half with each iteration of the loop.
Space complexity: O(1), because we only use a constant amount of space to store the result and the current values of x and n.
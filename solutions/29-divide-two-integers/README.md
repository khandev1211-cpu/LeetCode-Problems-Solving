# Divide Two Integers
[LeetCode URL](https://leetcode.com/problems/divide-two-integers/)
Difficulty: Medium, Language: python3
## Approach
The key insight here is to use bit manipulation to achieve division without using the division operator. A naive approach would be to repeatedly subtract the divisor from the dividend until the dividend is less than the divisor, but this would be inefficient for large numbers. Instead, we use a while loop to repeatedly double the divisor and add the corresponding value to the quotient until the dividend is less than the divisor. Here's a short walkthrough:
1. Handle the special case where the dividend is the minimum integer and the divisor is -1 to avoid overflow.
2. Determine the sign of the result by checking if exactly one of the dividend and divisor is negative.
3. Use a while loop to repeatedly double the divisor and add the corresponding value to the quotient until the dividend is less than the divisor.
## Complexity
Time complexity: The time complexity is O(log N), where N is the absolute value of the dividend, because we are effectively dividing the dividend by 2 in each iteration of the while loop.
Space complexity: The space complexity is O(1), because we only use a constant amount of space to store the quotient, dividend, and divisor.